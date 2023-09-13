from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class A:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def B(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
        sleep(2)
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
        sleep(5)

        print('user can able to Reset the password')
        self.driver.close()

A().B()
