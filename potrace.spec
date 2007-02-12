Summary:	Potrace - a utility for tracing a bitmap
Summary(pl.UTF-8):   Potrace - narzędzie służące do "trasowania" bitmap
Name:		potrace
Version:	1.7
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	8bfaabf935c03643a6875bde36fe6302
URL:		http://potrace.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image. The input is a portable bitmap
(PBM), and the default output is an encapsulated PostScript file
(EPS).

%description -l pl.UTF-8
Potrace jest narzędziem służącym do "trasowania" bitmap, czyli
konwertowania obrazów rastrowych do gładkich i skalowanych obrazów
wektorowych. Wejściem dla programu jest przenośna bitmapa (PBM), a
domyślnym wyjściem jest plik encapsulated PostScript (EPS).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-a4 \
	--enable-metric

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
