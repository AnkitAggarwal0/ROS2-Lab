from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='labredo',
            executable='newpublisher',
            output='screen'),

        Node(
            package='labredo',
            executable='newsubscriber',
            output='screen'),
    ])