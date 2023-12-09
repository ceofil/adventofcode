package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func get_prediction(line string) int {
	last_value_in_each_row := []int{}
	split_line := strings.Split(line, " ")
	row := []int{}
	for _, num_str := range split_line {
		num, _ := strconv.Atoi(num_str)
		row = append(row, num)
	}

	all_zeros := false
	for !all_zeros {
		fmt.Println(len(row))
		new_row := []int{}
		last_value_in_each_row = append(last_value_in_each_row, row[len(row)-1])
		all_zeros = true
		for idx := 1; idx < len(row); idx++ {
			new_value := row[idx] - row[idx-1]
			new_row = append(new_row, new_value)
			if new_value != 0 {
				all_zeros = false
			}
		}
		row = new_row
	}

	prediction := 0
	for _, value := range last_value_in_each_row {
		prediction += value
	}

	return prediction
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	result := 0
	lines := strings.Split(string(fileContent), "\n")
	for _, line := range lines {
		prediction := get_prediction(line)
		result += prediction
	}

	fmt.Println("result", result)
}
