package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func position_near_symbol(x int, y int, rows []string) bool {
	for dy := y - 1; dy <= y+1; dy++ {
		for dx := x - 1; dx <= x+1; dx++ {
			if !(0 <= dy && dy < len(rows) && 0 <= dx && dx < len(rows[0])) {
				continue
			}
			if !(rows[dy][dx] == '.' || unicode.IsDigit(rune(rows[dy][dx]))) {
				// fmt.Printf("here %c \n", rows[dy][dx])
				return true
			}
		}
	}
	return false
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	rows := strings.Split(string(fileContent), "\n")
	result := 0
	for y := 0; y < len(rows); y++ {
		number := 0
		near_symbol := false
		for x, char := range rows[y] {
			if unicode.IsDigit(char) {
				near_symbol = near_symbol || position_near_symbol(x, y, rows)
				digit, _ := strconv.Atoi(string(char))
				number = number*10 + digit
			} else {
				if near_symbol {
					result += number
				}
				number = 0
				near_symbol = false
			}
		}
		if near_symbol {
			result += number
		}
		number = 0
		near_symbol = false
	}

	fmt.Println("result:", result)
}
