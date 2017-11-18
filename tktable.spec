%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tktable
Summary:       A Table/Matrix Widget Extension to Tcl/Tk
Version:       2.11.cvs20130418
Release:       1
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        tktable-tktable.tar.gz
URL:           http://tktable.cvs.sourceforge.net/viewvc/tktable/tktable/
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.4
BuildRequires: tk-devel >= 8.4
Requires:      tcl >= 8.4
Requires:      tk >= 8.4
BuildRoot:     %{buildroot}

%description
The basic features of the widgets are:
* multi-line cells
* support for embedded windows (one per cell)
* row & column spanning
* variable width/height columns/rows (interactively re-sizable)
* row and column titles
* multiple data sources ((Tcl array || Tcl command) &| internal caching)
* supports standard Tk reliefs, fonts, colors, etc.
* x/y scrollbar support
* 'tag' styles per row, column or cell to change visual appearance
* in-cell editing - returns value back to data source
* support for disabled (read-only) tables or cells (via tags)
* multiple selection modes, with "active" cell
* multiple drawing modes to get optimal performance for larger tables
* optional 'flashes' when things update
* cell validation support
* works everywhere Tk does (including Windows and Mac!)
* unicode support (Tk8.1+)

%prep
%setup -q -n %{name}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit \
%endif
	--with-tcl=%{directory}/%{_lib} \
	--with-tk=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install
rm %{buildroot}%{tcl_archdir}/%{name}%{version}/license.txt
rm %{buildroot}%{tcl_archdir}/%{name}%{version}/README.txt
rm -rf %{buildroot}%{tcl_archdir}/%{name}%{version}/html

%clean
rm -rf %buildroot

%files
%doc license.txt README.txt
%defattr(-,root,root)
%{tcl_archdir}

