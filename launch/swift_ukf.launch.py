import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='robot_localization',
            node_executable='ukf_localization_node',
            node_name='ukf_se',
            parameters=[
                get_package_share_directory(
                    'robot_localization') + '/params/swift_ukf.yaml'
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
