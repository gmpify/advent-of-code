package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestProcessMessage(t *testing.T) {
	m := message{}
	m.parseErrorMessage("eedadn")

	assert.Equal(t, 6, len(m.frequencies))

	assert.Equal(t, 1, m.frequencies[0]['e'])
	assert.Equal(t, 1, m.frequencies[1]['e'])
	assert.Equal(t, 1, m.frequencies[2]['d'])
	assert.Equal(t, 1, m.frequencies[3]['a'])
	assert.Equal(t, 1, m.frequencies[4]['d'])
	assert.Equal(t, 1, m.frequencies[5]['n'])

	m.parseErrorMessage("eandsr")
	assert.Equal(t, 2, m.frequencies[0]['e'])
	assert.Equal(t, 1, m.frequencies[1]['a'])
	assert.Equal(t, 1, m.frequencies[2]['n'])
	assert.Equal(t, 1, m.frequencies[3]['d'])
	assert.Equal(t, 1, m.frequencies[4]['s'])
	assert.Equal(t, 1, m.frequencies[5]['r'])
}

func TestProcessFromFile(t *testing.T) {
	m := message{}
	m.processFromFile("input_test.txt")

	assert.Equal(t, "easter", m.assembleMessage(1))
}
