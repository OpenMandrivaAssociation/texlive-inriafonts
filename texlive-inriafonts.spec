%global tl_name inriafonts
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Inria fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/inriafonts
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inriafonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inriafonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

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

