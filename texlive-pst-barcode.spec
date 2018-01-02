Name:		texlive-pst-barcode
Version:	0.18
Release:	1
Summary:	Print barcodes using PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-barcode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.doc.tar.xz
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
%{_texmfdistdir}/dvips/pst-barcode
%{_texmfdistdir}/tex/generic/pst-barcode
%{_texmfdistdir}/tex/latex/pst-barcode
%doc %{_texmfdistdir}/doc/generic/pst-barcode

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
