# kadai2

![test](https://github.com/yama-121/kadai2/actions/workflows/test.yml/badge.svg)

# モールス信号
ROS 2 環境で動作する、英単語からモールス信号に変更するシステムです。
 `translator` ノードと、変更結果を受け取って表示する `display` ノードの2つで構成されています。

# ノード・トピック
# translator ノード
入力された文字列をモールス信号に変換します。
- 入力トピック:`　/input_text` (std_msgs/String)
- 出力トピック:`/morse_code` (std_msgs/String)

# display ノード
変換結果を購読し、標準出力に表示します。
- 入力トピック:`/morse_code` (std_msgs/String)

# 使い方
パッケージのノードは標準的なROS 2トピックを使用しており、他のノードや標準コマンドと柔軟に連携可能です。

launchファイルを使用して、trnslatorとdisplayの両ノードを立ち上げます。
```
$ ros2 launch kadai2 morse.launch.py
$ ros2 topic pub /input_text std_msgs/String "data: 'HELLO'" -1
$ ros2 topic echo /morse_code
```
以下のように変換後の信号が表示されます  
例
[display-2]: [INFO] .... . .-.. .-.. ---

# 必要なソフトウェア
- Python 3.10 ~ 3.13
- Ubuntu 22.04.5
- git version 2.34.1
- ROS 2

# 権利関係
- このソフトウェアパッケージは、3条項BSDライセンスの下，再頒布および使用が許可されます。
- © 2025 ikki yamanaka

