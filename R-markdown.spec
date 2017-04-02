#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-markdown
Version  : 0.7.7
Release  : 25
URL      : http://cran.r-project.org/src/contrib/markdown_0.7.7.tar.gz
Source0  : http://cran.r-project.org/src/contrib/markdown_0.7.7.tar.gz
Summary  : 'Markdown' Rendering for R
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-markdown-lib
Requires: R-mime
BuildRequires : R-mime
BuildRequires : clr-R-helpers

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

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488814668

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1488814668
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library markdown
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library markdown


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/markdown/COPYING
/usr/lib64/R/library/markdown/DESCRIPTION
/usr/lib64/R/library/markdown/INDEX
/usr/lib64/R/library/markdown/Meta/Rd.rds
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
/usr/lib64/R/library/markdown/libs/symbols.rds
/usr/lib64/R/library/markdown/resources/markdown.css
/usr/lib64/R/library/markdown/resources/markdown.html
/usr/lib64/R/library/markdown/resources/mathjax.html
/usr/lib64/R/library/markdown/resources/r_highlight.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/markdown/libs/markdown.so
