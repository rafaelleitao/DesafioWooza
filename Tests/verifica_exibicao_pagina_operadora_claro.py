from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

browser = webdriver.Chrome(options=option,
                           executable_path="../drivers/chromedriver.exe")

browser.set_window_size(1280, 680)
browser.get("https://www.celulardireto.com.br/")




operadoras = browser.find_element_by_css_selector("#menu-item-686 > a")
menuClaro = browser.find_element_by_id("menu-item-879")


actions = ActionChains(browser)
actions.move_to_element(operadoras).perform()
sleep(2)
wait = WebDriverWait(browser, 2)
actions.move_to_element(menuClaro).click().perform()

element = browser.find_element_by_tag_name('h1')
assert element.text == 'Claro'
sleep(2)
browser.close()
