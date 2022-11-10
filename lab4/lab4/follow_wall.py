#! /usr/bin/env 

from operator import truediv
import rospy 
from std_srvs.srv import *
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



pub_ = None 
regions_ = {
        'right': 0,
        'left': 0,
        'front': 0,
        'fright': 0,
        'fleft': 0,
}
state_ = 0 
state_dict_ = {
    0: 'find the wall',
    1: 'turn left',
    2: 'follow the wall',
}
active_ = False 


# define callback function
def clbk_laser(msg):
    global regions_
    regions_ = {
        'right': min(min(msg.ranges[0:143]), 10),
        'fright' : min(min(msg.ranges[144:287]), 10),
        'front' : min(min(msg.ranges[288:431]), 10),
        'fleft' : min(min(msg.ranges[432:575]), 10),
        'left' : min(min(msg.ranges[576:713]), 10),
    }

    take_action()

def wall_follower_switch(req):
    global active_
    active_ = req.data
    res = SetBoolResponse()
    res.success = True
    res.message = 'Done!'
    return res 


# define take action function
def take_action():
    global regions_
    msg = Twist()
    linear_x = 0
    angular_z = 0 

    state_description = ''

    d = 1.5 

    if regions_['front'] > d and regions_['fleft'] > d and regions_['fright'] > d :
        state_description = 'case 1 - nothing'
        change_state(0)
    elif regions_['front'] < d and regions_['fleft'] > d and regions_['fright'] > d :
        state_description = 'case 2 - front'
        change_state(1)
    elif regions_['front'] > d and regions_['fleft'] > d and regions_['fright'] < d :
        state_description = 'case 3 - fright'
        change_state(2)
    elif regions_['front'] > d and regions_['fleft'] < d and regions_['fright'] > d :
        state_description = 'case 4 - fleft'
        change_state(0)
    elif regions_['front'] < d and regions_['fleft'] > d and regions_['fright'] < d :
        state_description = 'case 5 - front and fright'
        change_state(1)
    elif regions_['front'] < d and regions_['fleft'] < d and regions_['fright'] > d :
        state_description = 'case 6 front and fleft'
        change_state(1)
    elif regions_['front'] < d and regions_['fleft'] < d and regions_['fright'] < d :
        state_description = 'case 7 - front and fleft and fright'
        change_state(1)
    elif regions_['front'] > d and regions_['fleft'] < d and regions_['fright'] < d :
        state_description = 'case 8 - fleft and fright'
        change_state(0)
    else:
        state_description = 'unknown case'
        rospy.loginfo(regions_)


# define change state
def change_state(state):
    global state_ , state_dict_ 
    if state is not state_:
        print ('wall follower - [%s]')  %(state, state_dict_[state])
        state_ = state


# def finding wall
def find_wall():
    msg = Twist()
    msg.linear.x = 0.2
    msg.angular.z = -0.3
    return msg 


# define turning left 
def turn_left():
    msg = Twist()
    msg.angular.z = 0.3 
    return msg 


# define following wall
def follow_the_wall():
    msg = Twist()
    msg.linear.x = 0.5 
    return msg 


# define the main function 
def main():
    global pub_

    rospy.init_node('reading_laser')

    pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1 )

    sub = rospy.Subscriber('/m2wr/laser/scan', LaserScan, clbk_laser)

    srv = rospy.Service('/wall_follower_switch', SetBool , wall_follower_switch)

    rate = rospy.Rate(20)
    while not rospy.is_shutdown:
        if not active_:
            rate.sleep()
            continue
        
        msg = Twist()
        if state_ == 0:
            msg = find_wall()
        elif state_ == 1:
            msg = turn_left()
        elif state_ ==2:
            msg = follow_the_wall()
            pass
        else:
            rospy.logerr('Unknow State!')
        pub_.publish(msg)
        rate.sleep()


if __name__ == "__main__":
    main()