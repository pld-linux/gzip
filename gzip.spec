Summary:	GNU gzip file compression
Summary(de):	Dateikomprimierung GNU-gzip
Summary(fr):	GNU gzip pour la compression de fichiers.
Summary(pl):	GNU gzip
Summary(tr):	GNU gzip dosya sýkýþtýrma aracý
Name:		gzip
Version:	1.2.4
Release:	17
Copyright:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://alpha.gnu.org/gnu/%{name}-%{version}.tar.gz
Source1:	gzip.1.pl
Source2:	zcmp.1.pl
Source3:	zdiff.1.pl
Source4:	zforce.1.pl
Source5:	zgrep.1.pl
Source6:	zmore.1.pl
Source7:	znew.1.pl
Patch0:		gzip-basename.patch
Patch1:		gzip-gzexe.patch
Patch2:		gzip-mktemp.patch
Patch3:		gzip-info.patch
Prereq:		/sbin/install-info
Requires:	mktemp
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is the popular GNU file compression and decompression
program, gzip.  

%description -l de
Dies ist das beliebte GNU-Dateikompressions- und Dekompressionsprogramm, 
gzip. 

%description -l fr
Programme de compression et de décompression gzip de GNU

%description -l pl
GNU gzip to popularny program s³u¿±cy do kompresji i dekompresji danych.

%description -l tr
gzip, Unix iþletim sistemlerinde çok yaygýn olarak kullanýlan bir dosya
sýkýþtýrma ve açma aracýdýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/man/pl/man1}

make install prefix=$RPM_BUILD_ROOT/usr

mv -f $RPM_BUILD_ROOT/usr/bin/gzip $RPM_BUILD_ROOT/bin/gzip
rm -f $RPM_BUILD_ROOT/usr/bin/gunzip $RPM_BUILD_ROOT/usr/bin/zcat

ln -sf /bin/gzip $RPM_BUILD_ROOT/bin/gunzip
ln -sf /bin/gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT/usr/bin/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT/usr/bin/gunzip

for i in zcmp zdiff zforce zgrep zmore znew ; do
	sed -e "s|$RPM_BUILD_ROOT||g" < $RPM_BUILD_ROOT/usr/bin/$i > $RPM_BUILD_ROOT/usr/bin/.$i
	rm -f $RPM_BUILD_ROOT/usr/bin/$i
	mv $RPM_BUILD_ROOT/usr/bin/.$i $RPM_BUILD_ROOT/usr/bin/$i
done

cat > $RPM_BUILD_ROOT/usr/bin/zless <<EOF
#!/bin/sh
/bin/zcat "\$@" | /usr/bin/less
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/gzip.1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zcmp.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zdiff.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zforce.1
install %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zgrep.1
install %{SOURCE6} $RPM_BUILD_ROOT%{_mandir}/pl/man1/zmore.1
install %{SOURCE7} $RPM_BUILD_ROOT%{_mandir}/pl/man1/znew.1

gzip -9nf NEWS README \
	$RPM_BUILD_ROOT/usr/{info/gzip.info*,man/{man1/*,pl/man1/*}}

%post
/sbin/install-info %{_infodir}/gzip.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/gzip.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz

%attr(755,root,root) /bin/*
%attr(755,root,root) /usr/bin/*

%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%{_infodir}/gzip.info*

%changelog
* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.4-17]
- recompiles on new rpm.

* Sat Jan 02 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.4-15]
- standarized {un}registering info pages; second try (added
  gzip-info.patch).

* Sat Dec 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.4-14]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment,
- added some pl man pages: gzip(1), zcmp(1), zdiff(1), zforce(1),
  zgrep(1), zmore(1), znew(1),
- standarized {un}registering info pages.

* Thu Sep 24 1998 Andrzej Nakonieczny <dzemik@shadow.eu.org>
  [1.2.4-13]
- added pl translation,
- changed buildroot for /tmp/%{name}-%{version}-root,
- added %%{name} and %%{version} macros in Source.
- added %defattr support,
- start at RH spec.
