%define name	libgsasl
%define version	1.8.0
%define release	3
%define major 7
%define libname %mklibname gsasl %major
%define develname %mklibname -d gsasl

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Implementation of the Simple Authentication and Security Layer framework
License:	LGPLv2+
Group:		System/Libraries
Source0:	ftp://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gsasl/

%description
GNU SASL is an implementation of the Simple Authentication and 
Security Layer framework and a few common SASL mechanisms. SASL 
is used by network servers (e.g., IMAP, SMTP) to request 
authentication from clients, and in clients to authenticate against 
servers.

%files -f %name.lang
#--------------------------------------------------------------------

%package -n %libname
Group: System/Libraries
Summary: Implementation of the Simple Authentication and Security Layer framework

%description -n %libname
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL
is used by network servers (e.g., IMAP, SMTP) to request
authentication from clients, and in clients to authenticate against
servers.

%files -n %libname
%_libdir/libgsasl.so.%{major}
%_libdir/libgsasl.so.%{major}.*

#--------------------------------------------------------------------

%package -n %develname
Group: Development/C
Summary: Implementation of the Simple Authentication and Security Layer framework
Requires: %libname = %version
Provides: %name-devel = %version-%release

%description -n %develname
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL
is used by network servers (e.g., IMAP, SMTP) to request
authentication from clients, and in clients to authenticate against
servers.

%files -n %develname
%_libdir/pkgconfig/libgsasl.pc
%_libdir/libgsasl.so
%_includedir/gsasl-compat.h
%_includedir/gsasl-mech.h
%_includedir/gsasl.h

#-------------------------------------------------------------------

%prep
%setup -q 

%build
%configure
%make

%install
%makeinstall_std
%find_lang %name


%changelog
* Tue May 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.8.0-1
+ Revision: 801090
- version update 1.8.0

* Mon Sep 27 2010 John Balcaen <mikala@mandriva.org> 1.4.4-1mdv2011.0
+ Revision: 581404
- Update to 1.4.4
- Use last stable release and update SOURCE url

* Sat Jun 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.29-1mdv2010.0
+ Revision: 383251
- update to new version 0.2.29

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 0.2.28-1mdv2009.0
+ Revision: 282158
- New version 0.2.28

* Sun Aug 17 2008 Emmanuel Andry <eandry@mandriva.org> 0.2.27-1mdv2009.0
+ Revision: 272932
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Mar 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2.9-1mdv2008.1
+ Revision: 177077
- import libgsasl

