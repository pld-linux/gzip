Summary:	GNU gzip file compression
Summary(de):	Dateikomprimierung GNU-gzip
Summary(fr):	GNU gzip pour la compression de fichiers.
Summary(pl):	GNU gzip
Summary(tr):	GNU gzip dosya sýkýþtýrma aracý
Name:		gzip
Version:	1.2.4
Release:	20
License:	GPL
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Group(pl):	Narzêdzia/Archiwizacja
Source:		ftp://alpha.gnu.org/gnu/%{name}-%{version}.tar.gz
Patch0:		gzip-basename.patch
Patch1:		gzip-gzexe.patch
Patch2:		gzip-mktemp.patch
Patch3:		gzip-info.patch
Patch4:		gzip-plman.patch
Prereq:		/usr/sbin/fix-info-dir
Requires:	mktemp
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is the popular GNU file compression and decompression program, gzip.

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
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure
make LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,%{_mandir}/pl/man1}

make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	infodir=$RPM_BUILD_ROOT/%{_infodir}

mv -f $RPM_BUILD_ROOT%{_bindir}/gzip $RPM_BUILD_ROOT/bin/gzip
rm -f $RPM_BUILD_ROOT%{_bindir}/gunzip $RPM_BUILD_ROOT%{_bindir}/zcat

ln -sf /bin/gzip $RPM_BUILD_ROOT/bin/gunzip
ln -sf /bin/gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT%{_bindir}/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT%{_bindir}/gunzip

for i in zcmp zdiff zforce zgrep zmore znew ; do
	sed -e "s|$RPM_BUILD_ROOT||g" < $RPM_BUILD_ROOT%{_bindir}/$i > $RPM_BUILD_ROOT%{_bindir}/.$i
	rm -f $RPM_BUILD_ROOT%{_bindir}/$i
	mv $RPM_BUILD_ROOT%{_bindir}/.$i $RPM_BUILD_ROOT%{_bindir}/$i
done

cat > $RPM_BUILD_ROOT%{_bindir}/zless <<EOF
#!/bin/sh
/bin/zcat "\$@" | %{_bindir}/less
EOF

install pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9nf NEWS README \
	$RPM_BUILD_ROOT{%{_infodir}/gzip.info*,%{_mandir}/{man1/*,pl/man1/*}}

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
