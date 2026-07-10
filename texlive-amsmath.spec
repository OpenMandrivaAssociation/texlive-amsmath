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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/amsmath
%dir %{_datadir}/texmf-dist/source/latex/amsmath
%dir %{_datadir}/texmf-dist/tex/latex/amsmath
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/README.md
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/ams-external.txt
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/ams-internal.txt
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsbsy.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amscd.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsgen.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsldoc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsldoc.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsmath.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsopn.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amstext.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/amsxtra.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/changes.txt
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/diffs-m.txt
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/manifest.txt
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/subeqn.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/subeqn.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/technote.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/technote.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/testmath.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsmath/testmath.tex
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsbsy.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsbsy.ins
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amscd.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amscd.ins
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsgen.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsgen.ins
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsmath.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsmath.ins
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsopn.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsopn.ins
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amstext.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amstext.ins
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsxtra.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsmath/amsxtra.ins
%{_datadir}/texmf-dist/tex/latex/amsmath/amsbsy.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amscd.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amsgen.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amsmath-2018-12-01.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amsmath.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amsopn.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amstex.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amstext.sty
%{_datadir}/texmf-dist/tex/latex/amsmath/amsxtra.sty
