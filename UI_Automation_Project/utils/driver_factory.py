from selenium import webdriver

def create_driver(browser="chrome"):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unknown browser")

    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver

