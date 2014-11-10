cmake_minimum_required(VERSION 2.8)
project(calvin_navigation_experiments)

find_package(catkin REQUIRED COMPONENTS
             calvin_navigation)

catkin_package(CATKIN_DEPENDS calvin_navigation)

install(DIRECTORY launch/ DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch)
install(DIRECTORY maps/ DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/maps)
