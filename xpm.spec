#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	Cross package maker. DEB/RPM generation or conversion
Name:		xpm
Version:	1.3.3.6
Release:	0.2
License:	MIT-like
Group:		Development/Languages
Source0:	http://fossil.include-once.org/xpm/tarball/%{name}-%{version}.tar.gz?uuid=v%{version}&/%{name}-%{version}.tar.gz
# Source0-md5:	f73ececfa6725965fc41d4e11ea85992
Patch0:	templates.patch
URL:		http://fossil.include-once.org/xpm/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-insist < 0.1
BuildRequires:	ruby-insist >= 0.0.5
BuildRequires:	ruby-pry
BuildRequires:	ruby-rspec < 3.1
BuildRequires:	ruby-rspec >= 3.0.0
BuildRequires:	ruby-stud
%endif
Requires:	ruby-arr-pm < 0.1
Requires:	ruby-arr-pm >= 0.0.9
Requires:	ruby-backports >= 2.6.2
Requires:	ruby-cabin >= 0.6.0
Requires:	ruby-childprocess
Requires:	ruby-clamp < 1
Requires:	ruby-clamp >= 0.6
Requires:	ruby-ffi
Requires:	ruby-json >= 1.7.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fpm greatly simplifies distribution package generation. xpm is a
feature-oriented branch of fpm.

It creates or converts between:
- Debian deb
- RedHat rpm
- Node npm
- OSX pkg
- Ruby gem
- Solaris packages, plain zip or tar archives, and a few more...

%prep
%setup -q
%patch0 -p1
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a templates $RPM_BUILD_ROOT%{ruby_vendorlibdir}/fpm
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELIST CODE_OF_CONDUCT.md CONTRIBUTORS NOTES.md LICENSE
%attr(755,root,root) %{_bindir}/xpm
%{ruby_vendorlibdir}/fpm.rb
%{ruby_vendorlibdir}/fpm
