Summary:	Potrace - a utility for tracing a bitmap
Summary(pl):	Potrace - narzêdzie s³u¿ace do "trasowania" bitmap
Name:		potrace
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Utilities
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	8da9dc246770bae832610699beb27ec0
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

%description -l pl
Potrace jest narzêdziem s³u¿±cym do "trasowania" bitmap, czyli
konwertowania obrazów rastrowych do g³adkich i skalowanych obrazów
wektorowych. Wej¶ciem dla programu jest przeno¶na bitmapa (PBM), a
domy¶lnym wyj¶ciem jest plik encapsulated PostScript (EPS).

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

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README doc/potrace.pdf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
