%global tl_name inriafonts
%global tl_revision 77682
%global tl_version 1.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Inria fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/inriafonts
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inriafonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inriafonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Inria is a free font designed by Black[Foundry] for Inria research
institute. The font is available for free. It comes as Serif and Sans
Serif, each with three weights and matching italics. Using these fonts
with XeLaTeX and LuaLaTeX is easy using the fontspec package; we refer
to the documentation of fontspec for more information. The present
package provides a way of using them with LaTeX and pdfLaTeX: it
provides two style files, InriaSerif.sty and InriaSans.sty, together
with the PostScript version of the fonts and their associated files.
These were created using autoinst.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from inriafonts:
Map InriaSans.map
Map InriaSerif.map
TL_DROPIN_EOF
