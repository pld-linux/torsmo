Summary:	Tyopoyta ORvelo System MOnitor
Summary(pl.UTF-8):	Monitor systemu dla X Window System
Name:		torsmo
Version:	0.18
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/torsmo/%{name}-%{version}.tar.gz
# Source0-md5:	88bd8f627637d785a1d681f4f15f00b6
URL:		http://torsmo.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	help2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Torsmo is a system monitor that sits in the corner of your desktop.
Torsmo renders itself on the root window (on the desktop) without any
special eyecandy. Torsmo can show lots of info about your system,
including:
- kernel version
- uptime
- network interface information
- memory and swap usage
- hostname
- machine, i686 for example
- system name, Linux for example
- temperatures from i2c-sensors

%description -l pl.UTF-8
Torsmo jest monitorem systemu który siedzi w rogu ekranu. Torsmo
wyświetlany jest na głównym oknie bez żadnych specjalnych wodotrysków.
Torsmo może pokazać wiele informacji o systemie, włączając w to:
- wersję jądra
- czas pracy systemu
- informacje o interfejsach sieciowych
- użycie pamięci i swapu
- nazwę hosta
- architekturę systemu
- nazwę systemu
- temperaturę z czujników i2c

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog COPYING NEWS README torsmorc.sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
