from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.service import service, Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class A:
    def __init__(self):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.username = 'Admin'
        self.password = 'admin123'

    # It will help to login the first page
    def B(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        #steps to signin 
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(5)
        WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located)

        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        sleep(5)

        # steps to Check the Menu Visisblity
        # Check the visibility and click on PIM
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
            print('PIM is Visible')

        # In case, can't find the element it will print the except Condition

        except NoSuchElementException:
            print('PIM is Not Visible')

        sleep(2)
        # Check the visibility and click on Leave
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
            print('Leave is Visible')
        except NoSuchElementException:
            print('Leave is Not Visible')

        sleep(2)
        # Check the visibility and click on Time
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()
            print('Time is Visible')
        except NoSuchElementException:
            print('Time is Not Visible')

        sleep(2)
        # Check the visibility and click on Recruitment
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()
            print('Recruitment is Visible')
        except NoSuchElementException:
            print('Recruitment is Not Visible')

        sleep(2)
        # Check the visibility and click on My Info
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
            print('My info is Visible')
        except NoSuchElementException:
            print('My Info is Not Visible')

        sleep(2)
        # Check the visibility and click on Performance
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
            print('Performance is Visible')
        except NoSuchElementException:
            print('Performance is Not Visible')

        sleep(2)
        # Check the visibility and click on Dashboard
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
            print('Dashboard is Visible')
        except NoSuchElementException:
            print('Dashboard is Not Visible')

        sleep(2)
        # Check the visibility and click on Directory
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()
            print('Directory is Visible')
        except NoSuchElementException:
            print('Directory is Not Visible')

        sleep(2)
        # Check the visibility and on Maintenance
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
            print('Maintenance is Visible')
        except NoSuchElementException:
            print('Maintenance is Not Visible')

        sleep(2)
        # Check the visibility and click on Claim
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a').click()
            print('Claim is Visible')
        except NoSuchElementException:
            print('Claim is Not Visible')

        sleep(2)
        # Check the visibility and click on Buzz
        try:
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a').click()
            print('Buzz is Visible')
        except NoSuchElementException:
            print('Buzz is Not Visible')

        sleep(2)

        print('The User able to see the Menu Options')

        self.driver.close()


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
A().B()
