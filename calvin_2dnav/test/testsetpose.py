#!/usr/bin/env python
import roslib; roslib.load_manifest('calvin_2dnav')
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
import random

if __name__ == '__main__':
  try:
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped)
    rospy.init_node('setposeestimate')
    pose = PoseWithCovarianceStamped()
    pose.header.frame_id = "/map"
    pose.header.stamp = rospy.Time.now()
    pose.pose.pose.position.x = random.randint(1,5)
    pose.pose.pose.position.y = random.randint(1,5)
    pose.pose.pose.position.z = 1.0
    pose.pose.pose.orientation.x = 0.0
    pose.pose.pose.orientation.y = 0.0
    pose.pose.pose.orientation.z = 0.0
    pose.pose.pose.orientation.w = 1.0
    rospy.sleep(0.1)
    pub.publish(pose)
    rospy.loginfo("Pose sent: %d %d %d", pose.pose.pose.position.x, pose.pose.pose.position.y, pose.pose.pose.position.z)
  except rospy.ROSInterruptException:
    rospy.logerror("exception")
