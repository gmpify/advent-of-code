package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestProcess(t *testing.T) {
	assert.Equal(t, 6, process("ADVENT", false))
	assert.Equal(t, 7, process("A(1x5)BC", false))
	assert.Equal(t, 9, process("(3x3)XYZ", false))
	assert.Equal(t, 11, process("A(2x2)BCD(2x2)EFG", false))
	assert.Equal(t, 6, process("(6x1)(1x3)A", false))
	assert.Equal(t, 18, process("X(8x2)(3x3)ABCY", false))
}

func TestProcessPart2(t *testing.T) {
	assert.Equal(t, len("XABCABCABCABCABCABCY"), process("X(8x2)(3x3)ABCY", true))
	assert.Equal(t, 241920, process("(27x12)(20x12)(13x14)(7x10)(1x12)A", true))
	assert.Equal(t, 445, process("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", true))
}
