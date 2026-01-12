#!/bin/bash
# SPDX-FileCopyrightText: 2025 ikki yamanaka
# SPDX-License-Identifier: BSD-3-Clause

source /opt/ros/humble/setup.bash
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=1

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build --packages-select kadai2
source install/setup.bash

rm -f /tmp/morse.log

timeout 60 ros2 launch kadai2 morse.launch.py > /tmp/morse.log 2>&1 &

sleep 20

ros2 topic pub /input_text std_msgs/String "data: 'HELLO'" -t 10

sleep 5

if grep -q "Published" /tmp/morse.log; then
    echo "0"
    exit 0
else
    cat /tmp/morse.log
    echo "1"
    exit 1
fi
