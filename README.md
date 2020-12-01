# ros-bagfile-extraction

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
