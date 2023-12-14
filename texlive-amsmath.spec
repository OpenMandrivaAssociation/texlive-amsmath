Name:		texlive-amsmath
Version:	68720
Release:	1
Summary:	AMS mathematical facilities for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/amslatex/math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the principal packages in the AMS-LaTeX
distribution. It adapts for use in LaTeX most of the
mathematical features found in AMS-TeX; it is highly
recommendsd as an adjunct to serious mathematical typesetting
in LaTeX. When amsmath is loaded, AMS-LaTeX packages amsbsy
(for bold symbols), amsopn (for operator names) and amstext
(for text embdedded in mathematics) are also loaded. Amsmath is
part of the LaTeX required distribution; however, several
contributed packages add still further to its appeal; examples
are empheq, which provides functions for decorating and
highlighting mathematics, and ntheorem, for specifying theorem
(and similar) definitions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/amsmath
%doc %{_texmfdistdir}/doc/latex/amsmath
#- source
%doc %{_texmfdistdir}/source/latex/amsmath

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
