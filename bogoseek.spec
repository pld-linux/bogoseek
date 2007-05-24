Summary:	Disk Speed Graphs
Summary(pl.UTF-8):	Wykresy szybkości dysku
Name:		bogoseek
Version:	0.3.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://sweaglesw.com/~djwong/programs/bogodisk/%{name}-%{version}.tar.gz
# Source0-md5:	3b0e52b9ffd0c77d1fcebb98db743ef0
URL:		http://sweaglesw.com/~djwong/programs/bogodisk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disk throughput benchmarking tool.

%description -l pl.UTF-8
Narzędzie do pomiaru przepustowości dysku.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
