#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Data
Summary:	Test::Data Perl module - test functions for particular variable types
Summary(pl):	Modu� Perla Test::Data - funkcje testuj�ce typy okre�lonych zmiennych
Name:		perl-Test-Data
Version:	1.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a9a9819cf2d91d85c731bb52742977f
BuildRequires:	perl-devel >= 1:5.8.7
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Prereq
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Test::Builder::Tester)
%endif
BuildRequires:	rpm-lib >= 3.0.3-1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Data Perl module provides utility functions to check properties
and values of data and variables.

%description -l pl
Modu� Perla Test::Data udost�pnia funkcje us�ugowe sprawdzaj�ce
w�asno�ci oraz warto�ci danych i zmiennych.

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
