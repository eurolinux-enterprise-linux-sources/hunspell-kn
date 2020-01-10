Name: hunspell-kn
Summary: Kannada hunspell dictionaries
Version: 1.0.3
Release: 6%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/2628/1/kannada.oxt
URL: http://extensions.services.openoffice.org/project/kannada
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Kannada hunspell dictionaries.

%prep
%setup -q -c -n hunspell-kn

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p kn_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_kn_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> - 1.0.3-1
- initial version
