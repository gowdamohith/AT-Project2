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

    # It will help to Login the first Page
    def B(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        #steps to signin 
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located)

        sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        sleep(5)
        # steps to Check the Admin Visibility
        #check the Visibility of User Management
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]")
            print("User management is visible")

        # In case, can't find the element it will print the except Condition

        except NoSuchElementException:
            print("User management is not visible")

        #check the Visibility of job
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]")
            print("Job is visible")
        except NoSuchElementException:
            print("Job is not visible")
            
        #check the Visibility of Organization
        
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]")
            print("Organization is visible")
        except NoSuchElementException:
            print("Organization is not visible")
            
        #check the Visibility of qulification
        
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]")
            print("Qualifications is visible")
        except NoSuchElementException:
            print("Qualifications is not visible")

        #check the Visibility of Nationalities
        
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]")
            print("Nationalities is visible")
        except NoSuchElementException:
            print("Nationalities is not visible")

        #check the Visibility of Corporate Branding
        
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]")
            print("Corporate branding is visible")
        except NoSuchElementException:
            print("Corporate branding is not visible")

        #check the Visibility of Configuration
        
        try:
            self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]")
            print("Configuration is visible")
        except NoSuchElementException:
            print("Configuration is not visible")

        sleep(3)

        print("All the admin page headers are visibles")

        self.driver.close()


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
A().B()
