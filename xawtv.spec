Summary:	Video4Linux Stream Capture Viewer
Summary(pl):	Aplikacje video dla Linuxa
Name:		xawtv
Version:	3.01
Release:	1
Source:		http://www.in-berlin.de/User/kraxel/v4l/%{name}-%{version}.tar.gz
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Copyright:	GNU 
BuildRoot:	/tmp/%{name}-%{version}-root

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
A collection tools for video4linux:
 * xawtv    - X11 TV application
 * fbtv     - console TV application
 * streamer - capture tool (images / movies)
 * v4lctl   - command line tool to control v4l devices

%description -l pl
Kolekcja narz�dzi video dla Linuxa
 * xawtv    - X11 aplikacje TV
 * fbtv     - aplikacje TV pod konsol�
 * streamer - narz�dzie do przechwytywanie obrazu (zdj�cia / filmy)
 * v4lctl   - narz�dzie do kontroli urz�dze� v4l


%package radio
Summary:	radio
Summary(pl):	radio
Group:		Applications/Sound
Group(pl):	Aplikacje/D�wi�k
      

%description radio
This is a ncurses-based radio application

%description -l pl radio
Aplikacje radiowe bazuj�ce na ncurses

%package misc
Summary:	Misc utils related (or not) to xawtv
Summary:	R�ne narz�dzia pomocnicze do xawtv
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
Ten pakiet zawiera sporo u�ytecznych narz�dzi. Nie maj� wiele wsp�lnego z
xawtv. Zosta�y napisane w celu debagowania xawtv.
 * propwatch   -  monitor ustawie�
 * dump-mixers - "Dump" mixer
 * record      - Rejestrator d�wi�ku.
 * showriff    - Wy�wietla struktur� plik�w RIFF (avi, wav).

%prep
%setup -q


%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_prefix}/bin,%{_mandir}/man1}
make ROOT="$RPM_BUILD_ROOT" SUID_ROOT="" install


gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README Changes COPYING Programming-FAQ Trouble-Shooting \
	Sound-FAQ README.lirc README.bttv UPDATE_TO_v3.0 tools/README
%post
cd %{_prefix}/lib/X11/fonts/misc
mkfontdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes,COPYING,Programming-FAQ,Trouble-Shooting,Sound-FAQ}.gz
%doc {README.lirc,README.bttv,UPDATE_TO_v3.0}.gz

%attr(755,root,root) %{_prefix}/bin/v4l-conf
%attr(755,root,root) %{_prefix}/bin/fbtv
%attr(755,root,root) %{_prefix}/bin/streamer
%attr(755,root,root) %{_prefix}/bin/xawtv-remote
%attr(755,root,root) %{_prefix}/bin/xawtv
%attr(755,root,root) %{_prefix}/bin/v4lctl

%{_prefix}/lib

%{_mandir}/man1/fbtv.1*
%{_mandir}/man1/v4l-conf.1*
%{_mandir}/man1/v4lctl.1*
%{_mandir}/man1/xawtv-remote.1*
%{_mandir}/man1/xawtv.1*

%files radio
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/bin/radio
%{_mandir}/man1/radio.1*

%files misc
%defattr(644,root,root,755)
%doc tools/README.gz
%attr(755,root,root) %{_prefix}/bin/dump-mixers
%attr(755,root,root) %{_prefix}/bin/propwatch
%attr(755,root,root) %{_prefix}/bin/record
%attr(755,root,root) %{_prefix}/bin/showriff
%{_mandir}/man1/propwatch.1*
