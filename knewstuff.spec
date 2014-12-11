%define major 5
%define libname %mklibname KF5NewStuff %{major}
%define devname %mklibname KF5NewStuff -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: knewstuff
Version: 5.4.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Support for downloading application assets from the network
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
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
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Support for downloading application assets from the network

%package -n %{libname}
Summary: Support for downloading application assets from the network
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Support for downloading application assets from the network

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 NewStuff library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 NewStuff library

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/kf5/knewstuff

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
