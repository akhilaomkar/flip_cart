

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from Testdata.Td import Td

class GoToPriceList:
    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions
        self.te=Td()
        self.prices=GetLowPriceInPage(driver,wait,actions)
        self.fashion_xpath=self.te.fashion_xpath

    def repeat_process(self, driver):
        left_ele_xpath = "//div[@class='_16rZTH']//a"
        right_ele_xpath = "//div[@class='_31z7R_']//a"

        # Navigate to the fashion page
        left_items = self.driver.find_elements(By.XPATH, left_ele_xpath)

        for index in range(2, min(10, len(left_items)-7)):
            left_item_present_xpath = f"{left_ele_xpath}[{index}]"
            print("left_present",left_item_present_xpath)
            left_present_item = self.load_page(left_item_present_xpath)
            print("left text",left_present_item.text)

            # Interact with the right-side elements
            right_elements = self.driver.find_elements(By.XPATH, right_ele_xpath)
            for element in right_elements:
                element.click()
                self.prices.get_low_prices()
                time.sleep(1)
                break
            self.go_back(self.fashion_xpath)
    def go_back(self,fashion_xpath):
        self.driver.back()
        self.handle_login_popup()
        self.load_page(fashion_xpath)
        # Stop after the first right-side interaction
        print()

    def load_page(self, xpath):
        """Load a page by clicking on an element identified by XPath."""
        try:
            print("xpath is",xpath)
            element = self.driver.find_element(By.XPATH, xpath)
            self.wait_for_clickable_and_hover(element)
            return element
        except (StaleElementReferenceException,NoSuchElementException) :
            element = self.driver.find_element(By.XPATH, xpath)
            self.wait_for_clickable_and_hover(element)
            return element

    def handle_login_popup(self):
        """Close login popup if present."""
        try:
            login_popup = self.driver.find_element(By.XPATH, "//span[@class='_30XB9F']")
            self.wait.until(EC.element_to_be_clickable(login_popup)).click()
        except (TimeoutException,StaleElementReferenceException,NoSuchElementException):
            pass  # Popup not present, proceed



    def wait_for_clickable_and_hover(self, element):
        """Wait until the element is clickable and hover over it."""
        self.wait.until(EC.element_to_be_clickable(element))
        self.actions.move_to_element(element).perform()

class GetLowPriceInPage:
    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def get_low_prices(self):
        """Extract and print low-price items."""
        price_elements = self.driver.find_elements(By.XPATH, "//div[@class='Nx9bqj']")
        prices = [elem.text[1:] for elem in price_elements]  # Remove currency symbol

        if prices:
            lowest_price_xpath = f"//div[contains(text(), '{prices[0]}')]"
            print("low price is ", prices[0])
            low_price_elements = self.driver.find_elements(By.XPATH, lowest_price_xpath)
            for element in low_price_elements:
                parent = element.find_element(By.XPATH, "../..")
                time.sleep(5)
                self.actions.move_to_element(parent).perform()
                self.driver.save_screenshot("low_price.png")
                print("The link is", parent.get_attribute("href"))
                time.sleep(1)