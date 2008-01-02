%define module  Test-MockObject
%define name    perl-%{module}
%define version 1.08
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl extension for emulating troublesome interfaces
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(UNIVERSAL::isa)
BuildRequires:  perl(UNIVERSAL::can)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(CGI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
It's a simple program that doesn't use any other modules, and those are easy to
test. More often, testing a program completely means faking up input to another
module, trying to coax the right output from something you're not supposed to
be testing anyway.

Testing is a lot easier when you can control the entire environment. With
Test::MockObject, you can get a lot closer.

Test::MockObject allows you to create objects that conform to particular
interfaces with very little code. You don't have to reimplement the behavior,
just the input and the output.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


