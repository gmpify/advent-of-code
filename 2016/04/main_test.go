package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestValidRoom(t *testing.T) {
	r := NewFromString("aaaaa-bbb-z-y-x-123[abxyz]")
	assert.True(t, r.IsValid())
}

func TestDecryptName(t *testing.T) {
	n := decryptName("qzmt-zixmtkozy-ivhz", 343)
	assert.Equal(t, "very encrypted name", n)
}

func TestDecryptNameNoShift(t *testing.T) {
	n := decryptName("a", 0)
	assert.Equal(t, "a", n)
}

func TestDecryptNameShift1(t *testing.T) {
	n := decryptName("a", 1)
	assert.Equal(t, "b", n)
}

func TestDecryptNameShift1FromZ(t *testing.T) {
	n := decryptName("z", 1)
	assert.Equal(t, "a", n)
}

func TestDecryptNameShiftFromAThroughA(t *testing.T) {
	n := decryptName("a", 26)
	assert.Equal(t, "a", n)
}

func TestDecryptNameShiftFromBThroughZ(t *testing.T) {
	n := decryptName("a", 27)
	assert.Equal(t, "b", n)
}
