package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Mapper struct {
	dst, src, length int
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	groups := strings.Split(string(fileContent), "\n\n")
	seeds := []int{}
	seeds_as_str := strings.Split(groups[0], ": ")
	for _, seed_str := range strings.Split(seeds_as_str[1], " ") {
		seed_int, _ := strconv.Atoi(seed_str)
		seeds = append(seeds, seed_int)
	}

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
		new_seeds := []int{}
		for _, seed := range seeds {
			new_seed := seed
			for _, mapper := range mappers {
				if !(seed >= mapper.src && seed < mapper.src+mapper.length) {
					continue
				}
				new_seed = seed - mapper.src + mapper.dst
				// fmt.Println(seed, "-->", new_seed, "with", mapper)
				break
			}
			new_seeds = append(new_seeds, new_seed)
		}
		seeds = new_seeds
		// break

	}

	min := seeds[0]
	for _, seed := range seeds {
		if seed < min {
			min = seed
		}
	}
	fmt.Println(min)

}
