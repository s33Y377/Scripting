package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	display(5)
	fmt.Println()
	httprequest()
	fmt.Println()
	foriteration(30)
	fmt.Println()
}

func display(number int) {
	fmt.Print(number, "\n")
}

func foriteration(n int) {
	for i := 1; i <= n; i++ {
		fmt.Printf("%d  ", 2*i)
	}
}

func httprequest() {
	resp, err := http.Get("https://api.github.com/user")
	if err != nil {
		fmt.Println(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(body)
}
