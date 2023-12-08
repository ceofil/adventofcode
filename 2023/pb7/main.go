package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Hand struct {
	cards    string
	bid      int
	strength int
}

func compute_strength(cards string) int {
	counter := map[rune]int{}
	n_of_a_kind := map[int]int{}

	for _, card := range cards {
		counter[card]++
	}

	for _, value := range counter {
		// fmt.Println("here", key, value)
		if value > 1 {
			n_of_a_kind[value]++
		}
	}
	// fmt.Println(n_of_a_kind, cards)

	if n_of_a_kind[5] == 1 {
		return 6
	}
	if n_of_a_kind[4] == 1 {
		return 5
	}
	if n_of_a_kind[3] == 1 && n_of_a_kind[2] == 1 {
		return 4
	}
	if n_of_a_kind[3] == 1 {
		return 3
	}
	if n_of_a_kind[2] == 2 {
		return 2
	}
	if n_of_a_kind[2] == 1 {
		return 1
	}

	return 0
}

func main() {
	fileContent, err := os.ReadFile(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	lines := strings.Split(string(fileContent), "\n")

	hands := []Hand{}
	for _, line := range lines {
		split_line := strings.Split(line, " ")
		cards := split_line[0]
		bid, _ := strconv.Atoi(split_line[1])
		hands = append(hands, Hand{cards: cards, bid: bid, strength: compute_strength(cards)})
	}

	CARDS := "23456789TJQKA"
	sort.Slice(hands, func(i, j int) bool {
		if hands[i].strength < hands[j].strength {
			return true
		} else if hands[i].strength > hands[j].strength {
			return false
		}
		for idx := 0; idx < len(hands[i].cards); idx++ {
			icard := strings.Index(CARDS, string(hands[i].cards[idx]))
			jcard := strings.Index(CARDS, string(hands[j].cards[idx]))
			if icard != jcard {
				return icard < jcard
			}
		}
		panic("two equal hands")
		// return false
	})

	result := 0
	for rank, hand := range hands {
		fmt.Println(hand.cards, rank, "strenght", hand.strength)
		result += hand.bid * (rank + 1)
	}
	fmt.Println("result: ", result)
}
