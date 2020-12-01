# ros-bagfile-extraction

## Dependencies
```
sudo apt-get install ros-<ROS_VERSION>-image-transport
sudo apt-get install ros-<ROS_VERSION>-image-view

```

## Quick demo
```
cd catkin_ws
catkin_make
source devel/setup.bash
export ROS_HOME=`pwd`/datasets
roslaunch export.launch
```
Result will be in `datasets/` folder

## Custom types extraction
Look into `export.launch` and `wheels_cmd_extractor` for more info
