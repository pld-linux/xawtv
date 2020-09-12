#
# Conditional build:
%bcond_without	aalib	# compile without aalib support
%bcond_without	lirc	# compile without lirc remote control support
%bcond_with	mmx	# MMX support (if enabled, linear-plugin won't work on non-MMX CPU)
#
# asm code has 32-bit addressing, so x86_64 ABI is not supported
%ifarch pentium3 pentium4 athlon x32
%define	with_mmx	1
%endif
Summary:	Video4Linux Stream Capture Viewer
Summary(pl.UTF-8):	Aplikacje video dla Linuksa
Summary(pt_BR.UTF-8):	Visualizador de fluxos de imagens obtidas através do Video4Linux
Summary(ru.UTF-8):	Просмотр и запись видеопотоков
Summary(uk.UTF-8):	Перегляд та запис відеопотоків
Name:		xawtv
Version:	3.107
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://linuxtv.org/downloads/xawtv/%{name}-%{version}.tar.bz2
# Source0-md5:	3c9171aeeda7ca3eb2287f45ca7e86a9
Source1:	Xawtv.ad-pl
Source2:	%{name}.desktop
Source3:	%{name}-noxv.desktop
Source4:	%{name}-conf_example-PTK
Source5:	http://dl.bytesex.org/releases/tv-fonts/tv-fonts-1.1.tar.bz2
# Source5-md5:	ae73fc0efd53e53dca7077383cc22b5a
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-channels_list-cable_poland_PTK.patch
Patch2:		%{name}-fullscreen.patch
Patch3:		%{name}-libng_fix.patch
Patch4:		%{name}-path-fix.patch
Patch5:		%{name}-glibc.patch
URL:		https://www.kraxel.org/blog/linux/xawtv/
BuildRequires:	OpenGL-devel
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	fontconfig-devel
BuildRequires:	iconv
BuildRequires:	libdv-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libv4l-devel
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	motif-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zvbi-devel
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	%{_datadir}/X11/app-defaults
%define 	font_dir 	tv-fonts-1.1

%description
A collection tools for video4linux:
- xawtv - X11 TV application
- fbtv - console TV application
- streamer - capture tool (images / movies)
- v4lctl - command line tool to control v4l devices

%description -l pl.UTF-8
Kolekcja narzędzi video dla Linuksa
- xawtv - X11 aplikacje TV
- fbtv - aplikacje TV pod konsolę
- streamer - narzędzie do przechwytywanie obrazu (zdjęcia / filmy)
- v4lctl - narzędzie do kontroli urządzeń v4l

%description -l pt_BR.UTF-8
Uma coleção de ferramentas para o video4linux:
- xawtv - Visualização de filmes (fluxos de imagens) para o X
- fbtv - Versão do xawtv para console com framebuffer
- streamer - ferramenta e captura (imagens / filmes)
- v4lctl - ferramenta de linha de comando para controlar dispositivos
  v4l

%description -l ru.UTF-8
Набор инструментов для работы с видеопотоками по протоколу
video4linux:
- xawtv - интерфейс под X11
- fbtv - консольный интерфейс
- streamer - инструмент для записи (изображение/фильм)
- v4lctl - инструмент командной строки для управления v4l устройствами

Включает также основанную на ncurses программу работы с радио.

%description -l uk.UTF-8
Набір інструментів для роботи з відеопотоками по протоколу
video4linux:
- xawtv - інтерфейс під X11
- fbtv - консольний інтерфейс
- streamer - інструмент для запису (зображення/фільм)
- v4lctl - інструмент командного рядка для управління v4l пристроями

Включає також основану на ncurses програму роботи з радіо.

%package radio
Summary:	radio
Summary(es.UTF-8):	xawtv: radio
Summary(pl.UTF-8):	radio
Summary(pt_BR.UTF-8):	Suporte a rádio no xawtv
Group:		Applications/Sound

%description radio
This is a ncurses-based radio application.

%description radio -l pl.UTF-8
Aplikacje radiowe bazujące na ncurses.

%package misc
Summary:	Misc utils related (or not) to xawtv
Summary(es.UTF-8):	xawtv: misc
Summary(pl.UTF-8):	Różne narzędzia pomocnicze do xawtv
Summary(pt_BR.UTF-8):	Ferramentas adicionais do xawtv
Group:		X11/Applications

%description misc
This package has a few tools you might find useful. They have not to
do very much to do with xawtv. I've used/wrote them for debugging:
- propwatch - monitors properties of X11 windows. If you want to know
  how to keep track of xawtv's _XAWTV_STATION property, look at this.
- dump-mixers - dump mixer settings to stdout
- record - console sound recorder. Has a simple input level meter
  which might be useful to trouble shoot sound problems.
- showriff - display the structure of RIFF files (avi, WAV).

%description misc -l pl.UTF-8
Ten pakiet zawiera sporo użytecznych narzędzi. Nie mają wiele
wspólnego z xawtv. Zostały napisane w celu debagowania xawtv.
- propwatch - monitor ustawień
- dump-mixers - "Dump" mixer
- record - Rejestrator dźwięku.
- showriff - Wyświetla strukturę plików RIFF (avi, WAV).

