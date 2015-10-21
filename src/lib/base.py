import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from lib import environment, constants, exception


class _CustomDriver(webdriver.Chrome):
    def __init__(self, **kwargs):
        super(_CustomDriver, self).__init__(**kwargs)

    def find_elements_by_visible_locator(self, locator):
        """
        :type locator: Locator
        :rtype: selenium.webdriver.remote.Webelement
        """
        elements = self.find_elements(locator.type, locator.value)

        for element in elements:
            if element.is_displayed():
                return element

        raise exception.ElementNotFound(locator)


class InstanceRepresentation(object):
    def __repr__(self):
        return str(self.__dict__)


class Test(object):
    _multiprocess_can_split_ = True

    def _set_driver(self):
        self.driver = _CustomDriver(
            executable_path=environment.CHROME_DRIVER_PATH
        )

    def setup(self):
        self._set_driver()

    def teardown(self):
        self.driver.close()

    def wait_for_redirect(self):
        from_url = self.driver.current_url

        while from_url == self.driver.current_url:
            time.sleep(0.1)

        assert from_url != self.driver.current_url, \
            "Not redirected from: %s" % from_url


class Locator(InstanceRepresentation):
    def __init__(self, selector_type, selector):
        """
        :param selector_type: One of supported locator strategies by Selenium
        :param selector: str
        """
        self.type = selector_type
        self.value = selector


class Page(object):
    def __init__(self, driver):
        """
        :type driver: selenium.webdriver.Chrome
        """
        self._driver = driver

    def _get_element_when_visible(self, locator):
        """
        :type locator: Locator
        :rtype: selenium.webdriver.remote.Webelement
        """
        element = WebDriverWait(self._driver,
                                constants.ux.MAX_USER_WAIT_SECONDS) \
            .until(EC.element_to_be_clickable((locator.type, locator.value)))
        return element

    def click_and_wait(self, locator):
        """
        :type locator: Locator
        """
        element = self._get_element_when_visible(locator)
        element.click()

    def _find_field_and_enter_data(self, locator, data):
        """
        :type locator: Locator
        :type data: str
        """
        element = self._get_element_when_visible(locator)
        element.clear()
        self._get_element_when_visible(locator).send_keys(data)

    def _find_iframe_and_enter_data(self, locator, data):
        """
        :type locator: Locator
        :type data: str
        """
        iframe = self._get_element_when_visible(locator)

        self._driver.switch_to.frame(iframe)
        self._driver.find_element_by_tag_name(constants.tag.BODY)\
            .send_keys(data)
        self._driver.switch_to.default_content()

    def _get_datepicker_elements_for_current_month(self, date_picker_locator,
                                                   field_locator):
        """
        :type field_locator: Locator
        :type date_picker_locator: Locator
        :rtype: selenium.webdriver.remote.Webelement
        """
        self.click_and_wait(field_locator)
        elements = self._driver.find_elements(date_picker_locator.type,
                                              date_picker_locator.value)
        return elements

    def _datepicker_month_start(self, date_picker_locator, field_locator):
        """
        :type field_locator: Locator
        :type date_picker_locator: Locator
        """
        elements = self._get_datepicker_elements_for_current_month(
            date_picker_locator, field_locator)
        elements[0].click()

    def _datepicker_month_end(self, date_picker_locator, field_locator):
        """
        :type field_locator: Locator
        :type date_picker_locator: Locator
        """
        elements = self._get_datepicker_elements_for_current_month(
            date_picker_locator, field_locator)
        elements[-1].click()
