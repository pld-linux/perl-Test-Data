#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%define		pdir	Test
%define		pnam	Data
Summary:	Test::Data Perl module - test functions for particular variable types
Summary(pl.UTF-8):	Moduł Perla Test::Data - funkcje testujące typy określonych zmiennych
Name:		perl-Test-Data
Version:	1.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7ddba8cfb2e523d218ffd383926b580
URL:		http://search.cpan.org/dist/Test-Data/
BuildRequires:	perl-devel >= 1:5.8.7
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Prereq
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Test::Builder::Tester)
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Data Perl module provides utility functions to check properties
and values of data and variables.

%description -l pl.UTF-8
Moduł Perla Test::Data udostępnia funkcje usługowe sprawdzające
własności oraz wartości danych i zmiennych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/*.pm
%dir %{perl_vendorlib}/Test/Data
%{perl_vendorlib}/Test/Data/*.pm
%{_mandir}/man3/*
