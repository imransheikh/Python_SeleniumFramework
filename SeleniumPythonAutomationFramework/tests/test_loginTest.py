#!/usr/bin/env python
# coding: utf-8

# In[1]:
from datetime import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver

urls = [
    "https://shopee.com.my/huggies.os"
]
driver = webdriver.Chrome(ChromeDriverManager().install())
for url in urls:
    try:

        driver.get(url)


    except:
        button = driver.find_element_by_xpath('/html/body/main/div[2]/div/a')
        button.click()
        driver.refresh()
        driver.get(url)
        continue
    try:
        english = driver.find_element(By.XPATH, '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')
        english.click()


    except NoSuchElementException:
        pass
    all_products = WebDriverWait(driver, 18).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"main\"]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/a[2]")))

    driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/a[2]").click()
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/button[2]')))
    while True:
        product_elements = WebDriverWait(driver, 12).until(EC.presence_of_all_elements_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]')))
        print(f"Total products: {len(product_elements)}")

        for i, product_element in enumerate(product_elements):
            product_name = product_element.find_element(By.CLASS_NAME, 'sN5Sxy').text

            try:
                product_offer_price = product_element.find_element(By.XPATH,
                                                                   '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/a/div/div/div[2]/div[2]/div[2]').text
            except NoSuchElementException:
                product_offer_price = "NLA"

            # try:
            # product_ori_price = product_element.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/a/div/div/div[2]/div[2]/div[1]').text
            # except NoSuchElementException:
            # product_ori_price = "N/A"

            try:
                product_promo = product_element.find_element(By.XPATH,
                                                             '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[7]/a/div/div/div[2]/div[1]/div[2]').text
            except NoSuchElementException:
                product_promo = "N/A"

            try:
                product_sold = product_element.find_element(By.XPATH, './/a/div/div/div[2]/div[3]/div[2]').text
            except NoSuchElementException:
                product_sold = "N/A"

            try:
                product_image = product_element.find_element(By.XPATH,
                                                             '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[4]/a/div/div/div[1]/div').get_attribute(
                    "src")
            except NoSuchElementException:
                product_image = "N/A"

            try:
                product_link = product_element.find_element(By.XPATH, './/a').get_attribute('href')
            except NoSuchElementException:
                product_link = "N/A"

            print(f"Product name: {product_name}")
            print(f"Product promo price: {product_offer_price}")
            print(f"Product promo: {product_promo}")
            print(f"Product sold: {product_sold}")
            print(f"Product image: {product_image}")
            print(f"Product Link: {product_link}")

            data = data.append({'Product name': product_name, 'Product promo price': product_offer_price,
                                'Product promo ': product_promo, 'Product sold': product_sold,
                                'Product image': product_image, 'Product Link': product_link}, ignore_index=True)

        next_button = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/button[2]')
        if not next_button.is_enabled():
            break
        next_button.click()

    time.sleep(5)

# In[ ]:




