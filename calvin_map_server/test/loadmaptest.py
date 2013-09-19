#!/usr/bin/env python
import roslib; roslib.load_manifest('map_server')

import sys

import rospy
from map_server.srv import *

def usage():
    return "%s yamlfile"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        yaml = sys.argv[1]
    else:
        print usage()
        sys.exit(1)
    print "Requesting to load map from "+yaml
    rospy.wait_for_service('load_map')
    try:
        loadmapproxy = rospy.ServiceProxy('load_map', LoadMap)
        resp = loadmapproxy(yaml)
        print resp.response
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
