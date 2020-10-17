#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

PI = 3.1415926535897

def pose_callback(msg):
	msg.x=0
	msg.angular_velocity=0

def draw_circle():
	rospy.init_node('node_turle_revolve1', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	vel_msg = Twist()
	speed = 1
	radius = 1.5

	relative_angle = 2*PI


	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = speed/radius
	
	# Setting the current time for distance calculus
	t0 = rospy.Time.now().to_sec()
	current_angle = 0

	while(current_angle <= relative_angle):
        	pub.publish(vel_msg)
		rospy.loginfo("Moving in a circle")
    		rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        	t1 = rospy.Time.now().to_sec()
        	current_angle = (speed/radius)*(t1-t0)
		print(current_angle)


	#Forcing our robot to stop
	vel_msg.linear.x=0
	vel_msg.angular.z = 1
	pub.publish(vel_msg)
	rospy.loginfo("goal reached")
	rospy.spin()

if __name__ == "__main__":
	try:
		draw_circle()
	except rospy.ROSInterruptException:
		pass


