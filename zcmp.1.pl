.\" {PTM/LK/0.1/27-09-1998/"zcmp - porównywanie skompresowanych plików"}
.\" T³umaczenie: 27-09-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZDIFF 1
.SH NAZWA
zcmp, zdiff \- porównaj skompresowane pliki
.SH SK£ADNIA
.B zcmp
[ opcje_dla_cmp ] plik1
[ plik2 ]
.br
.B zdiff
[ opcje_dla_diff ] plik1
[ plik2 ]
.SH OPIS
.I  Zcmp
oraz
.I zdiff
u¿ywane s± do wywo³ywania programów
.I cmp
i
.I diff
dla skompresowanych plików. Wszystkie opcje s± przekazywane bezpo¶rednio
do programu 
.I cmp
lub
.IR diff "."
Je¿eli podana zostanie tylko jedna nazwa pliku, wówczas porównywane s± pliki
.I plik1
oraz zdekompresowany
.IR plik1 ".gz."
Je¿eli podane zostan± dwie nazwy plików, pliki s± dekompresowane je¿eli jest
to konieczne, a nastêpnie przekazywane do programu
.I cmp
lub
.IR diff "."
Zachowywany jest kod wyj¶cia
.I cmp
lub
.IR diff "."
.SH "ZOBACZ TAK¯E"
cmp(1), diff(1), zmore(1), zgrep(1), znew(1), zforce(1), gzip(1), gzexe(1)
.SH B£ÊDY
Komunikaty programów
.I cmp
lub
.I diff
odnosz± siê do plików tymczasowych, zamiast do podanych w linii poleceñ.


