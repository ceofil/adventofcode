package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func capture_numbers(line string) int {
	re := regexp.MustCompile(`\b\d+\b`)
	matches := re.FindAllString(line, -1)
	number_str := strings.Join(matches, "")
	number, _ := strconv.Atoi(number_str)
	return number
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	lines := strings.Split(string(fileContent), "\n")
	// fmt.Println(string(fileContent), len(lines))
	time := capture_numbers(lines[0])
	record_distance := capture_numbers(lines[1])
	result := 1
	race_winning_moves := 0
	for hold := 0; hold <= time; hold++ {
		distance := (time - hold) * hold
		if distance > record_distance {
			race_winning_moves += 1
		}
	}
	result *= race_winning_moves
	fmt.Println("result: ", result)
}
