from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import time as t

def get_records():
    # Uruchom przeglądarkę i przejdź do strony
    driver = Firefox()
    driver.get("https://migracje.gov.pl/statystyki/zakres/polska/typ/wnioski/widok/tabele/rok/2021/")

    # Czekaj aż się załaduje
    t.sleep(10)

    elem = driver.find_element_by_xpath("//select[@name='DataTables_Table_0_length']")
    elem.click()
    elem.send_keys("100")

    # Pobierz tekst z tabeli

    # Tekst do listy list:
    tablica = []
    for table in driver.find_elements_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr"):
        data = [int(item.text) for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
        tablica.append(data)

    # Zamykam przeglądarkę
    driver.close()

    # Utworzyć funkcje: zwracającą tablicę jako pandas DataFrame
    return pd.DataFrame(tablica)

# Utworzyć funkcje przetwarzające DataFrame do csv & sqli
def tablica_csv(dataframe):
    pass

def tablica_sql(dataframe):
    pass

tablica = get_records()
print(tablica)
