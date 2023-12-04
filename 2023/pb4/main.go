package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	result := 0
	for scanner.Scan() {

		line := scanner.Text()
		split_line := strings.Split(line, ":")
		card_info := split_line[1]
		split_info := strings.Split(card_info, "|")
		winning_numbers_str := strings.Split(split_info[0], " ")
		numbers_str := strings.Split(split_info[1], " ")
		winning_number_flags := make(map[string]bool)
		for _, number_str := range winning_numbers_str {
			if len(number_str) == 0 {
				continue
			}
			winning_number_flags[number_str] = false
		}
		// fmt.Println("len", len(winning_numbers_str))
		for _, number_str := range numbers_str {
			if len(number_str) == 0 {
				continue
			}
			_, exists := winning_number_flags[number_str]
			if exists {
				// fmt.Printf("drawn --%s--\n", number_str)
				winning_number_flags[number_str] = true
			}
		}

		matching := 0
		for _, flag := range winning_number_flags {
			// fmt.Println(flag)
			if flag {
				matching += 1
			}
		}
		if matching > 0 {
			score := int(math.Pow(2, float64(matching)-1))
			// fmt.Println(score, matching)
			result += score
		}
		// break
	}
	fmt.Println("result: ", result)
}
