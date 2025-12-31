# ros2_kadai2

![test](https://github.com/yama-121/kadai2/actions/workflows/test.yml/badge.svg)

# モールス信号
ROS 2 Humble環境で動作する、英単語からモールス信号に変更するシステムです。
 `translator` ノードと、変更結果を受け取って表示する `display` ノードの2つで構成されています。

# インストール
```
$ cd ~/ros2_ws/src
$ git clone [https://github.com/yama-121/kadai2.git](https://github.com/yama-121/kadai2.git)
$ cd ~/ros2_ws
$ colcon build --packages-select ros2_kadai2
$ source install/setup.bash
```

# 使い方
2つのターミナルを用いて使用します。   　　
launchファイルを使用して、変更・表示の両ノードを立ち上げます。
```
$ ros2 launch ros2_kadai2 morse.launch.py
```

別のターミナルから、英単語を入力します。
```
$ ros2 topic pub /input_text std_msgs/String "data: 'HELLO'" --once
```

launshファイル側に、以下のように変換後の信号が表示されます  
例
[display-2]: [INFO] .... . .-.. .-.. ---

# 必要なソフトウェア
- Python 3.10 ~ 3.13
- Ubuntu 22.04.5
- git version 2.34.1

# 権利関係
- このソフトウェアパッケージは、3条項BSDライセンスの下，再頒布および使用が許可されます。
- © 2025 ikki yamanaka

