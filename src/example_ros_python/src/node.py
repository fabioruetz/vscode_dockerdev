#!/usr/bin/env python
import numpy as np
import rospy


class ExampleRosNode:
    """ExampleRosNode"""

    def __init__(self):
        self.load_ros_params()

    def load_ros_params(self) -> None:
        self.model_dir = rospy.get_param("~model_dir", "")

    def main_cb(self, event=None) -> None:
        """Main callback to call all the process to enable the predictions data"""
        a = 1


def main(args=None):
    rospy.init_node("scnn_ftm_ros")

    node = ExampleRosNode()

    rospy.Timer(rospy.Duration(0.1), node.main_cb)

    rospy.spin()


if __name__ == "__main__":
    main()
