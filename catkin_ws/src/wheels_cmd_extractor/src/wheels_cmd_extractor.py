#!/usr/bin/env python
import rospy
import csv
from duckietown_msgs.msg import WheelsCmdStamped

class WheelsCmdExtractorNode(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        self.wheels_cmd_topic = rospy.get_param("~wheels_cmd_topic")
        self.csvfile = open('wheels_cmd_topic.csv', 'w')
        self.spamwriter = csv.writer(self.csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # rospy.loginfo("[%s] Initializing " %(self.node_name))
        #self.mappings = rospy.get_param("~mappings")


        self.sub = rospy.Subscriber(self.wheels_cmd_topic,WheelsCmdStamped,self.cbWheelsCmd)


    def cbWheelsCmd(self,msg):
            self.spamwriter.writerow(['{}.{}'.format(str(msg.header.stamp.secs),str(msg.header.stamp.nsecs)),
                                      msg.vel_left,
                                      msg.vel_right])
            rospy.loginfo("Saved wheels command ({},{})".format(msg.vel_left, msg.vel_right))

    def on_shutdown(self):
        self.csvfile.close()
        rospy.loginfo("[%s] Shutting down." %(self.node_name))

if __name__ == '__main__':
    # Initialize the node with rospy
    rospy.init_node('car_cmd_switch_node', anonymous=False)
    # Create the DaguCar object
    node = WheelsCmdExtractorNode()
    # Setup proper shutdown behavior
    rospy.on_shutdown(node.on_shutdown)
    # Keep it spinning to keep the node alive
    rospy.spin()
