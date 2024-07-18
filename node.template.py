#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class TemplateNode(Node): #değiştir.
    def __init__(self):
       super().__init__ ("template_node") #değiştir.


def main(args=None):
    rclpy.init(args=args) 

    node=TemplateNode() #değiştir.

    rclpy.spin(node) 
    rclpy.shutdown() 

if __name__== "__main__":
    main()

