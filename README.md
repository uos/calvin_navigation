calvin_navigation
=============

This stack contains navigation components for Calvin. Specifically, it provides: 

##calvin_navigation

This package contains launch files for the basic navigation behaviors and configurations for the used components. There are three top level launch files:

* slam.launch - starts gmapping, frontier exploration and move_base for semi-automatic 2d mapping
* single_map_navigation.launch - starts move_base and move_base using a single map for navigation
* dual_map_navigation.launch - starts move_base and move_base using two different maps for navigation and localization

As the latter two launch files require prepared maps they are intended to be included in more sophisticated launch files, located elsewhere, e.g. in `calvin_navigation_experiments`.

##calvin_navigation_experiments

This package contains high-level launch files to call Calvin's navigation behaviors in different environments.

For more information, visit the [calvin_navigation ROS wiki page](http://www.ros.org/wiki/calvin_navigation).
