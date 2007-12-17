%define	module	DBIx-Class-HTMLWidget
%define name	perl-%{module}
%define	modprefix DBIx/Class/

%define version 0.11

%define	rel	1
%define release %mkrel %{rel}

Summary:	Like FromForm but with DBIx::Class and HTML::Widget
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/%{module}-%{version}.tar.gz
BuildRequires:	perl(HTML::Widget) >= 1.03
BuildArch:	noarch

%description
Something like Class::DBI::FromForm / Class::DBI::FromCGI but using
HTML::Widget for form creation and validation and DBIx::Class as a ORM.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


