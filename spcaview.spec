# TODO: 
# - optflags
# - add http://mxhaard.free.fr/spca50x/Download/spcagui20060127.tar.gz
# - add http://mxhaard.free.fr/spca50x/Download/sp54convert.tar.gz
# - add spcacat	

%define		_snap 20051212

Summary:	spcaview - streaming, recording and playing video and sound
Summary(pl):	spcaview - tworzenie strumieni, nagrywanie i odtwarzanie obrazu i d¼wiêku
Name:		spcaview
Version:	1.1.5
Release:	0.1
Epoch:		0
License:	GPL
Group:		X11/Applications
Source0:	http://mxhaard.free.fr/spca50x/Download/spcaview-%{_snap}.tar.gz
# Source0-md5:	1420f4e5e31bcb53c31eaba9850a2c01
URL:		http://spca50x.sourceforge.net/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spcaview is able to stream, record and play video and sound in MJPG
I420, RGB16, RGB24 or RGB32 and raw data RAWD Norme PAL, SECAM, NTSC
and Channel CBVS or S-VIDEO.

%description -l pl
spcaview potrafi tworzyæ strumienie, nagrywaæ i odtwarzaæ obraz i
d¼wiêk w formatach MJPG I420, RGB16, RGB24 i RGB32 oraz surowe dane
RAWD Norme PAL, SECAM, NTSC oraz Channel CBVS i S-VIDEO.

%prep
%setup -q -n spcaview-%{_snap}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install spcaview spcaserv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/spcaview
%attr(755,root,root) %{_bindir}/spcaserv
