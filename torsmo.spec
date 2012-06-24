Summary:	Tyopoyta ORvelo System MOnitor
Summary(pl):	Monitor systemu dla X Window System
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

%description -l pl
Torsmo jest monitorem systemu kt�ry siedzi w rogu ekranu. Torsmo
wy�wietlany jest na g��wnym oknie bez �adnych specjalnych wodotrysk�w.
Torsmo mo�e pokaza� wiele informacji o systemie, w��czaj�c w to:
- wersj� j�dra
- czas pracy systemu
- informacje o interfejsach sieciowych
- u�ycie pami�ci i swapu
- nazw� hosta
- architektur� systemu
- nazw� systemu
- temperatur� z czujnik�w i2c

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
