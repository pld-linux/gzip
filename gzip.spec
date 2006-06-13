# TODO
# - security http://www.gentoo.org/security/en/glsa/glsa-200505-05.xml
Summary:	GNU gzip file compression
Summary(de):	Dateikomprimierung GNU-gzip
Summary(es):	Compresor de archivos gzip GNU
Summary(fr):	GNU gzip pour la compression de fichiers
Summary(pl):	GNU gzip
Summary(pt_BR):	Compressor de arquivos gzip GNU
Summary(ru):	ðÒÏÇÒÁÍÍÁ ÓÖÁÔÉÑ ÄÁÎÎÙÈ GNU gzip
Summary(tr):	GNU gzip dosya sýkýþtýrma aracý
Summary(uk):	ðÒÏÇÒÁÍÁ ËÏÍÐÒÅÓ¦§ ÄÁÎÉÈ GNU gzip
Name:		gzip
Version:	1.3.5
Release:	8.1
License:	GPL
Group:		Applications/Archiving
# 1.2.x versions only
#Source0:	ftp://ftp.gnu.org/gnu/gzip/%{name}-%{version}.tar.gz
# not present at the moment, but can be found on alpha.gnu mirrors
Source0:	ftp://alpha.gnu.org/gnu/gzip/%{name}-%{version}.tar.gz
# Source0-md5:	3d6c191dfd2bf307014b421c12dc8469
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ea70155215d7b7d413ff476b668bcbbd
Patch0:		%{name}-mktemp.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-stderr.patch
Patch3:		%{name}-zgreppipe.patch
Patch4:		%{name}-noppid.patch
Patch5:		%{name}-segfault.patch
Patch6:		%{name}-dir-traversal.patch
Patch7:		%{name}-rsyncable.patch
URL:		http://www.gnu.org/software/gzip/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	texinfo
Requires:	mktemp
Provides:	gzip(rsyncable)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the popular GNU file compression and decompression program,
gzip.

%description -l de
Dies ist das beliebte GNU-Dateikompressions- und
Dekompressionsprogramm, gzip.

%description -l es
Este es el popular programa GNU de compresión y descompresión de
archivos, gzip.

%description -l fr
Programme de compression et de décompression gzip de GNU

%description -l pl
GNU gzip to popularny program s³u¿±cy do kompresji i dekompresji
danych.

%description -l pt_BR
Este é o popular programa GNU de compressão e descompressão de
arquivos, gzip.

%description -l ru
ðÁËÅÔ gzip ÓÏÄÅÒÖÉÔ ÐÏÐÕÌÑÒÎÕÀ ÐÒÏÇÒÁÍÍÕ ÓÖÁÔÉÑ ÄÁÎÎÙÈ GNU gzip.
óÖÁÔÙÅ ÅÀ ÆÁÊÌÙ ÉÍÅÀÔ ÒÁÓÛÉÒÅÎÉÅ .gz.

%description -l tr
gzip, Unix iþletim sistemlerinde çok yaygýn olarak kullanýlan bir
dosya sýkýþtýrma ve açma aracýdýr.

%description -l uk
ðÁËÅÔ gzip Í¦ÓÔÉÔØ ÐÏÐÕÌÑÒÎÕ ÐÒÏÇÒÁÍÕ ËÏÍÐÒÅÓ¦§ ÄÁÎÉÈ GNU gzip.
ïÂÒÏÂÌÅÎ¦ ÎÅÀ ÆÁÊÌÉ ÍÁÀÔØ ÒÏÚÛÉÒÅÎÎÑ .gz.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
# this fixes reading "window" array out of bounds (sometimes causing
# producing of little bigger .gz files, but I couldn't find better fix)
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
rm -f missing
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,%{_mandir}/pt/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/gzip $RPM_BUILD_ROOT/bin
rm -f $RPM_BUILD_ROOT%{_bindir}/gunzip $RPM_BUILD_ROOT%{_bindir}/zcat

ln -sf gzip $RPM_BUILD_ROOT/bin/gunzip
ln -sf gzip $RPM_BUILD_ROOT/bin/zcat
ln -sf /bin/gzip $RPM_BUILD_ROOT%{_bindir}/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT%{_bindir}/gunzip

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
mv $RPM_BUILD_ROOT%{_mandir}/pt/*.1 $RPM_BUILD_ROOT%{_mandir}/pt/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
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
%lang(pt) %{_mandir}/pt/man1/*
%{_infodir}/gzip.info*
