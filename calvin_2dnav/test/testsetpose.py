#!/usr/bin/env python
import roslib; roslib.load_manifest('calvin_2dnav')
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

if __name__ == '__main__':
  try:
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped)
    rospy.init_node('setposeestimate')
    pose = PoseWithCovarianceStamped()
    pose.header.frame_id = "/map"
    pose.header.stamp = rospy.Time.now()
    pose.pose.pose.position.x = 5
    pose.pose.pose.position.y = 5
    pose.pose.pose.position.z = 0
    pose.pose.covariance[0] = 0.7
    pose.pose.covariance[35] = 0.7
    rospy.loginfo("Pose sent: %d %d %d", pose.pose.pose.position.x, pose.pose.pose.position.y, pose.pose.pose.position.z)
    pub.publish(pose)
  except rospy.ROSInterruptException:
    rospy.logerror("exception")
