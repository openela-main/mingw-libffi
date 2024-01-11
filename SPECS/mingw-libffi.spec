%?mingw_package_header

Name:		mingw-libffi
Version:	3.1
Release:	4%{?dist}
Summary:	A portable foreign function interface library for MinGW

License:	BSD
URL:		http://sourceware.org/libffi
Source0:	ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz

BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64

BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-binutils
BuildRequires:	mingw32-gcc

BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-binutils
BuildRequires:	mingw64-gcc


%description
Foreign function interface library for MinGW.


# Win32
%package -n mingw32-libffi
Summary:	A portable foreign function interface library for MinGW

%description -n mingw32-libffi
Foreign function interface library for MinGW.

# Win32 static
%package -n mingw32-libffi-static
Summary:       A portable foreign function interface static library for MinGW

%description -n mingw32-libffi-static
Foreign function interface static library for MinGW.


# Win64
%package -n mingw64-libffi
Summary:	A portable foreign function interface library for MinGW

%description -n mingw64-libffi
Foreign function interface library for MinGW.

# Win64 static
%package -n mingw64-libffi-static
Summary:       A portable foreign function interface static library for MinGW

%description -n mingw64-libffi-static
Foreign function interface static library for MinGW.


%?mingw_debug_package


%prep
%setup -q -n libffi-%{version}


%build
%mingw_configure --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-libffi
%license LICENSE
%doc README
%{mingw32_bindir}/libffi-6.dll
%{mingw32_libdir}/libffi.dll.a
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_libdir}/libffi-%{version}

%files -n mingw32-libffi-static
%{mingw32_libdir}/libffi.a

%files -n mingw64-libffi
%license LICENSE
%doc README
%{mingw64_bindir}/libffi-6.dll
%{mingw64_libdir}/libffi.dll.a
%{mingw64_libdir}/pkgconfig/*.pc
%{mingw64_libdir}/libffi-%{version}

%files -n mingw64-libffi-static
%{mingw64_libdir}/libffi.a


%changelog
* Tue Aug 14 2018 Victor Toso <victortoso@redhat.com> - 3.1-4
- ExclusiveArch: i686, x86_64
- Related: rhbz#1615874

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 3.1-1
- Update to 3.1
- Use license macro

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.13-3
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Fri May 31 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.13-2
- Rebuild against latest mingw-filesystem

* Sun May  5 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.13-1
- Update to 3.0.13

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.5.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.4.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Eric Smith <eric@brouhaha.com> - 3.0.11-0.3.rc2
- Added static subpackages

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.11-0.2.rc2
- Added win64 support

* Thu Mar 08 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.11-0.1.rc2
- Update to 3.0.11-rc2
- Removed .la file

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.0.9-5
- Renamed the source package to mingw-libffi (#800427)
- Spec clean up

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.9-4
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 9 2010 Paolo Bonzini <pbonzini@redhat.com> - 3.0.9-1
- Created.
