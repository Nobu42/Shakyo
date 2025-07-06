package main

import (
	"errors"
	"fmt"
	"math"
	"strings"
	"time"
)

// 定数宣言（グローバル）
const Pi = 3.14159

// グローバル変数
var version = "v1.0.0"

// 構造体の定義
type Person struct {
	Name string
	Age  int
}

// 構造体のメソッド（値レシーバ）
func (p Person) Greet() string {
	return fmt.Sprintf("こんにちは、私は%s、%d歳です！", p.Name, p.Age)
}

// 構造体のメソッド（ポインタレシーバ）
func (p *Person) Birthday() {
	p.Age++
}

// インタフェースの定義
type Shape interface {
	Area() float64
	Perimeter() float64
}

// 構造体Circle
type Circle struct {
	Radius float64
}

// CircleがShapeインタフェースを実装
func (c Circle) Area() float64 {
	return Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
	return 2 * Pi * c.Radius
}

// エラーを返す関数
func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("0で割ることはできません")
	}
	return a / b, nil
}

// スライスとmapの操作例
func sliceAndMapDemo() {
	fmt.Println("=== スライスとmapの例 ===")
	numbers := []int{1, 2, 3, 4, 5}

	// スライスの追加とループ
	numbers = append(numbers, 6)
	for i, n := range numbers {
		fmt.Printf("Index: %d, Value: %d\n", i, n)
	}

	// mapの定義とアクセス
	colors := map[string]string{
		"red":   "赤",
		"blue":  "青",
		"green": "緑",
	}

	// 要素追加
	colors["white"] = "白"

	// mapのループ
	for key, value := range colors {
		fmt.Printf("%s => %s\n", key, value)
	}
}

// 値渡しとポインタ渡しの違い
func squareByValue(n int) {
	n = n * n
}

func squareByPointer(n *int) {
	*n = (*n) * (*n)
}

// GoroutineとChannelの例
func count(name string, ch chan string) {
	for i := 1; i <= 3; i++ {
		msg := fmt.Sprintf("[%s] count %d", name, i)
		ch <- msg
		time.Sleep(500 * time.Millisecond)
	}
	close(ch)
}

func goroutineDemo() {
	fmt.Println("=== GoroutineとChannelの例 ===")
	ch := make(chan string)

	go count("GoroutineA", ch)

	for msg := range ch {
		fmt.Println(msg)
	}
}

// ユーティリティ関数
func wordCount(s string) map[string]int {
	result := make(map[string]int)
	words := strings.Fields(s)
	for _, word := range words {
		result[word]++
	}
	return result
}

func main() {
	fmt.Println("🔷 Go鉄板サンプルコード集 🔷")
	fmt.Printf("バージョン: %s\n", version)

	// 構造体の使用例
	taro := Person{Name: "太郎", Age: 30}
	fmt.Println(taro.Greet())
	taro.Birthday()
	fmt.Println("誕生日の後:", taro.Greet())

	// エラーハンドリング
	result, err := divide(10, 0)
	if err != nil {
		fmt.Println("エラー:", err)
	} else {
		fmt.Println("割り算結果:", result)
	}

	// スライスとmapの操作
	sliceAndMapDemo()

	// 値渡し vs ポインタ渡し
	x := 5
	squareByValue(x)
	fmt.Println("値渡しの後:", x) // 変わらない

	squareByPointer(&x)
	fmt.Println("ポインタ渡しの後:", x) // 変わる

	// インタフェースの使用
	c := Circle{Radius: 5}
	var s Shape = c
	fmt.Printf("円の面積: %.2f\n", s.Area())
	fmt.Printf("円の周囲長: %.2f\n", s.Perimeter())

	// Goroutineの実行
	goroutineDemo()

	// mapを返す関数の実行
	text := "hello world hello go"
	wordMap := wordCount(text)
	fmt.Println("単語出現数:", wordMap)

	// 配列の例（固定長）
	fmt.Println("=== 配列の例 ===")
	var arr [3]int = [3]int{10, 20, 30}
	for i := 0; i < len(arr); i++ {
		fmt.Printf("arr[%d] = %d\n", i, arr[i])
	}

	// for + rangeでスライスを扱う
	fmt.Println("=== rangeによるスライスループ ===")
	fruits := []string{"apple", "banana", "orange"}
	for _, fruit := range fruits {
		fmt.Println("果物:", fruit)
	}

	// deferの例
	fmt.Println("=== deferの例 ===")
	defer fmt.Println("これは最後に実行されます")
	fmt.Println("処理中...")

	// timeの使用
	fmt.Println("=== 現在時刻 ===")
	now := time.Now()
	fmt.Println("現在:", now.Format("2006-01-02 15:04:05"))
}
