package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMove(t *testing.T) {
	p := NewPerson()
	p.move("R2", false)
	p.move("L3", false)
	assert.Equal(t, 5, p.Distance())
}

func TestParseInstructionsAndMove(t *testing.T) {
	p := NewPerson()
	p.ParseInstructionsAndMove("R2, L3", false)
	assert.Equal(t, 5, p.Distance())
}

func TestParseInstructionsAndMoveButStopAtDuplicated(t *testing.T) {
	p := NewPerson()
	p.ParseInstructionsAndMove("R8, R4, R4, R8", true)
	assert.Equal(t, 4, p.Distance())
}
