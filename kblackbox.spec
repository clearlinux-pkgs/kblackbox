#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kblackbox
Version  : 22.12.2
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.12.2/src/kblackbox-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/kblackbox-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/kblackbox-22.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kblackbox-bin = %{version}-%{release}
Requires: kblackbox-data = %{version}-%{release}
Requires: kblackbox-license = %{version}-%{release}
Requires: kblackbox-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Program: KBlackBox
Authors:
Robert Cimrman, e-mail: cimrman3@students.zcu.cz
Nicolas Roffet, e-mail: nicolas-kde@roffet.com

%package bin
Summary: bin components for the kblackbox package.
Group: Binaries
Requires: kblackbox-data = %{version}-%{release}
Requires: kblackbox-license = %{version}-%{release}

%description bin
bin components for the kblackbox package.


%package data
Summary: data components for the kblackbox package.
Group: Data

%description data
data components for the kblackbox package.


%package doc
Summary: doc components for the kblackbox package.
Group: Documentation

%description doc
doc components for the kblackbox package.


%package license
Summary: license components for the kblackbox package.
Group: Default

%description license
license components for the kblackbox package.


%package locales
Summary: locales components for the kblackbox package.
Group: Default

%description locales
locales components for the kblackbox package.


%prep
%setup -q -n kblackbox-22.12.2
cd %{_builddir}/kblackbox-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675654533
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1675654533
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kblackbox
cp %{_builddir}/kblackbox-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kblackbox/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kblackbox-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kblackbox/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kblackbox-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kblackbox/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kblackbox-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kblackbox/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kblackbox-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kblackbox/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build
%make_install
popd
%find_lang kblackbox

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kblackbox

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kblackbox.desktop
/usr/share/icons/hicolor/128x128/apps/kblackbox.png
/usr/share/icons/hicolor/16x16/apps/kblackbox.png
/usr/share/icons/hicolor/22x22/apps/kblackbox.png
/usr/share/icons/hicolor/32x32/apps/kblackbox.png
/usr/share/icons/hicolor/48x48/apps/kblackbox.png
/usr/share/icons/hicolor/64x64/apps/kblackbox.png
/usr/share/kblackbox/pics/kblackbox.svgz
/usr/share/metainfo/org.kde.kblackbox.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kblackbox/gameboard.png
/usr/share/doc/HTML/ca/kblackbox/index.cache.bz2
/usr/share/doc/HTML/ca/kblackbox/index.docbook
/usr/share/doc/HTML/de/kblackbox/index.cache.bz2
/usr/share/doc/HTML/de/kblackbox/index.docbook
/usr/share/doc/HTML/en/kblackbox/gameboard.png
/usr/share/doc/HTML/en/kblackbox/index.cache.bz2
/usr/share/doc/HTML/en/kblackbox/index.docbook
/usr/share/doc/HTML/es/kblackbox/index.cache.bz2
/usr/share/doc/HTML/es/kblackbox/index.docbook
/usr/share/doc/HTML/et/kblackbox/index.cache.bz2
/usr/share/doc/HTML/et/kblackbox/index.docbook
/usr/share/doc/HTML/fr/kblackbox/index.cache.bz2
/usr/share/doc/HTML/fr/kblackbox/index.docbook
/usr/share/doc/HTML/it/kblackbox/index.cache.bz2
/usr/share/doc/HTML/it/kblackbox/index.docbook
/usr/share/doc/HTML/nl/kblackbox/index.cache.bz2
/usr/share/doc/HTML/nl/kblackbox/index.docbook
/usr/share/doc/HTML/pt/kblackbox/index.cache.bz2
/usr/share/doc/HTML/pt/kblackbox/index.docbook
/usr/share/doc/HTML/pt_BR/kblackbox/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kblackbox/index.docbook
/usr/share/doc/HTML/sv/kblackbox/index.cache.bz2
/usr/share/doc/HTML/sv/kblackbox/index.docbook
/usr/share/doc/HTML/uk/kblackbox/gameboard.png
/usr/share/doc/HTML/uk/kblackbox/index.cache.bz2
/usr/share/doc/HTML/uk/kblackbox/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kblackbox/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kblackbox/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kblackbox/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kblackbox/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kblackbox/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kblackbox.lang
%defattr(-,root,root,-)

