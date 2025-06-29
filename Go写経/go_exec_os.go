// go_exec_os.go
// GoでOSコマンドを実行するサンプル：ls, date, pingなど

package main

import (
	"bytes"
	"fmt"
	"os"
	"os/exec"
	"time"
)

func main() {
	fmt.Println("=== GoでOSコマンドを実行する ===")

	// 1. dateコマンドを実行して出力を取得
	dateOut, err := exec.Command("date").Output()
	if err != nil {
		fmt.Println("dateコマンド失敗:", err)
		return
	}
	fmt.Printf("現在の時刻: %s\n", dateOut)

	// 2. ls -l を実行（出力を表示）
	fmt.Println("--- カレントディレクトリの一覧（ls -l） ---")
	lsCmd := exec.Command("ls", "-l")
	lsOut, err := lsCmd.CombinedOutput() // stderrも取得
	if err != nil {
		fmt.Println("ls失敗:", err)
	} else {
		fmt.Println(string(lsOut))
	}

	// 3. 環境変数を渡してコマンドを実行（env コマンドで確認）
	fmt.Println("--- 環境変数TEST=helloを追加してenv表示 ---")
	envCmd := exec.Command("env")
	envCmd.Env = append(os.Environ(), "TEST=hello")
	envOut, _ := envCmd.Output()
	fmt.Println(string(envOut))

	// 4. pingコマンド（短時間だけ実行）
	fmt.Println("--- pingを3回だけ実行（Google） ---")
	pingCmd := exec.Command("ping", "-c", "3", "8.8.8.8")
	pingOut, err := pingCmd.CombinedOutput()
	if err != nil {
		fmt.Println("ping失敗:", err)
	} else {
		fmt.Println(string(pingOut))
	}

	// 5. コマンドに標準入力を送る（echoとcatの連携）
	fmt.Println("--- echoとcatの標準入力を試す ---")
	catCmd := exec.Command("cat")
	stdin, _ := catCmd.StdinPipe()
	var outBuf bytes.Buffer
	catCmd.Stdout = &outBuf

	catCmd.Start()
	stdin.Write([]byte("これは標準入力から送った文字列です\n"))
	stdin.Close()
	catCmd.Wait()
	fmt.Print(outBuf.String())

	fmt.Println("=== コマンド実行完了 ===")
}
