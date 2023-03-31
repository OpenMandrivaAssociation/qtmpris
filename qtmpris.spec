%define _empty_manifest_terminate_build 0

%define major 1
%define libname %mklibname qtmpris %{major}
%define devname %mklibname qtmpris -d

Name: qtmpris
Version: 1.0.6
Release: 2
Source0: https://github.com/sailfishos/qtmpris/archive/refs/tags/%{version}.tar.gz
Summary: MPRIS (Media Player Remote Interfacing Specification) v.2 implementation for Qt and QML
URL: https://github.com/qtmpris/qtmpris
License: LGPLv2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Widgets)

%description
MPRIS (Media Player Remote Interfacing Specification) v.2 implementation for Qt and QML

%package -n %{libname}
Summary: MPRIS (Media Player Remote Interfacing Specification) v.2 implementation for Qt and QML
Group: System/Libraries

%description -n %{libname}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
qmake-qt5 mpris-qt.pro

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/org/nemomobile/

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/qt5/mkspecs/features/mpris-qt5.prf
