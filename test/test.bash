#!/bin/bash

source /opt/ros/humble/setup.bash
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=1

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build --packages-select ros2_kadai2
source install/setup.bash

rm -f /tmp/morse.log

timeout 60 ros2 launch ros2_kadai2 morse.launch.py > /tmp/morse.log &

sleep 15

ros2 topic pub -r 10 /input_text std_msgs/String "data: 'HELLO'" --once-for 3

sleep 5

if grep -p "Published: \.\.\.\. \. \.\-\.\. \.\-\.\. \-\-\-" /tmp/morse.log; then
    echo "0"
    exit 0
else
    cat /tmp/morse.log
    echo "1"
    exit 1
fi
