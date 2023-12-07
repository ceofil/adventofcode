package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	lines := strings.Split(string(fileContent), "\n")
	fmt.Println(len(lines))
}
