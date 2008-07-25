%define name	libgsasl
%define version	0.2.9
%define release	%mkrel 3
%define major 7
%define libname %mklibname gsasl %major
%define develname %mklibname -d gsasl

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Implementation of the Simple Authentication and Security Layer framework
License:	GPL
Group:		System/Libraries
Source:		%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gsasl/
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
GNU SASL is an implementation of the Simple Authentication and 
Security Layer framework and a few common SASL mechanisms. SASL 
is used by network servers (e.g., IMAP, SMTP) to request 
authentication from clients, and in clients to authenticate against 
servers.

%files -f %name.lang
%defattr(-,root,root)

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

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%_libdir/libgsasl.so.7
%_libdir/libgsasl.so.7.2.5

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
%defattr(-,root,root)
%_libdir/pkgconfig/libgsasl.pc
%_libdir/libgsasl.a
%_libdir/libgsasl.la
%_libdir/libgsasl.so
%_includedir/gsasl-compat.h
%_includedir/gsasl-mech.h
%_includedir/gsasl.h

#--------------------------------------------------------------------

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q 

%build
%configure
%make

%install 
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
