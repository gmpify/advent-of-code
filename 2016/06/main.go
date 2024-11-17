package main

import (
	"bufio"
	"os"
	"sort"
)

type message struct {
	frequencies []map[rune]int
	value       string
}

func (m *message) parseErrorMessage(errorMessage string) {
	if len(m.frequencies) < len(errorMessage) {
		m.frequencies = make([]map[rune]int, len(errorMessage))
	}

	for i, c := range errorMessage {
		if _, ok := m.frequencies[i][c]; !ok {
			if m.frequencies[i] == nil {
				m.frequencies[i] = make(map[rune]int)
			}
			m.frequencies[i][c] = 0
		}
		m.frequencies[i][c] += 1
	}
}

func (m *message) processFromFile(filename string) {
	f, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)
	for s.Scan() {
		l := s.Text()
		m.parseErrorMessage(l)
	}
}

func (m *message) assembleMessage(part int) (value string) {
	for _, f := range m.frequencies {
		keys := []rune{}
		for k := range f {
			keys = append(keys, k)
		}

		sort.SliceStable(keys, func(i, j int) bool {
			if part == 1 {
				return f[keys[i]] > f[keys[j]]
			} else {
				return f[keys[i]] < f[keys[j]]
			}
		})

		value += string(keys[0])
	}
	return
}

func main() {
	m := message{}
	m.processFromFile("input.txt")

	println("Part 1:", m.assembleMessage(1))

	println("Part 2:", m.assembleMessage(2))
}
