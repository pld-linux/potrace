Summary:	Potrace - a utility for tracing a bitmap
Summary(pl.UTF-8):	Potrace - narzędzie służące do "trasowania" bitmap
Name:		potrace
Version:	1.11
Release:	2
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	1d76e350ff277959e1f6b580d818d48f
URL:		http://potrace.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.0
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

%package devel
Summary:	Header file for potrace library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki potrace
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for potrace library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki potrace.

%package static
Summary:	Static potrace library
Summary(pl.UTF-8):	Statyczna biblioteka potrace
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static potrace library.

%description static -l pl.UTF-8
Statyczna biblioteka potrace.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-a4 \
	--enable-metric \
	--with-libpotrace

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/placement.pdf
%attr(755,root,root) %{_bindir}/mkbitmap
%attr(755,root,root) %{_bindir}/potrace
%attr(755,root,root) %{_libdir}/libpotrace.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpotrace.so.0
%{_mandir}/man1/mkbitmap.1*
%{_mandir}/man1/potrace.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpotrace.so
%{_libdir}/libpotrace.la
%{_includedir}/potracelib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpotrace.a
