#
# Conditional build:
# _without_aalib	- compile without aalib support
# _without_lirc		- compile without lirc remote control support

Summary:	Video4Linux Stream Capture Viewer
Summary(es):	Video4Linux Stream Capture Viewer
Summary(pl):	Aplikacje video dla Linuksa
Summary(pt_BR):	Visualizador de fluxos de imagens obtidas atravИs do Video4Linux
Summary(ru):	Просмотр и запись видеопотоков
Summary(uk):	Перегляд та запис в╕деопоток╕в
Name:		xawtv
Version:	3.88
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://bytesex.org/xawtv/%{name}_%{version}.tar.gz
# Source0-md5:	9f43ae410965101f77c7c5d847c6842c
Source1:	Xawtv.ad-pl
Source2:	%{name}.desktop
Source3:	%{name}-noxv.desktop
Source4:	%{name}-conf_example-PTK
Source5:	http://bytesex.org/xawtv/tv-fonts-1.0.tar.bz2
# Source5-md5:	46c68df4976306e25a1526a762371770
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-channels_list-cable_poland_PTK.patch
Patch2:		%{name}-fullscreen.patch
Patch3:		%{name}-deinterlace.patch
Patch4:		%{name}-libng_fix.patch
URL:		http://bytesex.org/xawtv/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel >= 1.5
%{!?_without_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel
BuildRequires:	libjpeg-devel
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openmotif-devel
BuildRequires:	xft-devel
BuildRequires:	zvbi-devel
Prereq:		/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	font_dir 	tv-fonts-1.0

%description
A collection tools for video4linux:
 - xawtv - X11 TV application
 - fbtv - console TV application
 - streamer - capture tool (images / movies)
 - v4lctl - command line tool to control v4l devices

%description -l pl
Kolekcja narzЙdzi video dla Linuksa
 - xawtv - X11 aplikacje TV
 - fbtv - aplikacje TV pod konsolЙ
 - streamer - narzЙdzie do przechwytywanie obrazu (zdjЙcia / filmy)
 - v4lctl - narzЙdzie do kontroli urz╠dzeЯ v4l

%description -l pt_BR
Uma coleГЦo de ferramentas para o video4linux:
- xawtv - VisualizaГЦo de filmes (fluxos de imagens) para o X
- fbtv - VersЦo do xawtv para console com framebuffer
- streamer - ferramenta e captura (imagens / filmes)
- v4lctl - ferramenta de linha de comando para controlar dispositivos
  v4l

%description -l ru
Набор инструментов для работы с видеопотоками по протоколу
video4linux:
 - xawtv - интерфейс под X11
 - fbtv - консольный интерфейс
 - streamer - инструмент для записи (изображение/фильм)
 - v4lctl - инструмент командной строки для управления v4l устройствами

Включает также основанную на ncurses программу работы с радио.

%description -l uk
Наб╕р ╕нструмент╕в для роботи з в╕деопотоками по протоколу
video4linux:
 - xawtv - ╕нтерфейс п╕д X11
 - fbtv - консольний ╕нтерфейс
 - streamer - ╕нструмент для запису (зображення/ф╕льм)
 - v4lctl - ╕нструмент командного рядка для управл╕ння v4l пристроями

Включа╓ також основану на ncurses програму роботи з рад╕о.

%package radio
Summary:	radio
Summary(es):	xawtv: radio
Summary(pl):	radio
Summary(pt_BR):	Suporte a rАdio no xawtv
Group:		Applications/Sound

%description radio
This is a ncurses-based radio application.

%description radio -l pl
Aplikacje radiowe bazuj╠ce na ncurses.

%package misc
Summary:	Misc utils related (or not) to xawtv
Summary(es):	xawtv: misc
Summary(pl):	RС©ne narzЙdzia pomocnicze do xawtv
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
Ten pakiet zawiera sporo u©ytecznych narzЙdzi. Nie maj╠ wiele
wspСlnego z xawtv. ZostaЁy napisane w celu debagowania xawtv.
 - propwatch - monitor ustawieЯ
 - dump-mixers - "Dump" mixer
 - record - Rejestrator d╪wiЙku.
 - showriff - Wy╤wietla strukturЙ plikСw RIFF (avi, wav).

%description misc -l pt_BR
Ferramentas adicionais para depuraГЦo dos componentes do pacote xawtv:

 - propwatch - monitora as propriedades de janelas X11. Se vocЙ quiser
   saber como monitorar a propriedade _XAWTV_STATION use esta ferramenta.
 - dump-mixers - apresenta as configuraГУes do misturador na saМda
   padrЦo.
 - record - gravador de som para o console. Tem um medidor de nМvel de
   entrada que deve ser Зtil para auxiliar na resoluГЦo de problemas de
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
Summary(pl):	Tekstowy program do ogl╠dania TV
Group:		X11/Applications

%description ttv
TV tuner program using ASCII characters to display picture.

%description ttv -l pl
Program do obsЁugi tunera TV wy╤wietlaj╠cy obraz przy u©yciu znakСw
ASCII.

%prep
%setup -q -a 5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"; export CFLAGS
%configure \
	%{!?_without_aalib:--enable-aalib} \
	%{?_without_aalib:--disable-aalib} \
	%{!?_without_lirc:--enable-lirc} \
	%{?_without_lirc:--disable-lirc} \
	--enable-motif \
	--disable-quicktime \
	--enable-xfree-ext \
	--enable-xvideo
%{__make}

%{__make} -C %{font_dir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT/usr/X11R6/lib/X11{,/pl}/app-defaults \
	$RPM_BUILD_ROOT%{_applnkdir}/Multimedia \
	$RPM_BUILD_ROOT/usr/bin \
	$RPM_BUILD_ROOT%{_fontsdir}/misc

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	SUID_ROOT=""

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults/Xawtv
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/
install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/
install %{SOURCE4} .

cp %{font_dir}/*.gz $RPM_BUILD_ROOT%{_fontsdir}/misc/

%post
cd %{_fontsdir}
/usr/X11R6/bin/mkfontdir

%postun
cd %{_fontsdir}
/usr/X11R6/bin/mkfontdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README* xawtv-conf_example-*
%attr(4755,root,root) %{_bindir}/v4l-conf
%attr(755,root,root) %{_bindir}/fbtv
%attr(755,root,root) %{_bindir}/streamer
%attr(755,root,root) %{_bindir}/xawtv-remote
%attr(755,root,root) %{_bindir}/xawtv
%attr(755,root,root) %{_bindir}/v4lctl
%attr(755,root,root) %{_bindir}/rootv
%attr(755,root,root) %{_bindir}/webcam
%attr(755,root,root) %{_bindir}/scantv
%attr(755,root,root) %{_bindir}/showqt
%attr(755,root,root) %{_bindir}/pia
%attr(755,root,root) %{_bindir}/v4l-info
%attr(755,root,root) %{_bindir}/motv
%attr(755,root,root) %{_bindir}/mtt
%{_libdir}/%{name}

/usr/X11R6/lib/X11/app-defaults/Xawtv
/usr/X11R6/lib/X11/app-defaults/MoTV
/usr/X11R6/lib/X11/app-defaults/mtt
%lang(pl) /usr/X11R6/lib/X11/pl/app-defaults/Xawtv
%lang(it) /usr/X11R6/lib/X11/it/app-defaults/MoTV
%lang(fr) /usr/X11R6/lib/X11/fr/app-defaults/MoTV
%lang(de) /usr/X11R6/lib/X11/de/app-defaults/MoTV
%lang(de) /usr/X11R6/lib/X11/de_DE.UTF-8/app-defaults/MoTV

%{_applnkdir}/Multimedia/*

%{_datadir}/%{name}
%{_fontsdir}/misc/*

%{_mandir}/man1/fbtv.1*
%{_mandir}/man1/v4lctl.1*
%{_mandir}/man1/xawtv-remote.1*
%{_mandir}/man1/xawtv.1*
%{_mandir}/man1/webcam.1*
%{_mandir}/man1/rootv.1*
%{_mandir}/man1/scantv.1*
%{_mandir}/man1/streamer.1*
%{_mandir}/man1/pia.1*
%{_mandir}/man1/mtt.1*
%{_mandir}/man1/motv.1*
%{_mandir}/man5/xawtvrc.5*
%{_mandir}/man8/v4l-conf.8*
%lang(es) %{_mandir}/es/man1/fbtv.1*
%lang(es) %{_mandir}/es/man1/rootv.1*
%lang(es) %{_mandir}/es/man1/scantv.1*
%lang(es) %{_mandir}/es/man1/streamer.1*
%lang(es) %{_mandir}/es/man1/ttv.1*
%lang(es) %{_mandir}/es/man1/v4lctl.1*
%lang(es) %{_mandir}/es/man1/xawtv-remote.1*
%lang(es) %{_mandir}/es/man1/xawtv.1*
%lang(es) %{_mandir}/es/man5/xawtvrc.5*
%lang(es) %{_mandir}/es/man8/v4l-conf.8*
%lang(fr) %{_mandir}/fr/man1/xawtv.1*

%files radio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/radio
%{_mandir}/man1/radio.1*

%files misc
%defattr(644,root,root,755)
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
%lang(es) %{_mandir}/es/man1/subtitles.1*

%files alevtd
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/alevtd
%{_mandir}/man1/alevtd.1*

%if %{!?_without_aalib:1}0
%files ttv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ttv
%{_mandir}/man1/ttv.1*
%endif
