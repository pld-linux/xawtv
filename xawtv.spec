Summary:	Video4Linux Stream Capture Viewer
Summary(pl):	Aplikacje video dla Linuxa
Name:		xawtv
Version:	3.12
Release:	3
License:	GNU 
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	http://me.in-berlin.de/~kraxel/v4l/%{name}-%{version}.tar.gz
Source1:	Xawtv.ad-pl
Patch0:		xawtv-home_etc.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libjpeg-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
A collection tools for video4linux:
 * xawtv    - X11 TV application
 * fbtv     - console TV application
 * streamer - capture tool (images / movies)
 * v4lctl   - command line tool to control v4l devices

%description -l pl
Kolekcja narzêdzi video dla Linuxa
 * xawtv    - X11 aplikacje TV
 * fbtv     - aplikacje TV pod konsolê
 * streamer - narzêdzie do przechwytywanie obrazu (zdjêcia / filmy)
 * v4lctl   - narzêdzie do kontroli urz±dzeñ v4l

%package radio
Summary:	radio
Summary(pl):	radio
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
      
%description radio
This is a ncurses-based radio application.

%description -l pl radio
Aplikacje radiowe bazuj±ce na ncurses.

%package misc
Summary:	Misc utils related (or not) to xawtv
Summary:	Ró¿ne narzêdzia pomocnicze do xawtv
Group:		X11/Applications
Group(pl):	X11/Aplikacje

%description misc
This package has a few tools you might find useful.  They
have not to do very much to do with xawtv.  I've used/wrote
them for debugging:
 * propwatch   - monitors properties of X11 windows.  If you
                 want to know how to keep track of xawtv's
                 _XAWTV_STATION property, look at this.
 * dump-mixers - dump mixer settings to stdout
 * record      - console sound recorder.  Has a simple input
                 level meter which might be useful to trouble
                 shoot sound problems.
 * showriff    - display the structure of RIFF files (avi, wav).

%description -l pl misc
Ten pakiet zawiera sporo u¿ytecznych narzêdzi. Nie maj± wiele wspólnego z
xawtv. Zosta³y napisane w celu debagowania xawtv.
 * propwatch   -  monitor ustawieñ
 * dump-mixers - "Dump" mixer
 * record      - Rejestrator d¼wiêku.
 * showriff    - Wy¶wietla strukturê plików RIFF (avi, wav).

%prep
%setup -q
%patch0 -p1

%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_prefix}/bin,%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults

make ROOT="$RPM_BUILD_ROOT" SUID_ROOT="" install

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults/Xawtv

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README Changes COPYING Programming-FAQ Trouble-Shooting \
	Sound-FAQ README.lirc README.bttv UPDATE_TO_v3.0 tools/README \
	$RPM_BUILD_ROOT%{_libdir}/X11/fonts/misc/*

%post
cd %{_libdir}/X11/fonts/misc
/usr/X11R6/bin/mkfontdir

%postun
cd %{_libdir}/X11/fonts/misc
/usr/X11R6/bin/mkfontdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes,COPYING,Programming-FAQ,Trouble-Shooting,Sound-FAQ}.gz
%doc {README.lirc,README.bttv,UPDATE_TO_v3.0}.gz

%attr(4755,root,root) %{_bindir}/v4l-conf
%attr(755,root,root) %{_bindir}/fbtv
%attr(755,root,root) %{_bindir}/streamer
%attr(755,root,root) %{_bindir}/xawtv-remote
%attr(755,root,root) %{_bindir}/xawtv
%attr(755,root,root) %{_bindir}/v4lctl

%{_libdir}/X11/app-defaults/Xawtv
%lang(pl) %{_libdir}/X11/pl/app-defaults/Xawtv

%{_libdir}/X11/fonts/misc/*

%{_mandir}/man1/fbtv.1*
%{_mandir}/man1/v4l-conf.1*
%{_mandir}/man1/v4lctl.1*
%{_mandir}/man1/xawtv-remote.1*
%{_mandir}/man1/xawtv.1*

%files radio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/radio
%{_mandir}/man1/radio.1*

%files misc
%defattr(644,root,root,755)
%doc tools/README.gz
%attr(755,root,root) %{_bindir}/dump-mixers
%attr(755,root,root) %{_bindir}/propwatch
%attr(755,root,root) %{_bindir}/record
%attr(755,root,root) %{_bindir}/showriff
%{_mandir}/man1/propwatch.1*
