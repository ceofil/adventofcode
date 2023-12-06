package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Interval struct {
	start, end int
}
type Mapper struct {
	dst, src Interval
}

func between(value int, interval Interval) bool {
	return interval.start <= value && value < interval.end
}

func interesct(a, b Interval) bool {
	return between(a.start, b) || between(a.end-1, b) || between(b.start, a) || between(b.end-1, a)
}

func apply_mapper(m Mapper, s Interval) ([]Interval, []Interval) {
	intersections := []Interval{}
	unmapped := []Interval{}

	s_start_inside_src := between(s.start, m.src)
	s_end_inside_src := between(s.end-1, m.src)

	src_start_inside_s := between(m.src.start, s)
	src_end_inside_s := between(m.src.end-1, s)

	if s_start_inside_src && s_end_inside_src {
		// fmt.Println("s inside src")
		intersections = append(intersections, s)
	} else if src_start_inside_s && src_end_inside_s {
		// fmt.Println("src inside s")
		intersections = append(intersections, m.src)
		unmapped = append(unmapped, Interval{start: s.start, end: m.src.start})
		unmapped = append(unmapped, Interval{start: m.src.end, end: s.end})
	} else if s_start_inside_src {
		// fmt.Println("s.start inside src")
		intersections = append(intersections, Interval{start: s.start, end: m.src.end})
		unmapped = append(unmapped, Interval{start: m.src.end, end: s.end})
	} else if s_end_inside_src {
		// fmt.Println("s.end inside src")
		unmapped = append(unmapped, Interval{start: s.start, end: m.src.start})
		intersections = append(intersections, Interval{start: m.src.start, end: s.end})
	} else {
		// no intersection
		unmapped = append(unmapped, s)
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
		seeds = append(seeds, Interval{start: start, end: start + length})
	}

	for group_idx, group := range groups[1:] {
		fmt.Println("group", group_idx, "initial seeds: ", len(seeds))
		lines := strings.Split(group, "\n")
		mappers := []Mapper{}
		for _, line := range lines[1:] {
			split_line := strings.Split(line, " ")
			dst, _ := strconv.Atoi(split_line[0])
			src, _ := strconv.Atoi(split_line[1])
			length, _ := strconv.Atoi(split_line[2])
			mapper := Mapper{dst: Interval{dst, dst + length}, src: Interval{src, src + length}}
			mappers = append(mappers, mapper)
		}
		all_new_seeds := []Interval{}
		for _, seed := range seeds {
			// fmt.Println("\n-----------------------\nprocessing seed:\t", seed)
			current_seeds := []Interval{}
			current_seeds = append(current_seeds, seed)
			current_new_seeds := []Interval{}
			for iteration_idx := 0; len(current_seeds) > 0; iteration_idx++ {
				if iteration_idx%1 == 0 && iteration_idx > 0 {
					// fmt.Println(iteration_idx)
					fmt.Println(len(current_seeds))
				}
				time.Sleep(time.Second)
				current_seed := current_seeds[0]
				// fmt.Println("seed from queue\t\t", current_seed)
				current_seeds = current_seeds[1:]
				// fmt.Println("after", current_seeds)
				// check if intersects with any mapper
				any_intersection := false
				for _, mapper := range mappers {
					if interesct(current_seed, mapper.src) {
						// fmt.Println("inter", mapper)
						any_intersection = true
						break
					}
				}
				if !any_intersection {
					current_new_seeds = append(current_new_seeds, current_seed)
					// fmt.Printf("no intersection continue\n")
					continue
				}

				for _, mapper := range mappers {
					// fmt.Println("\nMAPPER: ", mapper)
					mapped, unmapped := apply_mapper(mapper, current_seed)
					// fmt.Println("mapped: ", mapped, "unmapped: ", unmapped)
					if len(mapped) > 0 {
						//if some intersection occured
						fmt.Printf("+%d  -%d  \n", len(unmapped), len(mapped))
						current_new_seeds = append(current_new_seeds, mapped...)
						current_seeds = append(current_seeds, unmapped...)
					}
				}
				// fmt.Println("end loop currend_seeds", current_seeds)
				// break
			}
			all_new_seeds = append(all_new_seeds, current_new_seeds...)
		}
		seeds = all_new_seeds
		// fmt.Println("\n\nseeds after group", group_idx+1, seeds)
		// break

	}

	fmt.Println(len(seeds))
	min := seeds[0].start
	for _, seed := range seeds {
		if seed.start < min {
			min = seed.start
		}
	}
	fmt.Println(min)

}
