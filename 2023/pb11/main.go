package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

type Pos struct {
	x, y int
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func mhtDist(a, b Pos) int {
	return abs(a.x-b.x) + abs(a.y-b.y)
}

func hasGalaxy(line string) bool {
	return strings.Index(line, "#") != -1
}

func getColumn(x int, lines []string) string {
	result := ""
	for _, line := range lines {
		result += string(line[x])
	}
	return result
}

func duplicateColumns(columns []int, lines []string) []string {
	result := []string{}
	for _, line := range lines {
		newLine := ""
		for ix, chr := range line {
			newLine += string(chr)
			if slices.Contains(columns, ix) {
				newLine += string(chr)
			}
		}
		result = append(result, newLine)
	}

	return result
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	lines := strings.Split(string(fileContent), "\n")
	new_lines := []string{}
	for _, line := range lines {
		new_lines = append(new_lines, line)
		if !hasGalaxy(line) {
			new_lines = append(new_lines, line)
		}
	}
	lines = new_lines
	xs := []int{}
	for xi := 0; xi < len(lines[0]); xi++ {
		if !hasGalaxy(getColumn(xi, lines)) {
			xs = append(xs, xi)
		}
	}

	lines = duplicateColumns(xs, lines)
	galaxies := []Pos{}
	for y, line := range lines {
		for x, chr := range line {
			if string(chr) == "#" {
				galaxies = append(galaxies, Pos{x: x, y: y})
			}
		}
	}

	// fmt.Println("galaxies", len(galaxies))
	result := 0
	for i := 0; i < len(galaxies)-1; i++ {
		for j := i + 1; j < len(galaxies); j++ {
			dist := mhtDist(galaxies[i], galaxies[j])
			// fmt.Println(i+1, j+1, dist)
			result += dist
		}
	}

	fmt.Println(result)
}
