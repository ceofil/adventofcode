package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"time"
)

type Mapper struct {
	dst, src, length int
}

type Interval struct {
	start, end int
}

// 1 680 883 088
func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	groups := strings.Split(string(fileContent), "\n\n")
	seed_intervals := []Interval{}
	seeds_as_str := strings.Split(groups[0], ": ")
	seeds_as_str_split := strings.Split(seeds_as_str[1], " ")
	for idx := 0; idx < len(seeds_as_str_split); idx += 2 {
		start, _ := strconv.Atoi(seeds_as_str_split[idx])
		length, _ := strconv.Atoi(seeds_as_str_split[idx+1])
		seed_intervals = append(seed_intervals, Interval{start: start, end: start + length})
	}

	groups_mappers := [][]Mapper{}
	for _, group := range groups[1:] {
		lines := strings.Split(group, "\n")
		mappers := []Mapper{}
		for _, line := range lines[1:] {
			split_line := strings.Split(line, " ")
			dst, _ := strconv.Atoi(split_line[0])
			src, _ := strconv.Atoi(split_line[1])
			length, _ := strconv.Atoi(split_line[2])
			mapper := Mapper{dst, src, length}
			mappers = append(mappers, mapper)
		}
		groups_mappers = append(groups_mappers, mappers)
	}

	total_iterations := 1680883088
	current_iterations := 0
	global_min := math.MaxInt

	start_time := time.Now()
	for _, seed_interval := range seed_intervals {
		for seed := seed_interval.start; seed < seed_interval.end; seed++ {
			if current_iterations%1000000 == 0 {
				fmt.Printf("%.2f%%  %.2fs\n", float64(current_iterations)/float64(total_iterations)*100, time.Now().Sub(start_time).Seconds())
			}
			current_iterations++
			new_seed := seed
			for _, mappers := range groups_mappers {
				for _, mapper := range mappers {
					if !(new_seed >= mapper.src && new_seed < mapper.src+mapper.length) {
						continue
					}
					new_seed = new_seed - mapper.src + mapper.dst
					break
				}
			}
			// fmt.Println(seed, new_seed)
			if new_seed < global_min {
				global_min = new_seed
			}
		}
	}
	fmt.Println("final global min", global_min)

}
