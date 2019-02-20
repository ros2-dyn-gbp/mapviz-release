Name:           ros-melodic-multires-image
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS multires_image package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/mapviz
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-gps-common
Requires:       ros-melodic-libqt-core
Requires:       ros-melodic-libqt-opengl
Requires:       ros-melodic-mapviz
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-swri-math-util
Requires:       ros-melodic-swri-transform-util
Requires:       ros-melodic-swri-yaml-util
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-gps-common
BuildRequires:  ros-melodic-libqt-dev
BuildRequires:  ros-melodic-libqt-opengl-dev
BuildRequires:  ros-melodic-mapviz
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-qt-qmake
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-swri-math-util
BuildRequires:  ros-melodic-swri-transform-util
BuildRequires:  ros-melodic-swri-yaml-util
BuildRequires:  ros-melodic-tf

%description
multires_image

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Feb 20 2019 Marc Alban <malban@swri.org> - 1.1.0-0
- Autogenerated by Bloom

* Fri Jan 25 2019 Marc Alban <malban@swri.org> - 1.0.1-0
- Autogenerated by Bloom

* Wed Jan 23 2019 Marc Alban <malban@swri.org> - 1.0.0-0
- Autogenerated by Bloom

* Fri Nov 16 2018 Marc Alban <malban@swri.org> - 0.3.0-0
- Autogenerated by Bloom

* Tue Jul 31 2018 Marc Alban <malban@swri.org> - 0.2.6-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Marc Alban <malban@swri.org> - 0.2.5-0
- Autogenerated by Bloom

