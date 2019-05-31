from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")

# bloqueia modal "Site deseja saber sua localização"
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

browser = webdriver.Chrome(options=option,
                           executable_path="../drivers/chromedriver.exe")

# 1 | Abre Janela
browser.get("https://www.celulardireto.com.br/")
# 2 | define tamanho da janela | 1280x680
browser.set_window_size(1280, 680)
# 3 | Clicar na searchbox
browser.find_element_by_id("s").click()
# - | variavel para asserção
valorEsperado = 'motorola'
# 4 | preencher o valor esperado na searchbox
browser.find_element_by_id("s").send_keys(valorEsperado)
# 5 | Clicar no botão de pesquisa
browser.find_element_by_xpath("(//button[@id=\'searchsubmit\'])[2]").click()
# - | Obtem-se o valor exibido pesquisado
valorExibido = browser.find_element_by_css_selector("strong")
# espera-se que valor exibido é igual ao valor digitado
assert valorExibido.text == valorEsperado
sleep(2)
browser.close()
