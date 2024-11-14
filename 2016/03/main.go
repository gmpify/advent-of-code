package main

import (
	"bufio"
	"errors"
	"log"
	"os"
	"strconv"
	"strings"
)

type triangle struct {
	a int
	b int
	c int
}

func NewTriangle(a, b, c int) (triangle, error) {
	if a+b <= c || a+c <= b || b+c <= a {
		return triangle{}, errors.New("invalid triangle due sides length")
	}

	return triangle{a: a, b: b, c: c}, nil
}

func processPart1(filename string) int {
	f, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	validTriangles := 0

	s := bufio.NewScanner(f)
	for s.Scan() {
		var sides []int
		for _, side := range strings.Fields(s.Text()) {
			s, err := strconv.Atoi(side)
			if err != nil {
				panic(err)
			}
			sides = append(sides, s)
		}
		if len(sides) != 3 {
			log.Fatalf("Should only have 3 sides, got %v", sides)
		}

		_, err = NewTriangle(sides[0], sides[1], sides[2])
		if err == nil {
			validTriangles += 1
		}
	}
	return validTriangles
}

func processPart2(filename string) int {
	f, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	sides := [][]int{{}, {}, {}}
	validTriangles := 0

	s := bufio.NewScanner(f)
	for s.Scan() {
		for i, side := range strings.Fields(s.Text()) {
			s, err := strconv.Atoi(side)
			if err != nil {
				panic(err)
			}
			sides[i] = append(sides[i], s)

			if len(sides[i]) == 3 {
				_, err = NewTriangle(sides[i][0], sides[i][1], sides[i][2])
				if err == nil {
					validTriangles += 1
				}
				sides[i] = []int{}
			}
		}
	}
	return validTriangles
}

func main() {
	println("Part 1:", processPart1("input.txt"))
	println("Part 2:", processPart2("input.txt"))
}
