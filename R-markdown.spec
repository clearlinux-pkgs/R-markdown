#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-markdown
Version  : 2.0
Release  : 111
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/markdown_2.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/markdown_2.0.tar.gz
Summary  : Render Markdown with 'commonmark'
Group    : Development/Tools
License  : MIT
Requires: R-litedown
Requires: R-xfun
BuildRequires : R-litedown
BuildRequires : R-xfun
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
the 'commonmark' package. This package has been superseded by 'litedown'.

%prep
%setup -q -n markdown
pushd ..
cp -a markdown buildavx2
popd
pushd ..
cp -a markdown buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742849158

%install
export SOURCE_DATE_EPOCH=1742849158
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/markdown/DESCRIPTION
/usr/lib64/R/library/markdown/INDEX
/usr/lib64/R/library/markdown/LICENSE
/usr/lib64/R/library/markdown/Meta/Rd.rds
/usr/lib64/R/library/markdown/Meta/features.rds
/usr/lib64/R/library/markdown/Meta/hsearch.rds
/usr/lib64/R/library/markdown/Meta/links.rds
/usr/lib64/R/library/markdown/Meta/nsInfo.rds
/usr/lib64/R/library/markdown/Meta/package.rds
/usr/lib64/R/library/markdown/NAMESPACE
/usr/lib64/R/library/markdown/NEWS.md
/usr/lib64/R/library/markdown/R/markdown
/usr/lib64/R/library/markdown/R/markdown.rdb
/usr/lib64/R/library/markdown/R/markdown.rdx
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
/usr/lib64/R/library/markdown/tests/tests.R
/usr/lib64/R/library/markdown/tests/tests.Rout.save
