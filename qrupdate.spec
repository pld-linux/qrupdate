Summary:	QRupdate - library for fast updating of QR and Cholesky decompositions
Summary(pl.UTF-8):	QRupdate - biblioteka do szybkiego uaktualniania rozkładów QR i Cholesky'ego
Name:		qrupdate
Version:	1.1.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/qrupdate/%{name}-%{version}.tar.gz
# Source0-md5:	7782c7ee6c234e56a72d6b86c1856fa0
URL:		http://qrupdate.sourceforge.net/
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QRupdate is a library for fast updating of QR and Cholesky
decompositions.

%description -l pl.UTF-8
QRupdate to biblioteka do szybkiego uaktualniania rozkładów QR i
Cholesky'ego

%package devel
Summary:	Development files for QRupdate library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki QRupdate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for QRupdate library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki QRupdate.

%package static
Summary:	Static QRupdate library
Summary(pl.UTF-8):	Statyczna biblioteka QRupdate
Group:		Development/Libraries
Requires:	blas-devel
Requires:	%{name}-devel = %{version}-%{release}
Requires:	lapack-devel

%description static
Static QRupdate library.

%description static -l pl.UTF-8
Statyczna biblioteka QRupdate.

%prep
%setup -q

%build
%{__make} lib solib \
	FC=gfortran \
	FFLAGS="%{rpmcflags}" \
	BLAS="%{rpmldflags} -lblas"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib}

# let rpm autodeps work
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libqrupdate.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libqrupdate.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libqrupdate.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqrupdate.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libqrupdate.a
