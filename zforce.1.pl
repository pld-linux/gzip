.\" {PTM/LK/0.1/27-09-1998/"zforce - przywracanie rozszerze� plikom gzip-a"}
.\" T�umaczenie: 27-09-1998 �ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZFORCE 1
.SH NAZWA
zforce \- przywr�� rozszerzenie '.gz' plikom skompresowanym przez gzip
.SH SK�ADNIA
.B zforce
[ nazwa ...  ]
.SH OPIS
.I  zforce
dodaje rozszerzenie .gz do wszystkich plik�w skompresowanych przez program
.IR "gzip" ","
aby 
.I gzip
nie kompresowa� ich ponownie.
Jest to u�yteczne w wypadku, gdy nazwy plik�w zosta�y obci�te po transferze. W
systemach z ograniczeniem d�ugo�ci nazwy pliku do 14 znak�w obcinana jest
bazowa cz�� nazwy tak, aby zmie�ci�o si� rozszerzenie .gz . Na przyk�ad,
nazwa 12345678901234 jest zmieniana na 12345678901.gz. Nazwy takie, jak
foo.tgz s� pozostawiane bez zmian.
.SH "ZOBACZ TAK�E"
gzip(1), znew(1), zmore(1), zgrep(1), zdiff(1), gzexe(1)
