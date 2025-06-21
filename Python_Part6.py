import os
import sys

def main():
    print(f"[親] プログラム開始（PID: {os.getpid()}）")

    # パイプを作成（読み取り用FD, 書き込み用FD）
    read_fd, write_fd = os.pipe()

    try:
        pid = os.fork()
    except OSError as e:
        print(f"fork失敗: {e}")
        sys.exit(1)

    if pid == 0:
        # ===== 子プロセス =====
        os.close(write_fd)  # 書き込み用は使わない
        print(f"[子] 開始（PID: {os.getpid()}）")

        # 子プロセスはパイプからメッセージを受け取る
        r = os.fdopen(read_fd)
        message = r.read()
        print(f"[子] 親から受け取ったメッセージ: {message}")
        r.close()
        print(f"[子] 終了")
        sys.exit(0)

    else:
        # ===== 親プロセス =====
        os.close(read_fd)  # 読み取り用は使わない
        print(f"[親] 子プロセス生成（PID: {pid}）")

        # 親から子へのメッセージ
        w = os.fdopen(write_fd, "w")
        message = "こんにちは、のぶさん！こちらは親プロセスです。"
        print(f"[親] 子に送信中: {message}")
        w.write(message)
        w.close()

        # 子プロセス終了待ち
        _, status = os.waitpid(pid, 0)
        print(f"[親] 子プロセス終了（コード: {os.WEXITSTATUS(status)}）")
        print(f"[親] プログラム終了")

if __name__ == "__main__":
    main()
