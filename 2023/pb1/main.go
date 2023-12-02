package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	digit_strings := []string{
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
	}
	scanner := bufio.NewScanner(file)
	var sum int = 0
	for scanner.Scan() {
		var first int = -1
		var last int = -1
		var first_index = -1
		var last_index = -1

		var line = scanner.Text()

		for char_idx, char := range line {
			if !unicode.IsDigit(char) {
				continue
			}
			digit := int(char - '0')
			if first == -1 {
				first = digit
				first_index = char_idx
			}
			last = digit
			last_index = char_idx
		}
		for digit_index, digit_str := range digit_strings {
			first_occurance := strings.Index(line, digit_str)
			last_occurance := strings.LastIndex(line, digit_str)
			if first_index == -1 || (first_occurance != -1 && first_occurance < first_index) {
				first_index = first_occurance
				first = digit_index + 1
			}
			if last_index == -1 || (last_occurance != -1 && last_occurance > last_index) {
				last_index = last_occurance
				last = digit_index + 1
			}
		}
		sum += first*10 + last
	}

	fmt.Println(sum)

}
