Summary:	GNU gzip file compression
Summary(de):	Dateikomprimierung GNU-gzip
Summary(fr):	GNU gzip pour la compression de fichiers
Summary(pl):	GNU gzip
Summary(tr):	GNU gzip dosya s�k��t�rma arac�
Name:		gzip
Version:	1.3
Release:	19
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://ftp.gnu.org/pub/gnu/gzip/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/gzip-non-english-man-pages.tar.bz2
Patch0:		%{name}-mktemp.patch
Patch1:		%{name}-info.patch
Patch3:		%{name}-zforce.patch
Patch4:		%{name}-DESTDIR.patch
Patch5:		%{name}-stderr.patch
Patch6:		%{name}-zgreppipe.patch
Patch7:		%{name}-noppid.patch
Patch8:		%{name}-ac_fix.patch
Patch9:		%{name}-cpp_macros.patch
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the popular GNU file compression and decompression program,
gzip.

%description -l de
Dies ist das beliebte GNU-Dateikompressions- und
Dekompressionsprogramm, gzip.

%description -l fr
Programme de compression et de d�compression gzip de GNU

%description -l pl
GNU gzip to popularny program s�u��cy do kompresji i dekompresji
danych.

%description -l tr
gzip, Unix i�letim sistemlerinde �ok yayg�n olarak kullan�lan bir
dosya s�k��t�rma ve a�ma arac�d�r.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
aclocal
autoconf
automake -a -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/gzip $RPM_BUILD_ROOT/bin
rm -f $RPM_BUILD_ROOT%{_bindir}/gunzip $RPM_BUILD_ROOT%{_bindir}/zcat

ln -sf gzip $RPM_BUILD_ROOT/bin/gunzip
ln -sf gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT%{_bindir}/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT%{_bindir}/gunzip

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf NEWS README

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(id) %{_mandir}/id/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/gzip.info*
