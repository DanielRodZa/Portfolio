import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class BrowserAutoSearch:
    def __init__(self):
        self.browser = self._initialize_browser()

    def _initialize_browser(self):
        browsers = {
            "firefox": {
                "manager": GeckoDriverManager,
                "service": FirefoxService,
                "options": webdriver.FirefoxOptions(),
                "driver": webdriver.Firefox
            },
            "chrome": {
                "manager": ChromeDriverManager,
                "service": ChromeService,
                "options": webdriver.ChromeOptions(),
                "driver": webdriver.Chrome
            }
        }

        # Inicalizamos los navegadores
        for browser_name, browser_info in browsers.items():
            try:
                return browser_info["driver"](
                    service=browser_info["service"](browser_info["manager"]().install()),
                    options=browser_info["options"]
                )
            except Exception as e:
                print(f"Error al iniciar el navegador {e}")

        raise Exception("No se pudo iniciar ningún navegador por favor instala Firefox o Chrome.")

    def accept_cookies(self, button_selector):
        """
        Acepta el anuncio de cookies de un navegador
        Args:
            button_selector:

        Returns:
            None
        """
        try:
            accept_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, button_selector))
            )
            accept_button.click()
        except Exception as e:
            print(f"Error al encontrar o hacer click en el botón de aceptar cookies: {e}")

    def search_google(self, query):
        """
        Realiza una búsqueda en google
        Returns:
            None
        """
        self.browser.get("https://www.google.com/")
        time.sleep(2)
        self.accept_cookies("L2AGLb")
        time.sleep(2)
        search_box = self.browser.find_element(By.NAME, "q")
        search_box.send_keys(query + Keys.ENTER)

        # Esperamos a que la página cargue los resultados
        time.sleep(5)

    def google_search_results(self):
        """
        Filtra los resultados de la consulta.
        Returns:
            custom_results (list): Lista de resultados de la busqueda.
        """
        results = self.browser.find_elements(By.CSS_SELECTOR, "div.g")
        custom_results = []
        for result in results:
            try:
                cresult = {}
                cresult['title'] = result.find_element(By.CSS_SELECTOR, "h3").text
                cresult["description"] = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                cresult["link"] = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                custom_results.append(cresult)
            except Exception as e:
                print(f"Un elemento no pudo ser extraido.\nError: {e}")
                continue
        return custom_results

    def quit(self):
        self.browser.quit()

