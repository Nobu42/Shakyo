package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"os/signal"
	"runtime"
	"strings"
	"syscall"
	"time"
)

func main() {
	fmt.Println("🔧 Goで学ぶOS/システム機能の基本 🔧")
	fmt.Println(strings.Repeat("=", 40))

	// 1. OS情報を取得
	printSystemInfo()

	// 2. 環境変数を操作
	handleEnv()

	// 3. ファイルの読み書き
	handleFile()

	// 4. 外部コマンドを実行
	runExternalCommand()

	// 5. シグナル処理（Ctrl+C で終了）
	handleSignal()

	// 6. タイマー処理
	runTicker()

	fmt.Println("🌟 プログラム終了！")
}

// 1. OSやCPUなどの基本情報を表示
func printSystemInfo() {
	fmt.Println("🖥️ OS/CPU 情報")
	fmt.Printf("OS: %s\n", runtime.GOOS)
	fmt.Printf("アーキテクチャ: %s\n", runtime.GOARCH)
	fmt.Printf("CPU数: %d\n", runtime.NumCPU())
	fmt.Printf("Goバージョン: %s\n", runtime.Version())
	fmt.Println(strings.Repeat("-", 40))
}

// 2. 環境変数の取得・設定
func handleEnv() {
	fmt.Println("🌱 環境変数の例")

	// 既存の環境変数取得
	path := os.Getenv("PATH")
	fmt.Println("PATH:", path)

	// 新しい環境変数を設定
	os.Setenv("MY_ENV_VAR", "NOBU_TEST")
	fmt.Println("MY_ENV_VAR:", os.Getenv("MY_ENV_VAR"))

	fmt.Println(strings.Repeat("-", 40))
}

// 3. ファイルの作成、書き込み、読み取り、削除
func handleFile() {
	fmt.Println("📄 ファイル操作の例")

	filename := "sample.txt"

	// 書き込み
	file, err := os.Create(filename)
	if err != nil {
		fmt.Println("ファイル作成エラー:", err)
		return
	}
	defer file.Close()

	content := "これはGoで書かれたサンプルファイルです。\nシステム機能の練習に使います。\n"
	_, err = file.WriteString(content)
	if err != nil {
		fmt.Println("書き込みエラー:", err)
		return
	}

	// 読み込み
	fmt.Println("ファイルから読み込み中:")
	readFile(filename)

	// 削除
	err = os.Remove(filename)
	if err != nil {
		fmt.Println("ファイル削除エラー:", err)
	} else {
		fmt.Println("ファイルを削除しました:", filename)
	}

	fmt.Println(strings.Repeat("-", 40))
}

// ファイル読み取り関数
func readFile(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("ファイル読み込みエラー:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

// 4. 外部コマンドを実行（例：ls や date）
func runExternalCommand() {
	fmt.Println("💻 外部コマンド実行の例")

	// OSによってコマンドを変える（Windowsの場合は dir）
	cmd := exec.Command("ls", "-l")
	if runtime.GOOS == "windows" {
		cmd = exec.Command("cmd", "/C", "dir")
	}

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println("コマンド実行エラー:", err)
	} else {
		fmt.Println("出力:")
		fmt.Println(string(output))
	}

	fmt.Println(strings.Repeat("-", 40))
}

// 5. シグナル（Ctrl+Cなど）を処理して安全に終了
func handleSignal() {
	fmt.Println("📢 Ctrl+Cで停止できます。10秒以内に試してください。")

	// シグナルチャンネルを作成
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)

	// 別のgoroutineで待機
	go func() {
		s := <-sigChan
		fmt.Println("\n📍 シグナル受信:", s)
		fmt.Println("クリーンアップして終了します。")
		os.Exit(0)
	}()

	// 10秒待機（シグナルが来なければそのまま次へ）
	time.Sleep(10 * time.Second)
	fmt.Println("（シグナルは来ませんでした）")
	fmt.Println(strings.Repeat("-", 40))
}

// 6. Ticker（一定間隔で実行）
func runTicker() {
	fmt.Println("⏱️ Tickerで時間を1秒おきに表示（5回まで）")

	ticker := time.NewTicker(1 * time.Second)
	defer ticker.Stop()

	count := 0
	for t := range ticker.C {
		fmt.Println("現在時刻:", t.Format("15:04:05"))
		count++
		if count >= 5 {
			break
		}
	}
	fmt.Println(strings.Repeat("-", 40))
}
