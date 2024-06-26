Name:       xwayland
Summary:    Xwayland
Version:    23.2.7
Release:    1%{?dist}
URL:        https://gitlab.freedesktop.org/xorg/xserver
Source0:    %{name}-%{version}.tar.bz2
License:    MIT
Patch0:     0001-wl_seat-patch.patch
Patch1:     0002-wl_shell-support-for-lipstick.patch
Requires:   xkbcomp
BuildRequires:  ccache
BuildRequires:  meson >= 0.52.0
BuildRequires:  pkgconfig(bigreqsproto) >= 1.1.0
BuildRequires:  pkgconfig(compositeproto) >= 0.4
BuildRequires:  pkgconfig(damageproto) >= 1.1
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dri3proto) >= 1.2
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fixesproto) >= 6.0
BuildRequires:  pkgconfig(fontsproto) >= 2.1.3
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(gbm) >= 10.2
BuildRequires:  pkgconfig(inputproto) >= 2.3.99.1
BuildRequires:  pkgconfig(kbproto) >= 1.0.3
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(presentproto) >= 1.3
BuildRequires:  pkgconfig(randrproto) >= 1.6.0
BuildRequires:  pkgconfig(recordproto) >= 1.13.99.1
BuildRequires:  pkgconfig(renderproto) >= 0.11
BuildRequires:  pkgconfig(resourceproto) >= 1.2.0
BuildRequires:  pkgconfig(scrnsaverproto) >= 1.1
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(wayland-client) >= 1.21.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.30
BuildRequires:  pkgconfig(xcmiscproto) >= 1.2.0
BuildRequires:  pkgconfig(xextproto) >= 7.2.99.901
BuildRequires:  pkgconfig(xf86bigfontproto) >= 1.2.0
BuildRequires:  pkgconfig(xf86vidmodeproto) >= 2.2.99.1
BuildRequires:  pkgconfig(xfont2) >= 2.0
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbcomp)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto) >= 7.0.31
BuildRequires:  pkgconfig(xshmfence) >= 1.1
BuildRequires:  pkgconfig(xtrans) >= 1.3.5
BuildRequires:  pkgconfig(xwaylandproto) >= 1.0

%description
Xwayland is an X server for running X clients under Wayland.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%meson \
    -Dglx=false \
    -Dxdmcp=false \
    -Dxvfb=false
%meson_build

%install
%meson_install --tags runtime

%files
%license COPYING
%{_bindir}/Xwayland
