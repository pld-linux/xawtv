#
# _without_lirc	compile without lirc remote control support

Summary:	Video4Linux Stream Capture Viewer
Summary(es):	Video4Linux Stream Capture Viewer
Summary(pl):	Aplikacje video dla Linuxa
Summary(pt_BR):	Visualizador de fluxos de imagens obtidas através do Video4Linux
Name:		xawtv
Version:	3.68
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://bytesex.org/xawtv/%{name}_%{version}.tar.gz
Source1:	Xawtv.ad-pl
Source2:	%{name}.desktop
Source3:	%{name}-noxv.desktop
Source4:	%{name}-conf_example-PTK
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-newkeys-radio.patch
Patch2:		%{name}-channels_list-cable_poland_PTK.patch
URL:		http://bytesex.org/xawtv/
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	libjpeg-devel
BuildRequires:	Xaw3d-devel >= 1.5
BuildRequires:	XFree86-devel
BuildRequires:	aalib-devel
%{?_with_lirc:BuildRequires: lirc-devel}
Prereq:		/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_libdir		%{_prefix}/lib
%define         _mandir         %{_prefix}/man

%description
A collection tools for video4linux:
 - xawtv - X11 TV application
 - fbtv - console TV application
 - streamer - capture tool (images / movies)
 - v4lctl - command line tool to control v4l devices

%description -l pl
Kolekcja narzêdzi video dla Linuxa
 - xawtv - X11 aplikacje TV
 - fbtv - aplikacje TV pod konsolê
 - streamer - narzêdzie do przechwytywanie obrazu (zdjêcia / filmy)
 - v4lctl - narzêdzie do kontroli urz±dzeñ v4l

%description -l pt_BR
Uma coleção de ferramentas para o video4linux:
- xawtv - Visualização de filmes (fluxos de imagens) para o X
- fbtv - Versão do xawtv para console com framebuffer
- streamer - ferramenta e captura (imagens / filmes)
- v4lctl - ferramenta de linha de comando para controlar dispositivos
  v4l

%package radio
Summary:	radio
Summary(es):	xawtv: radio
Summary(pl):	radio
Summary(pt_BR):	Suporte a rádio no xawtv
Group:		Applications/Sound

%description radio
This is a ncurses-based radio application.

%description radio -l pl
Aplikacje radiowe bazuj±ce na ncurses.

%package misc
Summary:	Misc utils related (or not) to xawtv
Summary(es):	xawtv: misc
Summary(pl):	Ró¿ne narzêdzia pomocnicze do xawtv
Summary(pt_BR):	Ferramentas adicionais do xawtv
Group:		X11/Applications

%description misc
This package has a few tools you might find useful. They have not to
do very much to do with xawtv. I've used/wrote them for debugging:
 - propwatch - monitors properties of X11 windows. If you want to know
   how to keep track of xawtv's _XAWTV_STATION property, look at this.
 - dump-mixers - dump mixer settings to stdout
 - record - console sound recorder. Has a simple input level meter
   which might be useful to trouble shoot sound problems.
 - showriff - display the structure of RIFF files (avi, wav).

%description misc -l pl
Ten pakiet zawiera sporo u¿ytecznych narzêdzi. Nie maj± wiele
wspólnego z xawtv. Zosta³y napisane w celu debagowania xawtv.
 - propwatch - monitor ustawieñ
 - dump-mixers - "Dump" mixer
 - record - Rejestrator d¼wiêku.
 - showriff - Wy¶wietla strukturê plików RIFF (avi, wav).

%description misc -l pt_BR
Ferramentas adicionais para depuração dos componentes do pacote xawtv:

 - propwatch - monitora as propriedades de janelas X11. Se você quiser
   saber como monitorar a propriedade _XAWTV_STATION use esta ferramenta.
 - dump-mixers - apresenta as configurações do misturador na saída
   padrão.
 - record - gravador de som para o console. Tem um medidor de nível de
   entrada que deve ser útil para auxiliar na resolução de problemas de
   som.
 - showriff - mostra a estrutura de arquivos RIFF (avi, wav).

%package alevtd
Summary:	HTTP daemon for alevt teletext decoder
Summary(pl):	Daemon HTTP dla dekodera teletekstu alevt
Group:		Daemons
Requires:	alevt

%description alevtd
HTTP daemon for alevt teletext decoder

%description alevtd -l pl
Daemon HTTP dla dekodera teletekstu alevt

%package ttv
Summary:	ASCII Art TV viewer
Summary(pl):	Tekstowy program do ogl±dania TV
Group:		X11/Applications

%description ttv
TV tuner program using ASCII characters to display picture.

%description ttv -l pl
Program do obs³ugi tunera TV wy¶wietlaj±cy obraz przy u¿yciu znaków
ASCII.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure2_13 \
%{!?_without_lirc:	--enable-lirc} \
%{?_without_lirc:	--disable-lirc} \
	--disable-quicktime \
	--enable-xfree-ext \
	--enable-xvideo

%{__make} -C src Xawtv.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir} \
	$RPM_BUILD_ROOT%{_libdir}/X11{,/pl}/app-defaults \
	$RPM_BUILD_ROOT%{_applnkdir}/Multimedia \
	$RPM_BUILD_ROOT/usr/bin

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	SUID_ROOT=""

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults/Xawtv
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/
install %{SOURCE4} .

install http/alevtd $RPM_BUILD_ROOT/usr/bin

gzip -9nf Changes Programming-FAQ README* UPDATE_TO_v3.0 tools/README \
	xawtv-conf_example-*

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
%doc *.gz
%attr(4755,root,root) %{_bindir}/v4l-conf
%attr(755,root,root) %{_bindir}/fbtv
%attr(755,root,root) %{_bindir}/streamer
%attr(755,root,root) %{_bindir}/xawtv-remote
%attr(755,root,root) %{_bindir}/xawtv
%attr(755,root,root) %{_bindir}/v4lctl
%attr(755,root,root) %{_bindir}/rootv
%attr(755,root,root) %{_bindir}/webcam
%attr(755,root,root) %{_bindir}/scantv
%{_libdir}/%{name}

%{_libdir}/X11/app-defaults/Xawtv
%lang(pl) %{_libdir}/X11/pl/app-defaults/Xawtv
%{_applnkdir}/Multimedia/*

%{_libdir}/X11/fonts/misc/*

%{_mandir}/man1/fbtv.1*
%{_mandir}/man1/v4lctl.1*
%{_mandir}/man1/xawtv-remote.1*
%{_mandir}/man1/xawtv.1*
%{_mandir}/man1/webcam.1*
%{_mandir}/man1/rootv.1*
%{_mandir}/man1/scantv.1*
%{_mandir}/man1/streamer.1*
%{_mandir}/man5/xawtvrc.5*
%{_mandir}/man8/v4l-conf.8*

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
%attr(755,root,root) %{_bindir}/ntsc-cc
%attr(755,root,root) %{_bindir}/subtitles
%{_mandir}/man1/propwatch.1*
%{_mandir}/man1/showriff.1*
%{_mandir}/man1/dump-mixers.1*
%{_mandir}/man1/ntsc-cc.1*
%{_mandir}/man1/record.1*
%{_mandir}/man1/subtitles.1*

%files alevtd
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/alevtd
%{_mandir}/man1/alevtd.1*

%files ttv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ttv
%{_mandir}/man1/ttv.1*
