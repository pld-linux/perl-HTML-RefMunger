%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	HTML-RefMunger perl module
Summary(pl):	Modu³ perla HTML-RefMunger
Name:		perl-HTML-RefMunger
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-RefMunger-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTML-RefMunger is a module that will parse HTML files for HREF and IMG tags 
and munge the links within them to suit various file naming conventions.
Supported formats for conversion are:
    MacOS   -   32 character limit
    MS-DOS  -   8.3 character limit
    UNIX    -   Some older UNIX platforms have a 14-character limit

%description -l pl
HTML-RefMunger jest modu³em, który wyszukuje w plikach HTML znaczniki
HREF i IMG i przekszta³ca zawarte w nich odno¶niki tak, by pasowa³y
do okre¶lonych konwencji nazewnictwa. Wspierane formaty konwersji to:
    MacOS   -  do 32 znaków
    MS-DOS  -  format 8.3
    UNIX    -  niektóre starsze platformy zezwalaj± na nie wiêcej ni¿
               14-znakowe nazwy plików

%prep
%setup -q -n HTML-RefMunger-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/RefMunger
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/refmunger

%{perl_sitelib}/HTML/RefMunger.pm
%{perl_sitearch}/auto/HTML/RefMunger

%{_mandir}/man[13]/*
