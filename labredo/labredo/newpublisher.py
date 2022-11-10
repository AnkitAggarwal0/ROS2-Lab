#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NewPublisher(Node):

    def __init__(self):
        super().__init__("new_publisher")
        self.robot_name_ = "Revolution"
        self.publisher_ = self.create_publisher(String,"lab_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info(":)")

    def publish_news(self):
        msg = String()
        msg.data = "Vive la " + str(self.robot_name_)
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args = args)
    node = NewPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()