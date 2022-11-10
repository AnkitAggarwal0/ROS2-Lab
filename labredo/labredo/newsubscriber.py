#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String, Int32
     
class NewSubscriber(Node): 
    def __init__(self):
        super().__init__("newsubscriber") 
        self.subscriber_ = self.create_subscription(String, "lab_news", self.callback_lab_news, 10)
        self.get_logger().info(":(")
        
    def callback_lab_news(self, msg):
        self.get_logger().info(msg.data)
     
def main(args=None):
    rclpy.init(args=args)
    node = NewSubscriber() 
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()