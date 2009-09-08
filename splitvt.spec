Summary:	Split terminal into two windows
Name:		splitvt
Version:	1.6.6
Release:	%mkrel 5
License:	GPL
Group:		Terminals 
URL:		http://www.devolution.com/~slouken/projects/splitvt
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-destdir.patch
Patch1:		splitvt-1.6.5.gcc4.patch
BuildRequires:	libnet1.1.2-devel
BuildRequires:	libtermcap-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This program takes any VT100 terminal window and splits it
into two shell windows, one on top and one on bottom.
It allows you to watch two terminal sessions at once, which can
be very useful whenever you want more screen real-estate without
messing with windows.

%prep

%setup -q
%patch0 -p0 -b .destdir
%patch1 -p0 -b .gcc4

# lib64 fix
perl -pi -e "s|/usr/lib\b|%{_libdir}|g" config.c
perl -pi -e "s|\.a\b|\.so|g" config.c

%build
./configure
%make

%install
rm -rf $RPM_BUILD_ROOT

chmod 644 README BLURB ANNOUNCE CHANGES NOTES COPYING TODO
mkdir -p %buildroot%{_bindir}
mkdir -p %buildroot%{_mandir}/man1/

%makeinstall_std PREFIX=%_prefix MANDIR=%_mandir

chmod 755 %buildroot%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BLURB ANNOUNCE CHANGES NOTES COPYING TODO
%_bindir/splitvt
%_bindir/xsplitvt
%attr(0644,root,root) %_mandir/man1/splitvt.1*

