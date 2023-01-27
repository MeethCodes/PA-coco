from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import cocoerrors
import cocospeaks


def moodlelogin(username, password):
    options = Options()
    options.headless = True
    driver = webdriver.Edge(executable_path="P:\edgedriver_win64\msedgedriver")

    driver.get("http://moodle.apsit.org.in/moodle/login/")

    driver.find_element("id", "username").send_keys(username)

    driver.find_element("id", "password").send_keys(password)

    driver.find_element("id", "loginbtn").click()
    try:
        driver.find_element(By.CLASS_NAME, "errormessage").get_attribute("innerHTML")
        cocoerrors.moodleerror()
    except():
        cocospeaks.inmoodle()

    # driver.get("http://moodle.apsit.org.in/moodle/mod/assign/view.php?id=131928")
    # driver.implicitly_wait(5)
    # element = driver.find_element("css selector", "tr:nth-child(1) > td:nth-child(2)").get_attribute("innerHTML")
    # print(element)
