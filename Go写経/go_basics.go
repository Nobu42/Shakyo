// go_basics.go
// Goの基本文法を広く網羅し、OS操作の基礎にもつながる要素を体験できる
// コンパイル
// go build -o gobase go_basics.go
// ./gobase
// コンパイルなしで実行
// go run go_basics.go


package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	fmt.Println("=== Go 基本文法 + OS基礎機能体験 ===")

	// 定数・変数
	const version = "v1.0"
	var username string = "のぶ"
	count := 3 // 型推論

	fmt.Println("ようこそ,", username)
	fmt.Printf("このプログラムのバージョンは %s です\n", version)

	// 入力受付
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("好きなコマンド名を入力してください（例: ls）: ")
	cmd, _ := reader.ReadString('\n')
	cmd = strings.TrimSpace(cmd)

	// 条件分岐
	if cmd == "ls" {
		fmt.Println("ファイル一覧を表示したいですね！")
	} else {
		fmt.Println("他のコマンドも面白いですね。")
	}

	// スライスとループ（引数処理風）
	args := []string{"-h", "--help", "-v"}
	for i, a := range args {
		fmt.Printf("引数[%d] = %s\n", i, a)
	}

	// マップ（環境変数的な扱い）
	config := map[string]string{
		"USER": os.Getenv("USER"),
		"SHELL": os.Getenv("SHELL"),
	}
	for key, val := range config {
		fmt.Printf("環境変数 %s = %s\n", key, val)
	}

	// 関数：ファイル存在チェック
	filename := "test.txt"
	if exists, _ := fileExists(filename); exists {
		fmt.Println("ファイル", filename, "は存在します")
	} else {
		fmt.Println("ファイル", filename, "は存在しません。作成します...")
		createTestFile(filename)
	}

	// 時刻表示
	now := time.Now()
	fmt.Printf("現在時刻: %s\n", now.Format("2006-01-02 15:04:05"))

	// 複数戻り値を持つ関数（数値変換）
	numStr := "42"
	num, err := strconv.Atoi(numStr)
	if err != nil {
		fmt.Println("数値変換に失敗:", err)
	} else {
		fmt.Println("文字列", numStr, "は数値", num, "に変換されました")
	}

	// ファイル読み取り
	fmt.Println("--- test.txt の内容を読み込みます ---")
	readFileLineByLine(filename)

	fmt.Println("=== 処理完了 ===")
}

// ファイルが存在するか確認する関数
func fileExists(name string) (bool, error) {
	_, err := os.Stat(name)
	if os.IsNotExist(err) {
		return false, nil
	}
	return err == nil, err
}

// ファイル作成関数（OS I/O）
func createTestFile(filename string) {
	content := "このファイルはGoで作成されました\nこれは2行目です\n"
	err := os.WriteFile(filename, []byte(content), 0644)
	if err != nil {
		fmt.Println("ファイル作成エラー:", err)
	}
}

// ファイルを1行ずつ読む（OS I/O + bufio）
func readFileLineByLine(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("ファイル読み込みエラー:", err)
		return
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	lineNo := 1
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			if err != io.EOF {
				fmt.Println("読み取り中にエラー:", err)
			}
			break
		}
		fmt.Printf("[%d] %s", lineNo, line)
		lineNo++
	}
}
