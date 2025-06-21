import os

def main():
    print("[子スクリプト] 実行中")
    message = os.environ.get("NOBU_MESSAGE", "メッセージがありません")
    print(f"[子スクリプト] 環境変数 NOBU_MESSAGE の値: {message}")

if __name__ == "__main__":
    main()
