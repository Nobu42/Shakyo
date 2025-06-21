"""
Part 9: 実行中のプロセス一覧からメモリ使用量を取得し、
        上位のプロセスを棒グラフで可視化する。

- psutil を使ってプロセス情報を収集
- 各プロセスのRSS（実メモリ）を取得
- 上位N件を棒グラフで表示（matplotlib使用）

学習ポイント:
- psutil.Process の使い方
- プロセスの属性取得と例外処理
- リストのソートと可視化処理
"""
import psutil
import matplotlib.pyplot as plt

def get_top_memory_processes(top_n=10):
    """
    実行中のプロセスのうち、メモリ使用量（RSS）が多いものを上位N件取得
    """
    process_info = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            rss = proc.info['memory_info'].rss  # 実メモリ使用量（バイト）
            process_info.append((proc.info['name'], proc.info['pid'], rss))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue  # 権限不足や消滅したプロセスをスキップ

    # メモリ使用量でソート（降順）
    process_info.sort(key=lambda x: x[2], reverse=True)
    return process_info[:top_n]

def plot_process_memory(process_list):
    """
    プロセスのメモリ使用量を棒グラフで可視化
    """
    names = [f"{name}({pid})" for name, pid, _ in process_list]
    rss_mb = [rss / (1024 * 1024) for _, _, rss in process_list]

    plt.figure(figsize=(12, 6))
    plt.barh(names, rss_mb, color="skyblue")
    plt.xlabel("メモリ使用量（MB）")
    plt.title("上位プロセスのメモリ使用量")
    plt.gca().invert_yaxis()  # 上位が上に来るように
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

def main():
    print("[処理] プロセス情報を取得中...")
    top_processes = get_top_memory_processes(top_n=10)

    print("上位メモリ使用プロセス:")
    for name, pid, rss in top_processes:
        print(f"{name} (PID {pid}) - {rss / (1024 * 1024):.1f} MB")

    plot_process_memory(top_processes)

if __name__ == "__main__":
    main()
