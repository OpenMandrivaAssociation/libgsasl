%define major 7
%define libname %mklibname gsasl %major
%define develname %mklibname -d gsasl

%define _disable_rebuild_configure 1

Name:		libgsasl
Version:	1.10.0
Release:	2
Summary:	Implementation of the Simple Authentication and Security Layer framework
License:	LGPLv2+
Group:		System/Libraries
Source0:	ftp://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gsasl/
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(mit-krb5-gssapi)
BuildRequires:	pkgconfig(libntlm)
BuildRequires:	pkgconfig(libgcrypt)

%description
GNU SASL is an implementation of the Simple Authentication and 
Security Layer framework and a few common SASL mechanisms. SASL 
is used by network servers (e.g., IMAP, SMTP) to request 
authentication from clients, and in clients to authenticate against 
servers.

%files -f %{name}.lang
#--------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	Implementation of the Simple Authentication and Security Layer framework

%description -n %{libname}
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL
is used by network servers (e.g., IMAP, SMTP) to request
authentication from clients, and in clients to authenticate against
servers.

%files -n %{libname}
%{_libdir}/libgsasl.so.%{major}
%{_libdir}/libgsasl.so.%{major}.*

#--------------------------------------------------------------------

%package -n %{develname}
Group:		Development/C
Summary:	Implementation of the Simple Authentication and Security Layer framework
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL
is used by network servers (e.g., IMAP, SMTP) to request
authentication from clients, and in clients to authenticate against
servers.

%files -n %{develname}
%{_libdir}/pkgconfig/libgsasl.pc
%{_libdir}/libgsasl.so
%{_includedir}/gsasl-compat.h
%{_includedir}/gsasl-mech.h
%{_includedir}/gsasl.h

#-------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure --with-gssapi-impl=mit
%make_build

%install
%make_install
%find_lang %{name}
