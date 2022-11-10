#! /usr/bin/env python
import rclpy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
import transforms3d
from rclpy.node import Node


import math

#active_ = False

# robot state variables
position_ = Point()
yaw_ = 0
# machine state
state_ = 0
# goal
desired_position_ = Point()
desired_position_.x = 0.0
desired_position_.y = 7.0
#desired_position_.z = 0
# parameters
yaw_precision_ = math.pi / 10 # +/- 2 degree allowed
dist_precision_ = 0.1

# publishers

# service callbacks
#def go_to_point_switch(req):
 #   global active_
  #  active_ = req.data
  #  res = SetBoolResponse()
  #  res.success = True
  #  res.message = 'Done!'
  #  return res

# callbacks
def clbk_odom(msg):
    global position_
    global yaw_
    
    # position
    position_ = msg.pose.pose.position
    
    # yaw
    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w)
    euler = transforms3d.euler_from_quaternion(quaternion)
    yaw_ = euler[2]

def change_state(state):
    global state_
    state_ = state
    print ('State changed to [%s]' % state_)

def normalize_angle(angle):
    if(math.fabs(angle) > math.pi):
        angle = angle - (2 * math.pi * angle) / (math.fabs(angle))
    return angle

def fix_yaw(des_pos):
    global yaw_, pub, yaw_precision_, state_ 
    desired_yaw = math.atan2(des_pos.y - position_.y, des_pos.x - position_.x)
    err_yaw = normalize_angle(desired_yaw - yaw_)
    
    print(err_yaw)
    
    twist_msg = Twist()
    if math.fabs(err_yaw) > yaw_precision_:
        twist_msg.angular.z = 0.6 if err_yaw > 0 else -0.6
    
    pub.publish(twist_msg)
    
    # state change conditions
    if math.fabs(err_yaw) <= yaw_precision_:
        print ('Yaw error: [%s]' % err_yaw)
        change_state(1)

def go_straight_ahead(des_pos):
    global yaw_, pub, yaw_precision_, state_
    desired_yaw = math.atan2(des_pos.y - position_.y, des_pos.x - position_.x)
    err_yaw = desired_yaw - yaw_
    err_pos = math.sqrt(pow(des_pos.y- position_.y, 2) + pow(des_pos.x - position_.x, 2)) 
    
    if err_pos > dist_precision_:
        twist_msg = Twist()
        twist_msg.linear.x = 0.8
        pub.publish(twist_msg)
    else:
        print ('Position error: [%s]' % err_pos)
        change_state(2)
    
    # state change conditions
    if math.fabs(err_yaw) > yaw_precision_:
        print ('Yaw error: [%s]' % err_yaw)
        change_state(0)

def done():
    twist_msg = Twist()
    twist_msg.linear.x = 0
    twist_msg.angular.z = 0
    pub.publish(twist_msg)

def main(args=None):
    global pub, node
    rclpy.init(args=args)
    
    node = Node('go_to_point')
    
    pub = node.create_publisher(Twist, '/cmd_vel', 10)
    sub_odom = node.create_subscription(Odometry, '/odom', clbk_odom, 10)
    
    #srv = rospy.Service('go_to_point_switch', SetBool, go_to_point_switch)
    
    rclpy.spin(node)
    while not rclpy.shutdown():
        #if not active_:
             #continue
        #else:
            if state_ == 0:
                # fix_yaw(desired_position_)
                node.create_timer(2, fix_yaw(desired_position_))
            elif state_ == 1:
                 # go_straight_ahead(desired_position_)
                node.create_timer(2, go_straight_ahead(desired_position_))
            elif state_ == 2:
                #done()
                node.create_timer(2, done())
            else:
                print('Unknown state!')
                
    rclpy.shutdown()
if __name__ == '__main__':
    main()