# Vilo_sklep
Projekt Dashboardu dla sklepu Vilo

Zródło: plik szkoleniowy (szkolenie z DAX)

Cel: stworzenie dashoboardu z najważniejszymi statystykami i interaktywnymi wizualizacjami dla sklepu Vilo. Zawiera informacje pozwalające segmentację klientów, analizę najbardziej dochodowych marek, anaizę sprzedaży w czasie, szybkie filtrowanie statystyk.

IDE: Power BI Desktop, Power Query, Excel, 

Kod: próbki kodu w języku DAX w osobnym pliku.

Opis projektu: projekt przygowany od A do Z- czyli od połączenia danych do Excela i załadowaniu ich do Power Bi poprzez Power Query. W Power Query czyszczenie danych, sprawdzanie jakości danych, usuwanie zbędnych kolumn w celu optymalizacji. Następnie przegląd tabel, dodanie kolumn obliczeniowych, określenie modelu danych - relacje między tabelami i kardynalność, utworzenie tabeli z miarami i tabeli kalendarza (optymalizacja i szybsze pisanie miar),  utworzenie miar do wizualizacji oraz opracowanie płótna raportu.

Optymalizacja poprzez:
--> usuwanie zbędnych kolumn na poziomie power query
--> dodanie kolumn obliczeniowych tylko tam, gdzie to konieczne, a zamiast tego zastosowanie miar
--> w miarach posługiwanie się zmiennymi - przyspieszenie wykonania, zapobieganie wielokrotnej ewaluacji
-->utworzenie dodatkowej tabeli kalendarza, zamiast odwołanie do tabel*
--> unikanie relacji many-to-many - opcjonalnie może być zastąpiona funkcją USERRELATIONSHIP

Przykładowe wizualizacje i fragmenty kodu:
<img width="1797" height="712" alt="image" src="https://github.com/user-attachments/assets/2138e4ef-98b0-40fe-b6f8-8a5a0f70b15d" />

Kod przykąłdowej miary
<img width="1017" height="241" alt="image" src="https://github.com/user-attachments/assets/ee42b06a-43d3-41da-9064-d8460a19355f" />

Model danych:
<img width="1190" height="642" alt="image" src="https://github.com/user-attachments/assets/b03bae02-8df2-45b1-a96f-ec64681f1fbb" />



