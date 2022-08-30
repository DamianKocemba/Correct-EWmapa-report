## PL: Poprawa raportu obliczeniowego o brakujące dane

Skrypt uzupełnia raport "Raport.txt" utworzony z programu geodezyjnego EWmapa 
o brkujące numery punktów osnowy geodezyjnej w "Linii bazowej" (w pliku są same
współrzędne, bez numeru punktu). Brakujące numery punktów są dopasowywane na podstawie
współrzędnych (porównanie współrzędnych z pliku Raport.txt oraz osnowa.txt). 
Wynikiem końcowym jest plik "results.txt" - analogiczny plik jak "Raport.txt", ale uzupełniony 
o numery punktów w "Linii bazowej".

## ENG: Report's correction for missing data

Script allows to fill in report "Raport.txt" made by geodetic programm EWmapa where
there are missing numbers of geodetic network in baseline - "Linia bazowa" in "Raport.txt"
(in report file there are only coordinates without point numbers). Missing point numbers are
matched based on the coordinates from file "osnowa.txt". The result of the script is a file 
"results.txt" which is the same file as "Raport.txt" but there are added point numbers in line 
containing text "Linia bazowa".
