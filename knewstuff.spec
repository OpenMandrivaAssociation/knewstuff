%define major 5
%define libname %mklibname KF5NewStuff %{major}
%define devname %mklibname KF5NewStuff -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
# Workaround for a build failure with clang 3.7, gold 2.26
# http://file-store.rosalinux.ru/api/v1/file_stores/9c718b3a47d628f0af10f7f5e1545b8ea9ff0852.log?show=true
%define _disable_lto 1

Name: knewstuff
Version:	5.38.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Support for downloading application assets from the network
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5Attica)
Requires: %{libname} = %{EVRD}

%description
Support for downloading application assets from the network.

%package -n %{libname}
Summary: Support for downloading application assets from the network
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Support for downloading application assets from the network.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 NewStuff library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Requires: cmake(KF5XmlGui)
Requires: cmake(KF5Attica)

%description -n %{devname}
Development files for the KDE Frameworks 5 NewStuff library.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/kf5/knewstuff
%{_datadir}/kf5/kmoretools
%{_libdir}/qt5/qml/org/kde/newstuff
%{_sysconfdir}/xdg/knewstuff.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
