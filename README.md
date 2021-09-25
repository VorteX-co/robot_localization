robot_localization
==================

robot_localization is a package of nonlinear state estimation nodes. The package was developed by Charles River Analytics, Inc.

Please see documentation here: http://wiki.ros.org/robot_localization

--------
Parameters Specification
------

| Parameter           |  Description  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| map_frame        | world-fixed frame, the robot's pose will be with respect to it. This frame is not continuous, meaning that the pose of a robot in this frame can change in discrete jumps at any time (used when fusing GPS data). |
| odom_frame         | world-fixed frame, the robot's pose will be with respect to it. This frame is continuous, meaning that the pose of a robot in this frame can evolve in a smooth way, without discrete jumps. |
| base_link_frame     | body-fixed frame, the robot's velocity and acceleration will be with resepct to it. |
| world_frame  |  global frame can be either map_frame or odom_frame. If you are fusing global absolute position data that is subject to discrete jumps set this frame to map_frame, else set it to  odom_frame. |

--------
Data preparation
------

The robot_localization supports the following ROS message types:-
- **`nav_msgs/Odometry`** All pose data (position and orientation) is transformed from the message
header’s frame_id into the coordinate frame specified by the world_frame parameter. All twist data (linear and angular velocity) is transformed from the child_frame_id of the message into the coordinate frame specified by the base_link_frame parameter.
- **`geometry_msgs/PoseWithCovarianceStamped`** Handled in the same fashion as the pose data in
the Odometry message.
- **`geometry_msgs/TwistWithCovarianceStamped`** Handled in the same fashion as the twist data in
the Odometry message.
- **`sensor_msgs/Imu`** robot_localization assumes an ENU frame (East, North, Up) for the IMU data. The IMU measurments are used as the control inputs for the preditiction step.

--------
Common errors
------
- Using NED IMU. Make sure that all the orientation angles increase and decrease in the correct directions.
- Incorrect frame_id values. Velocity data should be reported in the frame given by the base_link_frame parameter, or a transform should exist between the frame_id of the velocity data and the base_link_frame.
- Inflated covariances. The preferred method for ignoring variables in measurements is through the odom_config or imu_config parameters, by setting the respective variables to false.
- Missing covariances. make sure to set the covariances appropriately for each variable for all the measurments.

--------
Usage
------
Configure the paramteres file by specifying the topic names for both your odometry data as well as the IMU data.

For launching the UKF state estimation node:-
```sh
  $ ros2 launch  robot_localization swift_ukf.launch.py
```
Or launching the EKF state estimation node:-
```sh
  $ ros2 launch  robot_localization swift_ekf.launch.py
```





















