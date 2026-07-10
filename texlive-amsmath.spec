%global tl_name amsmath
%global tl_revision 79234

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	AMS mathematical facilities for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/amsmath
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the principal packages in the AMS-LaTeX
distribution. It adapts for use in LaTeX most of the mathematical
features found in AMS-TeX; it is highly recommended as an adjunct to
serious mathematical typesetting in LaTeX. When amsmath is loaded, AMS-
LaTeX packages amsbsy (for bold symbols), amsopn (for operator names)
and amstext (for text embedded in mathematics) are also loaded. amsmath
is part of the LaTeX required distribution; however, several contributed
packages add still further to its appeal; examples are empheq, which
provides functions for decorating and highlighting mathematics, and
ntheorem, for specifying theorem (and similar) definitions.

