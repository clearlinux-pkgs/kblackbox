#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kblackbox
Version  : 20.04.2
Release  : 21
URL      : https://download.kde.org/stable/release-service/20.04.2/src/kblackbox-20.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.2/src/kblackbox-20.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.2/src/kblackbox-20.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kblackbox-bin = %{version}-%{release}
Requires: kblackbox-data = %{version}-%{release}
Requires: kblackbox-license = %{version}-%{release}
Requires: kblackbox-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kblackbox-20.04.2
cd %{_builddir}/kblackbox-20.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591906331
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591906331
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kblackbox
cp %{_builddir}/kblackbox-20.04.2/COPYING %{buildroot}/usr/share/package-licenses/kblackbox/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kblackbox-20.04.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kblackbox/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
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
/usr/share/kxmlgui5/kblackbox/kblackboxui.rc
/usr/share/metainfo/org.kde.kblackbox.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kblackbox/index.cache.bz2
/usr/share/doc/HTML/de/kblackbox/index.docbook
/usr/share/doc/HTML/en/kblackbox/gameboard.png
/usr/share/doc/HTML/en/kblackbox/index.cache.bz2
/usr/share/doc/HTML/en/kblackbox/index.docbook
/usr/share/doc/HTML/es/kblackbox/index.cache.bz2
/usr/share/doc/HTML/es/kblackbox/index.docbook
/usr/share/doc/HTML/et/kblackbox/index.cache.bz2
/usr/share/doc/HTML/et/kblackbox/index.docbook
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
/usr/share/package-licenses/kblackbox/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kblackbox/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kblackbox.lang
%defattr(-,root,root,-)

