# revision 30645
# category Package
# catalog-ctan /macros/latex/required/amslatex/math
# catalog-date 2013-03-09 20:29:31 +0100
# catalog-license lppl
# catalog-version 2.14
Name:		texlive-amsmath
Version:	2.14
Release:	3
Summary:	AMS mathematical facilities for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/amslatex/math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.source.tar.xz
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
%{_texmfdistdir}/tex/latex/amsmath/amsbsy.sty
%{_texmfdistdir}/tex/latex/amsmath/amscd.sty
%{_texmfdistdir}/tex/latex/amsmath/amsgen.sty
%{_texmfdistdir}/tex/latex/amsmath/amsmath.sty
%{_texmfdistdir}/tex/latex/amsmath/amsopn.sty
%{_texmfdistdir}/tex/latex/amsmath/amstex.sty
%{_texmfdistdir}/tex/latex/amsmath/amstext.sty
%{_texmfdistdir}/tex/latex/amsmath/amsxtra.sty
%doc %{_texmfdistdir}/doc/latex/amsmath/amsbsy.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amscd.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsgen.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsldoc.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsmath.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsopn.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amstext.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsxtra.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/subeqn.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/technote.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/testmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/amsmath/README
%doc %{_texmfdistdir}/source/latex/amsmath/amsbsy.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsbsy.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amscd.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amscd.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amsgen.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsgen.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amsldoc.tex
%doc %{_texmfdistdir}/source/latex/amsmath/amsmath.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsmath.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amsopn.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsopn.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amstext.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amstext.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amsxtra.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsxtra.ins
%doc %{_texmfdistdir}/source/latex/amsmath/diffs-m.txt
%doc %{_texmfdistdir}/source/latex/amsmath/install.txt
%doc %{_texmfdistdir}/source/latex/amsmath/manifest.txt
%doc %{_texmfdistdir}/source/latex/amsmath/subeqn.tex
%doc %{_texmfdistdir}/source/latex/amsmath/technote.tex
%doc %{_texmfdistdir}/source/latex/amsmath/testmath.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
