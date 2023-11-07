from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    productRowsAtCart = (By.XPATH, "//table[@class='cartTable']/tbody/tr")
    totalPriceInEachRow = (By.XPATH, "td[5]/p")
    totalAmount = (By.CLASS_NAME, "totAmt")
    promoText = (By.CLASS_NAME, "promoCode")
    applyButton = (By.CLASS_NAME, "promoBtn")
    placeOrderButton = (By.XPATH, "//button[contains(text(),'Place Order')]")
    codeAppliedText = (By.XPATH, "//span[contains(text(),'Code applied')]")

    def sumOfProductPrice(self):
        rows = self.find_web_elements(self.productRowsAtCart)
        allItemSum = 0
        size = len(rows)
        for i in range(1, size + 1):
            value = self.driver.find_element(By.XPATH, "//table[@class='cartTable']/tbody/tr[" + str(i) + "]/td[5]/p")
            allItemSum = allItemSum + int(value.text)
        return int(allItemSum)

    def getTotalAmount(self):
        total_Amount = self.get_text(self.totalAmount)
        return int(total_Amount)

    def enterPromoCode(self, promoCode):
        self.send_keys(self.promoText, promoCode)

    def clickOnApplyButton(self):
        self.click_on(self.applyButton)

    def clickOnPlaceOrderButton(self):
        self.click_on(self.placeOrderButton)

    def verifyCodeAppliedIsDisplayed(self):
        self.verify_element_present(self.codeAppliedText)
