#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clutter-gst
Version  : 3.0.27
Release  : 14
URL      : https://download.gnome.org/sources/clutter-gst/3.0/clutter-gst-3.0.27.tar.xz
Source0  : https://download.gnome.org/sources/clutter-gst/3.0/clutter-gst-3.0.27.tar.xz
Summary  : Clutter GStreamer integration
Group    : Development/Tools
License  : LGPL-2.1
Requires: clutter-gst-data = %{version}-%{release}
Requires: clutter-gst-lib = %{version}-%{release}
Requires: clutter-gst-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(cogl-2.0-experimental)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : sed

%description
========================
Clutter-Gst is an integration library for using GStreamer with Clutter.
It provides a GStreamer sink to upload frames to GL and an actor that
implements the ClutterGstPlayer interface using playbin.

%package data
Summary: data components for the clutter-gst package.
Group: Data

%description data
data components for the clutter-gst package.


%package dev
Summary: dev components for the clutter-gst package.
Group: Development
Requires: clutter-gst-lib = %{version}-%{release}
Requires: clutter-gst-data = %{version}-%{release}
Provides: clutter-gst-devel = %{version}-%{release}
Requires: clutter-gst = %{version}-%{release}

%description dev
dev components for the clutter-gst package.


%package doc
Summary: doc components for the clutter-gst package.
Group: Documentation

%description doc
doc components for the clutter-gst package.


%package lib
Summary: lib components for the clutter-gst package.
Group: Libraries
Requires: clutter-gst-data = %{version}-%{release}
Requires: clutter-gst-license = %{version}-%{release}

%description lib
lib components for the clutter-gst package.


%package license
Summary: license components for the clutter-gst package.
Group: Default

%description license
license components for the clutter-gst package.


%prep
%setup -q -n clutter-gst-3.0.27
cd %{_builddir}/clutter-gst-3.0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664140489
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664140489
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clutter-gst
cp %{_builddir}/clutter-gst-%{version}/COPYING %{buildroot}/usr/share/package-licenses/clutter-gst/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/ClutterGst-3.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-aspectratio.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-camera-device.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-camera-manager.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-camera.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-content.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-crop.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-enum-types.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-playback.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-player.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-types.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-util.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-version.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst-video-sink.h
/usr/include/clutter-gst-3.0/clutter-gst/clutter-gst.h
/usr/lib64/libclutter-gst-3.0.so
/usr/lib64/pkgconfig/clutter-gst-3.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstAspectratio.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstCamera.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstCameraDevice.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstCameraManager.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstContent.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstCrop.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstPlayback.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ClutterGstPlayer.html
/usr/share/gtk-doc/html/clutter-gst-3.0/annotation-glossary.html
/usr/share/gtk-doc/html/clutter-gst-3.0/api-index-all.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ch01.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ch02.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ch03.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ch04.html
/usr/share/gtk-doc/html/clutter-gst-3.0/ch05.html
/usr/share/gtk-doc/html/clutter-gst-3.0/clutter-gst-3.0.devhelp2
/usr/share/gtk-doc/html/clutter-gst-3.0/clutter-gst-Types.html
/usr/share/gtk-doc/html/clutter-gst-3.0/clutter-gst-Utilities.html
/usr/share/gtk-doc/html/clutter-gst-3.0/clutter-gst-Versioning-Macros.html
/usr/share/gtk-doc/html/clutter-gst-3.0/clutter-gst-Video-Sink.html
/usr/share/gtk-doc/html/clutter-gst-3.0/home.png
/usr/share/gtk-doc/html/clutter-gst-3.0/index.html
/usr/share/gtk-doc/html/clutter-gst-3.0/left-insensitive.png
/usr/share/gtk-doc/html/clutter-gst-3.0/left.png
/usr/share/gtk-doc/html/clutter-gst-3.0/license.html
/usr/share/gtk-doc/html/clutter-gst-3.0/right-insensitive.png
/usr/share/gtk-doc/html/clutter-gst-3.0/right.png
/usr/share/gtk-doc/html/clutter-gst-3.0/style.css
/usr/share/gtk-doc/html/clutter-gst-3.0/up-insensitive.png
/usr/share/gtk-doc/html/clutter-gst-3.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libcluttergst3.so
/usr/lib64/libclutter-gst-3.0.so.0
/usr/lib64/libclutter-gst-3.0.so.0.27.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clutter-gst/01a6b4bf79aca9b556822601186afab86e8c4fbf
