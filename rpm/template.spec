Name:           ros-kinetic-mapviz-plugins
Version:        0.2.5
Release:        0%{?dist}
Summary:        ROS mapviz_plugins package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/mapviz
Source0:        %{name}-%{version}.tar.gz

Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-gps-common
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-mapviz
Requires:       ros-kinetic-marti-common-msgs
Requires:       ros-kinetic-marti-nav-msgs
Requires:       ros-kinetic-marti-visualization-msgs
Requires:       ros-kinetic-move-base-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-stereo-msgs
Requires:       ros-kinetic-swri-image-util
Requires:       ros-kinetic-swri-math-util
Requires:       ros-kinetic-swri-route-util
Requires:       ros-kinetic-swri-transform-util
Requires:       ros-kinetic-swri-yaml-util
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-gui
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-gps-common
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-mapviz
BuildRequires:  ros-kinetic-marti-common-msgs
BuildRequires:  ros-kinetic-marti-nav-msgs
BuildRequires:  ros-kinetic-marti-visualization-msgs
BuildRequires:  ros-kinetic-move-base-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-stereo-msgs
BuildRequires:  ros-kinetic-swri-image-util
BuildRequires:  ros-kinetic-swri-math-util
BuildRequires:  ros-kinetic-swri-route-util
BuildRequires:  ros-kinetic-swri-transform-util
BuildRequires:  ros-kinetic-swri-yaml-util
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs

%description
Common plugins for the Mapviz visualization tool

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 12 2018 Marc Alban <malban@swri.org> - 0.2.5-0
- Autogenerated by Bloom

* Fri Aug 11 2017 Marc Alban <malban@swri.org> - 0.2.4-0
- Autogenerated by Bloom

* Sat Dec 10 2016 Marc Alban <malban@swri.org> - 0.2.3-0
- Autogenerated by Bloom

* Wed Dec 07 2016 Marc Alban <malban@swri.org> - 0.2.2-0
- Autogenerated by Bloom

* Thu Jun 23 2016 Marc Alban <malban@swri.org> - 0.2.0-0
- Autogenerated by Bloom

