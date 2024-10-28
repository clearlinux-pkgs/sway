#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : sway
Version  : 1.10
Release  : 40
URL      : https://github.com/swaywm/sway/archive/1.10/sway-1.10.tar.gz
Source0  : https://github.com/swaywm/sway/archive/1.10/sway-1.10.tar.gz
Summary  : i3-compatible Wayland compositor
Group    : Development/Tools
License  : CC0-1.0 MIT
Requires: sway-bin = %{version}-%{release}
Requires: sway-data = %{version}-%{release}
Requires: sway-license = %{version}-%{release}
Requires: sway-man = %{version}-%{release}
Requires: xkeyboard-config
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fish)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(scdoc)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(wlroots-0.18)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : wayland-protocols-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# sway
sway
هو مدير للمجموعات المركبة لـ[Wayland] متوافق مع [i3] -
إقرأ [الأسئلة الشائعة](https://github.com/swaywm/sway/wiki)

%package bin
Summary: bin components for the sway package.
Group: Binaries
Requires: sway-data = %{version}-%{release}
Requires: sway-license = %{version}-%{release}

%description bin
bin components for the sway package.


%package data
Summary: data components for the sway package.
Group: Data

%description data
data components for the sway package.


%package license
Summary: license components for the sway package.
Group: Default

%description license
license components for the sway package.


%package man
Summary: man components for the sway package.
Group: Default

%description man
man components for the sway package.


%prep
%setup -q -n sway-1.10
cd %{_builddir}/sway-1.10
pushd ..
cp -a sway-1.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730148865
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/sway
cp %{_builddir}/sway-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/sway/7dfd46ff6b01e0649f270341bfb06d662a4f9ee9 || :
cp %{_builddir}/sway-%{version}/assets/LICENSE %{buildroot}/usr/share/package-licenses/sway/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/sway
/V3/usr/bin/swaybar
/V3/usr/bin/swaymsg
/V3/usr/bin/swaynag
/usr/bin/sway
/usr/bin/swaybar
/usr/bin/swaymsg
/usr/bin/swaynag

%files data
%defattr(-,root,root,-)
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_1136x640.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_1136x640_Portrait.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_1366x768.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_1920x1080.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_2048x1536.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_2048x1536_Portrait.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_768x1024.png
/usr/share/backgrounds/sway/Sway_Wallpaper_Blue_768x1024_Portrait.png
/usr/share/bash-completion/completions/sway
/usr/share/bash-completion/completions/swaybar
/usr/share/bash-completion/completions/swaymsg
/usr/share/fish/vendor_completions.d/sway.fish
/usr/share/fish/vendor_completions.d/swaymsg.fish
/usr/share/fish/vendor_completions.d/swaynag.fish
/usr/share/wayland-sessions/sway.desktop
/usr/share/zsh/site-functions/_sway
/usr/share/zsh/site-functions/_swaymsg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sway/7dfd46ff6b01e0649f270341bfb06d662a4f9ee9
/usr/share/package-licenses/sway/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sway.1
/usr/share/man/man1/swaymsg.1
/usr/share/man/man1/swaynag.1
/usr/share/man/man5/sway-bar.5
/usr/share/man/man5/sway-input.5
/usr/share/man/man5/sway-output.5
/usr/share/man/man5/sway.5
/usr/share/man/man5/swaynag.5
/usr/share/man/man7/sway-ipc.7
/usr/share/man/man7/swaybar-protocol.7
