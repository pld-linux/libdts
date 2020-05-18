# TODO: rename spec to libdca, swap Name/Provides?
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	DTS Coherent Acoustics streams decoder
Summary(pl.UTF-8):	Dekoder strumieni DTS Coherent Acoustics
Name:		libdts
Version:	0.0.7
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdca/%{version}/libdca-%{version}.tar.bz2
# Source0-md5:	68916db60e3017d92841f77908518a11
Patch0:		%{name}-opt.patch
Patch1:		%{name}-link.patch
URL:		http://www.videolan.org/developers/libdca.html
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.5
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.402
Provides:	libdca = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
Free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality
multi-channel (5.1) digital audio format used in DVDs and DTS audio
CDs.

%description -l pl.UTF-8
Wolnodostępny dekoder formatu DTS Coherent Acoustics. Składa się z
biblioteki i dekodera działającego z linii poleceń. DTS jest wysokiej
jakości wielokanałowym (5.1) cyfrowym formatem audio używanym w DVD i
DTS audio CD.

%package devel
Summary:	Header files for libdca library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdca
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libdca-devel = %{version}-%{release}

%description devel
Header files for libdca library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdca.

%package static
Summary:	Static libdca library
Summary(pl.UTF-8):	Statyczna biblioteka libdca
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libdca-static = %{version}-%{release}

%description static
Static libdca library.

%description static -l pl.UTF-8
Statyczna biblioteka libdca.

%package tools
Summary:	DTS Coherent Acoustics streams decoder tools
Summary(pl.UTF-8):	Narzędzia dekodera strumieni DTS Coherent Acoustics
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	libdca-tools = %{version}-%{release}

%description tools
DTS Coherent Acoustics streams decoder tools.

%description tools -l pl.UTF-8
Narzędzia dekodera strumieni DTS Coherent Acoustics.

%prep
%setup -q -n libdca-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdca.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libdca.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdca.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/libdca.txt
%attr(755,root,root) %{_libdir}/libdca.so
%{_includedir}/dca.h
%{_includedir}/dts.h
%{_pkgconfigdir}/libdca.pc
%{_pkgconfigdir}/libdts.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdca.a
%{_libdir}/libdts.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcadec
%attr(755,root,root) %{_bindir}/dtsdec
%attr(755,root,root) %{_bindir}/extract_dca
%attr(755,root,root) %{_bindir}/extract_dts
%{_mandir}/man1/dcadec.1*
%{_mandir}/man1/dtsdec.1*
%{_mandir}/man1/extract_dca.1*
%{_mandir}/man1/extract_dts.1*
