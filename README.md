# kadai2

![test](https://github.com/yama-121/kadai2/actions/workflows/test.yml/badge.svg)

# モールス信号
入力された英語をモールス信号に変換する

# インストール
```
$ git clone https://github.com/yama-121/robosys2025.git
$ cd robosys2025
$ chmod +x count
```

# 使い方
このプログラムは、標準入力から日付を受け取り、標準出力に経過日数を返します。

入力形式: YYYY-MM-DD形式の日付文字列 (例: 2000-01-01)

出力形式: 経過した日数

未来の日付を指定することはできません。
日付の月や日が1桁の場合でも、07のように2桁で入力する必要があります。
例
```
$ echo "2000-01-01" | ./count
9475
```

# 必要なソフトウェア
- Python 3.9 ~ 3.13
- Ubuntu 22.04.5
- git version 2.34.1

# 権利関係
- このソフトウェアパッケージは、3条項BSDライセンスの下，再頒布および使用が許可されます。
- © 2025 ikki yamanaka

