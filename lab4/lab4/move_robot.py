#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import transforms3d
import math
     
     

global publis, subscri 
               
def control_loop(self, msg):
        
    target_x = 27
    target_y = 34
    dist_x = target_x - msg.pose.pose.position.x
    dist_y = target_y - msg.pose.pose.position.y
        #print('current position: {} {}'.format(msg.pose.pose.position.x,msg.pose.pose.position.y))
    distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        #print('distance : {}'.format(round(distance, 3)))
        
        
    goal_theta = math.atan2(dist_y, dist_x)
    quat = msg.pose.pose.orientation
    roll, pitch, yaw = transforms3d.euler.quat2euler([quat.w,quat.x,quat.y,quat.z])
    diff = math.pi - round(yaw, 2) + round(goal_theta, 2)
       # print('yaw: {}'.format(round(yaw, 2)))
       # print('target angle: {}'.format(round(goal_theta, 2)))

    if diff > math.pi:
        diff -= 2*math.pi
    elif diff < -math.pi:
        diff += 2*math.pi
        #print('orientation : {}'.format(round(diff, 2)))   
        
    vel = Twist()
        
    if diff > 0.8:
        vel.linear.x = 0.0
        vel.angular.z = 0.8 
        publis.publish(vel)
          
    else:
        if distance > 0.2:
            vel.linear.x = 1.0
            vel.angular.z = 0.0  
            
               
        else:
            vel.linear.x = 0.0
            vel.angular.z = 0.0 
        
        publis.publish(vel)            
        # print('speed : {}'.format(vel))    
        # self.publisher.publish(vel)
        
     
def main(args=None):
    global publis, subscri 
    rclpy.init(args=args)
    GotoGoal = Node('go_to_goalie')
    publis = GotoGoal.create_publisher(Twist,'/cmd_vel',10)
    subscri = GotoGoal.create_subscription(Odometry, '/odom',control_loop,10)
    rclpy.spin(GotoGoal)
    rclpy.shutdown()
    
       
if __name__ == "__main__":
	main()