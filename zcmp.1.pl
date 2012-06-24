.\" {PTM/LK/0.1/27-09-1998/"zcmp - por�wnywanie skompresowanych plik�w"}
.\" T�umaczenie: 27-09-1998 �ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZDIFF 1
.SH NAZWA
zcmp, zdiff \- por�wnaj skompresowane pliki
.SH SK�ADNIA
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
u�ywane s� do wywo�ywania program�w
.I cmp
i
.I diff
dla skompresowanych plik�w. Wszystkie opcje s� przekazywane bezpo�rednio
do programu 
.I cmp
lub
.IR diff "."
Je�eli podana zostanie tylko jedna nazwa pliku, w�wczas por�wnywane s� pliki
.I plik1
oraz zdekompresowany
.IR plik1 ".gz."
Je�eli podane zostan� dwie nazwy plik�w, pliki s� dekompresowane je�eli jest
to konieczne, a nast�pnie przekazywane do programu
.I cmp
lub
.IR diff "."
Zachowywany jest kod wyj�cia
.I cmp
lub
.IR diff "."
.SH "ZOBACZ TAK�E"
cmp(1), diff(1), zmore(1), zgrep(1), znew(1), zforce(1), gzip(1), gzexe(1)
.SH B��DY
Komunikaty program�w
.I cmp
lub
.I diff
odnosz� si� do plik�w tymczasowych, zamiast do podanych w linii polece�.


