#!/bin/bash
# ファイル名: basics.sh
# 内容: Bashスクリプトの基本構文を幅広く実演

set -e  # エラーが起きたら即終了
trap 'echo "エラーが発生しました（行: $LINENO）"; exit 1' ERR

echo "=== Bash 基本文法デモ ==="

# 引数処理
echo "引数一覧: $@"
echo "第1引数: $1"

# 変数と文字列
name="のぶ"
greeting="こんにちは、${name}さん！"
echo "$greeting"

# 日付と文字列長
today=$(date "+%Y-%m-%d")
echo "今日は $today です（長さ: ${#today}）"

# if文とファイルチェック
file="basics.sh"
if [[ -f "$file" ]]; then
    echo "$file は存在します"
else
    echo "$file は存在しません"
fi

# 数値条件と比較演算
num=5
if (( num > 3 )); then
    echo "$num は 3 より大きい"
fi

# case文
case "$1" in
    start) echo "開始処理します";;
    stop) echo "停止処理します";;
    *) echo "使い方: $0 {start|stop}";;
esac

# forループとコマンド置換
echo "現在のログインユーザ:"
for u in $(who | awk '{print $1}'); do
    echo " - $u"
done

# whileループ
count=1
while [[ $count -le 3 ]]; do
    echo "カウント: $count"
    ((count++))
done

# untilループ
until [[ $count -ge 6 ]]; do
    echo "until: $count"
    ((count++))
done

# 配列とループ
fruits=("apple" "banana" "orange")
for fruit in "${fruits[@]}"; do
    echo "果物: $fruit"
done

# 関数定義
greet() {
    local user=$1
    echo "こんにちは、$user さん！"
}
greet "デューク"

# 戻り値のある関数
square() {
    echo $(( $1 * $1 ))
}
result=$(square 4)
echo "4の2乗 = $result"

# 連想配列（bash 4以降）
declare -A capitals
capitals["Japan"]="Tokyo"
capitals["France"]="Paris"
echo "日本の首都は ${capitals["Japan"]}"

# 入力とリダイレクト
read -p "名前を入力してください: " uname
echo "こんにちは、$unameさん" | tee output.txt

# ファイル処理と標準エラー出力
logfile="log.txt"
echo "これは標準出力" > $logfile
ls /no/such/file 2>> $logfile

# パイプと文字列処理
echo "1:foo 2:bar 3:baz" | tr ':' '\n' | while read item; do
    echo "要素: $item"
done

echo "=== 終了しました ==="
