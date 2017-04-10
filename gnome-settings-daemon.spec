#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-settings-daemon
Version  : 3.24.0
Release  : 8
URL      : http://ftp.gnome.org/pub/gnome/sources/gnome-settings-daemon/3.24/gnome-settings-daemon-3.24.0.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/gnome-settings-daemon/3.24/gnome-settings-daemon-3.24.0.tar.xz
Summary  : gnome-settings-daemon specific enumerations
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-settings-daemon-config
Requires: gnome-settings-daemon-lib
Requires: gnome-settings-daemon-bin
Requires: gnome-settings-daemon-data
Requires: gnome-settings-daemon-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libwacom-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-x11-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(gweather-3.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libwacom)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-wacom)
BuildRequires : pkgconfig(xtst)
BuildRequires : sed
Patch1: 0002-plugins-Use-usr-share-xdg-autostart-for-stateless-co.patch
Patch2: add_hidden.patch

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
Requires: gnome-settings-daemon-config

%description lib
lib components for the gnome-settings-daemon package.


%package locales
Summary: locales components for the gnome-settings-daemon package.
Group: Default

%description locales
locales components for the gnome-settings-daemon package.


%prep
%setup -q -n gnome-settings-daemon-3.24.0
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491784243
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -ffat-lto-objects -ffunction-sections -flto "
export FCFLAGS="$CFLAGS -O3 -Os -ffat-lto-objects -ffunction-sections -flto "
export FFLAGS="$CFLAGS -O3 -Os -ffat-lto-objects -ffunction-sections -flto "
export CXXFLAGS="$CXXFLAGS -O3 -Os -ffat-lto-objects -ffunction-sections -flto "
%reconfigure --disable-static --disable-network-manager --disable-smartcard-support --disable-schemas-compile --disable-cups
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1491784243
rm -rf %{buildroot}
%make_install
%find_lang gnome-settings-daemon

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/gsd-a11y-keyboard
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
/usr/libexec/gsd-orientation
/usr/libexec/gsd-power
/usr/libexec/gsd-rfkill
/usr/libexec/gsd-screensaver-proxy
/usr/libexec/gsd-sharing
/usr/libexec/gsd-sound
/usr/libexec/gsd-test-input-helper
/usr/libexec/gsd-wacom
/usr/libexec/gsd-wacom-led-helper
/usr/libexec/gsd-wacom-oled-helper
/usr/libexec/gsd-xrandr
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
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xrandr.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xsettings.gschema.xml
/usr/share/gnome-settings-daemon/datetime/backward
/usr/share/icons/hicolor/16x16/apps/gsd-xrandr.png
/usr/share/icons/hicolor/22x22/apps/gsd-xrandr.png
/usr/share/icons/hicolor/24x24/apps/gsd-xrandr.png
/usr/share/icons/hicolor/32x32/apps/gsd-xrandr.png
/usr/share/icons/hicolor/scalable/apps/gsd-xrandr.svg
/usr/share/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
/usr/share/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.A11yKeyboard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Clipboard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Mouse.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Orientation.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.XRANDR.desktop
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

