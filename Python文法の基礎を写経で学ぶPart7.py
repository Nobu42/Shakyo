import time
import psutil
import matplotlib.pyplot as plt
import multiprocessing

def stress_cpu(duration_sec):
    """CPUに負荷をかける処理（ダミー）"""
    end_time = time.time() + duration_sec
    while time.time() < end_time:
        _ = sum(i * i for i in range(10000))  # 計算負荷

def monitor_cpu(interval_sec=0.5, total_duration=10):
    """CPU使用率を一定間隔で取得して記録"""
    usage_history = []
    timestamps = []

    print("[監視] CPU使用率を記録開始...")
    start_time = time.time()
    while (time.time() - start_time) < total_duration:
        usage = psutil.cpu_percent(interval=None)
        timestamp = time.time() - start_time
        usage_history.append(usage)
        timestamps.append(timestamp)
        time.sleep(interval_sec)
        print(f"経過: {timestamp:.1f}秒 | CPU使用率: {usage:.1f}%")

    return timestamps, usage_history

def plot_cpu_usage(timestamps, usages):
    """CPU使用率の変化をグラフ化"""
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, usages, marker="o", linestyle="-", color="blue")
    plt.title("CPU使用率の変化")
    plt.xlabel("経過時間（秒）")
    plt.ylabel("CPU使用率（%）")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    duration = 10  # 秒数

    # 背景で負荷をかけるプロセスを起動
    stress_process = multiprocessing.Process(target=stress_cpu, args=(duration,))
    stress_process.start()

    # CPU監視を開始
    times, usages = monitor_cpu(interval_sec=0.5, total_duration=duration)

    # 負荷プロセス終了を待機
    stress_process.join()

    # グラフ表示
    plot_cpu_usage(times, usages)
