# revision 27004
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-barcode
# catalog-date 2012-06-28 12:34:54 +0200
# catalog-license lppl
# catalog-version 0.09
Name:		texlive-pst-barcode
Version:	0.09
Release:	1
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
pstricks package, the package requires pstricks. The package
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


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.09-1
+ Revision: 812790
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.08-2
+ Revision: 755221
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.08-1
+ Revision: 719334
- texlive-pst-barcode
- texlive-pst-barcode
- texlive-pst-barcode
- texlive-pst-barcode

