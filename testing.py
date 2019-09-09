#browser
from selenium import webdriver
# keys 
from selenium.webdriver.common.keys import Keys
# browser logs
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
import os
path = str(os.getcwd()) + "/chromedriver_/chromedriver"

chrome_options = Options()  
chrome_options.add_argument("--headless")

def LoginAndPost():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    driver = webdriver.Chrome(path,options=chrome_options, desired_capabilities=d)
    driver.get("https://www.atg.party")
    flag = False
    for entry in driver.get_log('browser'):
        if entry["level"] == "SEVERE":
            flag = True
            print("some resources are unloaded", entry["message"])
        if entry["level"] == "WARNING":
            flag = True
            print("java script DOM Error",entry["message"])
    # uncomment next line to run full testcase
    flag = False
    if not flag:
        login_link = driver.find_element_by_link_text('Login')
        login_link.send_keys(Keys.RETURN)
        time.sleep(2)
        email = driver.find_element_by_id("email")
        email.send_keys("hello@atg.world")
        paswrd = driver.find_element_by_id("password")
        paswrd.send_keys("Pass@123")
        signin = driver.find_element_by_css_selector("button.log-btn")
        signin.click()
        time.sleep(3)
        dropdown_click = driver.find_element_by_id("arrow")
        dropdown_click.click()
        # article = driver.find_element_by_xpath("//div[id= 'collapse1']/ul[contains(@class, 'list-group')]/li")
        # # button[text()="Some text"]
        # print(article)
        # article.click()
        driver.get("https://www.atg.party/article")
        time.sleep(3)
        title = driver.find_element_by_id("title")
        title.click()
        title.send_keys("this is test post")
        desc = driver.find_element_by_css_selector("div.fr-element")
        desc.click()
        desc.send_keys("this is test post body")
        post_btn = driver.find_element_by_id("featurebutton")
        post_btn.click()
        time.sleep(3)
        driver.close()
    else:
        print("found Errors")
        print("Exiting testing Test case Failed")
        # time.sleep(1000)
        driver.close()


def Login():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    driver = webdriver.Chrome(path, options=chrome_options, desired_capabilities=d)
    driver.get("https://www.atg.party")
    flag = False
    for entry in driver.get_log('browser'):
        if entry["level"] == "SEVERE":
            flag = True
            print("some resources are unloaded", entry["message"])
        if entry["level"] == "WARNING":
            flag = True
            print("java script DOM Error",entry["message"])
    # uncomment next line to run full testcase 
    flag = False
    if not flag:
        login_link = driver.find_element_by_link_text('Login')
        login_link.send_keys(Keys.RETURN)
        time.sleep(2)
        email = driver.find_element_by_id("email")
        email.send_keys("hello@atg.world")
        paswrd = driver.find_element_by_id("password")
        paswrd.send_keys("Pass@123")
        signin = driver.find_element_by_css_selector("button.log-btn")
        signin.click()
        time.sleep(2)
        driver.close()
    else:
        print("found Errors")
        print("Exiting test ,Testcase Failed")
        # time.sleep(1000)
        driver.close()
if __name__ == '__main__':
    #uncomment this for only Login
    #Login()
    # Login and Post Data
    LoginAndPost()
