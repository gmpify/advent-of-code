package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHasABBA(t *testing.T) {
	term1 := "abba"
	assert.True(t, hasABBA(term1))

	term2 := "mnop"
	assert.False(t, hasABBA(term2))

	term3 := "ioxxoj"
	assert.True(t, hasABBA(term3))

	term4 := "asdfgh"
	assert.False(t, hasABBA(term4))
}

func TestSupportTLS(t *testing.T) {
	ip1 := "abba[mnop]qrst"
	assert.True(t, supportTLS(ip1))

	ip2 := "abcd[bddb]bxyyx"
	assert.False(t, supportTLS(ip2))

	ip3 := "aaaa[qwer]tyui"
	assert.False(t, supportTLS(ip3))

	ip4 := "ioxxoj[asdfgh]zxcvbn"
	assert.True(t, supportTLS(ip4))

	ip5 := "zxcvbn[asdfgh]ioxxo"
	assert.True(t, supportTLS(ip5))
}
