
%define realname   Parse-CPAN-Packages
%define version    2.29
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Parse 02packages.details.txt.gz
Source:     http://www.cpan.org/modules/by-module/Parse/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(CPAN::DistnameInfo)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(IO::Zlib)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*


