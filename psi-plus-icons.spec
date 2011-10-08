%define rev 20110924git1a6d4f7

Name:           psi-plus-icons
Version:        0.15
Release:        0.1%{rev}%{?dist}.R
Epoch:          2
BuildArch:      noarch
Summary:        Iconsets for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        %{name}-%{version}-20110924git1a6d4f7.tar.gz
Source1:        generate-tarball.sh

BuildRequires:  tar
Requires:       psi-plus >= 1:0.15-0.20.20110919git5117.R

%description
This package contains iconsets for Psi+.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/psi-plus/
%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/psi-plus/

%files
%defattr(-,root,root,-)
%{_datadir}/psi-plus/iconsets/*

%changelog
* Sat Sep 24 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.1.20110924git1a6d4f7.R
- Initial version of package
