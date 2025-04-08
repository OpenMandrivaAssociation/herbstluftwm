Name:		herbstluftwm
Version:    0.9.5
Release:	    1
Source0:	    https://github.com/herbstluftwm/herbstluftwm/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	    A manual tiling window manager for X11
URL:		https://github.com/herbstluftwm/herbstluftwm
License:    BSD-2-Clause
Group:		Window Manager/Other

BuildSystem:	cmake
BuildRequires:	asciidoc
BuildRequires:	a2x
BuildRequires:  pkgconfig(x11)

Requires: libx11
Requires: libxft
Requires: freetype
Requires: lib64xrandr2
Requires: libxinerama1

%description
%summary

%prep
%autosetup -p1

%files
%{_sysconfdir}/xdg/%{name}
%{_bindir}/*
%{_datadir}/doc/%{name}
%{_datadir}/man
%{_datadir}/fish
%{_datadir}/bash-completion
%{_datadir}/zsh
%{_datadir}/xsessions
