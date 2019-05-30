from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
option = Options()

option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# bloqueia modal "Site deseja saber sua localização"
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

browser = webdriver.Chrome(options=option,
                           executable_path="../drivers/chromedriver.exe")
browser.set_window_size(1280, 680)
browser.get("https://www.celulardireto.com.br/")


menuBandaLarga = browser.find_element_by_id("menu-item-185")
cobertura = browser.find_element_by_id("menu-item-6065")


actions = ActionChains(browser)
actions.move_to_element(menuBandaLarga).perform()
sleep(2)
wait = WebDriverWait(browser, 2)
actions.move_to_element(cobertura).click().perform()


def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


root1 = browser.find_element_by_tag_name('custom-wooza')
shadow_root1 = expand_shadow_element(root1)
print(root1)
root2 = shadow_root1.browser.find_element_by_tag_name('custom-modal-cep-search')
shadow_root2 = expand_shadow_element(root2)
print(root2)
print(shadow_root2)

# root3 = shadow_root2.find_element_by_xpath("//div[contains(@class, 'modal-container')]")
# shadow_root3 = expand_shadow_element(root3)
#
# root4 = shadow_root3.find_element_by_xpath("//div[contains(@class, 'backdrop-container')]")
# shadow_root4 = expand_shadow_element(root4)
#
# root5 = shadow_root4.find_element_by_xpath("//div[contains(@class, 'modal-searchbox')]")
# shadow_root5 = expand_shadow_element(root5)
#
# inputCep = shadow_root5.find_element_by_xpath("//input[@placeholder='Search in your collabs']")
# inputCep.send_keys("24346040")



# WebDriverWait block = new WebDriverWait(driver,10);
# block.until(ExpectedConditions.visibilityOfElementLocated(By.className("ute-pay-now-modalContent")));
# driver.switchTo().frame("sema");
#
#
# WebElement modal = browser.findElement(By.xpath("//div[contains(@class,'modal-container)]"));

