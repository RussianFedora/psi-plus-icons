%define rev 20131101git1bb3532

Name:           psi-plus-icons
Version:        0.16
Release:        0.4.%{rev}%{?dist}
Epoch:          2
BuildArch:      noarch
Summary:        Iconsets for Psi+

License:        Unknown
URL:            http://code.google.com/p/psi-dev/
Source0:        http://files.psi-plus.com/sources/%{name}-%{version}-%{rev}.tar.gz
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
%{_datadir}/psi-plus/iconsets/*

%changelog
* Fri Nov  1 2013 Ivan Romanov <drizt@land.ru> - 2:0.16-0.4.20131101git1bb3532.R
- updated to 1bb3532

* Wed Jan 30 2013 Ivan Romanov <drizt@land.ru> - 2:0.16-0.3.20130130git4c189ec.R
- dropped non-free kolobok smiles

* Thu Jan 24 2013 Ivan Romanov <drizt@land.ru> - 2:0.16-0.2.20130124git4c189ec.R
- a new version
- dropped %%defattr
- tarball moved to http://files.psi-plus.com/sources

* Sun Oct 09 2011 Ivan Romanov <drizt@land.ru> - 0.15-0.1.20110924git1a6d4f7.R
- Initial version of package
