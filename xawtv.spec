Summary: Video4Linux Stream Capture Viewer
Summary(pl): Aplikacje video dla Linuxa
Name: xawtv
Version: 3.01
Release: 1
Source: xawtv-%{version}.tar.gz
Group: X11/Applications
Group(pl): X11/Aplikacje
Copyright: GNU 
URL: http://www.in-berlin.de/User/kraxel/v4l/xawtv-%{version}.tar.gz
BuildRoot:      /tmp/%{name}-%{version}-root

%define         _prefix         /usr/X11R6
%define         _mandir         /usr/X11R6/man


%package radio
Summary: radio
Summary(pl): radio
Group: Applications/Sound
Group(pl): Aplikacje/D¼wiêk
      
%package misc
Summary: ró¿ne
Group: X11/Applications
Group(pl): X11/Aplikacje

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


%description radio
This is a ncurses-based radio application

%description -l pl radio
Aplikacje radiowe bazuj±ce na ncurses

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
%setup -q -n xawtv-%{version}


%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_prefix}/bin,%{_mandir}/man1}
make ROOT="$RPM_BUILD_ROOT" SUID_ROOT="" install


gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
{README,Changes,COPYING,Programming-FAQ,Trouble-Shooting,Sound-FAQ,README.lirc,README.bttv,UPDATE_TO_v3.0,tools/README}


%files

%{_mandir}/man1/fbtv.1.gz
%{_mandir}/man1/v4l-conf.1.gz
%{_mandir}/man1/v4lctl.1.gz
%{_mandir}/man1/xawtv-remote.1.gz
%{_mandir}/man1/xawtv.1.gz

%defattr(644,root,root,755) 
%doc {README,Changes,COPYING,Programming-FAQ,Trouble-Shooting,Sound-FAQ,README.lirc,README.bttv,UPDATE_TO_v3.0}.gz

%attr(755,root,root) %{_prefix}/bin/v4l-conf
%attr(755,root,root) %{_prefix}/bin/fbtv
%attr(755,root,root) %{_prefix}/bin/streamer
%attr(755,root,root) %{_prefix}/bin/xawtv-remote
%attr(755,root,root) %{_prefix}/bin/xawtv
%attr(755,root,root) %{_prefix}/bin/v4lctl
%defattr(-,root,root)
%{_prefix}/lib

%files radio
%attr(755,root,root) %{_prefix}/bin/radio
%{_mandir}/man1/radio.1.gz

%files misc
%attr(755,root,root) %{_prefix}/bin/dump-mixers
%attr(755,root,root) %{_prefix}/bin/propwatch
%attr(755,root,root) %{_prefix}/bin/record
%attr(755,root,root) %{_prefix}/bin/showriff
%{_mandir}/man1/propwatch.1.gz
%doc tools/README.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_prefix}/lib/X11/fonts/misc
mkfontdir
