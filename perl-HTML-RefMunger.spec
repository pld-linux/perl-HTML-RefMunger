%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	RefMunger
Summary:	HTML::RefMunger perl module
Summary(pl):	Modu³ perla HTML::RefMunger
Name:		perl-HTML-RefMunger
Version:	0.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9dbaf3b7a2c8d3115695485392c3f729
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::RefMunger is a module that will parse HTML files for HREF and IMG
tags and munge the links within them to suit various file naming
conventions. Supported formats for conversion are:
- MacOS - 32 character limit,
- MS-DOS - 8.3 character limit,
- UNIX - Some older UNIX platforms have a 14-character limit.

%description -l pl
HTML::RefMunger jest modu³em, który wyszukuje w plikach HTML znaczniki
HREF i IMG i przekszta³ca zawarte w nich odno¶niki tak, by pasowa³y do
okre¶lonych konwencji nazewnictwa. Wspierane formaty konwersji to:
- MacOS - do 32 znaków,
- MS-DOS - format 8.3,
- UNIX - niektóre starsze platformy zezwalaj± na nie wiêcej ni¿
  14-znakowe nazwy plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/refmunger
%{perl_vendorlib}/HTML/RefMunger.pm
%{_mandir}/man[13]/*
