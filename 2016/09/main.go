package main

import (
	"os"
	"regexp"
	"strconv"
)

func parseMarker(in string) (int, int) {
	re := regexp.MustCompile(`(\d+)x(\d+)`)
	m := re.FindStringSubmatch(in)

	a, err := strconv.Atoi(m[1])
	if err != nil {
		panic(err)
	}

	b, err := strconv.Atoi(m[2])
	if err != nil {
		panic(err)
	}

	return a, b
}

func process(in string, recurse bool) (out int) {
	i := 0
	for i < len(in) {
		c := in[i]
		if c == ' ' {
			i += 1
		} else if c == '(' {
			marker := ""
			for {
				i += 1
				c = in[i]
				if c == ')' {
					i += 1
					break
				}
				marker += string(c)
			}
			a, b := parseMarker(marker)
			if recurse {
				out += process(in[i:i+a], true) * b
			} else {
				out += a * b
			}
			i += a
		} else {
			out += 1
			i += 1
		}
	}
	return
}

func main() {
	in, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	out := process(string(in), false)
	println("Part 1:", out)

	out = process(string(in), true)
	println("Part 2:", out)
}
