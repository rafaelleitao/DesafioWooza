from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest
import HtmlTestRunner


class CelularDireto(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        option = Options()
        # bloqueia modal "Site deseja saber sua localização"
        option.add_argument("--disable-infobars")
        # option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
                                       "profile.default_content_setting_values.notifications": 1})
        cls.browser = webdriver.Chrome(options=option,
                                       executable_path="../drivers/chromedriver.exe")
        cls.browser.implicitly_wait(5)
        cls.browser.set_window_size(1280, 680)

    def test_valida_searchbox(self):
        self.browser.get("https://www.celulardireto.com.br/")
        self.browser.find_element_by_id("s").click()
        valor_esperado = 'motorola'
        self.browser.find_element_by_id("s").send_keys(valor_esperado)
        self.browser.find_element_by_xpath("(//button[@id=\'searchsubmit\'])[2]").click()
        valor_exibido = self.browser.find_element_by_css_selector("strong")
        #self.assertEqual(valor_exibido, valor_esperado)
        assert valor_exibido.text == valor_esperado

    def test_valida_exibicao_pagina_operadora_claro(self):
        self.browser.get("https://www.celulardireto.com.br/")
        operadoras = self.browser.find_element_by_css_selector("#menu-item-686 > a")
        menu_claro = self.browser.find_element_by_id("menu-item-879")
        actions = ActionChains(self.browser)
        actions.move_to_element(operadoras).perform()
        wait = WebDriverWait(self.browser, 2)
        actions.move_to_element(menu_claro).click().perform()
        valor_esperado = 'Claro'
        valor_exibido = self.browser.find_element_by_tag_name('h1')
        assert valor_exibido.text == valor_esperado

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("Teste(s)finalizados")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/rafa_/PycharmProjects/desafioWooza/reports'))
