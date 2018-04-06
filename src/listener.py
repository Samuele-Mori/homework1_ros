#!/usr/bin/env python2

import rospy
from homework1.msg import Student
from std_msgs.msg import String


print_mode = "a"


def callback_talker(data):
	if print_mode == "a":
		rospy.loginfo("Info studente: %s, %s, %s\n", data.nome, data.eta, data.corso_laurea)
	if print_mode == "n":
		rospy.loginfo("Nome: %s\n", data.nome)
	if print_mode == "e":
		rospy.loginfo("Eta: %s\n", data.eta)
	if print_mode == "c":
		rospy.loginfo("Corso di laurea: %s\n", data.corso_laurea)
	

def callback_filter(data):
	rospy.loginfo("Print_mode = %s\n", data.data)

	global print_mode
	print_mode = data.data


def listener():
	rospy.init_node('Listener', anonymous=True)

	rospy.Subscriber("students", Student, callback_talker)
	rospy.Subscriber("filter", String, callback_filter)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
