package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	result := 0
	number_of_instances := make(map[int]int)
	for scanner.Scan() {

		line := scanner.Text()
		split_line := strings.Split(line, ":")
		card_title := strings.Split(split_line[0], " ")
		card_id_str := card_title[len(card_title)-1]
		card_id, _ := strconv.Atoi(card_id_str)
		card_info := split_line[1]
		number_of_instances[card_id] += 1
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
		for _, number_str := range numbers_str {
			if len(number_str) == 0 {
				continue
			}
			_, exists := winning_number_flags[number_str]
			if exists {
				winning_number_flags[number_str] = true
			}
		}

		matching := 0
		for _, flag := range winning_number_flags {
			if flag {
				matching += 1
			}
		}
		fmt.Println("card", card_id, "matching", matching, "instances", number_of_instances[card_id])
		result += number_of_instances[card_id]
		for i := 1; i <= matching; i++ {
			number_of_instances[card_id+i] += number_of_instances[card_id]
		}
	}
	fmt.Println("result: ", result)
}
