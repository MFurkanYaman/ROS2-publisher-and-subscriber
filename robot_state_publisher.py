#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotStatePublisherNode(Node):
    def __init__(self):
        super().__init__ ("robot_state_publisher")

        self.robot_name="Rover-006"
        self.publisher_=self.create_publisher(String,"state_publisher",10) #1:mesaj tipi,2:topic ismi,3:buffer size
        self.timer=self.create_timer(0.5,self.publish_state)
        self.get_logger().info("Robot State Publisher has been started.")

    def publish_state(self):
        msg=String() #mesaj tipi
        msg.data=f"Hello! This is {self.robot_name} from mars"
        self.publisher_.publish(msg)
    

   


def main(args=None):
    rclpy.init(args=args) #ros2'nin haberleşmesini başlatır.

    node=RobotStatePublisherNode()
    

    rclpy.spin(node) #nodeun sürekli çalışmasını sağlar.

    rclpy.shutdown() #haberleşmeyi sonlandırır ve yazdığın kodu bellekten siler 


if __name__== "__main__":
    main()

