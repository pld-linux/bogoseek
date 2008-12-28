Summary:	Disk Speed Graphs
Summary(pl.UTF-8):	Wykresy szybkości dysku
Name:		bogoseek
Version:	0.3.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://sweaglesw.com/~djwong/programs/bogodisk/%{name}-%{version}.tar.gz
# Source0-md5:	6f7f4cfb6d81a592a0e3287316b2c173
Patch0:		%{name}-as-needed.patch
URL:		http://sweaglesw.com/~djwong/programs/bogodisk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disk throughput benchmarking tool.

%description -l pl.UTF-8
Narzędzie do pomiaru przepustowości dysku.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
