#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Expands [%here] into its location
Summary(pl.UTF-8):	Rozwijanie [%here] na jego położenie
Name:		ocaml-ppx_here
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_here/tags
Source0:	https://github.com/janestreet/ppx_here/archive/v%{version}/ppx_here-%{version}.tar.gz
# Source0-md5:	c188e5c348d52ca3da39aca20fb04171
URL:		https://github.com/janestreet/ppx_here
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx rewriter that defines an extension node whose value is its
source position.

This package contains files needed to run bytecode executables using
ppx_here library.

%description -l pl.UTF-8
Moduł przepisujący ppx definiujący węzeł rozszerzenia, którego
wartością jest jego położenie w kodzie źródłowym.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_here.

%package devel
Summary:	Expands [%here] into its location - development part
Summary(pl.UTF-8):	Rozwijanie [%here] na jego położenie - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_here library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_here.

%prep
%setup -q -n ppx_here-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_here/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_here/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_here

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_here
%attr(755,root,root) %{_libdir}/ocaml/ppx_here/ppx.exe
%{_libdir}/ocaml/ppx_here/META
%{_libdir}/ocaml/ppx_here/*.cma
%dir %{_libdir}/ocaml/ppx_here/expander
%{_libdir}/ocaml/ppx_here/expander/*.cma
%dir %{_libdir}/ocaml/ppx_here/runtime-lib
%{_libdir}/ocaml/ppx_here/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_here/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_here/expander/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_here/runtime-lib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_here/*.cmi
%{_libdir}/ocaml/ppx_here/*.cmt
%{_libdir}/ocaml/ppx_here/*.cmti
%{_libdir}/ocaml/ppx_here/*.mli
%{_libdir}/ocaml/ppx_here/expander/*.cmi
%{_libdir}/ocaml/ppx_here/expander/*.cmt
%{_libdir}/ocaml/ppx_here/expander/*.cmti
%{_libdir}/ocaml/ppx_here/expander/*.mli
%{_libdir}/ocaml/ppx_here/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_here/runtime-lib/*.cmt
%{_libdir}/ocaml/ppx_here/runtime-lib/*.cmti
%{_libdir}/ocaml/ppx_here/runtime-lib/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_here/ppx_here.a
%{_libdir}/ocaml/ppx_here/*.cmx
%{_libdir}/ocaml/ppx_here/*.cmxa
%{_libdir}/ocaml/ppx_here/expander/ppx_here_expander.a
%{_libdir}/ocaml/ppx_here/expander/*.cmx
%{_libdir}/ocaml/ppx_here/expander/*.cmxa
%{_libdir}/ocaml/ppx_here/runtime-lib/ppx_here_lib.a
%{_libdir}/ocaml/ppx_here/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_here/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_here/dune-package
%{_libdir}/ocaml/ppx_here/opam
