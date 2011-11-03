# revision 23390
# category Package
# catalog-ctan /macros/latex/required/amslatex/math
# catalog-date 2010-12-31 18:17:46 +0100
# catalog-license lppl
# catalog-version 2.13
Name:		texlive-amsmath
Version:	2.13
Release:	1
Summary:	AMS mathematical facilities for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/amslatex/math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is the principal package in the AMS-LaTeX
distribution. It adapts for use in LaTeX most of the
mathematical features found in AMS-TeX; it is a near-
indispensable adjunct to serious mathematical typesetting in
LaTeX. When amsmath is loaded, AMS-LaTeX packages amsbsy (for
bold symbols), amsopn (for operator names) and amstext (for
text embdedded in mathematics) are also loaded. Amsmath is part
of the LaTeX required distribution; however, several
contributed packages add still further to its appeal; examples
are empheq, which provides functions for decorating and
highlighting mathematics, and ntheorem, for specifying theorem
(and similar) definitions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_texmfdistdir}/doc/latex/amsmath/00LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/amsmath/amsbsy.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amscd.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsgen.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsldoc.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsmath.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsopn.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amstext.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/amsxtra.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/diffs-m.txt
%doc %{_texmfdistdir}/doc/latex/amsmath/subeqn.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/technote.pdf
%doc %{_texmfdistdir}/doc/latex/amsmath/testmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/amsmath/00LICENSE.txt
%doc %{_texmfdistdir}/source/latex/amsmath/00readme.txt
%doc %{_texmfdistdir}/source/latex/amsmath/ams-m1.ins
%doc %{_texmfdistdir}/source/latex/amsmath/amsbsy.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amscd.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsdtx.cls
%doc %{_texmfdistdir}/source/latex/amsmath/amsgen.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsldoc.cls
%doc %{_texmfdistdir}/source/latex/amsmath/amsldoc.tex
%doc %{_texmfdistdir}/source/latex/amsmath/amsmath.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsopn.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amstext.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/amsxtra.dtx
%doc %{_texmfdistdir}/source/latex/amsmath/install.txt
%doc %{_texmfdistdir}/source/latex/amsmath/manifest.txt
%doc %{_texmfdistdir}/source/latex/amsmath/subeqn.tex
%doc %{_texmfdistdir}/source/latex/amsmath/technote.tex
%doc %{_texmfdistdir}/source/latex/amsmath/testmath.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
