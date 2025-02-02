from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation:
    def __init__(self):
        # Define driver, service, and options.
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service('chromedriver-linux64/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        

    def login(self, username, password):
        # Load the web page
        self.driver.get('https://demoqa.com/login')
        # Locate username, password, and login button
        username_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'password')))
        # login_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'login')))
        login_button = self.driver.find_element(By.ID, 'login')


        # Fill in username and password, and click the button
        username_field.send_keys(username)
        password_field.send_keys(password)
        # login_button.click()
        self.driver.execute_script("arguments[0].click();", login_button)
        

    def fill_form(self, fullname, email, curraddress, peraddress):
        # Locate the Elements dropdown and Text Box
        elements = (WebDriverWait(self.driver, 20).
                    until(EC.visibility_of_element_located((By.XPATH, 
                    '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()

        TextBox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,
                                'item-0')))
        TextBox.click()

        # Locate the form fields
        fullname_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(curraddress)
        permanent_address_field.send_keys(peraddress)
        self.driver.execute_script("arguments[0].click();", submit_button)
        

    def download(self):
        # Locate the Upload and Download section and the Download button
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,
                                'item-7')))
        upload_download.click()

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)
        

    def close(self):
        # input("Press Enter to quit the application")
        self.driver.quit()

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login("pythonuser", "Doitc@kgh11")
    webautomation.fill_form("Michale Kahnwald", "Mikel@gmail.com", "Street 99, Winden Street, Germany", "Street 99, Winden Street, Germany")
    webautomation.download()
    webautomation.close()

        








