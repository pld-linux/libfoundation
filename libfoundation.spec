%define		libf_makeflags	-w
%define		__source	.

Summary:	libFoundation Objective-C library.
Name:		libfoundation
Version:	1.0
Release:	62.1
Vendor:		OpenGroupware.org
License:	libFoundation license
Group:		Development/Libraries
AutoReqProv:	off

Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-latest.tar.gz
#Patch0:
URL:		http://www.opengroupware.org

BuildRoot:	%{tmpdir}/%{name}-%{version}.%{release}-root-%(id -u -n)

Requires:	libobjc-lf2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	libobjc
BuildRequires:	gnustep-make >= 1.10.0
BuildRequires:	libobjc-lf2
BuildRequires:	libobjc-lf2-devel


%description
This package contains the libFoundation library, an Objective-C
library which aims to implement the Foundation part of the OpenStep
specification.

%package devel
Summary:	The header files for the libfoundation objective c library.
Group:		Development/Libraries
Requires:	gnustep-make >= 1.10.0
Requires:	%{name} = %{version}-%{release}
AutoReqProv:	off

%description devel
libFoundation objective-c development package.

%prep

%setup -q -n libfoundation


%build
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
./configure
%{__make} %{libf_makeflags} all


%install
rm -rf $RPM_BUILD_ROOT
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
install -d ${RPM_BUILD_ROOT}%{_libdir}
install -d ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Makefiles/Additional

%{__make} %{libf_makeflags} INSTALL_ROOT_DIR=${RPM_BUILD_ROOT} \
                       GNUSTEP_INSTALLATION_DIR=${RPM_BUILD_ROOT}%{_prefix} \
                       FHS_INSTALL_ROOT=${RPM_BUILD_ROOT}%{_prefix} \
                       install

rm -f ${RPM_BUILD_ROOT}%{_prefix}/GNUstep/System/Library/Headers/libFoundation/extensions/exceptions/FoundationException.h
rm -f ${RPM_BUILD_ROOT}%{_prefix}/GNUstep/System/Library/Headers/libFoundation/extensions/exceptions/GeneralExceptions.h
rm -f ${RPM_BUILD_ROOT}%{_prefix}/GNUstep/System/Library/Headers/libFoundation/extensions/exceptions/NSCoderExceptions.h



%post
if [ $1 = 1 ]; then
  if [ -d %{_sysconfdir}/ld.so.conf.d ]; then
    echo "/usr/lib" > %{_sysconfdir}/ld.so.conf.d/libfoundation.conf
  elif [ ! "`grep '/usr/lib' %{_sysconfdir}/ld.so.conf`" ]; then
    echo "/usr/lib" >> %{_sysconfdir}/ld.so.conf
  fi
  /sbin/ldconfig
fi


%postun
if [ $1 = 0 ]; then
  if [ -e %{_sysconfdir}/ld.so.conf.d/libfoundation.conf ]; then
    rm -f %{_sysconfdir}/ld.so.conf.d/libfoundation.conf
  fi
  /sbin/ldconfig
fi


%clean
rm -fr ${RPM_BUILD_ROOT}


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Defaults
%attr(755,root,root) %{_libdir}/libFoundation*.so.%{version}
# %attr(755,root,root) %{_libdir}/libFoundation*.so.1.0
%{_datadir}/libFoundation/CharacterSets
%{_datadir}/libFoundation/Defaults
%{_datadir}/libFoundation/TimeZoneInfo

%files devel
%defattr(644,root,root,755)
%dir %attr(755,root,root) %{_libdir}/GNUstep/System/Library/Makefiles/Additional
%{_libdir}/GNUstep/System/Library/Makefiles/Additional/libFoundation.make
%{_includedir}/lfmemory.h
%{_includedir}/real_exception_file.h
%{_includedir}/Foundation
%{_includedir}/extensions
%attr(755,root,root) %{_libdir}/libFoundation*.so
