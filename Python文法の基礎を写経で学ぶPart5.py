import os
import sys

def main():
    print(f"[親] 開始: PID={os.getpid()}")

    # 環境変数に設定する値
    env_vars = os.environ.copy()  # 現在の環境をコピー
    env_vars["NOBU_MESSAGE"] = "デュークからのメッセージです"

    # 起動するPythonスクリプトのパス
    script_path = os.path.abspath("child_script.py")

    # フォークで子プロセス作成
    try:
        pid = os.fork()
    except OSError as e:
        print("forkに失敗:", e)
        sys.exit(1)

    if pid == 0:
        # 子プロセス: 別スクリプトを実行
        print(f"[子] 実行準備中... PID={os.getpid()}")
        try:
            os.execle(sys.executable, sys.executable, script_path, env_vars)
        except Exception as e:
            print(f"[子] execleに失敗: {e}")
            sys.exit(1)
    else:
        # 親プロセス: 子の終了を待つ
        print(f"[親] 子プロセス（PID={pid}）の終了を待機")
        _, status = os.waitpid(pid, 0)
        exit_code = os.WEXITSTATUS(status)
        print(f"[親] 子プロセス終了（コード: {exit_code}）")

if __name__ == "__main__":
    main()
