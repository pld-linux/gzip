.\" {PTM/LK/0.1/27-09-1998/"znew - konersja plików .Z na .gz"}
.\" T³umaczenie: 27-09-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZNEW 1
.SH NAZWA
znew \- dokonaj konwersji pliku .Z do pliku .gz
.SH SK£ADNIA
.B znew
[ \-ftv9PK] [ name.Z ...  ]
.SH OPIS
.I  Znew
dokonuje konwersji wszystkich plików w formacie .Z (utworzonych programem
compress) do formatu .gz (utworzonych programem gzip). Je¿eli chcesz wymusiæ
ponown± kompresjê pliku bêd±cego ju¿ w formacie programu gzip, zmieñ
rozszerzenie nazwy tego pliku na .Z, a nastêpnie u¿yj programu znew.
.SH OPCJE
.TP
.B \-f
Wymusza konwersjê z formatu .Z do formatu .gz nawet, je¿eli plik .gz ju¿
istnieje
.TP
.B \-t
Testuje nowy plik przed usuniêciem orygina³u.
.TP
.B \-v
Pe³na informacja. Wy¶wietla nazwê i procent, o jaki zosta³ zredukowany
rozmiar ka¿dego pliku.
.TP
.B \-9
U¿ywa najwolniejszej (lecz najbardziej wydajnej) kompresji.
.TP
.B \-P
U¿ywa przetwarzania potokowego, by zredukowaæ zu¿ycie przestrzeni dysku.
.TP
.B \-K
Nie usuwa pliku .Z, je¿eli jest mniejszy od nowoutworzonego pliku .gz
.SH "ZOBACZ TAK¯E"
gzip(1), zmore(1), zdiff(1), zgrep(1), zforce(1), gzexe(1), compress(1)
.SH B£ÊDY
.I Znew
nie zachowuje pola daty/czasu pliku przy u¿yciu opcji -P, je¿eli polecenie
.IR cpmod (1)
jest niedostêpne, za¶
.IR touch (1)
nie obs³uguje opcji \-r
