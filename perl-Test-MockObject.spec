%define upstream_name    Test-MockObject
%define upstream_version 1.20140328

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Perl extension for emulating troublesome interfaces

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(UNIVERSAL::isa)
BuildRequires:	perl(UNIVERSAL::can)
BuildRequires:	perl(Test::Warn) >= 0.230
BuildRequires:	perl(Test::More) >= 0.980
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(CGI)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*



