Name:		texlive-pdftexcmds
Version:	55777
Release:	2
Summary:	LuaTeX support for pdfTeX utility functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdftexcmds
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftexcmds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftexcmds.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftexcmds.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LuaTeX provides most of the commands of pdfTeX 1.40. However, a
number of utility functions are not available. This package
tries to fill the gap and implements some of the missing
primitives using Lua.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/pdftexcmds
%{_texmfdistdir}/tex/generic/pdftexcmds
%doc %{_texmfdistdir}/doc/generic/pdftexcmds

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
