package main

import (
	"errors"
	"math"
	"os"
	"strconv"
	"strings"
)

type nothing struct{}

type xy struct {
	x int
	y int
}

type person struct {
	position  xy
	direction int

	visitedPositions map[xy]nothing
}

func NewPerson() *person {
	position := xy{
		x: 0,
		y: 0,
	}

	visited := make(map[xy]nothing)
	visited[position] = nothing{}

	return &person{
		position:         position,
		direction:        0,
		visitedPositions: visited,
	}
}

func (p *person) ParseInstructionsAndMove(instructions string, stopAtDuplicated bool) error {
	parsedInstructions := strings.Split(instructions, ", ")
	for _, instruction := range parsedInstructions {
		moved, err := p.move(instruction, stopAtDuplicated)
		if err != nil {
			return err
		}

		if !moved {
			break
		}
	}
	return nil
}

func (p person) Distance() int {
	return int(math.Abs(float64(p.position.x)) + math.Abs(float64(p.position.y)))
}

func (p *person) move(instruction string, stopAtDuplicated bool) (bool, error) {
	instruction_direction := instruction[0:1]
	if strings.EqualFold(instruction_direction, "L") {
		p.direction += 90
		p.direction %= 360
	} else if strings.EqualFold(instruction_direction, "R") {
		p.direction += 270
		p.direction %= 360
	} else {
		return false, errors.New("instruction must start with L or R")
	}

	instruction_distance, err := strconv.Atoi(instruction[1:])
	if err != nil {
		return false, err
	}
	for range instruction_distance {
		switch p.direction {
		case 0:
			p.position.y += 1
		case 90:
			p.position.x += 1
		case 180:
			p.position.y -= 1
		case 270:
			p.position.x -= 1
		}

		if stopAtDuplicated {
			if _, ok := p.visitedPositions[p.position]; ok {
				return false, nil
			}
		}

		p.visitedPositions[p.position] = nothing{}
	}

	return true, nil
}

func main() {
	input := "R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2"

	p1 := NewPerson()
	if err := p1.ParseInstructionsAndMove(input, false); err != nil {
		println(err)
		os.Exit(-1)
	}
	println("Part 1:", p1.Distance())

	p2 := NewPerson()
	if err := p2.ParseInstructionsAndMove(input, true); err != nil {
		println(err)
		os.Exit(-1)
	}
	println("Part 2:", p2.Distance())
}
