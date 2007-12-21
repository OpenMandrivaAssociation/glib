%define libname  %mklibname %{name} %{major}
%define major    1.2

Summary: A library of handy utility functions
Name: glib
Version: 1.2.10
Release: %mkrel 18
License: LGPL
Group: System/Libraries
Source: ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.bz2
# (fc) 1.2.10-3mdk Suppress warnings about varargs macros for -pedantic (Rawhide)
Patch0: glib-1.2.10-isowarning.patch
# (fc) 1.2.10-5mdk don't set -L/usr/lib in glib-config
Patch1: glib-1.2.10-libdir.patch
# (fc) 1.2.10-12mdk fix build with gcc 3.4 (Fedora)
Patch2: glib-1.2.10-gcc34.patch
# (fc) 1.2.10-13mdk fix underquoted m4 definitions
Patch3: glib-1.2.10-underquoted.patch
# (gb) 1.2.10-14mdk build static glib library with PIC as pam modules need it
Patch4: glib-1.2.10-pic.patch
# (gb) 1.2.10-17mdv use ancient libtool 1.4 with lib64 fixes
Patch5: glib-1.2.10-libtool.patch
%if %{mdkversion} >= 1010
BuildRequires: automake1.4, autoconf2.1
%else
BuildRequires: automake
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.gtk.org

%description
Glib is a handy library of utility functions. This C
library is designed to solve some portability problems
and provide other useful functionality which most
programs require.

Glib is used by GDK, GTK+ and many applications.
You should install Glib because many of your applications
will depend on this library.

%package -n %{libname}
Summary: Main library for glib
Group: System/Libraries
Provides: glib = %{version}-%{release}
Obsoletes: glib < %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with the glib.

%package -n %{libname}-devel
Summary: GIMP Toolkit and GIMP Drawing Kit support library
Group: Development/C
Requires: %{libname} = %{version}
Requires: pkgconfig
Provides: %{name}-devel = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Obsoletes: glib-devel < %{version}-%{release}

%description -n %{libname}-devel
Static libraries and header files for the support library for the GIMP's X
libraries, which are available as public libraries.  GLIB includes generally
useful data structures.

%prep
%setup -q
%patch0 -p1 -b .isowarnings
%patch1 -p1 -b .libdir
%patch2 -p1 -b .gcc34
%patch3 -p1 -b .underquoted
%patch4 -p1 -b .pic
%patch5 -p1 -b .libtool
automake-1.4
autoconf-2.13
libtoolize --copy --force

%build
%configure

%make

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/glib-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
%_install_info %{name}.info

%preun -n %{libname}-devel
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README COPYING docs/*.html
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*
%{_libdir}/glib
%{_includedir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*
%{_bindir}/*
%multiarch %{multiarch_bindir}/*
%{_infodir}/%{name}*
