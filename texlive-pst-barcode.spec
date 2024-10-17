Name:		texlive-pst-barcode
Version:	64182
Release:	2
Summary:	Print barcodes using PostScript
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-barcode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-barcode.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
