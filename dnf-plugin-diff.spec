Summary:	Show local changes in RPM packages
Name:		dnf-plugin-diff
Version:	1.1
Release:	3
License:	GPL v2+
Source0:	https://github.com/praiskup/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	85ecc6d16ff815280715a5dec02e8174
URL:		https://github.com/praiskup/dnf-plugin-diff
BuildRequires:	python3-modules
Requires:	cpio
Requires:	dnf
Requires:	file
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dnf plugin to diff the original package contents against the locally
changed files.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	PYTHON=%{__python3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libexecdir}/dnf-diff-*
%{py3_sitescriptdir}/dnf-plugins/*.py
%{py3_sitescriptdir}/dnf-plugins/__pycache__/*
