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

	galaxies := []Pos{}
	columns := []int{}
	rows := []int{}
	for y, line := range lines {
		for x, chr := range line {
			if chr == '#' {
				galaxies = append(galaxies, Pos{x, y})
			}
		}
	}
	for x := 0; x < len(lines[0]); x++ {
		if !hasGalaxy(getColumn(x, lines)) {
			columns = append(columns, x)
		}
	}

	for y, line := range lines {
		if !hasGalaxy(line) {
			rows = append(rows, y)
		}
	}

	expand := 1000000
	expand--
	for idx := range galaxies {
		xDiff := 0
		yDiff := 0
		for _, col := range columns {
			if galaxies[idx].x > col {
				xDiff += expand
			}
		}
		for _, row := range rows {
			if galaxies[idx].y > row {
				yDiff += expand
			}
		}
		galaxies[idx].x += xDiff
		galaxies[idx].y += yDiff
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
