import traceback

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys
import pytest
import time


class BasePage:
    wait = None
    wait_time = 5

    def __init__(self, driver):
        global wait
        global wait_time
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.wait_time)

    def click_on(self, By_Locator):
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
            element.click()
            print("Successfully clicked on the WebElement, using locator: " + str(
                By_Locator) + " using a timeout of: " + str(self.wait_time))
        except Exception as ex:
            print(
                "Unable to click on the WebElement, using locator: " + str(By_Locator) + " using a timeout of: " + str(
                    self.wait_time))
            assert False, str(ex.__class__)

    def send_keys(self, By_Locator, test_to_send):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(By_Locator)).clear()
            self.wait.until(expected_conditions.presence_of_element_located(By_Locator)).send_keys(test_to_send)
            print("Successfully sent the following keys: " + '"%s"' % str(test_to_send) + " to the element " + str(
                By_Locator) + " using a timeout of: " + str(self.wait_time))
        except Exception as ex:
            print("Unable to sent the following keys: " + str(test_to_send) + " to the element " + str(
                By_Locator) + " using a timeout of: " + str(self.wait_time))
            assert False, str(ex.__class__)

    def click_by_javascript_executor(self, By_Locator):
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
            self.driver.execute_script("arguments[0].click();", element)
            print("Successfully clicked on the WebElement, using locator: " + str(
                By_Locator) + " using a timeout of: " + str(self.wait_time))
        except Exception as ex:
            print("Unable to click on the WebElement, using locator: " + str(By_Locator) + " using a timeout of: " +
                  str(self.wait_time))
            assert False, str(ex.__class__)

    def waitFor(self, By_Locator):
        self.wait.until(expected_conditions.presence_of_element_located(By_Locator))

    def get_text(self, By_Locator):
        try:
            result = self.wait.until(expected_conditions.presence_of_element_located(By_Locator)).text
            print("Successfully get the text on the WebElement, using locator: " + str(
                By_Locator) + " using a timeout of: " + str(self.wait_time))
            return result
        except Exception as ex:
            print("Unable to get the text on the WebElement, using locator: " + str(
                By_Locator) + " using a timeout of: " + str(
                self.wait_time))
            assert False, str(ex.__class__)

    def get_inner_text(self, By_Locator):
        try:
            result = self.wait.until(expected_conditions.presence_of_element_located(By_Locator)).get_attribute(
                "innerText")
            print("Successfully get the inner text on the WebElement, using locator: " + str(By_Locator) +
                  " using a timeout of: " + str(self.wait_time))
            return result
        except Exception as ex:
            print("Unable to get the inner text on the WebElement, using locator: " + str(By_Locator) +
                  " using a timeout of: " + str(self.wait_time))
            assert False, str(ex.__class__)

    def select_by_text(self, By_Locator, text):
        selectElement = self.wait.until(expected_conditions.element_to_be_selected(By_Locator))
        selectDropDown = Select(selectElement)
        selectDropDown.select_by_visible_text(text)

    def select_by_value(self, By_Locator, value):
        selectElement = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        selectDropDown = Select(selectElement)
        selectDropDown.select_by_value(value)

    def select_by_index(self, By_Locator, index):
        selectElement = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        selectDropDown = Select(selectElement)
        selectDropDown.select_by_index(index)

    def find_web_element(self, By_Locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        return element

    def find_web_elements(self, By_Locator):
        elements = self.wait.until(expected_conditions.presence_of_all_elements_located(By_Locator))
        return elements

    def get_row_count(self, By_Locator):
        element = self.wait.until(expected_conditions.presence_of_all_elements_located(By_Locator))
        return len(element)

    def is_title_present(self, title):
        try:
            return self.wait.until(expected_conditions.title_is(title))
        except Exception as ex:
            print("{}, {}".format(ex.__class__, "Title is not present..."))
            return False

    def is_title_contains(self, title):
        try:
            return self.wait.until(expected_conditions.title_contains(title))
        except Exception as ex:
            return False

    # Need to update this method
    def get_title(self, title):
        try:
            if self.is_title_present(title):
                return self.driver.title
        except Exception as ex:
            print(title + " is not present on the page...")

    def mouse_move_to_element(self, By_Locator):
        elements = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        action = ActionChains(self.driver)
        action.move_to_element(elements).perform()

    def double_click(self, By_Locator):
        elements = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        action = ActionChains(self.driver)
        action.double_click(elements)

    def right_click(self, By_Locator):
        elements = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        action = ActionChains(self.driver)
        action.context_click(elements)

    def drag_and_drop(self, By_Source_Locator, By_Target_Locator):
        source_element = self.wait.until(expected_conditions.text_to_be_present_in_element(By_Source_Locator))
        target_element = self.wait.until(expected_conditions.presence_of_element_located(By_Target_Locator))
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)

    def accept_the_alert(self, By_Source_Locator, By_Target_Locator):
        self.wait.until(expected_conditions.alert_is_present())
        Alert(self.driver).accept()

    def dismiss_the_alert(self, By_Source_Locator, By_Target_Locator):
        self.wait.until(expected_conditions.alert_is_present())
        Alert(self.driver).dismiss()

    def get_text_from_alert(self, By_Source_Locator, By_Target_Locator):
        self.wait.until(expected_conditions.alert_is_present())
        return Alert(self.driver).text

    def send_text_to_alert(self, text):
        self.wait.until(expected_conditions.alert_is_present())
        Alert(self.driver).send_keys(text)

        """
        1. How to scroll to element
        2. Drag and Drop
        3. Handle frames
        4. Handle Authentication window
        5. Window Handles
        6. Handles tabs
        7. How to take screenshot
        8. Get current URL
        9. Action Chains  
        10. Navigation in browser
        11. cookies, create, delete
        12. get_attribute, get_dom_attribute, get_property
        13. is_displayed() , is_enabled(), is_selected()
        14. Wait for element visible
        15. Wait for element invisible
        
        """

    # ======================Verify element===============================

    def is_element_visible(self, By_Locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(By_Locator))
        return element

    def verify_element_present(self, By_Locator):
        self.wait.until(expected_conditions.presence_of_element_located(By_Locator))

    def verify_text_present(self, By_Locator):
        self.wait.until(expected_conditions.text_to_be_present_in_element_value(By_Locator))

    def verify_element_clickable(self, By_Locator):
        self.wait.until(expected_conditions.element_to_be_clickable(By_Locator))

    def verify_element_invisible(self, By_Locator):
        self.wait.until(expected_conditions.invisibility_of_element(By_Locator))

    def verify_element_disappeared_from_dom(self, By_Locator):
        self.wait.until(expected_conditions.staleness_of(By_Locator))
