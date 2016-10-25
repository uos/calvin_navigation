calvin_navigation
=================

This stack contains navigation components for Calvin.

Running calvin_navigation in Gazebo
-----------------------------------

1. Edit the file `calvin_navigation/config/common_costmap_params.yaml` and remove the `kinect` input from the `observation_sources`:

        -observation_sources: scan scan_filtered lms200 lms200_scan_filtered kinect
        +observation_sources: scan scan_filtered lms200 lms200_scan_filtered

   This is necessary in Gazebo because Calvin starts with an outstretched
   Katana arm, and there are some issues with the self filter in Gazebo. If we
   use the kinect for obstacle avoidance, there are always some points on the
   arm remaining in the filtered point cloud, which will always appear as an
   obstacle right in front of the robot in the collision map.

2. Bring up Calvin in Gazebo:

        LC_ALL=C roslaunch calvin_gazebo calvin_avz_world.launch

   This starts Calvin in the "AVZ 5th floor" world. (The `LC_ALL` trick is
   necessary to work around
   [this bug](https://bitbucket.org/osrf/sdformat/issues/60/error-when-starting-gazebo-if-lc_numeric)
   on indigo.)

   Make sure that it shows

        Started controllers: katana_arm_controller, kinect_pitch_joint_controller, webcam_pitch_joint_controller, joint_state_controller

   on the console. If it doesn't, kill and restart. You'll notice it's
   wrong when the Kinect camera is pointing straight down and the Katana arm
   doesn't show up in RViz. You can also try this instead (leave the last
   command running):

        rosrun controller_manager controller_manager stop katana_arm_controller kinect_pitch_joint_controller webcam_pitch_joint_controller joint_state_controller
        rosrun controller_manager controller_manager unload katana_arm_controller kinect_pitch_joint_controller webcam_pitch_joint_controller joint_state_controller
        rosrun controller_manager spawner katana_arm_controller kinect_pitch_joint_controller webcam_pitch_joint_controller joint_state_controller

3. Start the navigation stack with AMCL:

        roslaunch calvin_navigation single_map_navigation.launch mapmetafile:=$(rospack find uos_maps)/maps/avz5floor_gazebo.yaml

4. Run RViz:

        rosrun rviz rviz -d $(rospack find calvin_navigation)/rviz/navigation.rviz

   In RViz, click "2D Pose Estimate" and select the approximate position of the
   robot in the map.

5. Run teleop:

        rosrun uos_diffdrive_teleop uos_diffdrive_teleop_key

   Using teleop, drive the robot around a bit until it has a good localization
   (watch the AMCL Particle Swarm in RViz). Remember to keep the focus on the
   terminal window that runs `uos_diffdrive_teleop_key` while pressing buttons.
   It is important that the robot's localization is good before trying to pass
   any narrow doorways.

6. Give a goal to `move_base` by clicking the "2D Nav Goal" button in RViz and
   selecting a pose.


Alternatively, you can also run Calvin in the "AVZ 3rd floor" world by using
these commands in step 2 and 3:

    LC_ALL=C roslaunch calvin_gazebo calvin_avz3rd_world.launch
    roslaunch calvin_navigation single_map_navigation.launch mapmetafile:=$(rospack find calvin_navigation_experiments)/maps/avz3floor_complete.yaml

If you want to try [gmapping](http://wiki.ros.org/gmapping) instead of AMCL, run this instead of step 3:

    roslaunch calvin_navigation slam.launch

That launch file also starts
[frontier_exploration](http://wiki.ros.org/frontier_exploration). If you want
to try it, visualize the topics `exploration_polygon_marker` and
`/explore_server/explore_costmap/costmap` in RViz, draw a closed polygon using
the "Publish Point" button and click once inside the polygon.


calvin_navigation
-----------------

This package contains launch files for the basic navigation behaviors and
configurations for the used components. There are three top level launch files:

* slam.launch - starts gmapping, frontier exploration and move_base for semi-automatic 2d mapping
* single_map_navigation.launch - starts move_base and move_base using a single map for navigation
* dual_map_navigation.launch - starts move_base and move_base using two different maps for navigation and localization

As the latter two launch files require prepared maps they are intended to be
included in more sophisticated launch files, located elsewhere, e.g. in
`calvin_navigation_experiments`.

calvin_navigation_experiments
-----------------------------

This package contains high-level launch files to call Calvin's navigation behaviors in different environments.
