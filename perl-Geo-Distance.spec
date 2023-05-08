#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Geo-Distance
Version  : 0.25
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/Geo-Distance-0.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/Geo-Distance-0.25.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgeo-distance-perl/libgeo-distance-perl_0.20-4.debian.tar.xz
Summary  : 'Calculate distances and closest locations. (DEPRECATED)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-3.0
Requires: perl-Geo-Distance-license = %{version}-%{release}
Requires: perl-Geo-Distance-perl = %{version}-%{release}
Requires: perl(Const::Fast)
Requires: perl(GIS::Distance)
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
Geo::Distance - Calculate distances and closest locations. (DEPRECATED)
# SYNOPSIS

%package dev
Summary: dev components for the perl-Geo-Distance package.
Group: Development
Provides: perl-Geo-Distance-devel = %{version}-%{release}
Requires: perl-Geo-Distance = %{version}-%{release}

%description dev
dev components for the perl-Geo-Distance package.


%package license
Summary: license components for the perl-Geo-Distance package.
Group: Default

%description license
license components for the perl-Geo-Distance package.


%package perl
Summary: perl components for the perl-Geo-Distance package.
Group: Default
Requires: perl-Geo-Distance = %{version}-%{release}

%description perl
perl components for the perl-Geo-Distance package.


%prep
%setup -q -n Geo-Distance-0.25
cd %{_builddir}
tar xf %{_sourcedir}/libgeo-distance-perl_0.20-4.debian.tar.xz
cd %{_builddir}/Geo-Distance-0.25
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Geo-Distance-0.25/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Geo-Distance
cp %{_builddir}/Geo-Distance-0.25/LICENSE %{buildroot}/usr/share/package-licenses/perl-Geo-Distance/4a00d254c05e24e334448bc9019e3c4c8820f616
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Geo-Distance/efe1960f196dd212adbf29482417e5023045cb83
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Geo::Distance.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Geo-Distance/4a00d254c05e24e334448bc9019e3c4c8820f616
/usr/share/package-licenses/perl-Geo-Distance/efe1960f196dd212adbf29482417e5023045cb83

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
