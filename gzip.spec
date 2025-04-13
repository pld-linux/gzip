Summary:	GNU gzip file compression
Summary(de.UTF-8):	Dateikomprimierung GNU-gzip
Summary(es.UTF-8):	Compresor de archivos gzip GNU
Summary(fr.UTF-8):	GNU gzip pour la compression de fichiers
Summary(pl.UTF-8):	GNU gzip
Summary(pt_BR.UTF-8):	Compressor de arquivos gzip GNU
Summary(ru.UTF-8):	Программа сжатия данных GNU gzip
Summary(tr.UTF-8):	GNU gzip dosya sıkıştırma aracı
Summary(uk.UTF-8):	Програма компресії даних GNU gzip
Name:		gzip
Version:	1.13
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://ftp.gnu.org/gnu/gzip/%{name}-%{version}.tar.xz
# Source0-md5:	d5c9fc9441288817a4a0be2da0249e29
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ea70155215d7b7d413ff476b668bcbbd
Patch0:		%{name}-mktemp.patch
Patch1:		%{name}-info.patch
URL:		http://www.gnu.org/software/gzip/
BuildRequires:	autoconf >= 2.63
%if "%{pld_release}" == "ac"
BuildRequires:	automake >= 1:1.10
%else
BuildRequires:	automake >= 1:1.11
%endif
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
Requires:	mktemp
Provides:	gzip(rsyncable)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the popular GNU file compression and decompression program,
gzip.

%description -l de.UTF-8
Dies ist das beliebte GNU-Dateikompressions- und
Dekompressionsprogramm, gzip.

%description -l es.UTF-8
Este es el popular programa GNU de compresión y descompresión de
archivos, gzip.

%description -l fr.UTF-8
Programme de compression et de décompression gzip de GNU

%description -l pl.UTF-8
GNU gzip to popularny program służący do kompresji i dekompresji
danych.

%description -l pt_BR.UTF-8
Este é o popular programa GNU de compressão e descompressão de
arquivos, gzip.

%description -l ru.UTF-8
Пакет gzip содержит популярную программу сжатия данных GNU gzip.
Сжатые ею файлы имеют расширение .gz.

%description -l tr.UTF-8
gzip, Unix işletim sistemlerinde çok yaygın olarak kullanılan bir
dosya sıkıştırma ve açma aracıdır.

%description -l uk.UTF-8
Пакет gzip містить популярну програму компресії даних GNU gzip.
Оброблені нею файли мають розширення .gz.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%if "%{pld_release}" == "ac"
%{__sed} -i -e '/AM_SILENT_RULES/d' configure.ac
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s,1\.11,1.10,' configure.ac
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s,dist-xz,,' configure.ac
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s,color-tests,,' configure.ac
%{__sed} -i -e '/AM_INIT_AUTOMAKE/s,parallel-tests,,' configure.ac
%endif

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LESS=/usr/bin/less \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,%{_mandir}/pt/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_bindir}/gzip $RPM_BUILD_ROOT/bin
%{__rm} $RPM_BUILD_ROOT%{_bindir}/gunzip $RPM_BUILD_ROOT%{_bindir}/zcat

cat > $RPM_BUILD_ROOT/bin/gunzip <<'EOF'
#!/bin/sh
exec /bin/gzip -d "$@"
EOF
cat > $RPM_BUILD_ROOT/bin/zcat <<'EOF'
#!/bin/sh
exec /bin/gzip -cd "$@"
EOF
ln -sf /bin/gzip $RPM_BUILD_ROOT%{_bindir}/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT%{_bindir}/gunzip

# conflicts with ncompress
%{__rm} $RPM_BUILD_ROOT%{_bindir}/uncompress

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/pt/*.1 $RPM_BUILD_ROOT%{_mandir}/pt/man1

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.gzip-non-english-man-pages*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/gzip-da_de_gzip.patch*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%attr(755,root,root) /bin/gzip
%attr(755,root,root) /bin/gunzip
%attr(755,root,root) /bin/zcat
%attr(755,root,root) %{_bindir}/gzexe
%attr(755,root,root) %{_bindir}/gzip
%attr(755,root,root) %{_bindir}/gunzip
%attr(755,root,root) %{_bindir}/zcmp
%attr(755,root,root) %{_bindir}/zdiff
%attr(755,root,root) %{_bindir}/zegrep
%attr(755,root,root) %{_bindir}/zfgrep
%attr(755,root,root) %{_bindir}/zforce
%attr(755,root,root) %{_bindir}/zgrep
%attr(755,root,root) %{_bindir}/zless
%attr(755,root,root) %{_bindir}/zmore
%attr(755,root,root) %{_bindir}/znew
%{_mandir}/man1/gzexe.1*
%{_mandir}/man1/gzip.1*
%{_mandir}/man1/gunzip.1*
%{_mandir}/man1/zcat.1*
%{_mandir}/man1/zcmp.1*
%{_mandir}/man1/zdiff.1*
%{_mandir}/man1/zforce.1*
%{_mandir}/man1/zgrep.1*
%{_mandir}/man1/zless.1*
%{_mandir}/man1/zmore.1*
%{_mandir}/man1/znew.1*
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
%lang(pt) %{_mandir}/pt/man1/*
%{_infodir}/gzip.info*
