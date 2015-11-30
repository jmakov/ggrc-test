# # header6ff05843-c222-461f-8226-36a7abe6806e
#
# from selenium.webdriver.common.by import By
# from lib.constants import locator
# from lib import base
#
#
# class InfoProgramPage(base.Page):
#     _cls_selector = selector.WidgetBar.ProgramInfoWidget
#     SUBMIT_FOR_REVIEW = base.Locator(By.CSS_SELECTOR,
#                                      _cls_selector.SUBMIT_FOR_REVIEW)
#     TITLE = base.Locator(By.CSS_SELECTOR, _cls_selector.TITLE)
#     DESCRIPTION = base.Locator(By.CSS_SELECTOR, _cls_selector.DESCRIPTIONS)
#
#
# class WidgetBarPage(base.Page):
#     _cls_selector = selector.WidgetBar
#     BUTTON_ADD = base.Locator(By.CSS_SELECTOR, _cls_selector.BUTTON_ADD)
#     DROPDOWN = base.Locator(By.CSS_SELECTOR, _cls_selector.DROPDOWN)
#     TAB_ACTIVE = base.Locator(By.CSS_SELECTOR, _cls_selector.TAB_ACTIVE)
#
#     def add_widget(self, name):
#         """
#         Adds a new widget to the bar. Note that the allowed widgets names are
#         in the constants package.
#         """
#         self._click_when_visible(self.BUTTON_ADD)
#         elements = self._driver.find_elements(
#             self.DROPDOWN.type, self.DROPDOWN.value)
#
#         for element in elements:
#             if name == element.text:
#                 element.click()
#                 break
#
#     def get_active_tab_name(self):
#         """
#         In general multiple tabs are open. Here we get the name of the active
#         one.
#         :rtype: string
#         """
#         element = self._get_element_when_visible(self.TAB_ACTIVE)
#         return element.text
