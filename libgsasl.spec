%define name	libgsasl
%define version	1.8.0
%define release	1
%define major 7
%define libname %mklibname gsasl %major
%define develname %mklibname -d gsasl
%define develnamest %mklibname -d -s gsasl

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

%package -n %develnamest
Group: Development/C
Summary: Implementation of the Simple Authentication and Security Layer framework
Requires: %libname = %version
Provides: %name-devel-static = %version-%release
Requires: %name-devel = %version-%release

%description -n %develnamest
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL
is used by network servers (e.g., IMAP, SMTP) to request
authentication from clients, and in clients to authenticate against
servers.

%files -n %develnamest
%_libdir/libgsasl.a

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %name
