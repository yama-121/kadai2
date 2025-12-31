from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='ros2_kadai2', executable='translator', name='translator'),
        Node(package='ros2_kadai2', executable='display', name='display'),
    ])

