Summary:	Potrace is a utility for tracing a bitmap
Summary(pl):	Potrace jest narzêdziem s³u¿acym do "trasowania" bitmap
Name:		potrace
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Utilities
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	a56ef0209eaf1fecbfd8def988ae12e8
URL:		http://potrace.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image. The input is a portable bitmap
(PBM), and the default output is an encapsulated PostScript file
(EPS).

%description -l pl
Potrace jest narzêdziem s³u¿±cym do konwertowania obrazów bitowych w
wektorowe. Wej¶ciem dla programu jest przeno¶na bitmapa (PBM), a
standardowym wyj¶ciem jest plik encapsulated PostScript (EPS).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/potrace.pdf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
