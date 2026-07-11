%global tl_name pdftexcmds
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.33
Release:	%{tl_revision}.1
Summary:	LuaTeX support for pdfTeX utility functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/pdftexcmds
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftexcmds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftexcmds.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftexcmds.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LuaTeX provides most of the commands of pdfTeX 1.40. However, a number
of utility functions are not available. This package tries to fill the
gap and implements some of the missing primitives using Lua.

