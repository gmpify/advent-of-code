package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInvalidTriangle(t *testing.T) {
	_, err := NewTriangle(5, 10, 25)
	assert.EqualError(t, err, "invalid triangle due sides length")
}

func TestValidTriangle(t *testing.T) {
	triangle, err := NewTriangle(5, 10, 12)
	assert.Nil(t, err)
	assert.NotNil(t, triangle)
}
