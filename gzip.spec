Summary:	GNU gzip file compression
Summary(de):	Dateikomprimierung GNU-gzip
Summary(fr):	GNU gzip pour la compression de fichiers
Summary(pl):	GNU gzip
Summary(tr):	GNU gzip dosya s�k��t�rma arac�
Name:		gzip
Version:	1.3
Release:	4
License:	GPL
Group:		Utilities/Archiving
Group(pl):	Narz�dzia/Archiwizacja
Source0:	ftp://alpha.gnu.org/gnu/gzip/%{name}-%{version}.tar.gz
Patch0:		gzip-mktemp.patch
Patch1:		gzip-info.patch
Patch2:		gzip-plman.patch
Patch3:		gzip-zforce.patch
Patch4:		gzip-DESTDIR.patch
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
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,%{_mandir}/pl/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/gzip $RPM_BUILD_ROOT/bin
rm -f $RPM_BUILD_ROOT%{_bindir}/gunzip $RPM_BUILD_ROOT%{_bindir}/zcat

ln -sf gzip $RPM_BUILD_ROOT/bin/gunzip
ln -sf gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT%{_bindir}/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT%{_bindir}/gunzip

for i in zcmp zdiff zforce zgrep zmore znew ; do
	sed -e "s|$RPM_BUILD_ROOT||g" < $RPM_BUILD_ROOT%{_bindir}/$i > $RPM_BUILD_ROOT%{_bindir}/.$i
	rm -f $RPM_BUILD_ROOT%{_bindir}/$i
	mv $RPM_BUILD_ROOT%{_bindir}/.$i $RPM_BUILD_ROOT%{_bindir}/$i
done

install pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9nf NEWS README \
	$RPM_BUILD_ROOT{%{_infodir}/gzip.info*,%{_mandir}/{man1/*,pl/man1/*}}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%{_infodir}/gzip.info*
