package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestKeypadResolver(t *testing.T) {
	kr := NewKeypadResolverPart1()
	assert.Equal(t, "1", kr.FindNextButton("ULL"))
	assert.Equal(t, "9", kr.FindNextButton("RRDDD"))
	assert.Equal(t, "8", kr.FindNextButton("LURDL"))
	assert.Equal(t, "5", kr.FindNextButton("UUUUD"))
}

func TestKeypadResolver2(t *testing.T) {
	kr := NewKeypadResolverPart2()
	assert.Equal(t, "5", kr.FindNextButton("ULL"))
	assert.Equal(t, "D", kr.FindNextButton("RRDDD"))
	assert.Equal(t, "B", kr.FindNextButton("LURDL"))
	assert.Equal(t, "3", kr.FindNextButton("UUUUD"))
}
