.\" {PTM/LK/0.1/27-09-1998/"zmore - przegl±danie skompresowanych plików"}
.\" T³umaczenie: 27-09-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZMORE 1
.SH NAZWA
zmore \- pe³noekranowe przegl±danie skompresowanych plików tekstowych
.SH SK£ADNIA
.B zmore
[ plik ... ]
.SH OPIS
.I zmore 
pozwala na przegl±danie zwyk³ych lub skompresowanych plików tekstowych 
na ekranie terminala.
.I zmore
rozpoznaje pliki skompresowane za pomoc± programów
.IR compress ", " pack
lub
.I gzip
oraz pliki nieskompresowane.
Je¿eli podany plik nie istnieje,
.I zmore
poszukuje pliku o tej samej nazwie z dodanym rozszerzeniem .gz, .z lub .Z.
.I zmore
zatrzymuje wy¶wietlanie pliku po ka¿dorazowym pokazaniu pe³nego
ekranu, wypisuj±c w ostatniej linii \-\-More\-\-. Je¿eli u¿ytkownik
naci¶nie klawisz Enter, wy¶wietlana jest kolejna linia. Po naci¶niêciu
spacji wy¶wietlany jest nastepny ekran. Ni¿ej podane s± pozosta³e
mo¿liwo¶ci.
.PP
.I zmore
korzysta z pliku
.IR /etc/termcap ", "
aby poznaæ charakterystykê terminala i domy¶lny rozmiar okna. Na terminalu, 
który jest w stanie wy¶wietliæ 24 linie, domy¶lnym rozmiarem okna s± 22 linie.
Domy¶lnie pliki s± przegl±dane za pomoc± programu
.IR more "; "
aby u¿yæ innego programu, u¿yj zmiennej ¶rodowiskowej PAGER, ustawiaj±c j± na nazwê nowego programu, na przyk³ad
.IR less "."
.PP
Poni¿ej podano pozosta³e polecenia, które mo¿na wydaæ, gdy 
.I zmore
zatrzymuje wy¶wietlanie tekstu oraz ich efekty (\fIi\fP jest opcjonaln± liczb±
ca³kowit±, domy¶lnie 1) :
.PP
.IP \fIi\|\fP<spacja>
wy¶wietl kolejne
.I i
linii (lub nastêpny ekran gdy nie podano liczby)
.PP
.IP ^D
wy¶wietl kolejne 11 linii. Je¿eli podano
.IR i ", "
ekran jest przewijany o \fIi\fP linii.
.PP
.IP d
to samo, co ^D (control\-D)
.PP
.IP \fIi\|\fPz
to samo co spacja, je¿eli podano \fIi\|\fP, nowy rozmiar okna jest ustawiany na 
\fIi\fP linii. Wielko¶æ okna jest przywracana do poprzedniego rozmiaru, gdy 
zostanie zakoñczone wy¶wietlanie bie¿±cego pliku.
.PP
.IP \fIi\|\fPs
wy¶wietl kolejny ekran omijaj±c \fIi\|\fP linii
.PP
.IP \fIi\|\fPf
wy¶wietl kolejny ekran omijaj±c \fIi\fP ekranów
.PP
.IP "q or Q"
zakoñcz wy¶wietlanie bie¿±cego pliku i wy¶wietl nastêpny plik
.PP
.IP "e or q"
Je¿eli wy¶wietlany jest napis \-\-More\-\-(Next file:
.IR file )
polecenie powoduje zakoñczenie dzia³ania
.I zmore
.PP
.IP s
Je¿eli wy¶wietlany jest napis \-\-More\-\-(Next file:
.IR file )
polecenie powoduje ominiêcie kolejnego pliku
.PP
.IP =
wy¶wietl bie¿±cy numer linii
.PP
.IP \fIi\|\fP/wzorzec
znajd¼ \fIi\|\fP\-te wyst±pienie \fIwzorca\|\fP. Je¿eli wzorzec nie zosta³
znaleziony, 
.I zmore
przechodzi do przeszukiwania kolejnego pliku. W przeciwnym wypadku wy¶wietlany
jest fragment pliku ze znalezionym wzorcem rozpoczynaj±cy siê dwie linie
przed t±, w której znaleziono wzorzec. Do edycji wzorca (wyra¿enia regularnego)
mo¿na u¿yæ standardowych klawiszy usuwaj±cych znaki i linie. Próba usuniêcia 
znaku na lewo od pierwszej kolumny spowoduje anulowanie polecenia wyszukiwania.
.PP
.IP \fIi\|\fPn
znajd¼ \fIi\|\fP\-te wyst±pienie ostatnio wprowadzonego wzorca
.PP
.IP !polecenie
wywo³aj shell z \fIpoleceniem\|\fP. Znak `!' w "poleceniu" jest zastêpowany
poprzednio wprowadzonym poleceniem. Aby w poleceniu u¿yæ znaku `!', wprowad¼
`\\!'
.PP
.IP ":q or :Q"
zakoñcz wy¶wietlanie bie¿±cego pliku i przejd¼ do kolejnego (to samo, co
q lub Q).
.PP
.IP .
(kropka) powtórz poprzednie polecenie
.PP
Polecenia wykonywane s± natychmiast po ich wprowadzeniu tzn. nie trzeba
potwierdzaæ ich klawiszem Enter. Do czasu, gdy nie zosta³o wydane w³a¶ciwe
polecenie, mo¿na usun±æ dotychczas wpisan± liczbê za pomoc± klawisza
usuwaj±cego liniê. Dodatkowo, naci¶niêcie klawisza usuwaj±cego znak spowoduje
ponowne wy¶wietlenie wiadomo¶ci \-\-More\-\-
.PP
W ka¿dym momencie, gdy zawarto¶æ pliku jest wy¶wietlana na terminalu,
u¿ytkownik mo¿e nacisn±æ klawisz zatrzymania (zwykle control\-\\); wówczas
.I zmore
ponownie wy¶wietli standardowy komunikat \-\-More\-\-. Wtedy u¿ytkownik
mo¿e ponownie wpisaæ dowolne z powy¿szych poleceñ. Niestety, w takiej
sytuacji mo¿e doj¶æ do utraty czê¶ci informacji poniewa¿ w momencie, gdy
naci¶niêty zostanie klawisz zatrzymania, tracone s± wszystkie wpisane znaki nie 
odebrane do tej pory przez terminal.
.\" [ flush - ?? ]
.\" The user may then enter one of the above commands in the normal manner.
.\" Unfortunately, some output is lost when this is done, due to the
.\" fact that any characters waiting in the terminal's output queue
.\" are flushed when the quit signal occurs.
.PP
Terminal jest przez 
.I zmore
ustawiany w tryb
.IR noecho ", "
aby wy¶wietlanie plików by³o mozliwe w sposób ci±g³y. W zwi±zku z tym
polecenia wydawane przez u¿ytkownika bêd± niewidoczne z wyj±tkiem poleceñ /
oraz !.
.PP
Je¿eli standardowym wyj¶ciem nie jest terminal, wówczas
.I zmore
zachowuje siê jak
.IR zcat ", "
ale w przeciwieñstwie do niego wypisuje nag³ówek przed ka¿dym plikiem.
.SH PLIKI
.DT
/etc/termcap Baza danych o terminalach
.SH "ZOBACZ TAK¯E"
more(1), gzip(1), zdiff(1), zgrep(1), znew(1), zforce(1), gzexe(1)
