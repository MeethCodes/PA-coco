from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import cocoerrors
import cocospeaks

def moodlelogin(username, password):
    options = Options()
    options.headless = True
    driver = webdriver.Edge(executable_path="D:\mini-project\edgedriver_win64\msedgedriver")

    driver.get("http://moodle.apsit.org.in/moodle/login/")

    driver.find_element("id", "username").send_keys(username)

    driver.find_element("id", "password").send_keys(password)

    driver.find_element("id", "loginbtn").click()
    try:
        if driver.find_element(By.CLASS_NAME, "errormessage").get_attribute("innerHTML"):
            cocoerrors.moodleerror()
        else:
            print("hi")
            inmoodle()
    except():
        print("exception in cocomoodle")


def inmoodle():
    print("in inmoodle")
