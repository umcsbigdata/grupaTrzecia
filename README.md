# Grupa Trzecia

Bazowane na [projekcie głównym](https://github.com/umcsbigdata/migracje-webscrapping) przedmiotu.

Projekt automatycznego pobierania danych ze strony [map i danych statystycznych imigrantów i służb migracyjnych Polski](https://migracje.gov.pl)

Potrzebne biblioteki można zainstalować przy pomocy:

``` bash
pip install -r requirements.txt
```

Aby uruchomić projekt trzeba mieć zainstalowaną bibliotekę `Selenium` oraz `webdriver` (w tym wypadku `geckodriver`).

Uruchomienie skryptu: (Linux / Unix)

``` bash
python3 webscrap/run.py
```

Uruchomienie skryptu: (Windows)

``` powershell
py -3 webscrap/run.py
```

[Dokumentacja Selenium](https://selenium-python.readthedocs.io/)
