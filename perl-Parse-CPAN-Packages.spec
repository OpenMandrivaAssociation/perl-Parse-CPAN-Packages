%define upstream_name    Parse-CPAN-Packages
%define upstream_version 2.33

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse 02packages.details.txt.gz
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(IO::Zlib)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
The Comprehensive Perl Archive Network (CPAN) is a very useful collection
of Perl code. It has several indices of the files that it hosts, including
a file named "02packages.details.txt.gz" in the "modules" directory. This
file contains lots of useful information and this module provides a simple
interface to the data contained within.

In a future release the Parse::CPAN::Packages::Package manpage and the
Parse::CPAN::Packages::Distribution manpage might have more information.

Methods
    * new

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.330.0-2mdv2011.0
+ Revision: 657819
- rebuild for updated spec-helper

* Wed Dec 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.330.0-1mdv2011.0
+ Revision: 625954
- update to new version 2.33

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.310.0-1mdv2010.0
+ Revision: 401618
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.31-1mdv2010.0
+ Revision: 369666
- update to new version 2.31

* Sat Jan 24 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30-1mdv2009.1
+ Revision: 333228
- adding missing prereq
- update to new version 2.30

* Mon Dec 08 2008 Jérôme Quelin <jquelin@mandriva.org> 2.29-1mdv2009.1
+ Revision: 311923
- missing prereq
- import perl-Parse-CPAN-Packages


* Mon Dec 08 2008 cpan2dist 2.29-1mdv
- initial mdv release, generated with cpan2dist

