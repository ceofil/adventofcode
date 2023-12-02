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
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	// 12 red cubes, 13 green cubes, and 14 blue cubes
	config := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}
	sum := 0
	for scanner.Scan() {
		line := scanner.Text()
		game_is_valid := true
		game := strings.Split(line, ":")
		key, value := game[0], game[1]
		game_id, _ := strconv.Atoi(strings.Split(key, " ")[1])
		draws := strings.Split(value, ";")
		for _, draw := range draws {
			pairs := strings.Split(draw, ",")
			for _, pair := range pairs {
				split_pair := strings.Split(strings.TrimSpace(pair), " ")
				count, _ := strconv.Atoi(split_pair[0])
				color := split_pair[1]
				// fmt.Println(pair, color, count)
				if count > config[color] {
					game_is_valid = false
				}
			}
		}
		if game_is_valid {
			sum += game_id
		}
	}
	fmt.Println(sum)
}
