# Symulacja Lasu

Projekt to symulacja ekosystemu leśnego oparta na mechanice automatów komórkowych, działająca bezpośrednio w terminalu. Ukazuje cykl życia lasu, uwzględniając losowe generowanie terenu, rozprzestrzenianie się pożarów, obecność rzeki oraz proces odrastania flory.

## Główne funkcje

* **Dynamiczny ekosystem:** Prawdopodobieństwo wzrostu nowych drzew jest uzależnione od bliskości wody oraz sąsiedztwa innych drzew.
* **Zjawiska losowe:** Symulacja uwzględnia meandrującą rzekę oraz wybuchy pożarów spowodowane uderzeniami pioruna.
* **Interfejs konsolowy:** Wizualizacja mapy lasu wraz z panelem statystyk (aktualizowane na żywo słupki proporcji i rekordy) zbudowana za pomocą biblioteki Rich.
* **Płynna animacja:** Terminal nadpisuje klatki w miejscu, tworząc czytelny obraz bez "przewijania" ekranu w dół.

## Struktura plików

* `main.py` – główna pętla programu zarządzająca czasem (odświeżanie klatek) i czyszczeniem ekranu.
* `config.py` – scentralizowane miejsce na wszystkie stałe, w tym wymiary planszy, czas uśpienia i progi prawdopodobieństw.
* `simulation.py` – silnik logiczny odpowiadający za generowanie struktur, wykrywanie sąsiadów i aktualizację stanu siatki.
* `visualizer.py` – moduł odpowiedzialny za renderowanie układu kolumnowego, mapy tekstowej i panelu ze statystykami.

## Wymagania i instalacja

Projekt wymaga języka Python w wersji 3.x. Zewnętrzną zależnością jest wyłącznie biblioteka `rich`.

1. Sklonuj repozytorium lub pobierz pliki projektu.
2. Zainstaluj wymaganą bibliotekę wpisując w terminalu:
   ```bash
   pip install rich
