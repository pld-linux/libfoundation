%define		libf_makeflags	-w
%define		datatrunk	200503150006

Summary:	libFoundation Objective-C library
Summary(pl):	Biblioteka Objective-C libFoundation
Name:		libfoundation
Version:	r98
Release:	1
Vendor:		OpenGroupware.org
License:	libFoundation license
Group:		Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-%{version}-%{datatrunk}.tar.gz
# Source0-md5:	c28557d5e82d1909f64c74bdeff5d4c2
URL:		http://www.opengroupware.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make-devel >= 1.10.0
BuildRequires:	libobjc-lf2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}.%{release}-root-%(id -u -n)

%description
This package contains the libFoundation library, an Objective-C
library which aims to implement the Foundation part of the OpenStep
specification.

%description -l pl
Ten pakiet zawiera libFoundation - bibliotek� Objective-C, kt�rej
celem jest zaimplementowanie cz�ci Foundation ze specyfikacji
OpenStep.

%package devel
Summary:	The header files for the libFoundation Objective-C library
Summary(pl):	Pliki nag��wkowe biblioteki Objective-C libFoundation
Group:		Development/Libraries
Requires:	gnustep-make-devel >= 1.10.0
Requires:	%{name} = %{version}-%{release}

%description devel
libFoundation Objective-C development package.

%description devel -l pl
Pakiet programistyczny biblioteki Objective-C libFoundation.

%prep
%setup -q -n libfoundation

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
./configure
%{__make} %{libf_makeflags} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Makefiles/Additional

. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh

%{__make} %{libf_makeflags} install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Defaults
%attr(755,root,root) %{_libdir}/libFoundation*.so.*.*
%dir %{_datadir}/libFoundation
%{_datadir}/libFoundation/CharacterSets
%{_datadir}/libFoundation/Defaults
%{_datadir}/libFoundation/TimeZoneInfo

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFoundation*.so
%{_includedir}/lfmemory.h
%{_includedir}/real_exception_file.h
%{_includedir}/Foundation
%{_includedir}/extensions
%{_libdir}/GNUstep/System
