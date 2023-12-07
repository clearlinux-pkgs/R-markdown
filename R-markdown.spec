#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-markdown
Version  : 1.12
Release  : 107
URL      : https://cran.r-project.org/src/contrib/markdown_1.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/markdown_1.12.tar.gz
Summary  : Render Markdown with 'commonmark'
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-markdown-license = %{version}-%{release}
Requires: R-commonmark
Requires: R-xfun
BuildRequires : R-commonmark
BuildRequires : R-xfun
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
the 'commonmark' package. It also supports features that are missing in
    'commonmark', such as raw HTML/LaTeX blocks, LaTeX math, superscripts,
    subscripts, footnotes, element attributes, appendices, and fenced 'Divs'.
    With additional JavaScript and CSS, it can also create HTML slides and
    articles.

%package license
Summary: license components for the R-markdown package.
Group: Default

%description license
license components for the R-markdown package.


%prep
%setup -q -n markdown
pushd ..
cp -a markdown buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701910350

%install
export SOURCE_DATE_EPOCH=1701910350
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-markdown
cp %{_builddir}/markdown/inst/COPYING %{buildroot}/usr/share/package-licenses/R-markdown/77f89ea86902ea35fd3fc415dd5942fc0a289b5d || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/markdown/COPYING
/usr/lib64/R/library/markdown/DESCRIPTION
/usr/lib64/R/library/markdown/INDEX
/usr/lib64/R/library/markdown/LICENSE
/usr/lib64/R/library/markdown/Meta/Rd.rds
/usr/lib64/R/library/markdown/Meta/features.rds
/usr/lib64/R/library/markdown/Meta/hsearch.rds
/usr/lib64/R/library/markdown/Meta/links.rds
/usr/lib64/R/library/markdown/Meta/nsInfo.rds
/usr/lib64/R/library/markdown/Meta/package.rds
/usr/lib64/R/library/markdown/Meta/vignette.rds
/usr/lib64/R/library/markdown/NAMESPACE
/usr/lib64/R/library/markdown/NEWS.md
/usr/lib64/R/library/markdown/R/markdown
/usr/lib64/R/library/markdown/R/markdown.rdb
/usr/lib64/R/library/markdown/R/markdown.rdx
/usr/lib64/R/library/markdown/doc/article.R
/usr/lib64/R/library/markdown/doc/article.Rmd
/usr/lib64/R/library/markdown/doc/article.html
/usr/lib64/R/library/markdown/doc/index.html
/usr/lib64/R/library/markdown/doc/intro.R
/usr/lib64/R/library/markdown/doc/intro.Rmd
/usr/lib64/R/library/markdown/doc/intro.html
/usr/lib64/R/library/markdown/doc/markdown-examples.R
/usr/lib64/R/library/markdown/doc/markdown-examples.Rmd
/usr/lib64/R/library/markdown/doc/markdown-examples.html
/usr/lib64/R/library/markdown/doc/markdown-output.R
/usr/lib64/R/library/markdown/doc/markdown-output.Rmd
/usr/lib64/R/library/markdown/doc/markdown-output.html
/usr/lib64/R/library/markdown/doc/slides.R
/usr/lib64/R/library/markdown/doc/slides.Rmd
/usr/lib64/R/library/markdown/doc/slides.html
/usr/lib64/R/library/markdown/examples/render-options.R
/usr/lib64/R/library/markdown/help/AnIndex
/usr/lib64/R/library/markdown/help/aliases.rds
/usr/lib64/R/library/markdown/help/markdown.rdb
/usr/lib64/R/library/markdown/help/markdown.rdx
/usr/lib64/R/library/markdown/help/paths.rds
/usr/lib64/R/library/markdown/html/00Index.html
/usr/lib64/R/library/markdown/html/R.css
/usr/lib64/R/library/markdown/resources/default.css
/usr/lib64/R/library/markdown/resources/markdown.html
/usr/lib64/R/library/markdown/resources/markdown.latex
/usr/lib64/R/library/markdown/resources/prism-xcode.css
/usr/lib64/R/library/markdown/resources/snap.css
/usr/lib64/R/library/markdown/resources/snap.js
/usr/lib64/R/library/markdown/tests/empty.R
/usr/lib64/R/library/markdown/tests/smartypants.R
/usr/lib64/R/library/markdown/tests/tests.R
/usr/lib64/R/library/markdown/tests/tests.Rout.save

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-markdown/77f89ea86902ea35fd3fc415dd5942fc0a289b5d
