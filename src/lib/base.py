# header6ff05843-c222-461f-8226-36a7abe6806e

import time
import pyvirtualdisplay
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.constants import locator
from lib import environment, constants, exception, meta, mixin
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class _CustomDriver(webdriver.Chrome):
    def __init__(self, **kwargs):
        super(_CustomDriver, self).__init__(**kwargs)

    def find_elements_by_visible_locator(self, locator):
        """
        Sometimes we have to find in a list of elements only that one that is
        visible to the user.
        Args:
            locator (Locator)

        Returns:
            selenium.webdriver.remote.webelement.WebElement

        Raises:
            exception.ElementNotFound
        """
        elements = self.find_elements(locator[0], locator[1])

        for element in elements:
            if element.is_displayed():
                return element

        raise exception.ElementNotFound(locator)


class InstanceRepresentation(object):
    def __repr__(self):
        return str(
            {key: value for key, value in self.__dict__.items()
             if "__" not in key}
        )


class Element(InstanceRepresentation):
    def __init__(self, driver, locator):
        """
        Args:
            driver (_CustomDriver):
            locator (tuple):
        """
        self._driver = driver
        self.locator = locator
        self._element = driver.find_element(*locator)
        self.text = self._element.text

    def click(self):
        self._element.click()

    def _wait_until_invisible(self):
        """
        Some elements, upon activation, are overlaying others. Here we wait
        for the animation to end so that we can interact with the elements below
        the overlay.

        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """
        element = WebDriverWait(
            self._driver,
            constants.ux.MAX_USER_WAIT_SECONDS) \
            .until(EC.invisibility_of_element_located(self.locator))
        return element


class Test(InstanceRepresentation):
    __metaclass__ = mixin.MetaDocsDecorator

    def init_resources(self):
        """Prepares resources.

        Configures virtual display buffer for running the test suite in
        headless mode. Also the webdriver is configured here with custom
        resolution and separate log path.
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")

        self.display = pyvirtualdisplay.Display(
            visible=environment.DISPLAY_WINDOWS,
            size=environment.WINDOW_RESOLUTION
        )
        self.display.start()
        self.driver = _CustomDriver(
            executable_path=environment.CHROME_DRIVER_PATH,
            chrome_options=options,
            service_log_path=environment.PROJECT_ROOT_PATH +
            constants.path.LOGS_DIR +
            constants.path.CHROME_DRIVER
        )
        width, height = environment.WINDOW_RESOLUTION
        self.driver.set_window_size(width, height)

    def close_resources(self):
        """Closes resources.

        Closes and quits used resources in testing methods to prevent leaks and
        saves a screenshot on error with a unique file name.
        """
        self.driver.quit()
        self.display.stop()


class Page(object):
    __metaclass__ = meta.RequireDocs

    def __init__(self, driver):
        """
        Args:
            driver (_CustomDriver)
        """
        self._driver = driver

    def navigate_to(self, url):
        if self._driver.current_url != url:
            self._driver.get(url)

    def wait_for_redirect(self):
        """Wait until the current url changes"""
        from_url = self._driver.current_url

        while from_url == self._driver.current_url:
            time.sleep(0.1)

    def reload_page(self):
        """
        Reload page
        """
        self._get_element_when_visible(locator.Page.BODY).send_keys(Keys.F5)

    def scroll_to_bottom(self):
        """
        Scroll to bottom of page
        """
        self._driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);")

    def scroll_in_view(self, locator):
        """
        Scroll web element in view. (May not work in Chrome)
        """
        element = self._get_element_when_present(locator);
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def _get_element_when_present(self, locator):
        """
        Args:
             locator (tuple)

        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """
        element = WebDriverWait(self._driver,
                                constants.ux.MAX_USER_WAIT_SECONDS) \
            .until(EC.presence_of_element_located(locator))
        return element

    def _get_element_when_visible(self, locator):
        """
        Args:
             locator (tuple)

        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """
        element = WebDriverWait(self._driver,
                                constants.ux.MAX_USER_WAIT_SECONDS) \
            .until(EC.visibility_of_element_located(locator))
        return element

    def _get_element_when_clickable(self, locator):
        """
        Args:
             locator (tuple)

        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """
        element = WebDriverWait(self._driver,
                                constants.ux.MAX_USER_WAIT_SECONDS) \
            .until(EC.element_to_be_clickable(locator))
        return element


    def _click_when_visible(self, locator):
        """
        Args:
            locator (Locator)
        """
        element = self._get_element_when_visible(locator)
        hover = ActionChains(self._driver).move_to_element(element)
        hover.perform()

        element = self._get_element_when_clickable(locator)
        element.click()

    def _click_when_present(self, locator):
        """
        Args:
            locator (Locator)
        """
        element = self._get_element_when_present(locator)
        hover = ActionChains(self._driver).move_to_element(element)
        hover.perform()

        element = self._get_element_when_clickable(locator)
        element.click()

    def _hover_when_present(self, locator):
        """
        Args:
            locator (Locator)
        """
        element = self._get_element_when_present(locator)
        hover = ActionChains(self._driver).move_to_element(element)
        hover.perform()

    def _find_field_and_enter_data(self, locator, data):
        """
        Args:
            locator (tuple)
            data (str): the string we want to enter
        """
        element = self._get_element_when_visible(locator)
        element.clear()
        self._get_element_when_visible(locator).send_keys(data)

    def _find_iframe_and_enter_data(self, locator, data):
        """
        Args:
            locator (Locator)
            data (str): the string we want to enter
        """
        iframe = self._get_element_when_visible(locator)

        self._driver.switch_to.frame(iframe)
        self._driver.find_element_by_tag_name(constants.tag.BODY)\
            .send_keys(data)
        self._driver.switch_to.default_content()

    def _get_datepicker_elements_for_current_month(self, date_picker_locator,
                                                   field_locator):
        """
        Args:
            date_picker_locator (Locator)
            field_locator (Locator): locator of the field we have to click on to
            activate the datepicker
        """
        self._click_when_visible(field_locator)
        elements = self._driver.find_elements(*date_picker_locator)
        return elements

    def _datepicker_month_start(self, date_picker_locator, field_locator):
        """
        Args:
            date_picker_locator (Locator)
            field_locator (Locator): locator of the field we have to click on to
            activate the datepicker
        """
        elements = self._get_datepicker_elements_for_current_month(
            date_picker_locator, field_locator)
        elements[0].click()
        self._wait_until_invisible(date_picker_locator)




class Widget(Page, locator.Widget):
    def __init__(self, driver, url):
        super(Widget, self).__init__(driver)
        self.url = url
        self.url_info_widget = url + constants.url.INFO_WIDGET

    def delete_object(self):
        """Deletes object via the settings icon.
        Navigates to the info tab of the object and deletes the object via
        the dropdown in settings icon.
        """
        self.navigate_to(self.url_info_widget)
        self._click_when_visible(self.BUTTON_SETTINGS)
        self._click_when_visible(self.DROPDOWN_DELETE)