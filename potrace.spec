Summary:	Potrace - a utility for tracing a bitmap
Summary(pl):	Potrace - narz�dzie s�u�ace do "trasowania" bitmap
Name:		potrace
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Utilities
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	f24018c4a7d65bf88fb55bbda543204d
URL:		http://potrace.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zlib-devel
Requires:	ncompress
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image. The input is a portable bitmap
(PBM), and the default output is an encapsulated PostScript file
(EPS).

%description -l pl
Potrace jest narz�dziem s�u��cym do "trasowania" bitmap, czyli
konwertowania obraz�w rastrowych do g�adkich i skalowanych obraz�w
wektorowych. Wej�ciem dla programu jest przeno�na bitmapa (PBM), a
domy�lnym wyj�ciem jest plik encapsulated PostScript (EPS).

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
