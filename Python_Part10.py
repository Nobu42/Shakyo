"""
Part 10: UNIXシグナルを捕まえる実験

このプログラムは、Ctrl+C (SIGINT) や kill コマンド (SIGTERM) を受けたときに、
安全に終了処理を実行できるように signal モジュールでシグナルをハンドリングする。

学習ポイント:
- signal.signal() でシグナルをキャッチ
- シグナルを受けたときにクリーンアップ処理を行う
- SIGINT（Ctrl+C）と SIGTERM（kill）を扱う
"""

import signal
import time
import sys

running = True  # グローバルフラグ

def handle_sigint(signum, frame):
    print("\n[受信] SIGINT（Ctrl+C）を受け取りました。終了します。")
    global running
    running = False

def handle_sigterm(signum, frame):
    print("\n[受信] SIGTERM（kill）を受け取りました。安全に終了します。")
    global running
    running = False

def main():
    print("[開始] シグナル待機中（Ctrl+C または kill を送ってみてください）")

    # シグナルハンドラの登録
    signal.signal(signal.SIGINT, handle_sigint)
    signal.signal(signal.SIGTERM, handle_sigterm)

    count = 0
    while running:
        print(f"[実行中] {count} 秒経過...")
        time.sleep(1)
        count += 1

    print("[終了] 終了処理を完了しました。")

if __name__ == "__main__":
    main()
