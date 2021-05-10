from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time as t

# Uruchom przeglądarkę i przejdź do strony
driver = Firefox()
driver.get("https://migracje.gov.pl/statystyki/zakres/polska/typ/dokumenty/widok/tabele/rok/2021/")

# Czekaj aż się załaduje
t.sleep(5)
#wait = WebDriverWait(driver, 10)
#h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.udsc-stats-filter-type")))

# Znajdź menu po lewej i wybierz Wnioski decyzje dokumenty
elem = driver.find_element_by_class_name("udsc-stats-filter__title")
elem.click()
print('Klikam w menu')

# Znajdź Przyjęte wnioski i kliknij
elem = driver.find_element_by_class_name("udsc-stats-filter-type--applications")
elem.click()
print('Zaznaczam przyjęte wnioski')

# Odczekaj 5 s znajdź listę rozwijaną z liczbą pozycji przy tabeli wiek
t.sleep(5)
elem = driver.find_element_by_xpath("//select[@name='DataTables_Table_0_length']")
elem.click()
elem.send_keys("100")

# Pobierz tekst z tabeli
#elems = driver.find_element_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr").text
#print(elems.split(' '))

# Tekst do listy list:
tablica = []
for table in driver.find_elements_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr"):
    data = [int(item.text) for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
    tablica.append(data)
print(tablica)

# Zamykam przeglądarkę
driver.close()

# Utworzyć funkcje: zwracającą tablicę jako pandas DataFrame
#return tablica


# Utworzyć funkcje przetwarzające DataFrame do csv & sqli
def tablica_csv(dataframe):
    pass

def tablica_sql(dataframe):
    pass



