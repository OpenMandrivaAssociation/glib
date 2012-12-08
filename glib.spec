%define libname  %mklibname %{name} %{major}
%define major    1.2

Summary:	A library of handy utility functions
Name:		glib
Version:	1.2.10
Release:	26
License:	LGPL
Group:		System/Libraries
URL:		http://www.gtk.org
Source:		ftp://ftp.gtk.org/pub/gtk/v1.2/%{name}-%{version}.tar.bz2
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

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with the glib.

%package -n %{libname}-devel
Summary:	GIMP Toolkit and GIMP Drawing Kit support library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
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
%doc COPYING
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%doc AUTHORS ChangeLog NEWS README COPYING docs/*.html
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/glib
%{_includedir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal/*
%{_bindir}/*
%{_infodir}/%{name}*


%changelog
* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 1.2.10-25mdv2012.0
+ Revision: 701661
- fix build with modern automake
- update build deps
- rebuild

* Thu Sep 24 2009 Olivier Blin <blino@mandriva.org> 1.2.10-24mdv2011.0
+ Revision: 448436
- fix build on x86_64 (using a similar config.{guess,sub} hack than the one done in freetype by rtp)
- fix build with libtool and autotools stuff, by taking most of
  changes from newer glib autotools stuff (from Arnaud Patard)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-22mdv2009.1
+ Revision: 317534
- fix build with -Werror=format-security (P7)

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-21mdv2009.0
+ Revision: 264552
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Anssi Hannula <anssi@mandriva.org> 1.2.10-20mdv2009.0
+ Revision: 212166
- fix underlinking (underlinking.patch)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-19mdv2008.1
+ Revision: 150110
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 16 2007 David Walluck <walluck@mandriva.org> 1.2.10-18mdv2008.0
+ Revision: 52375
- version Obsoletes
- explicitly call autoconf-2.13
- call libtoolize --copy --force
- place make check inside %%check section
- rebuild to add Provides: pkgconfig(gmodule)


* Tue Dec 05 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.2.10-17mdv2007.0
+ Revision: 91240
- use ancient libtool 1.4 with lib64 fixes
- bunzip2 patches, use mkrel
- Import glib

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2.10-16mdk
- Rebuild

* Tue Feb 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-15mdk 
- Multiarch
- fix rpmlint errors

* Thu Sep 30 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.10-14mdk
- build static glib library with PIC as pam modules need it

* Sat Aug 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-13mdk
- Update patch2 to remove __const__ call 
- Patch3 (Fedora) : fix underquoted m4 definitions

* Fri Jul 09 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-12mdk
- Patch2 (Fedora): fix build with gcc 3.4

