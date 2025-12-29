#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch ros2_kadai2 morse.launch.py > /tmp/morse.log

sleep 3

ros2 topic pub /input_text std_msgs/String "data: 'HELLO'" --once

cat /tmp/morse.log | grep '.... . .-.. .-.. ---'\
grep'Listen:10'
