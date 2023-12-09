package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

type Destination struct {
	left, right string
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	lines := strings.Split(string(fileContent), "\n")

	instructions := lines[0]

	re := regexp.MustCompile(`\b\w+\b`)
	graph := map[string]Destination{}
	locs := []string{}
	for _, line := range lines[2:] {
		matches := re.FindAllString(line, -1)
		key := matches[0]
		left := matches[1]
		right := matches[2]
		graph[key] = Destination{left: left, right: right}
		if key[len(key)-1] == 'A' {
			locs = append(locs, key)
		}
	}

	for _, cloc := range locs {
		loc := cloc
		steps := 0

		for idx := 0; loc[2] != 'Z'; idx = (idx + 1) % len(instructions) {
			steps++
			// fmt.Println(steps)
			if rune(instructions[idx]) == rune('L') {
				loc = graph[loc].left
			} else {
				loc = graph[loc].right
			}
		}
		fmt.Println(steps)
	}
	//solution:
	//compute steps (line51) for each initial location: 22357 17263 14999 16697 13301 20659
	//compute lowest common multiple 14631604759649 (used an online LCM calculator for this)
}
