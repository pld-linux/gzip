.\" {PTM/LK/0.1/27-09-1998/"zgrep - szukanie wyra¿enia regularnego w skompresowanych plikach"}
.\" T³umaczenie: 27-09-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZGREP 1
.SH NAZWA
zgrep \- znajd¼ wyra¿enie regularne równie¿ w skompresowanych plikach
.SH SK£ADNIA
.B zgrep
[ opcje_grepa ]
.BI [ \-e ] " wzorzec"
.IR plik ".|.|."
.SH OPIS
.IR zgrep
wywo³uje program
.I grep
na plikach skompresowanych programami compress lub gzip. Wszystkie podane
opcje s± przekazywane bezpo¶rednio do programu 
.IR grep "."
Je¿eli nie podano ¿adnych plików, dane s± pobierane ze standardowego wej¶cia,
w razie potrzeby dekompresowane, a nastêpnie przekazywane do programu
.IR grep "."
W przeciwnym wypadku podane pliki s± dekompresowane, a nastêpnie przekazywane
do programu
.IR grep "."
.PP
Je¿eli
.I zgrep
jest uruchomiony pod nazw±
.IR zegrep " lub " zfgrep ", "
wówczas zamiast programu
.I grep
uruchamiany jest odpowiednio program
.IR egrep " lub " fgrep "."
Je¿eli istnieje zmienna ¶rodowiskowa
.BR GREP ", "
.I zgrep
u¿ywa jej warto¶ci, jako nazwy programu do uruchomienia, na przyk³ad:

.IP "dla sh: " 
GREP=fgrep; zgrep wzorzec pliki 
.IP "dla csh: "
(setenv GREP fgrep; zgrep wzorzec pliki)
.SH AUTOR
Charles Levert (charles@comm.polymtl.ca)
.SH "ZOBACZ TAK¯E"
grep(1), egrep(1), fgrep(1), zdiff(1), zmore(1), znew(1), zforce(1),
gzip(1), gzexe(1)
