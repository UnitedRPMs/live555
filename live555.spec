#
# spec file for package live555
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft

%global debug_package %{nil}

Name:		live555
Version:	2020.06.25
Release:	7%{?dist}
Summary:	Live555.com streaming libraries

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://live555.com/liveMedia/
Source0:	https://download.videolan.org/pub/contrib/live555/live.%{version}.tar.gz
#Source0:	http://live555.com/liveMedia/public/live.{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	openssl-devel

%description
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

%package	devel
Summary:	Development files for live555.com streaming libraries
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	live-devel < 0-0.19.2008.04.03
Provides:	live-devel = %{version}-%{release}

%description	devel
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

%package	tools
Summary:	RTSP streaming tools using live555.com streaming libraries
Group:		Applications/Multimedia
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	live-tools < 0-0.19.2008.04.03
Provides:	live-tools = %{version}-%{release}

%description	tools
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

This package contains the live555.com streaming server
(live555MediaServer), the example programs (openRTSP, playSIP, sapWatch,
vobStreamer) and a variety of test tools.


%prep
%setup -q -n live
sed -i -e "s|-O2|$RPM_OPT_FLAGS|" \
  config.linux-with-shared-libraries

sed -i '/xlocale.h/d' liveMedia/include/Locale.hh

  sed \
      -e 's/$(INCLUDES) -I. -O2 -DSOCKLEN_T/$(INCLUDES) -I. -O2 -I. -fPIC -DPIC -DXLOCALE_NOT_USED=1 -DRTSPCLIENT_SYNCHRONOUS_INTERFACE=1 -DSOCKLEN_T/g' \
      -i config.linux

%build
./genMakefiles %{_target_os}-with-shared-libraries
# make {?_smp_mflags}
make C_COMPILER="${CC:-gcc}" CPLUSPLUS_COMPILER="${CXX:-g++}"

%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}

#RPM Macros support
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
cat > $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.live555 << EOF
# live555 RPM Macros
%live555_version	%{version}
EOF
touch -r COPYING $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.live555

#Fix library dependency detection
chmod a+x $RPM_BUILD_ROOT%{_libdir}/*.so*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/libBasicUsageEnvironment.so.*
%{_libdir}/libgroupsock.so.*
%{_libdir}/libliveMedia.so.*
%{_libdir}/libUsageEnvironment.so.*

%files tools
%{_bindir}/*

%files devel
%doc COPYING README
%config %{_sysconfdir}/rpm/macros.live555
%{_libdir}/libBasicUsageEnvironment.so
%{_libdir}/libgroupsock.so
%{_libdir}/libliveMedia.so
%{_libdir}/libUsageEnvironment.so
%{_includedir}/BasicUsageEnvironment/
%{_includedir}/groupsock/
%{_includedir}/liveMedia/
%{_includedir}/UsageEnvironment/


%changelog

* Fri Jul 03 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.06.25-7
- Updated to 2020.06.25

* Sat May 16 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.05.15-7
- Updated to 2020.05.15

* Sun Apr 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.04.24-7
- Updated to 2020.04.24

* Wed Apr 15 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.04.12-7
- Updated to 2020.04.12

* Wed Apr 08 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.04.06-7
- Updated to 2020.04.06

* Sun Mar 15 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.03.06-7
- Updated to 2020.03.06

* Thu Feb 13 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.02.11-7
- Updated to 2020.02.11

* Wed Feb 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.01.28-7
- Updated to 2020.01.28

* Fri Jan 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2020.01.10-7
- Updated to 2020.01.10

* Fri Dec 13 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.12.10-7
- Updated to 2019.12.10

* Fri Dec 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.12.05-7
- Updated to 2019.12.05

* Mon Nov 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.11.22-7
- Updated to 2019.11.22

* Mon Nov 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.11.11-7
- Updated to 2019.11.11

* Wed Nov 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.11.05-7
- Updated to 2019.11.05

* Thu Oct 24 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.10.20-7
- Updated to 2019.10.20

* Mon Oct 14 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.10.11-7
- Updated to 2019.10.11

* Fri Oct 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.10.10-7
- Updated to 2019.10.10

* Fri Oct 04 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.09.30-7
- Updated to 2019.09.30

* Wed Sep 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.09.18-7
- Updated to 2019.09.18

* Fri Aug 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.08.28-7
- Updated to 2019.08.28

* Thu Aug 29 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.08.16-7
- Updated to 2019.08.16

* Tue Aug 13 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.08.12-7
- Updated to 2019.08.12

* Tue Jul 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.07.27-7
- Updated to 2019.07.27

* Sun Jun 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.06.28-7
- Updated to 2019.06.28

* Thu May 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.05.29-7
- Updated to 2019.05.29

* Fri May 17 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.05.12-7
- Updated to 2019.05.12

* Sat May 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.05.03-7
- Updated to 2019.05.03

* Thu Apr 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.04.24-7
- Updated to 2019.04.24

* Sat Apr 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.03.06-7
- Updated to 2019.03.06

* Fri Mar 01 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.02.27-7
- Updated to 2019.02.27

* Mon Feb 04 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2019.02.03-7
- Updated to 2019.02.03

* Sat Dec 15 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.12.14-7
- Updated to 2018.12.14

* Wed Nov 28 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.11.26-7
- Updated to 2018.11.26

* Mon Oct 22 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.10.17-7
- Updated to 2018.10.17

* Sun Oct 14 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.10.10-3
- Updated to 2018.10.10

* Wed Sep 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.09.18-3
- Updated to 2018.09.18

* Fri Sep 14 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.09.10-3
- Updated to 2018.09.10

* Fri Sep 07 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.09.06-3
- Updated to 2018.09.06

* Thu Aug 09 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.08.05-3
- Updated to 2018.08.05

* Sun Jul 08 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.07.07-3
- Updated to 2018.07.01

* Fri Jul 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.07.01-3
- Updated to 2018.07.01

* Thu May 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2018.04.25-3
- Updated to 2018.04.25

* Sat Mar 03 2018 David Vásquez <davidjeremias82 AT gmail DOT com> 2018.02.28-3
- Updated to 2018.02.28

* Fri Feb 16 2018 David Vásquez <davidjeremias82 AT gmail DOT com> 2018.02.12-3
- Updated to 2018.02.12

* Sun Feb 04 2018 David Vásquez <davidjeremias82 AT gmail DOT com> 2018.01.29-3
- Updated to 2018.01.29

* Tue Jan 30 2018 David Vásquez <davidjeremias82 AT gmail DOT com> 2018.01.24-3
- Updated to 2018.01.24

* Wed Nov 01 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 2017.10.28-3
- Updated to 2017.10.28

* Tue Sep 26 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 2017.09.12-3
- Updated to 2017.09.12-3

* Thu Jul 27 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 2017.07.18-3
- Updated to 2017.07.18-3

* Sun Jul 09 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 2017.06.04-3
- Updated to 2017.06.04

* Fri May 19 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 2017.04.26-3
- Updated to 2017.04.26-3

* Tue Mar 07 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 2017.01.26-2
- Updated to 2017.01.26

* Wed Oct 05 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 2016.09.22-1
- Updated to 2016.09.22

* Wed Aug 24 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 2016.08.07-1
- Updated 2016.08.07

* Tue Jul 05 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 2016.06.26-1
- Updated 2016.06.26

* Tue Apr 19 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 2016.04.01-1
- Updated to 2016.04.01
