# revision 21716
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-barcode
# catalog-date 2011-03-12 22:14:05 +0100
# catalog-license lppl
# catalog-version 0.08
Name:		texlive-pst-barcode
Version:	0.08
Release:	2
Summary:	Print barcodes using PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-barcode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pst-barcode package allows printing of barcodes, in a huge
variety of formats (see documentation for details). As a
pstricks package, pst-barcode requires pstricks. The package
uses PostScript for calculating the bars. For PDF output use a
multi-pass mechansism such as pst-pdf.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-barcode/pst-barcode.pro
%{_texmfdistdir}/tex/generic/pst-barcode/pst-barcode.tex
%{_texmfdistdir}/tex/latex/pst-barcode/pst-barcode.sty
%doc %{_texmfdistdir}/doc/generic/pst-barcode/Changes
%doc %{_texmfdistdir}/doc/generic/pst-barcode/README
%doc %{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-barcode/pst-barcode-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-barcode/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
