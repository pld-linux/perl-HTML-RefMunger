%include	/usr/lib/rpm/macros.perl
Summary:	HTML-RefMunger perl module
Summary(pl):	Modu³ perla HTML-RefMunger
Name:		perl-HTML-RefMunger
Version:	0.01
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-RefMunger-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-RefMunger is a module that will parse HTML files for HREF and IMG
tags and munge the links within them to suit various file naming
conventions. Supported formats for conversion are:
- MacOS - 32 character limit,
- MS-DOS - 8.3 character limit,
- UNIX - Some older UNIX platforms have a 14-character limit.

%description -l pl
HTML-RefMunger jest modu³em, który wyszukuje w plikach HTML znaczniki
HREF i IMG i przekszta³ca zawarte w nich odno¶niki tak, by pasowa³y do
okre¶lonych konwencji nazewnictwa. Wspierane formaty konwersji to:
- MacOS - do 32 znaków,
- MS-DOS - format 8.3,
- UNIX - niektóre starsze platformy zezwalaj± na nie wiêcej ni¿
  14-znakowe nazwy plików.

%prep
%setup -q -n HTML-RefMunger-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/refmunger
%{perl_sitelib}/HTML/RefMunger.pm
%{_mandir}/man[13]/*
