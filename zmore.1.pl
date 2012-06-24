.\" {PTM/LK/0.1/27-09-1998/"zmore - przegl�danie skompresowanych plik�w"}
.\" T�umaczenie: 27-09-1998 �ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH ZMORE 1
.SH NAZWA
zmore \- pe�noekranowe przegl�danie skompresowanych plik�w tekstowych
.SH SK�ADNIA
.B zmore
[ plik ... ]
.SH OPIS
.I zmore 
pozwala na przegl�danie zwyk�ych lub skompresowanych plik�w tekstowych 
na ekranie terminala.
.I zmore
rozpoznaje pliki skompresowane za pomoc� program�w
.IR compress ", " pack
lub
.I gzip
oraz pliki nieskompresowane.
Je�eli podany plik nie istnieje,
.I zmore
poszukuje pliku o tej samej nazwie z dodanym rozszerzeniem .gz, .z lub .Z.
.I zmore
zatrzymuje wy�wietlanie pliku po ka�dorazowym pokazaniu pe�nego
ekranu, wypisuj�c w ostatniej linii \-\-More\-\-. Je�eli u�ytkownik
naci�nie klawisz Enter, wy�wietlana jest kolejna linia. Po naci�ni�ciu
spacji wy�wietlany jest nastepny ekran. Ni�ej podane s� pozosta�e
mo�liwo�ci.
.PP
.I zmore
korzysta z pliku
.IR /etc/termcap ", "
aby pozna� charakterystyk� terminala i domy�lny rozmiar okna. Na terminalu, 
kt�ry jest w stanie wy�wietli� 24 linie, domy�lnym rozmiarem okna s� 22 linie.
Domy�lnie pliki s� przegl�dane za pomoc� programu
.IR more "; "
aby u�y� innego programu, u�yj zmiennej �rodowiskowej PAGER, ustawiaj�c j� na nazw� nowego programu, na przyk�ad
.IR less "."
.PP
Poni�ej podano pozosta�e polecenia, kt�re mo�na wyda�, gdy 
.I zmore
zatrzymuje wy�wietlanie tekstu oraz ich efekty (\fIi\fP jest opcjonaln� liczb�
ca�kowit�, domy�lnie 1) :
.PP
.IP \fIi\|\fP<spacja>
wy�wietl kolejne
.I i
linii (lub nast�pny ekran gdy nie podano liczby)
.PP
.IP ^D
wy�wietl kolejne 11 linii. Je�eli podano
.IR i ", "
ekran jest przewijany o \fIi\fP linii.
.PP
.IP d
to samo, co ^D (control\-D)
.PP
.IP \fIi\|\fPz
to samo co spacja, je�eli podano \fIi\|\fP, nowy rozmiar okna jest ustawiany na 
\fIi\fP linii. Wielko�� okna jest przywracana do poprzedniego rozmiaru, gdy 
zostanie zako�czone wy�wietlanie bie��cego pliku.
.PP
.IP \fIi\|\fPs
wy�wietl kolejny ekran omijaj�c \fIi\|\fP linii
.PP
.IP \fIi\|\fPf
wy�wietl kolejny ekran omijaj�c \fIi\fP ekran�w
.PP
.IP "q or Q"
zako�cz wy�wietlanie bie��cego pliku i wy�wietl nast�pny plik
.PP
.IP "e or q"
Je�eli wy�wietlany jest napis \-\-More\-\-(Next file:
.IR file )
polecenie powoduje zako�czenie dzia�ania
.I zmore
.PP
.IP s
Je�eli wy�wietlany jest napis \-\-More\-\-(Next file:
.IR file )
polecenie powoduje omini�cie kolejnego pliku
.PP
.IP =
wy�wietl bie��cy numer linii
.PP
.IP \fIi\|\fP/wzorzec
znajd� \fIi\|\fP\-te wyst�pienie \fIwzorca\|\fP. Je�eli wzorzec nie zosta�
znaleziony, 
.I zmore
przechodzi do przeszukiwania kolejnego pliku. W przeciwnym wypadku wy�wietlany
jest fragment pliku ze znalezionym wzorcem rozpoczynaj�cy si� dwie linie
przed t�, w kt�rej znaleziono wzorzec. Do edycji wzorca (wyra�enia regularnego)
mo�na u�y� standardowych klawiszy usuwaj�cych znaki i linie. Pr�ba usuni�cia 
znaku na lewo od pierwszej kolumny spowoduje anulowanie polecenia wyszukiwania.
.PP
.IP \fIi\|\fPn
znajd� \fIi\|\fP\-te wyst�pienie ostatnio wprowadzonego wzorca
.PP
.IP !polecenie
wywo�aj shell z \fIpoleceniem\|\fP. Znak `!' w "poleceniu" jest zast�powany
poprzednio wprowadzonym poleceniem. Aby w poleceniu u�y� znaku `!', wprowad�
`\\!'
.PP
.IP ":q or :Q"
zako�cz wy�wietlanie bie��cego pliku i przejd� do kolejnego (to samo, co
q lub Q).
.PP
.IP .
(kropka) powt�rz poprzednie polecenie
.PP
Polecenia wykonywane s� natychmiast po ich wprowadzeniu tzn. nie trzeba
potwierdza� ich klawiszem Enter. Do czasu, gdy nie zosta�o wydane w�a�ciwe
polecenie, mo�na usun�� dotychczas wpisan� liczb� za pomoc� klawisza
usuwaj�cego lini�. Dodatkowo, naci�ni�cie klawisza usuwaj�cego znak spowoduje
ponowne wy�wietlenie wiadomo�ci \-\-More\-\-
.PP
W ka�dym momencie, gdy zawarto�� pliku jest wy�wietlana na terminalu,
u�ytkownik mo�e nacisn�� klawisz zatrzymania (zwykle control\-\\); w�wczas
.I zmore
ponownie wy�wietli standardowy komunikat \-\-More\-\-. Wtedy u�ytkownik
mo�e ponownie wpisa� dowolne z powy�szych polece�. Niestety, w takiej
sytuacji mo�e doj�� do utraty cz�ci informacji poniewa� w momencie, gdy
naci�ni�ty zostanie klawisz zatrzymania, tracone s� wszystkie wpisane znaki nie 
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
aby wy�wietlanie plik�w by�o mozliwe w spos�b ci�g�y. W zwi�zku z tym
polecenia wydawane przez u�ytkownika b�d� niewidoczne z wyj�tkiem polece� /
oraz !.
.PP
Je�eli standardowym wyj�ciem nie jest terminal, w�wczas
.I zmore
zachowuje si� jak
.IR zcat ", "
ale w przeciwie�stwie do niego wypisuje nag��wek przed ka�dym plikiem.
.SH PLIKI
.DT
/etc/termcap Baza danych o terminalach
.SH "ZOBACZ TAK�E"
more(1), gzip(1), zdiff(1), zgrep(1), znew(1), zforce(1), gzexe(1)
