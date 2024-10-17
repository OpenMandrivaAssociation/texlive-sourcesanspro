Name:		texlive-sourcesanspro
Version:	54892
Release:	2
Summary:	Use SourceSansPro with TeX(-alike) systems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/sourcesanspro
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourcesanspro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourcesanspro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font is an open-source Sans-Serif development from Adobe.
The package provides fonts (in both Adobe Type 1 and OpenType
formats) and macros supporting their use in LaTeX (Type 1) and
XeLaTeX/LuaLaTeX (OTF).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/sourcesanspro
%{_texmfdistdir}/fonts/map/dvips/sourcesanspro
%{_texmfdistdir}/fonts/opentype/adobe/sourcesanspro
%{_texmfdistdir}/fonts/tfm/adobe/sourcesanspro
%{_texmfdistdir}/fonts/type1/adobe/sourcesanspro
%{_texmfdistdir}/fonts/vf/adobe/sourcesanspro
%{_texmfdistdir}/tex/latex/sourcesanspro
%doc %{_texmfdistdir}/doc/latex/sourcesanspro

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
