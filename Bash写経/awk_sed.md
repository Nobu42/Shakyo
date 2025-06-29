# 1. awk の基本：列を使った処理

```
# 1列目だけ表示
awk '{print $1}' sample.txt

# 1列目と3列目を「:」区切りで表示
awk '{print $1 ":" $3}' sample.txt

# 3列目（価格）が150以上の行だけ表示
awk '$3 >= 150 {print $0}' sample.txt

# 合計を出す
awk '{sum += $3} END {print "合計:", sum}' sample.txt

# 条件分岐（色がgreenの果物をマーク）
awk '$2 == "green" {print $1, "(これは緑色)"}' sample.txt
```

# 2. sed の基本：行の置換・削除・抽出など

```
# 色名「orange」を「オレンジ」に置換
sed 's/orange/オレンジ/' sample.txt

# すべての色名を置換（global）
sed 's/orange/オレンジ/g' sample.txt

# 2行目だけを表示
sed -n '2p' sample.txt

# 3行目を削除
sed '3d' sample.txt

# 1〜3行目だけ表示
sed -n '1,3p' sample.txt
```

# 応用編：組み合わせや実務的な処理

## 条件付きでデータ抽出（awk）

```
# 色がorangeかpurpleの果物だけ表示
awk '$2 == "orange" || $2 == "purple"' sample.txt
```

## 最大・最小・平均（awk）

```
# 価格の最大・最小・平均を求める
awk '{
  if (NR==1 || $3 > max) max=$3;
  if (NR==1 || $3 < min) min=$3;
  sum += $3
}
END {
  print "最大:", max
  print "最小:", min
  print "平均:", sum/NR
}' sample.txt
```

## 文字列の置換（sed）

```
# 「grape」を「ブドウ」に一括置換
sed 's/grape/ブドウ/g' sample.txt
```

## ファイルを直接変更（注意！）

```
# オリジナルを上書き（注意）
sed -i.bak 's/apple/りんご/g' sample.txt
```

## よく使うオプション集

| ツール   | オプション | 意味                  |
| ----- | ----- | ------------------- |
| `awk` | `-F:` | 区切り文字を指定（例：CSV）     |
| `sed` | `-n`  | 出力抑制（`p`で明示的に表示）    |
| `sed` | `-i`  | ファイルを直接編集（バックアップ推奨） |


## ちょい実用ワンライナー例

### CSVの1列目と2列目を表示（区切りはカンマ）

```
awk -F, '{print $1, $2}' data.csv
```

### 行末にコメントを追記（sed）

```
sed 's/$/ # コメント追加/' sample.txt
```

### 改行を削除（全行を1行に）

```
tr -d '\n' < sample.txt
```



