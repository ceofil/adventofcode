package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Interval struct {
	start, end int
}
type Mapper struct {
	dst, src Interval
}

func between(value int, interval Interval) bool {
	return interval.start <= value && value <= interval.end
}

func apply_mapper(m Mapper, seed Interval) ([]Interval, []Interval) {
	intersections := []Interval{}
	unmapped := []Interval{}

	s_start_inside_src := between(seed.start, m.src)
	s_end_inside_src := between(seed.end, m.src)

	src_start_inside_s := between(m.src.start, seed)
	src_end_inside_s := between(m.src.end, seed)

	if s_start_inside_src && s_end_inside_src {
		// fmt.Println("s inside src")
		intersections = append(intersections, seed)
	} else if src_start_inside_s && src_end_inside_s {
		// fmt.Println("src inside s")
		intersections = append(intersections, m.src)
		unmapped = append(unmapped, Interval{start: seed.start, end: m.src.start - 1})
		unmapped = append(unmapped, Interval{start: m.src.end + 1, end: seed.end})
	} else if s_start_inside_src {
		// fmt.Println("s.start inside src")
		intersections = append(intersections, Interval{start: seed.start, end: m.src.end})
		unmapped = append(unmapped, Interval{start: m.src.end + 1, end: seed.end})
	} else if s_end_inside_src {
		// fmt.Println("s.end inside src")
		unmapped = append(unmapped, Interval{start: seed.start, end: m.src.start - 1})
		intersections = append(intersections, Interval{start: m.src.start, end: seed.end})
	} else {
		// no intersection; leave the seed as it is
		// unmapped = append(unmapped, seed)
	}
	mapped := []Interval{}
	for _, intersection := range intersections {
		mapped = append(
			mapped,
			Interval{
				start: intersection.start - m.src.start + m.dst.start,
				end:   intersection.end - m.src.start + m.dst.start,
			},
		)
	}
	return mapped, unmapped
}

func apply_all_mappers(mappers []Mapper, seed Interval) []Interval {
	mapped := []Interval{}
	seeds_to_process := []Interval{}
	seeds_to_process = append(seeds_to_process, seed)

	for len(seeds_to_process) > 0 {
		new_seeds_to_process := []Interval{}
		for _, seed_to_process := range seeds_to_process {
			seed_intersects_with_mapper := false
			for _, mapper := range mappers {
				// fmt.Println("\nMAPPER: ", mapper)
				mapped_seeds, unmapped_seeds := apply_mapper(mapper, seed_to_process)
				if len(mapped_seeds) > 0 {
					mapped = append(mapped, mapped_seeds...)
					new_seeds_to_process = append(new_seeds_to_process, unmapped_seeds...)
					seed_intersects_with_mapper = true
					break
				}
			}
			if !seed_intersects_with_mapper {
				mapped = append(mapped, seed_to_process)
			}
		}
		seeds_to_process = new_seeds_to_process
	}
	// fmt.Println("before", seed, "after", mapped)
	return mapped
}
func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	groups := strings.Split(string(fileContent), "\n\n")
	seeds := []Interval{}
	seeds_as_str := strings.Split(groups[0], ": ")
	seeds_as_str_split := strings.Split(seeds_as_str[1], " ")
	for idx := 0; idx < len(seeds_as_str_split); idx += 2 {
		start, _ := strconv.Atoi(seeds_as_str_split[idx])
		length, _ := strconv.Atoi(seeds_as_str_split[idx+1])
		seeds = append(seeds, Interval{start: start, end: start + length - 1})
	}

	for group_idx, group := range groups[1:] {
		fmt.Println("group", group_idx, "initial seeds: ", len(seeds))
		// fmt.Println()
		lines := strings.Split(group, "\n")
		mappers := []Mapper{}
		for _, line := range lines[1:] {
			split_line := strings.Split(line, " ")
			dst, _ := strconv.Atoi(split_line[0])
			src, _ := strconv.Atoi(split_line[1])
			length, _ := strconv.Atoi(split_line[2])
			mapper := Mapper{dst: Interval{dst, dst + length - 1}, src: Interval{src, src + length - 1}}
			mappers = append(mappers, mapper)
		}
		all_new_seeds := []Interval{}
		for _, seed := range seeds {
			mapped := apply_all_mappers(mappers, seed)
			all_new_seeds = append(all_new_seeds, mapped...)
			// break
		}
		seeds = all_new_seeds
		// fmt.Println("\n\nseeds after group", group_idx+1, seeds)
		// break
	}

	// fmt.Println(len(seeds))
	min := seeds[0].start
	for _, seed := range seeds {
		if seed.start < min {
			min = seed.start
		}
	}
	// fmt.Println("final seeds: ", seeds)
	fmt.Println("result: ", min)

}
