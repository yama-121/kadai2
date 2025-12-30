#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws

colcon build --packages-select ros2_kadai2
source install/setup.bash

rm -f /tmp/morse.log

timeout 15 ros2 launch ros2_kadai2 morse.launch.py > /tmp/morse.log &
sleep 2
ros2 topic pub /input_text std_msgs/String "data: 'HELLO'" --once -w 1
sleep 2

if grep -q '\.\.\.\. \. \.\-\.\. \.\-\.\. \-\-\-' /tmp/morse.log; then
    echo "0"
    exit 0
else
    cat /tmp/morse.log
    echo "1"
    exit 1
fi
