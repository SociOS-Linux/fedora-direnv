# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0

# Used by automated scanning tools to run tests
# https://bugzilla.redhat.com/show_bug.cgi?id=1358215#c8
%global provider        github
%global provider_tld    com
%global project         direnv
%global repo            direnv
# https://github.com/direnv/direnv
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
# Keep SHA in sync with tagged commits
%global commit          2bb2df4ca3bf3f45d1f36372c279615239e5c0f4

Name: direnv
Version: 2.9.0
Release: 6%{?dist}
Summary: Environment variable switcher for the shell
License: MIT
URL: http://direnv.net/
Source0: https://%{provider_prefix}/archive/v%{version}.tar.gz
# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
direnv is an environment switcher for the shell. It knows how to hook
into bash, zsh, tcsh and fish shell to load or unload environment
variables depending on the current directory. This allows
project-specific environment variables without cluttering the
"~/.profile" file.

%prep
%setup -q

%build
make %{?_smp_mflags} GO_LDFLAGS="-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 direnv %{buildroot}%{_bindir}

install -d -p %{buildroot}%{_mandir}/man1
install -p -m 0644 man/*.1 %{buildroot}%{_mandir}/man1

%check
make test

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-stdlib.1*
%{_bindir}/direnv

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 30 2016 Dominic Cleal <dominic@cleal.org> - 2.9.0-4
- Use repo macros in Source0, add comments
- Replace URL with correct homepage

* Tue Aug 30 2016 Dominic Cleal <dominic@cleal.org> - 2.9.0-3
- Add upstream commit and repo macros

* Tue Aug 30 2016 Dominic Cleal <dominic@cleal.org> - 2.9.0-2
- Fix make call to use parallel flag macro
- Fix default values of EA/BRs when macros aren't defined

* Wed Jul 20 2016 Dominic Cleal <dominic@cleal.org> - 2.9.0-1
- Initial build for Fedora
