package main

import (
	"fmt"
)

func main() {
	// Fibonacci Series 0 0 1 1 2 3 5 8 13 21
	a := 0
	b := 1
	fmt.Print(a, " ")
	fmt.Print(b, " ")
	for i := 1; i <= 10; i++ {
		c := a + b
		a = b
		b = c
		fmt.Print(c, " ")
	}
	fmt.Println()
}
