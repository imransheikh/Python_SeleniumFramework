import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    logoText = (By.XPATH, "//div[contains(@class,'brand greenLogo')]")
    searchText = (By.XPATH, "//input[@type='search']")
    products = (By.XPATH, "//div[@class='products']/div[@class='product']")
    productButton = (By.XPATH, "div/button")
    cartIcon = (By.CLASS_NAME, "cart-icon")
    proceedToCheckoutButton = (By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
    bringal = (By.XPATH, "//h4[contains(text(),'Brinjaddl')]")
    top_dealLink = (By.XPATH, "//a[contains(text(),'Top Deals')]")

    def selectProduct(self, searchKeyword):
        self.is_title_present("GreenKart - veg and fruits kart")
        title = self.driver.title
        print("title......")
        print(title)
        #self.driver.find_element(*HomePage.bringal).click()

        #self.click_on(self.bringal)
        self.click_on(self.searchText)
        self.send_keys(self.searchText, searchKeyword)
        self.click_by_javascript_executor(self.cartIcon)
        text= self.get_inner_text(self.top_dealLink)
        print("Text is: " + str(text))


        #
        # self.send_keys(self.searchText, searchKeyword)
        # logo= self.get_text(self.logoText)
        # print("Logo text is: " + logo)
        # products = self.driver.find_elements(*HomePage.products)
        # print(len(products))
        # for product in products:
        #     product.find_element(*HomePage.productButton).click()
        #
        # self.driver.find_element(*HomePage.cartIcon).click()
        # self.driver.find_element(*HomePage.proceedToCheckoutButton).click()
        #
