# NOTE:
# - it has been renamed to libdca
# - distribution is temporarily suspended due to DTS Inc. patent clains (see URL)
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	DTS Coherent Acoustics decoder
Summary(pl):	Dekoder DTS Coherent Acoustics
Name:		libdts
Version:	0.0.2
Release:	3
License:	GPL
Group:		Libraries
#Source0:	http://download.videolan.org/pub/videolan/libdts/%{version}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	a1c0dac95d7031498c2d19d7a3107469
URL:		http://www.videolan.org/libdca.html
Patch0:		%{name}-shared.patch
Patch1:		%{name}-opt.patch
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

%description -l pl
Wolny dekoder formatu DTS Coherent Acoustics. Sk³ada siê z biblioteki
i dekodera dzia³aj±cego z linii poleceñ. DTS jest wysokiej jako¶ci
wielokana³owym (5.1) cyfrowym formatem audio u¿ywanym w DVD i DTS
audio CD.

%package devel
Summary:	Header files for libdts library
Summary(pl):	Pliki nag³ówkowe biblioteki libdts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdts library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libdts.

%package static
Summary:	Static libdts library
Summary(pl):	Statyczna biblioteka libdts
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdts library.

%description static -l pl
Statyczna biblioteka libdts.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

install libdts/dts_internal.h $RPM_BUILD_ROOT%{_includedir}

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
%doc doc/libdts.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
