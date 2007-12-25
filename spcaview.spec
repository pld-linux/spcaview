# TODO: 
# - add http://mxhaard.free.fr/spca50x/Download/spcagui20060127.tar.gz
# - add http://mxhaard.free.fr/spca50x/Download/sp54convert.tar.gz

%define		_snap 20071224

Summary:	spcaview - streaming, recording and playing video and sound
Summary(pl.UTF-8):	spcaview - tworzenie strumieni, nagrywanie i odtwarzanie obrazu i dźwięku
Name:		spcaview
Version:	1.1.8
Release:	0.%{_snap}.1
Epoch:		0
License:	GPL v2+
Group:		X11/Applications
Source0:	http://mxhaard.free.fr/spca50x/Download/spcaview-%{_snap}.tar.gz
# Source0-md5:	12e46424844b937dd55eab28f74bcd8d
Patch0:		%{name}-Makefile.patch
URL:		http://spca50x.sourceforge.net/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spcaview is able to stream, record and play video and sound in MJPG
I420, RGB16, RGB24 or RGB32 and raw data RAWD Norme PAL, SECAM, NTSC
and Channel CBVS or S-VIDEO.

%description -l pl.UTF-8
spcaview potrafi tworzyć strumienie, nagrywać i odtwarzać obraz i
dźwięk w formatach MJPG I420, RGB16, RGB24 i RGB32 oraz surowe dane
RAWD Norme PAL, SECAM, NTSC oraz Channel CBVS i S-VIDEO.

%prep
%setup -q -n spcaview-%{_snap}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install spcacat spcaserv spcaview $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/spcacat
%attr(755,root,root) %{_bindir}/spcaserv
%attr(755,root,root) %{_bindir}/spcaview
