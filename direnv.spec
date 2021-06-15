# Generated by go2rpm 1
%bcond_without check

# https://github.com/direnv/direnv
%global goipath         github.com/direnv/direnv
Version:                2.28.0

%gometa

%global common_description %{expand:
direnv augments existing shells with a new feature that can load and unload
environment variables depending on the current directory.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md README.md version.txt man/direnv-\\\
                        stdlib.1.md man/direnv.toml.1.md man/direnv.1.md

Name:           direnv
Release:        2%{?dist}
Summary:        Per-directory shell configuration tool

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/direnv/go-dotenv)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(golang.org/x/mod/semver)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/direnv %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -m 0755 -vd         %{buildroot}%{_mandir}/man1
install -m 0644 -vp man/*.1 %{buildroot}%{_mandir}/man1

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs CHANGELOG.md README.md version.txt
%{_bindir}/*
%{_mandir}/man1/*

%gopkgfiles

%changelog
* Tue Jun 15 2021 Ed Marshall <esm@logic.net> - 2.28.0-1
- Update to 2.28.0a
- Close: rhbz#1938419

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 17:52:00 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.27.0-1
- Update to 2.27.0
- Close: rhbz#1911955

* Fri Jan  1 17:53:53 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.26.0-1
- Update to 2.26.0
- Close: rhbz#1911127

* Sat Dec 26 15:34:39 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.25.2-1
- Update to 2.25.2
- Close: rhbz#1887117
- Close: rhbz#1910775

* Tue Oct 06 2020 Ed Marshall <esm@logic.net> - 2.22.1-1
- Update to 2.22.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Ed Marshall <esm@logic.net> - 2.21.3-1
- Update to 2.21.3
- Removed now-unneeded manpage lint fix

* Wed Jan 29 2020 Ed Marshall <esm@logic.net> - 2.21.2-1
- Update to 2.21.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Ed Marshall <esm@logic.net> - 2.21.1-1
- Update to 2.21.1

* Wed Oct 30 2019 Ed Marshall <esm@logic.net> - 2.20.1-1
- Update to 2.20.1
- Update spec to latest Fedora go packaging guidelines

* Tue Aug 30 2016 Dominic Cleal <dominic@cleal.org> - 2.9.0-2
- Fix make call to use parallel flag macro
- Fix default values of EA/BRs when macros aren't defined

* Wed Jul 20 2016 Dominic Cleal <dominic@cleal.org> - 2.9.0-1
- Initial build for Fedora
