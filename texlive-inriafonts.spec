Name:		texlive-inriafonts
Version:	54512
Release:	1
Summary:	Inria fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inriafonts
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inriafonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inriafonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Inria is a free font designed by Black[Foundry] for Inria
research institute. The font is available for free. It comes as
Serif and Sans Serif, each with three weights and matching
italics. Using these fonts with XeLaTeX and LuaLaTeX is easy
using the fontspec package; we refer to the documentation of
fontspec for more information. The present package provides a
way of using them with LaTeX and pdfLaTeX: it provides two
style files, InriaSerif.sty and InriaSans.sty, together with
the PostScript version of the fonts and their associated files.
These were created using autoinst.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/inriafonts
%{_texmfdistdir}/fonts/vf/public/inriafonts
%{_texmfdistdir}/fonts/type1/public/inriafonts
%{_texmfdistdir}/fonts/truetype/public/inriafonts
%{_texmfdistdir}/fonts/tfm/public/inriafonts
%{_texmfdistdir}/fonts/opentype/public/inriafonts
%{_texmfdistdir}/fonts/map/dvips/inriafonts
%{_texmfdistdir}/fonts/enc/dvips/inriafonts
%doc %{_texmfdistdir}/doc/fonts/inriafonts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
