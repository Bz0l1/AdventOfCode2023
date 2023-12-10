package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var directions = [8][2]int{
	{-1, -1}, {-1, 0}, {-1, 1},
	{0, -1}, {0, 1},
	{1, -1}, {1, 0}, {1, 1}}

func readFile(fileName string) ([][]rune, error) {
	file, err := os.Open(fileName)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var inputs [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inputs = append(inputs, []rune(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return inputs, nil
}

func isSymbol(ch rune) bool {
	return ch != '.' && ch != '\r' && ch != '\n' && !(ch >= '0' && ch <= '9')
}

func isAdjacentToSymbol(schematic [][]rune, row, col int) bool {
	for _, direction := range directions {
		newRow, newCol := row+direction[0], col+direction[1]
		if newRow > 0 && newRow < len(schematic) && newCol > 0 && newCol < len(schematic[newRow]) &&
			isSymbol(schematic[newRow][newCol]) {
			return true
		}
	}
	return false
}

func extractNumber(schematic [][]rune) []int {
	var nums []int
	for i, line := range schematic {
		for j, ch := range line {
			if ch >= '0' && ch <= '9' {
				if j+1 < len(line) && line[j+1] >= '0' && line[j+1] <= '9' {
					num, _ := strconv.Atoi(string([]rune{ch, line[j+1]}))
					if isAdjacentToSymbol(schematic, i, j) || isAdjacentToSymbol(schematic, i, j+1) {
						nums = append(nums, num)
					}
					j++
				} else if isAdjacentToSymbol(schematic, i, j) {
					num, _ := strconv.Atoi(string(ch))
					nums = append(nums, num)
				}
			}
		}
	}
	return nums
}

func part1(schematic [][]rune) (int, error) {
	nums := extractNumber(schematic)
	totalSum := 0
	for _, num := range nums {
		totalSum += num
	}
	return totalSum, nil
}

func main() {
	schematic, err := readFile("day_3/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	totalSum, err := part1(schematic)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(totalSum)
}
