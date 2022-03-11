#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-markdown
Version  : 1.1
Release  : 87
URL      : https://cran.r-project.org/src/contrib/markdown_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/markdown_1.1.tar.gz
Summary  : Render Markdown with the C Library 'Sundown'
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-markdown-lib = %{version}-%{release}
Requires: R-mime
Requires: R-xfun
BuildRequires : R-mime
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
Markdown rendering for R
=============================================================================

%package lib
Summary: lib components for the R-markdown package.
Group: Libraries

%description lib
lib components for the R-markdown package.


%prep
%setup -q -c -n markdown
cd %{_builddir}/markdown

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641053592

%install
export SOURCE_DATE_EPOCH=1641053592
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library markdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library markdown
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library markdown
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc markdown || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/markdown/COPYING
/usr/lib64/R/library/markdown/DESCRIPTION
/usr/lib64/R/library/markdown/INDEX
/usr/lib64/R/library/markdown/Meta/Rd.rds
/usr/lib64/R/library/markdown/Meta/features.rds
/usr/lib64/R/library/markdown/Meta/hsearch.rds
/usr/lib64/R/library/markdown/Meta/links.rds
/usr/lib64/R/library/markdown/Meta/nsInfo.rds
/usr/lib64/R/library/markdown/Meta/package.rds
/usr/lib64/R/library/markdown/Meta/vignette.rds
/usr/lib64/R/library/markdown/NAMESPACE
/usr/lib64/R/library/markdown/NEWS
/usr/lib64/R/library/markdown/NOTICE
/usr/lib64/R/library/markdown/R/markdown
/usr/lib64/R/library/markdown/R/markdown.rdb
/usr/lib64/R/library/markdown/R/markdown.rdx
/usr/lib64/R/library/markdown/doc/index.html
/usr/lib64/R/library/markdown/doc/markdown-examples.R
/usr/lib64/R/library/markdown/doc/markdown-examples.Rmd
/usr/lib64/R/library/markdown/doc/markdown-examples.html
/usr/lib64/R/library/markdown/doc/markdown-output.R
/usr/lib64/R/library/markdown/doc/markdown-output.Rmd
/usr/lib64/R/library/markdown/doc/markdown-output.html
/usr/lib64/R/library/markdown/examples/HTMLOptions.R
/usr/lib64/R/library/markdown/examples/markdownExtensions.R
/usr/lib64/R/library/markdown/help/AnIndex
/usr/lib64/R/library/markdown/help/aliases.rds
/usr/lib64/R/library/markdown/help/markdown.rdb
/usr/lib64/R/library/markdown/help/markdown.rdx
/usr/lib64/R/library/markdown/help/paths.rds
/usr/lib64/R/library/markdown/html/00Index.html
/usr/lib64/R/library/markdown/html/R.css
/usr/lib64/R/library/markdown/include/autolink.h
/usr/lib64/R/library/markdown/include/buffer.h
/usr/lib64/R/library/markdown/include/markdown.h
/usr/lib64/R/library/markdown/include/markdown_rstubs.c
/usr/lib64/R/library/markdown/include/markdown_rstubs.h
/usr/lib64/R/library/markdown/resources/markdown.css
/usr/lib64/R/library/markdown/resources/markdown.html
/usr/lib64/R/library/markdown/resources/mathjax.html
/usr/lib64/R/library/markdown/resources/r_highlight.html
/usr/lib64/R/library/markdown/tests/b64EncodeFile.R
/usr/lib64/R/library/markdown/tests/empty.R
/usr/lib64/R/library/markdown/tests/tests.R
/usr/lib64/R/library/markdown/tests/tests.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/markdown/libs/markdown.so
/usr/lib64/R/library/markdown/libs/markdown.so.avx2
/usr/lib64/R/library/markdown/libs/markdown.so.avx512
