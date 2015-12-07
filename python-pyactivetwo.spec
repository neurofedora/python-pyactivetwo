%global modname pyactivetwo

Name:           python-pyactivetwo
Version:        0.1
Release:        1%{?dist}
Summary:        Python library for reading signal from BioSemi ActiveTwo EEG device

License:        MIT
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.zip
Source1:        https://raw.githubusercontent.com/kuz/pyactivetwo/master/examples/example.py

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
%if 0%{?fedora} > 23
Requires:       python2-numpy
%else
Requires:       numpy
%endif

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
Requires:       python3-numpy

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

rm -rf *.egg-info
cp -p %{SOURCE1} .

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
# No tests

%files -n python2-%{modname}
%license LICENSE.txt
%doc README.rst example.py
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst example.py
%{python3_sitelib}/%{modname}*

%changelog
* Mon Dec 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-1
- Initial package
