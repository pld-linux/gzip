Summary:     GNU gzip file compression
Summary(de): Dateikomprimierung GNU-gzip
Summary(fr): GNU gzip pour la compression de fichiers.
Summary(pl): GNU gzip
Summary(tr): GNU gzip dosya sýkýþtýrma aracý
Name:        gzip
Version:     1.2.4
Release:     13
Copyright:   GPL
Group:       Utilities/Archiving
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch:       %{name}-1.2.4-basename.patch
Patch1:      %{name}-1.2.4-gzexe.patch
Patch2:      %{name}-1.2.4-mktemp.patch
Prereq:      /sbin/install-info
Requires:    mktemp
Buildroot:   /tmp/%{name}-%{version}-root

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
%patch -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make 

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/man}

make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/bin/gzip

mv -f $RPM_BUILD_ROOT/usr/bin/gzip $RPM_BUILD_ROOT/bin/gzip
rm -f $RPM_BUILD_ROOT/usr/bin/gunzip $RPM_BUILD_ROOT/usr/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT/bin/gunzip
ln -sf /bin/gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT/usr/bin/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT/usr/bin/gunzip
gzip -9nf $RPM_BUILD_ROOT/usr/info/gzip.info*

for i in zcmp zdiff zforce zgrep zmore znew ; do
	sed -e "s|$RPM_BUILD_ROOT||g" < $RPM_BUILD_ROOT/usr/bin/$i > $RPM_BUILD_ROOT/usr/bin/.$i
	rm -f $RPM_BUILD_ROOT/usr/bin/$i
	mv $RPM_BUILD_ROOT/usr/bin/.$i $RPM_BUILD_ROOT/usr/bin/$i
done

cat > $RPM_BUILD_ROOT/usr/bin/zless <<EOF
#!/bin/sh
/bin/zcat "\$@" | /usr/bin/less
EOF

%post
/sbin/install-info /usr/info/gzip.info.gz /usr/info/dir --entry="* gzip: (gzip).                 The GNU compression utility."

%preun
/sbin/install-info --delete /usr/info/gzip.info.gz /usr/info/dir --entry="* gzip: (gzip).                 The GNU compression utility."

%files
%defattr (644, root, root, 755)
%doc NEWS README
%attr(755, root, root) /bin/*
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/info/gzip.info*

%changelog
* Thu Sep 24 1998 Andrzej Nakonieczny <dzemik@shadow.eu.org>
  [1.2.4-13]
- added pl translation,
- changed buildroot for /tmp/%{name}-%{version}-root,
- added %%{name} and %%{version} macros in Source.
- added %defattr support.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- added /usr/bin/gzip and /usr/bin/gunzip symlinks as some programs are too
  brain dead to figure out they should be at least trying to use $PATH
- added BuildRoot

* Wed Jan 28 1998 Erik Troan <ewt@redhat.com>
- fix /tmp races

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info
- applied patch for gzexe

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Marc Ewing <marc@redhat.com>
- (Entry added for Marc by Erik) fixed gzexe to use /bin/gzip
