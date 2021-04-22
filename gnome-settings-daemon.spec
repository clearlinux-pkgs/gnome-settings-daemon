#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-settings-daemon
Version  : 40.0.1
Release  : 58
URL      : https://download.gnome.org/sources/gnome-settings-daemon/40/gnome-settings-daemon-40.0.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-settings-daemon/40/gnome-settings-daemon-40.0.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-settings-daemon-config = %{version}-%{release}
Requires: gnome-settings-daemon-data = %{version}-%{release}
Requires: gnome-settings-daemon-lib = %{version}-%{release}
Requires: gnome-settings-daemon-libexec = %{version}-%{release}
Requires: gnome-settings-daemon-license = %{version}-%{release}
Requires: gnome-settings-daemon-locales = %{version}-%{release}
Requires: gnome-settings-daemon-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
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
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(gcr-base-3)
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
BuildRequires : pkgconfig(mm-glib)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(upower-glib)
BuildRequires : pkgconfig(xorg-wacom)
BuildRequires : pkgconfig(xtst)
Patch1: wakeups.patch
Patch2: no-suspend-on-ac.patch

%description
Introduction to GNOME Settings Daemon
===============================================================================

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
Requires: gnome-settings-daemon-lib = %{version}-%{release}
Requires: gnome-settings-daemon-data = %{version}-%{release}
Provides: gnome-settings-daemon-devel = %{version}-%{release}
Requires: gnome-settings-daemon = %{version}-%{release}

%description dev
dev components for the gnome-settings-daemon package.


%package extras
Summary: extras components for the gnome-settings-daemon package.
Group: Default

%description extras
extras components for the gnome-settings-daemon package.


%package lib
Summary: lib components for the gnome-settings-daemon package.
Group: Libraries
Requires: gnome-settings-daemon-data = %{version}-%{release}
Requires: gnome-settings-daemon-libexec = %{version}-%{release}
Requires: gnome-settings-daemon-license = %{version}-%{release}

%description lib
lib components for the gnome-settings-daemon package.


%package libexec
Summary: libexec components for the gnome-settings-daemon package.
Group: Default
Requires: gnome-settings-daemon-config = %{version}-%{release}
Requires: gnome-settings-daemon-license = %{version}-%{release}

%description libexec
libexec components for the gnome-settings-daemon package.


%package license
Summary: license components for the gnome-settings-daemon package.
Group: Default

%description license
license components for the gnome-settings-daemon package.


%package locales
Summary: locales components for the gnome-settings-daemon package.
Group: Default

%description locales
locales components for the gnome-settings-daemon package.


%package services
Summary: services components for the gnome-settings-daemon package.
Group: Systemd services

%description services
services components for the gnome-settings-daemon package.


%prep
%setup -q -n gnome-settings-daemon-40.0.1
cd %{_builddir}/gnome-settings-daemon-40.0.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619122614
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-settings-daemon
cp %{_builddir}/gnome-settings-daemon-40.0.1/COPYING %{buildroot}/usr/share/package-licenses/gnome-settings-daemon/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/gnome-settings-daemon-40.0.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-settings-daemon/caeb68c46fa36651acf592771d09de7937926bb3
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-settings-daemon
## install_append content
mkdir -p %{buildroot}/usr/share/xdg/
mv %{buildroot}/etc/xdg/* %{buildroot}/usr/share/xdg/
## install_append end

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/gnome-settings-daemon.convert
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.color.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.housekeeping.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.media-keys.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.sharing.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.wwan.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xsettings.gschema.xml
/usr/share/gnome-settings-daemon/datetime/backward
/usr/share/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
/usr/share/xdg/Xwayland-session.d/00-xrdb
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.UsbProtection.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.Wwan.desktop
/usr/share/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-settings-daemon-40/gnome-settings-daemon/gsd-enums.h
/usr/lib64/pkgconfig/gnome-settings-daemon.pc

%files extras
%defattr(-,root,root,-)
/usr/libexec/gsd-wacom
/usr/share/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.wacom.gschema.xml
/usr/share/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-settings-daemon-40/libgsd.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gsd-a11y-settings
/usr/libexec/gsd-backlight-helper
/usr/libexec/gsd-color
/usr/libexec/gsd-datetime
/usr/libexec/gsd-housekeeping
/usr/libexec/gsd-keyboard
/usr/libexec/gsd-media-keys
/usr/libexec/gsd-power
/usr/libexec/gsd-print-notifications
/usr/libexec/gsd-printer
/usr/libexec/gsd-rfkill
/usr/libexec/gsd-screensaver-proxy
/usr/libexec/gsd-sharing
/usr/libexec/gsd-smartcard
/usr/libexec/gsd-sound
/usr/libexec/gsd-usb-protection
/usr/libexec/gsd-wacom-oled-helper
/usr/libexec/gsd-wwan
/usr/libexec/gsd-xsettings

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-settings-daemon/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/gnome-settings-daemon/caeb68c46fa36651acf592771d09de7937926bb3

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-session-x11-services-ready.target.wants/org.gnome.SettingsDaemon.XSettings.service
/usr/lib/systemd/user/gnome-session-x11-services.target.wants/org.gnome.SettingsDaemon.XSettings.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.A11ySettings.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.A11ySettings.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Color.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Color.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Datetime.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Datetime.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Housekeeping.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Housekeeping.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Keyboard.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Keyboard.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.MediaKeys.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.MediaKeys.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Power.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Power.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.PrintNotifications.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.PrintNotifications.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Rfkill.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Rfkill.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.ScreensaverProxy.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.ScreensaverProxy.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Sharing.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Sharing.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Smartcard.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Smartcard.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Sound.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Sound.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.UsbProtection.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.UsbProtection.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Wacom.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Wacom.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Wwan.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.Wwan.target
/usr/lib/systemd/user/org.gnome.SettingsDaemon.XSettings.service
/usr/lib/systemd/user/org.gnome.SettingsDaemon.XSettings.target

%files locales -f gnome-settings-daemon.lang
%defattr(-,root,root,-)

