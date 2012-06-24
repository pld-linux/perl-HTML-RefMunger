%include	/usr/lib/rpm/macros.perl
Summary:	HTML-RefMunger perl module
Summary(pl):	Modu� perla HTML-RefMunger
Name:		perl-HTML-RefMunger
Version:	0.01
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
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
HTML-RefMunger jest modu�em, kt�ry wyszukuje w plikach HTML znaczniki
HREF i IMG i przekszta�ca zawarte w nich odno�niki tak, by pasowa�y do
okre�lonych konwencji nazewnictwa. Wspierane formaty konwersji to:
- MacOS - do 32 znak�w,
- MS-DOS - format 8.3,
- UNIX - niekt�re starsze platformy zezwalaj� na nie wi�cej ni�
  14-znakowe nazwy plik�w.

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
