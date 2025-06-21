# -*- coding: utf-8 -*-
"""
Part 4: Pythonでプロセスを操作する（fork + exec）

- 親プロセスと子プロセスを分岐
- 子プロセスで `ls -l` を実行
- 親プロセスは子の終了を待つ

※ UNIX/Linux 環境専用（Windows非対応）
"""

import os
import sys

def main():
    print(f"[親] プロセス開始（PID: {os.getpid()}）")

    try:
        pid = os.fork()
    except OSError as e:
        print(f"forkに失敗しました: {e}")
        sys.exit(1)

    if pid == 0:
        # 子プロセス（PIDは0）
        print(f"[子] 子プロセス生成成功！（PID: {os.getpid()}, 親: {os.getppid()}）")
        
        # 子プロセスで `/bin/ls -l` を実行
        try:
            print("[子] ls -l を実行します...")
            os.execvp("ls", ["ls", "-l"])
        except Exception as e:
            print(f"[子] execに失敗しました: {e}")
            sys.exit(1)

    else:
        # 親プロセス
        print(f"[親] 子プロセス（PID: {pid}）を待機中...")
        try:
            finished_pid, status = os.waitpid(pid, 0)
            exit_code = os.WEXITSTATUS(status)
            print(f"[親] 子プロセス（PID: {finished_pid}）終了（コード: {exit_code}）")
        except ChildProcessError as e:
            print(f"[親] 子プロセスの待機に失敗しました: {e}")

    print(f"[親] プログラム終了（PID: {os.getpid()}）")

if __name__ == "__main__":
    main()
