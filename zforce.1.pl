.\" {PTM/LK/0.1/27-09-1998/"zforce - przywracanie rozszerzeñ plikom gzip-a"}
.\" T³umaczenie: 27-09-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZFORCE 1
.SH NAZWA
zforce \- przywróæ rozszerzenie '.gz' plikom skompresowanym przez gzip
.SH SK£ADNIA
.B zforce
[ nazwa ...  ]
.SH OPIS
.I  zforce
dodaje rozszerzenie .gz do wszystkich plików skompresowanych przez program
.IR "gzip" ","
aby 
.I gzip
nie kompresowa³ ich ponownie.
Jest to u¿yteczne w wypadku, gdy nazwy plików zosta³y obciête po transferze. W
systemach z ograniczeniem d³ugo¶ci nazwy pliku do 14 znaków obcinana jest
bazowa czê¶æ nazwy tak, aby zmie¶ci³o siê rozszerzenie .gz . Na przyk³ad,
nazwa 12345678901234 jest zmieniana na 12345678901.gz. Nazwy takie, jak
foo.tgz s± pozostawiane bez zmian.
.SH "ZOBACZ TAK¯E"
gzip(1), znew(1), zmore(1), zgrep(1), zdiff(1), gzexe(1)
