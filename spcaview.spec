
%define		_snap 20050701

Summary:	spcaview
Summary(pl):	spcaview
Name:		spcaview
Version:	1.0.8
Release:	0.1
Epoch:		0
License:	GPL
Group:		X11/Applications
Source0:	http://mxhaard.free.fr/spca50x/Download/spcaview-%{_snap}.tar.gz
# Source0-md5:	447f766db5e0b9dba304c5f3ebb55cdc
URL:		http://spca50x.sourceforge.net/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spcaview is able to stream, record and play video and sound in MJPG I420 RGB16 RGB24 
or RGB32 and raw data RAWD Norme PAL, SECAM, NTSC and Channel CBVS or S-VIDEO.

%prep
%setup -q -n spcaview-%{_snap}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install spcaview spcaserv $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/spcaview
%attr(755,root,root) %{_bindir}/spcaserv
