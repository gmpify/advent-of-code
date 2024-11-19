package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestOperations(t *testing.T) {
	s := newScreen(7, 3)

	s.rect(3, 2)
	e := "###....\n###....\n......."
	assert.Equal(t, e, s.readyToPrint())

	s.rotateColumn(1, 1)
	e = "#.#....\n###....\n.#....."
	assert.Equal(t, e, s.readyToPrint())

	s.rotateRow(0, 4)
	e = "....#.#\n###....\n.#....."
	assert.Equal(t, e, s.readyToPrint())

	s.rotateColumn(1, 1)
	e = ".#..#.#\n#.#....\n.#....."
	assert.Equal(t, e, s.readyToPrint())

	assert.Equal(t, 6, s.countLit())
}
