#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
  
  
class TurtleControllerNode1(Node):
    def __init__(self):
        super().__init__("turtlesim_controller")
        self.target_x = 8.0
        self.target_y = 0.0
        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
    
    def callback_turtle_pose(self,msg):
        self.pose_ = msg
        
    def control_loop(self):
        if self.pose_ == None:
            return
        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        msg = Twist()
        if distance > 0.5:
            msg.linear.x = distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
                
            msg.angular.z = diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
        self.cmd_vel_publisher_.publish(msg)

class TurtleControllerNode2(Node):
    def __init__(self):
        super().__init__("turtlesim_controller")
        self.target_x = 8.0
        self.target_y = 8.0
        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
    
    def callback_turtle_pose(self,msg):
        self.pose_ = msg
        
    def control_loop(self):
        if self.pose_ == None:
            return
        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        msg = Twist()
        if distance > 0.5:
            msg.linear.x = distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
                
            msg.angular.z = diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
        self.cmd_vel_publisher_.publish(msg)
        
class TurtleControllerNode3(Node):
    def __init__(self):
        super().__init__("turtlesim_controller")
        self.target_x = 0.0
        self.target_y = 8.0
        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
    
    def callback_turtle_pose(self,msg):
        self.pose_ = msg
        
    def control_loop(self):
        if self.pose_ == None:
            return
        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        msg = Twist()
        if distance > 0.5:
            msg.linear.x = distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
                
            msg.angular.z = diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
        self.cmd_vel_publisher_.publish(msg)

class TurtleControllerNode4(Node):
    def __init__(self):
        super().__init__("turtlesim_controller")
        self.target_x = 0.0
        self.target_y = 0.0
        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
    
    def callback_turtle_pose(self,msg):
        self.pose_ = msg
        
    def control_loop(self):
        if self.pose_ == None:
            return
        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
        msg = Twist()
        if distance > 0.5:
            msg.linear.x = distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
                
            msg.angular.z = diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
        self.cmd_vel_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node1 = TurtleControllerNode1()
    rclpy.spin(node1)
    rclpy.shutdown()
    
    rclpy.init(args=args)
    node2 = TurtleControllerNode2()
    rclpy.spin(node2)
    rclpy.shutdown() 

    rclpy.init(args=args)
    node3 = TurtleControllerNode3()
    rclpy.spin(node3)
    rclpy.shutdown() 

    rclpy.init(args=args)
    node4 = TurtleControllerNode4()
    rclpy.spin(node4)
    rclpy.shutdown()
       
if __name__ == "__main__":
	main()
