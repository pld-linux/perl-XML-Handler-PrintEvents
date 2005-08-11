#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Handler-PrintEvents
Summary:	XML::Handler::PrintEvents - prints PerlSAX events (for debugging)
Summary(pl):	XML::Handler::PrintEvents - wypisywanie zdarzeñ PerlSAX (dla odpluskwiania)
Name:		perl-XML-Handler-PrintEvents
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd3b3d840d98bca3e11f9dad34364da4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Filter-SAXT
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This PerlSAX handler prints the PerlSAX events it receives to STDOUT.
It can be useful when debugging PerlSAX filters. It supports all
PerlSAX handler including ignorable_whitespace.

%description -l pl
Ten modu³ obs³ugi PerlSAX wypisuje otrzymywane zdarzenia PerlSAX na
standardowe wyj¶cie. Mo¿e to byæ przydatne przy odpluskwianiu filtrów
PerlSAX. Obs³uguje wszystkie funkcje obs³ugi PerlSAX w³±cznie z
ignorable_whitespace.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Handler/PrintEvents.pm
%{_mandir}/man3/*
