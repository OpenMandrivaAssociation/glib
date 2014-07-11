%define api	1.2
%define major	0
%define libname		%mklibname %{name} %{api} %{major}
%define libgmodule	%mklibname gmodule %{api} %{major}
%define libgthread	%mklibname gthread %{api} %{major}
%define devname		%mklibname %{name} -d %{api}

Summary:	A library of handy utility functions
Name:		glib
Version:	1.2.10
Release:	33
License:	LGPLv2.1
Group:		System/Libraries
Url:		http://www.gtk.org
Source0:	ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
# (fc) 1.2.10-3mdk Suppress warnings about varargs macros for -pedantic (Rawhide)
Patch0:		glib-1.2.10-isowarning.patch
# (fc) 1.2.10-5mdk don't set -L/usr/lib in glib-config
Patch1:		glib-1.2.10-libdir.patch
# (fc) 1.2.10-12mdk fix build with gcc 3.4 (Fedora)
Patch2:		glib-1.2.10-gcc34.patch
# (fc) 1.2.10-13mdk fix underquoted m4 definitions
Patch3:		glib-1.2.10-underquoted.patch
# (gb) 1.2.10-14mdk build static glib library with PIC as pam modules need it
Patch4:		glib-1.2.10-pic.patch
# (gb) 1.2.10-17mdv use ancient libtool 1.4 with lib64 fixes
Patch5:		glib-1.2.10-libtool.patch
# (Anssi 05/2008) Fix underlinking
Patch6:		glib-1.2.10-underlinking.patch
Patch7:		glib-1.2.10-format_not_a_string_literal_and_no_format_arguments.diff
Patch8:		glib_divert.patch
Patch9:		glib-fix-automake.patch
Patch10:	glib-1.2.10-automake-1.13.patch
BuildRequires:	libtool

%description
Glib is a handy library of utility functions. This C
library is designed to solve some portability problems
and provide other useful functionality which most
programs require.

Glib is used by GDK, GTK+ and many applications.
You should install Glib because many of your applications
will depend on this library.

%package -n %{libname}
Summary:	Main library for glib
Group:		System/Libraries
Provides:	glib = %{version}-%{release}
Obsoletes:	%{_lib}glib1.2 < 1.2.10-27

%description -n %{libname}
This package contains a library needed to run programs dynamically
linked with the glib.

%package -n %{libgmodule}
Summary:	Main library for glib
Group:		System/Libraries
Obsoletes:	%{_lib}glib1.2 < 1.2.10-27

%description -n %{libgmodule}
This package contains a library needed to run programs dynamically
linked with the glib.

%package -n %{libgthread}
Summary:	Main library for glib
Group:		System/Libraries
Obsoletes:	%{_lib}glib1.2 < 1.2.10-27

%description -n %{libgthread}
This package contains a library needed to run programs dynamically
linked with the glib.

%package -n %{devname}
Summary:	GIMP Toolkit and GIMP Drawing Kit support library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libgmodule} = %{version}
Requires:	%{libgthread} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Static libraries and header files for the support library for the GIMP's X
libraries, which are available as public libraries.  GLIB includes generally
useful data structures.

%prep
%setup -q
%apply_patches

aclocal
libtoolize --install --force
rm -f config.{guess,sub}
automake --foreign -a -c
autoconf

%build
%configure2_5x --disable-static
%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libglib-%{api}.so.%{major}*

%files -n %{libgmodule}
%{_libdir}/libgmodule-%{api}.so.%{major}*

%files -n %{libgthread}
%{_libdir}/libgthread-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README COPYING docs/*.html
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/glib
%{_includedir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*
%{_bindir}/*
%{_infodir}/%{name}*

