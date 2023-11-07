from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.BasePage import BasePage


class ConfirmPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    countryDropDown = (By.XPATH, "//div[@class='products']/div/div/select")
    termAndConditionCheckBox = (By.XPATH, "//input[@class='chkAgree']")
    proceedButton = (By.XPATH, "//button[contains(text(),'Proceed')]")
    confirmMessage = (By.XPATH, "//div[@class='wrapperTwo']")

    def selectCountry(self, countryName):
        self.select_by_text(self.countryDropDown, countryName)

    def checkTermAndCondition(self):
        self.click_on(self.termAndConditionCheckBox)

    def clickOnProceedButton(self):
        self.click_on(self.proceedButton)

    def getConfirmMessage(self):
        message = self.get_text(self.confirmMessage)
        return message
