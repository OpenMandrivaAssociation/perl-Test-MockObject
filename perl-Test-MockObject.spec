%define upstream_name    Test-MockObject
%define upstream_version 1.20120301

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.20120301
Release:	1

Summary:	Perl extension for emulating troublesome interfaces
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-MockObject-1.20120301.tar.gz

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


%changelog
* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.201.106.120-1mdv2011.0
+ Revision: 685758
- new version

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 405555
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.09-2mdv2009.0
+ Revision: 268736
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2009.0
+ Revision: 212228
- update to new version 1.09

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.0
+ Revision: 47737
- update to new version 1.08


* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2007.0
+ Revision: 84321
- new version
- Import perl-Test-MockObject

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-2mdv2007.0
- Rebuild

* Tue Apr 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdk
- New release 1.06
- better source URL
- better buildrequires syntax

* Wed Apr 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdk
- New release 1.05
- better source URL

* Mon Mar 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdk
- New release 1.04

* Tue Mar 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdk
- New release 1.03

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdk
- New release 1.02

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-3mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-2mdk
- Fix BuildRequires

* Wed Sep 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- New release 1.01

* Tue Jul 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdk
- New release 1.00
- spec cleanup
- test in %%check
- fix source url

* Tue Dec 21 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.20-1mdk
- 0.20

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.14-2mdk
- fix buildrequires in a backward compatible way

* Mon Sep 13 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.14-1mdk 
- first mdk release


