import pytest

from pages.CartPage import CartPage
from pages.ConfirmPage import ConfirmPage
from pages.HomePage import HomePage
from utilities.BaseTest import BaseTest


# @pytest.mark.usefixtures("setup")
class TestOne(BaseTest):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        cartPage = CartPage(self.driver)
        confirmPage = ConfirmPage(self.driver)
        log = self.getLogger()

        searchKeyword = "ber"
        log.info("Searching the product of the home page")
        # assert "Test" == "Imran"

        homePage.selectProduct(searchKeyword)
        # log.info("Getting total amount of all added product")
        # sumOfProductPrice = cartPage.sumOfProductPrice()
        # log.info("Getting total amount Amount")
        # totalAmount = cartPage.getTotalAmount()
        # log.info("Verifying the assertion")
        # assert (sumOfProductPrice == totalAmount)
        # promoCode = "rahulshettyacademy"
        # cartPage.enterPromoCode(promoCode)
        # cartPage.clickOnApplyButton()
        # cartPage.verifyCodeAppliedIsDisplayed()
        # cartPage.clickOnPlaceOrderButton()
        # countryName = "India"
        # print("====================ADDING===========================")
        # print(countryName)
        # confirmPage.selectCountry(countryName)
        # confirmPage.checkTermAndCondition()
        # confirmPage.clickOnProceedButton()
        # confirmMessage = confirmPage.getConfirmMessage()
        # print(confirmMessage)
        # assert ("Thank you, your order has been placed successfully" in confirmMessage)
        #

    #
    # def test_e2e_2(self):
    #
    #     homePage = HomePage(self.driver)
    #     cartPage = CartPage(self.driver)
    #     confirmPage = ConfirmPage(self.driver)
    #     log = self.getLogger()
    #
    #     searchKeyword = "ber"
    #     log.info("Searching the product of the home page")
    #     homePage.selectProduct(searchKeyword)
    #     log.info("Getting total amount of all added product")
    #     sumOfProductPrice = cartPage.sumOfProductPrice()
    #     log.info("Getting total amount Amount")
    #     totalAmount = cartPage.getTotalAmount()
    #     log.info("Verifying the assertion")
    #     assert (sumOfProductPrice == totalAmount)
    #     promoCode = "rahulshettyacademy"
    #     cartPage.enterPromoCode(promoCode)
    #     cartPage.clickOnApplyButton()
    #     cartPage.verifyCodeAppliedIsDisplayed()
    #     cartPage.clickOnPlaceOrderButton()
    #     countryName = "India"
    #     print("====================ADDING===========================")
    #     print(countryName)
    #     confirmPage.selectCountry(countryName)
    #     confirmPage.checkTermAndCondition()
    #     confirmPage.clickOnProceedButton()
    #     confirmMessage = confirmPage.getConfirmMessage()
    #     print(confirmMessage)
    #     assert ("Thank you, your order has been placed successfully" in confirmMessage)

    # @pytest.fixture(params=[("Afghanistan"),("Cuba")])
    # def getCountryNames(self, request):
    #     return request.param
    #
    # @pytest.fixture(params=[("Chrome", "UserName", "Password"), "FF", "IE"])
    # def crossBrowser(request):
    #     return request.param
