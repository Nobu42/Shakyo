#!/bin/bash
# ファイル: process_data.sh サンプルファイル: data.csv
# 内容: awk/sedを使ってCSVを集計・整形して自動レポート化

set -euo pipefail
IFS=$'\n'

INPUT="data.csv"
REPORT="report.txt"
LOG="script.log"

echo "[INFO] 処理開始 $(date)" | tee -a "$LOG"

# 1. データが存在するかチェック
if [[ ! -f "$INPUT" ]]; then
    echo "[ERROR] ファイルが存在しません: $INPUT" | tee -a "$LOG"
    exit 1
fi

# 2. sedで小文字「error」があれば「ERROR」に変換して一時ファイルに保存
sed 's/error/ERROR/gI' "$INPUT" > "data_cleaned.csv"

# 3. awkで価格の統計を出す（合計・平均・最大・最小）
awk -F, '
BEGIN {
    sum = 0; max = 0; min = -1;
    print "==== 商品価格レポート ===="
}
NR > 1 {
    price = $3;
    sum += price;
    if (price > max) max = price;
    if (min == -1 || price < min) min = price;
    count++;
}
END {
    avg = (count > 0) ? sum / count : 0;
    printf "商品数: %d\n", count;
    printf "合計価格: %d\n", sum;
    printf "平均価格: %.2f\n", avg;
    printf "最高価格: %d\n", max;
    printf "最低価格: %d\n", min;
}
' data_cleaned.csv | tee "$REPORT"

# 4. 終了ログ
echo "[INFO] 処理完了 $(date)" | tee -a "$LOG"
