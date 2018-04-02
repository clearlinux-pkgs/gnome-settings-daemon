#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-settings-daemon
Version  : 3.28.0
Release  : 28
URL      : https://download.gnome.org/sources/gnome-settings-daemon/3.28/gnome-settings-daemon-3.28.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-settings-daemon/3.28/gnome-settings-daemon-3.28.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-settings-daemon-config
Requires: gnome-settings-daemon-lib
Requires: gnome-settings-daemon-bin
Requires: gnome-settings-daemon-data
Requires: gnome-settings-daemon-locales
BuildRequires : colord
BuildRequires : cups-dev
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : krb5-dev
BuildRequires : libwacom-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(gweather-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(xorg-wacom)
BuildRequires : pkgconfig(xtst)
BuildRequires : python3
BuildRequires : qtbase-dev
Patch1: add_hidden.patch
Patch2: wakeups.patch
Patch3: no-suspend-on-ac.patch

%description


%package bin
Summary: bin components for the gnome-settings-daemon package.
Group: Binaries
Requires: gnome-settings-daemon-data
Requires: gnome-settings-daemon-config

%description bin
bin components for the gnome-settings-daemon package.


%package config
Summary: config components for the gnome-settings-daemon package.
Group: Default

%description config
config components for the gnome-settings-daemon package.


%package data
Summary: data components for the gnome-settings-daemon package.
Group: Data

%description data
data components for the gnome-settings-daemon package.


%package dev
Summary: dev components for the gnome-settings-daemon package.
Group: Development
Requires: gnome-settings-daemon-lib
Requires: gnome-settings-daemon-bin
Requires: gnome-settings-daemon-data
Provides: gnome-settings-daemon-devel

%description dev
dev components for the gnome-settings-daemon package.


%package lib
Summary: lib components for the gnome-settings-daemon package.
Group: Libraries
Requires: gnome-settings-daemon-data

%description lib
lib components for the gnome-settings-daemon package.


%package locales
Summary: locales components for the gnome-settings-daemon package.
Group: Default

%description locales
locales components for the gnome-settings-daemon package.


%prep
%setup -q -n gnome-settings-daemon-3.28.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522438742
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain  builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-settings-daemon
## make_install_append content
mkdir -p %{buildroot}/usr/share/xdg/
mv %{buildroot}/etc/xdg/* %{buildroot}/usr/share/xdg/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/gsd-a11y-settings
/usr/libexec/gsd-backlight-helper
/usr/libexec/gsd-clipboard
/usr/libexec/gsd-color
/usr/libexec/gsd-datetime
/usr/libexec/gsd-dummy
/usr/libexec/gsd-housekeeping
/usr/libexec/gsd-keyboard
/usr/libexec/gsd-locate-pointer
/usr/libexec/gsd-media-keys
/usr/libexec/gsd-mouse
/usr/libexec/gsd-power
/usr/libexec/gsd-print-notifications
/usr/libexec/gsd-printer
/usr/libexec/gsd-rfkill
/usr/libexec/gsd-screensaver-proxy
/usr/libexec/gsd-sharing
/usr/libexec/gsd-smartcard
/usr/libexec/gsd-sound
/usr/libexec/gsd-test-input-helper
/usr/libexec/gsd-wacom
/usr/libexec/gsd-wacom-led-helper
/usr/libexec/gsd-wacom-oled-helper
/usr/libexec/gsd-xsettings

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gnome-settings-daemon.convert
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.wacom.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.color.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.housekeeping.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.media-keys.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.sharing.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xsettings.gschema.xml
/usr/share/gnome-settings-daemon/datetime/backward
/usr/share/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
/usr/share/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Clipboard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Mouse.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-settings-daemon-3.0/gnome-settings-daemon/gsd-enums.h
/usr/lib64/pkgconfig/gnome-settings-daemon.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-settings-daemon-3.0/libgsd.so

%files locales -f gnome-settings-daemon.lang
%defattr(-,root,root,-)

