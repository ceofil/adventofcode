package main

import (
	"fmt"
	"os"
	"strings"
)

type Pos struct {
	x, y int
}

type Pipe struct {
	from, to Pos
}

var top = Pos{x: 0, y: -1}
var bottom = Pos{x: 0, y: 1}
var left = Pos{x: -1, y: 0}
var right = Pos{x: 1, y: 0}
var runeToPipe = map[rune]Pipe{
	'-': {left, right},
	'|': {top, bottom},
	'J': {left, top},
	'7': {left, bottom},
	'L': {right, top},
	'F': {right, bottom},
}
var all_directions = []Pos{top, bottom, left, right}

func add(a, b Pos) Pos {
	return Pos{x: a.x + b.x, y: a.y + b.y}
}

func neg(a Pos) Pos {
	return Pos{x: -a.x, y: -a.y}
}

func validPos(a Pos, width, height int) bool {
	return 0 <= a.x &&
		a.x < width &&
		0 <= a.y &&
		a.y < height
}

func getPipe(a Pos, lines []string) (Pipe, bool) {
	chr := rune(lines[a.y][a.x])
	if chr == '.' {
		return Pipe{}, false
	}
	return runeToPipe[chr], true
}

func leadsTo(a, b Pos, lines []string) bool {
	//return true if a leads to b
	aPipe, aIsPipe := getPipe(a, lines)
	if !aIsPipe {
		return false
	}
	a_to_b := add(b, neg(a))
	return aPipe.to == a_to_b || aPipe.from == a_to_b
}

func connected(a, b Pos, lines []string) bool {
	if !(validPos(a, len(lines[0]), len(lines)) &&
		validPos(b, len(lines[0]), len(lines))) {
		return false
	}
	return leadsTo(a, b, lines) && leadsTo(b, a, lines)
}

func contains(haystack []rune, needle rune) bool {
	for _, element := range haystack {
		if element == needle {
			return true
		}
	}
	return false
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	lines := strings.Split(string(fileContent), "\n")
	s := Pos{}
	for y, line := range lines {
		x := strings.Index(line, "S")
		if x != -1 {
			s.x, s.y = x, y
			break
		}
	}
	width := len(lines[0])
	height := len(lines)

	visited := make([][]bool, height)
	for i := range visited {
		visited[i] = make([]bool, width)
	}
	visited[s.y][s.x] = true

	var first_step Pos
	for _, dir := range all_directions {
		next_pos := add(s, dir)
		if !validPos(next_pos, width, height) {
			continue
		}
		if leadsTo(next_pos, s, lines) {
			first_step = next_pos
			break
		}
	}
	visited[first_step.y][first_step.x] = true

	mobile := first_step
	steps := 1
	for mobile != s {
		found_next := false
		for _, dir := range all_directions {
			next_pos := add(mobile, dir)
			if !validPos(next_pos, width, height) {
				continue
			}
			if next_pos == s && mobile != first_step {
				if !leadsTo(mobile, s, lines) {
					continue
				}
			} else {
				if visited[next_pos.y][next_pos.x] {
					continue
				}
				if !connected(mobile, next_pos, lines) {
					continue
				}
			}
			visited[next_pos.y][next_pos.x] = true
			mobile = next_pos
			found_next = true
			break
		}
		if !found_next {
			fmt.Println("no next step for", mobile)
			panic("no next step")
		}
		steps += 1
	}

	s_visited_neighbors := []Pos{}
	for _, dir := range all_directions {
		next_pos := add(s, dir)
		if !validPos(next_pos, width, height) {
			continue
		}
		next_visited := visited[next_pos.y][next_pos.x]
		if next_visited {
			s_visited_neighbors = append(s_visited_neighbors, dir)
		}
	}

	//started part two and somehow decided to use camel case
	sRune := ' '
	for pipeRune, pipe := range runeToPipe {
		to := pipe.to == s_visited_neighbors[0] || pipe.to == s_visited_neighbors[1]
		from := pipe.from == s_visited_neighbors[0] || pipe.from == s_visited_neighbors[1]
		if to && from {
			sRune = pipeRune
			break
		}
	}
	lineAsRunes := []rune(lines[s.y])
	lineAsRunes[s.x] = sRune
	lines[s.y] = string(lineAsRunes)

	type PipeInfo struct {
		start, end bool
		y          int
	}
	pipeInfo := map[rune]PipeInfo{
		'-': {false, false, 0},
		'|': {false, false, 0},
		'J': {false, true, -1},
		'7': {false, true, 1},
		'L': {true, false, -1},
		'F': {true, false, 1},
	}

	insideLoopCount := 0
	for y := 0; y < height; y++ {
		contour := []bool{}
		// test := []Pos{}
		pipeStartY := 0
		for x := 0; x < width; x++ {
			chr := rune(lines[y][x])
			info := pipeInfo[rune(lines[y][x])]
			if !visited[y][x] {
				contour = append(contour, false)
				continue
			}
			//visited==true from now on
			if chr == '|' {
				contour = append(contour, true)
				continue
			}
			if info.start {
				pipeStartY = info.y
				contour = append(contour, true)
				continue
			}
			if info.end && info.y == pipeStartY {
				contour = append(contour, true)
				continue
			}
		}
		inside := false
		for _, wall := range contour {
			if wall {
				inside = !inside
			} else if inside {
				insideLoopCount++
			}
		}
	}
	fmt.Println("inside count", insideLoopCount)
}
