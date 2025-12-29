import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MorseDisplay(Node):
    def __init__(self):
        super().__init__('display')
        self.sub = self.create_subscription(String, 'morse_code', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'\n--- Morse Received ---\n{msg.data}\n----------------------')

def main():
    rclpy.init()
    node = MorseDisplay()
    rclpy.spin(node)
    rclpy.shutdown()
