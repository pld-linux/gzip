.\" {PTM/LK/0.1/27-09-1998/"znew - konersja plik�w .Z na .gz"}
.\" T�umaczenie: 27-09-1998 �ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZNEW 1
.SH NAZWA
znew \- dokonaj konwersji pliku .Z do pliku .gz
.SH SK�ADNIA
.B znew
[ \-ftv9PK] [ name.Z ...  ]
.SH OPIS
.I  Znew
dokonuje konwersji wszystkich plik�w w formacie .Z (utworzonych programem
compress) do formatu .gz (utworzonych programem gzip). Je�eli chcesz wymusi�
ponown� kompresj� pliku b�d�cego ju� w formacie programu gzip, zmie�
rozszerzenie nazwy tego pliku na .Z, a nast�pnie u�yj programu znew.
.SH OPCJE
.TP
.B \-f
Wymusza konwersj� z formatu .Z do formatu .gz nawet, je�eli plik .gz ju�
istnieje
.TP
.B \-t
Testuje nowy plik przed usuni�ciem orygina�u.
.TP
.B \-v
Pe�na informacja. Wy�wietla nazw� i procent, o jaki zosta� zredukowany
rozmiar ka�dego pliku.
.TP
.B \-9
U�ywa najwolniejszej (lecz najbardziej wydajnej) kompresji.
.TP
.B \-P
U�ywa przetwarzania potokowego, by zredukowa� zu�ycie przestrzeni dysku.
.TP
.B \-K
Nie usuwa pliku .Z, je�eli jest mniejszy od nowoutworzonego pliku .gz
.SH "ZOBACZ TAK�E"
gzip(1), zmore(1), zdiff(1), zgrep(1), zforce(1), gzexe(1), compress(1)
.SH B��DY
.I Znew
nie zachowuje pola daty/czasu pliku przy u�yciu opcji -P, je�eli polecenie
.IR cpmod (1)
jest niedost�pne, za�
.IR touch (1)
nie obs�uguje opcji \-r
