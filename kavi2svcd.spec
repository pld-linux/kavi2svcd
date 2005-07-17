Summary:	kavi2svcd - a GUI for generating MPEG files from an AVI file
Summary(pl):	kavi2svcd - GUI do generowania plików MPEG z plików AVI
Name:		kavi2svcd
Version:	0.8.5
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kavi2svcd/%{name}-%{version}.tar.gz
# Source0-md5:	cbe04045102b4991e8e1bd33e2f05468
URL:		http://www.cornelinux.de/web/linux/kavi2svcd/index-english.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.167
Requires:	cdrdao
Requires:	mjpegtools
Requires:	transcode
Requires:	vcdimager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kavi2svcd is a GUI for generating MPEG files from an AVI file using
transcode and mplex. It then generates a Video CD image using
vcdimager and burns to CD with cdrdao. It can generate m1v, m2v, and
mpa files, multiplex the MPEG file, generate cue and bin files, and
allows the generated command lines to be edited before executing them.

%description -l pl
kavi2svcd to GUI do generowania plików MPEG z plików AVI przy u¿yciu
narzêdzi transcode i mplex. Generuje tak¿e obrazy Video CD przy u¿yciu
vcdimagera i wypala na CD przy u¿yciu cdrdao. Mo¿e tak¿e generowaæ
pliki m1v, m2v i mpa, przeplataæ plik MPEG, generowaæ pliki cue i bin,
a tak¿e pozwala na modyfikowanie wygenerowanych linii poleceñ przed
ich wykonaniem.

%prep
%setup -q

%build
%configure
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT\
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kavi2svcd
