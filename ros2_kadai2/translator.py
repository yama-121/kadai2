import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MorseTranslator(Node):
    def __init__(self):
        super().__init__('translator') 
        self.sub = self.create_subscription(String, 'input_text', self.callback, 10)
        self.pub = self.create_publisher(String, 'morse_code', 10)
        self.dict = {
            'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
            'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
            'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
            'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
            'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
            'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
            'Y': '-.--',  'Z': '--..'
        }

    def callback(self, msg):
        text = msg.data.upper()
        morse_list = []
        for char in text:
            if char in self.dict:
                morse_list.append(self.dict[char]) 
        res = String()
        res.data = ' '.join(morse_list)
        self.pub.publish(res)
        self.get_logger().info(f'Published: {res.data}')

def main():
    rclpy.init()
    node = MorseTranslator()
    rclpy.spin(node)
    rclpy.shutdown()