%description misc -l pt_BR.UTF-8
Ferramentas adicionais para depuração dos componentes do pacote xawtv:
- propwatch - monitora as propriedades de janelas X11. Se você quiser
  saber como monitorar a propriedade _XAWTV_STATION use esta ferramenta.
- dump-mixers - apresenta as configurações do misturador na saída
  padrão.
- record - gravador de som para o console. Tem um medidor de nível de
  entrada que deve ser útil para auxiliar na resolução de problemas de
  som.
- showriff - mostra a estrutura de arquivos RIFF (avi, WAV).

%package alevtd
Summary:	HTTP daemon for alevt teletext decoder
Summary(pl.UTF-8):	Daemon HTTP dla dekodera teletekstu alevt
Group:		Daemons
Requires:	alevt

%description alevtd
HTTP daemon for alevt teletext decoder

%description alevtd -l pl.UTF-8
Daemon HTTP dla dekodera teletekstu alevt

%package ttv
Summary:	ASCII Art TV viewer
Summary(pl.UTF-8):	Tekstowy program do oglądania TV
Group:		X11/Applications

%description ttv
TV tuner program using ASCII characters to display picture.

%description ttv -l pl.UTF-8
Program do obsługi tunera TV wyświetlający obraz przy użyciu znaków
ASCII.

%package -n fonts-misc-xawtv
Summary:	TV fonts
Summary(pl.UTF-8):	Fonty TV
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-misc-xawtv
This package contains a number of fonts which are useful for TV
applications:
- led-fixed: This is the big font which xawtv uses by default for the
  onscreen display in fullscreen mode.
- ets-teletext: This is a teletext font. It contains the block graphic
  characters used by teletext pages. When watching teletext with the mtt
  teletext browser you'll get much better results with these fonts
  installed.
- ets-caption: A font for closed captions.

%description -n fonts-misc-xawtv -l pl.UTF-8
Ten pakiet zawiera zestaw fontów przydatnych dla aplikacji
telewizyjnych:
- led-fixed - duży font, używany domyślnie przez xawtv do wyświetlania
  napisów na ekranie (OSD) w trybie pełnoekranowym
- ets-teletext - font dla telegazety; zawiera znaki grafiki blokowej
  używane na stronach telegazety. Oglądając telegazetę w przeglądarce
  mtt można uzyskać dużo lepsze efekty mając zainstalowane te fonty.
- ets-caption - font do napisów.

%prep
%setup -q -a 5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	%{!?with_aalib:--disable-aalib} \
	%{!?with_lirc:--disable-lirc} \
	--enable-mmx%{!?with_mmx:=no} \
	--enable-motif \
	--disable-quicktime \
	--disable-silent-rules \
	--enable-xfree-ext \
	--enable-xvideo
%{__make} \
	verbose=yes

%{__make} -j1 -C %{font_dir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_fontsdir}/misc} \
	$RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	SUID_ROOT=""

%{__mv} $RPM_BUILD_ROOT%{_datadir}/X11/{de_DE.UTF-8,de}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/X11/{fr_FR.UTF-8,fr}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/X11/{it_IT.UTF-8,it}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/pl/app-defaults/Xawtv
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} .

cp -p %{font_dir}/*.pcf.gz $RPM_BUILD_ROOT%{_fontsdir}/misc
cp -p %{font_dir}/fonts.alias $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.xawtv

%clean
rm -rf $RPM_BUILD_ROOT

%post -n fonts-misc-xawtv
fontpostinst misc

%postun -n fonts-misc-xawtv
fontpostinst misc

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
%attr(755,root,root) %{_libdir}/%{name}

%{_appdefsdir}/Xawtv
%{_appdefsdir}/MoTV
%{_appdefsdir}/mtt
%lang(pl) %{_datadir}/X11/pl/app-defaults/Xawtv
%lang(de) %{_datadir}/X11/de/app-defaults/MoTV
%lang(fr) %{_datadir}/X11/fr/app-defaults/MoTV
%lang(it) %{_datadir}/X11/it/app-defaults/MoTV

%{_desktopdir}/xawtv.desktop
%{_desktopdir}/xawtv-noxv.desktop

%{_datadir}/%{name}

%{_mandir}/man1/fbtv.1*
%{_mandir}/man1/v4l-info.1*
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
%attr(755,root,root) %{_bindir}/alevtd
%{_mandir}/man1/alevtd.1*

%if %{with aalib}
%files ttv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ttv
%{_mandir}/man1/ttv.1*
%lang(es) %{_mandir}/es/man1/ttv.1*
%endif

%files -n fonts-misc-xawtv
%defattr(644,root,root,755)
%{_fontsdir}/misc/caption.pcf.gz
%{_fontsdir}/misc/captioni.pcf.gz
%{_fontsdir}/misc/led-iso8859-*.pcf.gz
%{_fontsdir}/misc/led-iso10646-1.pcf.gz
%{_fontsdir}/misc/led-koi8-r.pcf.gz
%{_fontsdir}/misc/teletext*.pcf.gz
%{_fontsdir}/misc/fonts.alias.xawtv
