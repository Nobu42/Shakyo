import time
import psutil
import matplotlib.pyplot as plt
from collections import deque

def monitor_memory(interval_sec=1.0, duration_sec=20):
    """
    メモリ使用率をリアルタイムで取得し、deque に記録
    """
    max_points = int(duration_sec / interval_sec)
    timestamps = deque(maxlen=max_points)
    mem_usages = deque(maxlen=max_points)

    print("[監視開始] メモリ使用率の記録...")
    start = time.time()
    while time.time() - start < duration_sec:
        ts = time.time() - start
        mem = psutil.virtual_memory().percent
        timestamps.append(ts)
        mem_usages.append(mem)
        print(f"経過 {ts:.1f}s — メモリ使用率: {mem:.1f}%")
        time.sleep(interval_sec)

    return list(timestamps), list(mem_usages)

def plot_memory(timestamps, mem_usages):
    """
    メモリ使用率の変化をリアルタイム描画
    """
    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, mem_usages, marker='.', color='green')
    plt.title("メモリ使用率の変化（リアルタイム記録）")
    plt.xlabel("経過時間（秒）")
    plt.ylabel("メモリ使用率（%）")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def allocate_memory(size_mb):
    """
    意図的にメモリを消費する関数
    """
    print(f"[負荷] {size_mb}MB のリストを確保します...")
    return [0] * (size_mb * 250_000)  # 約 size_mb MB

def main():
    duration = 20
    interval = 1

    # メモリ負荷なしでベースライン
    times1, mem1 = monitor_memory(interval, duration / 2)
    
    # メモリ負荷を掛ける
    leak = allocate_memory(200)
    
    # 負荷中をモニタリング
    times2, mem2 = monitor_memory(interval, duration / 2)
    
    # 結果結合
    timestamps = times1 + [t + times1[-1] for t in times2]
    mem_usages = mem1 + mem2

    # グラフ出力
    plot_memory(timestamps, mem_usages)
    print("[完了] メモリ負荷実験終了")

if __name__ == "__main__":
    main()
