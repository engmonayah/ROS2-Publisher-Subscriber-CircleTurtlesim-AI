import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.sub = self.create_subscription(String, 'robot_channel', self.receive, 10)

    def receive(self, msg):
        print(msg.data)

def main():
    rclpy.init()
    node = Subscriber()
    rclpy.spin(node)

main()
