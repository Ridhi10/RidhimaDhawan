# libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# method to popup google dictionary extension
def getdata(self):
    driver.get(
        "chrome-extension://mgijmajocgfcbeboacabfgobmjgjcoja/browser_action.html")
    driver.find_element_by_id("query-field").send_keys("Cases")
    driver.find_element_by_xpath('//*[@id="define-btn"]').click()
    # explicit wait until search result id displayed
    wait = WebDriverWait(driver, 30).until(method=EC.presence_of_element_located((By.CLASS_NAME, "headword-box")))

# add extension to remote chrome browser
opt = ChromeOptions()
opt.add_extension("app.crx")
# path to chromedriver.exe
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", options = opt)
getdata(driver)

# testing options page of Google Dict
driver.get("chrome-extension://mgijmajocgfcbeboacabfgobmjgjcoja/options.html")
langsel = Select(driver.find_element_by_id("language-selector"))
langsel.select_by_visible_text('Hindi')
driver.find_element_by_xpath('//*[@id="save-btn"]').click()
getdata(driver)


