package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

type Pos struct {
	x, y int
}

type Number struct {
	pos           Pos
	length, value int
}

func is_adjacent(num Number, symbol_pos Pos) bool {
	return symbol_pos.y >= num.pos.y-1 &&
		symbol_pos.y <= num.pos.y+1 &&
		symbol_pos.x >= num.pos.x-1 &&
		symbol_pos.x <= num.pos.x+num.length
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	rows := strings.Split(string(fileContent), "\n")

	numbers := []Number{}
	symbols := []Pos{}
	for y := 0; y < len(rows); y++ {
		nx, ny, length, value := 0, 0, 0, 0
		for x, char := range rows[y] {
			if unicode.IsDigit(char) {
				if length == 0 {
					nx, ny = x, y
				}
				digit, _ := strconv.Atoi(string(char))
				value = value*10 + digit
				length += 1
				continue
			}
			if length > 0 {
				numbers = append(
					numbers,
					Number{
						pos:    Pos{x: nx, y: ny},
						length: length,
						value:  value,
					},
				)
				nx, ny, length, value = 0, 0, 0, 0
			}
			if !(rows[y][x] == '.' || unicode.IsDigit(rune(rows[y][x]))) {
				symbols = append(symbols, Pos{x: x, y: y})
			}
		}
		if length > 0 {
			numbers = append(
				numbers,
				Number{
					pos:    Pos{x: nx, y: ny},
					length: length,
					value:  value,
				},
			)
			nx, ny, length, value = 0, 0, 0, 0
		}
	}
	result := 0
	for _, symbol := range symbols {
		adjacency := 0
		gear_ratio := 1
		is_star := rows[symbol.y][symbol.x] == '*'
		for _, number := range numbers {
			if is_adjacent(number, symbol) {
				if is_star {
					adjacency += 1
					gear_ratio *= number.value
				}
			}
		}
		if adjacency == 2 {
			result += gear_ratio
		}
	}
	fmt.Println("result:", result)
}
