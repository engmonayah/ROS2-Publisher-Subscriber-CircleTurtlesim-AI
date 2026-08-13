import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.pub = self.create_publisher(String, 'robot_channel', 10)
        self.timer = self.create_timer(1, self.send)

    def send(self):
        msg = String()
        msg.data = 'Hello, I am nony.'
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Publisher()
    rclpy.spin(node)

main()
