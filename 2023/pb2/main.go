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
	sum := 0
	for scanner.Scan() {
		maxes := map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}
		line := scanner.Text()
		game := strings.Split(line, ":")
		_, value := game[0], game[1]
		// game_id, _ := strconv.Atoi(strings.Split(key, " ")[1])
		draws := strings.Split(value, ";")
		for _, draw := range draws {
			pairs := strings.Split(draw, ",")
			for _, pair := range pairs {
				split_pair := strings.Split(strings.TrimSpace(pair), " ")
				count, _ := strconv.Atoi(split_pair[0])
				color := split_pair[1]
				// fmt.Println(pair, color, count)
				if count > maxes[color] {
					maxes[color] = count
				}
			}
		}
		sum += maxes["red"] * maxes["green"] * maxes["blue"]
	}
	fmt.Println(sum)
}
