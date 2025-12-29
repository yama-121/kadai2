import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MorseTranslator(Node):
    def __init__(self):
        super().__init__('translator')
        # 辞書の定義
        self.dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'}
        
        self.sub = self.create_subscription(String, 'input_text', self.callback, 10)
        self.pub = self.create_publisher(String, 'morse_code', 10)

    def callback(self, msg):
        text = msg.data.upper()
        morse = []
        for char in text:
            if char in self.dict:
                morse.append(self.dict[char])
        
        result = String()
        result.data = ' '.join(morse)
        self.pub.publish(result)
        self.get_logger().info(f'Published: {result.data}')

def main():
    rclpy.init()
    node = MorseTranslator()
    rclpy.spin(node)
    rclpy.shutdown()
