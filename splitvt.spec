%define debug_package %{nil}

Summary:	Split terminal into two windows
Name:		splitvt
Version:	1.6.6
Release:	7
License:	GPL
Group:		Terminals 
URL:		http://www.devolution.com/~slouken/projects/splitvt
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-destdir.patch
BuildRequires:	net-devel
BuildRequires:	termcap-devel

%description
This program takes any VT100 terminal window and splits it
into two shell windows, one on top and one on bottom.
It allows you to watch two terminal sessions at once, which can
be very useful whenever you want more screen real-estate without
messing with windows.

%prep

%setup -q
%patch0 -p0 -b .destdir

# lib64 fix
perl -pi -e "s|/usr/lib\b|%{_libdir}|g" config.c
perl -pi -e "s|\.a\b|\.so|g" config.c

%build
./configure
%make

%install
chmod 644 README BLURB ANNOUNCE CHANGES NOTES COPYING TODO
mkdir -p %buildroot%{_bindir}
mkdir -p %buildroot%{_mandir}/man1/

%makeinstall_std PREFIX=%_prefix MANDIR=%_mandir

chmod 755 %buildroot%{_bindir}/*

%clean

%files
%defattr(-,root,root)
%doc README BLURB ANNOUNCE CHANGES NOTES COPYING TODO
%_bindir/splitvt
%_bindir/xsplitvt
%attr(0644,root,root) %_mandir/man1/splitvt.1*



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.6-6mdv2011.0
+ Revision: 614950
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 1.6.6-5mdv2010.1
+ Revision: 509284
- gcc4 patch not needed

  + Thierry Vignaud <tv@mandriva.org>
    - relax BuildRequires
    - rebuild
    - fix man page permissions

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.6.6-4mdv2009.0
+ Revision: 260952
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.6.6-3mdv2009.0
+ Revision: 252958
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.6.6-1mdv2008.0
+ Revision: 20056
- 1.6.6


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:40:54 (54884)
- rebuild

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 16:37:20 (54883)
Import splitvt

* Sun Mar 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.5-6mdk
- rebuilt against libnet1.1.2
- fix deps

* Sat May 14 2005 Olivier Thauvin <nanardon@mandriva.org> 1.6.5-5mdk
- birthday rebuild

* Sun Apr 04 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.6.5-4mdk
- Birthday rebuild

