# NOTE:
# - it has been renamed to libdca
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	DTS Coherent Acoustics decoder
Summary(pl.UTF-8):	Dekoder DTS Coherent Acoustics
Name:		libdts
Version:	0.0.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdca/%{version}/libdca-%{version}.tar.bz2
# Source0-md5:	dab6b2795c66a82a6fcd4f8343343021
URL:		http://www.videolan.org/developers/libdca.html
Patch0:		%{name}-opt.patch
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
Free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality
multi-channel (5.1) digital audio format used in DVDs and DTS audio
CDs.

%description -l pl.UTF-8
Wolny dekoder formatu DTS Coherent Acoustics. Składa się z biblioteki
i dekodera działającego z linii poleceń. DTS jest wysokiej jakości
wielokanałowym (5.1) cyfrowym formatem audio używanym w DVD i DTS
audio CD.

%package devel
Summary:	Header files for libdts library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdts library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdts.

%package static
Summary:	Static libdts library
Summary(pl.UTF-8):	Statyczna biblioteka libdts
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdts library.

%description static -l pl.UTF-8
Statyczna biblioteka libdts.

%prep
%setup -q -n libdca-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/libdca.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
