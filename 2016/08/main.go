package main

import (
	"bufio"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type screen struct {
	pixels [][]string
}

func newScreen(x, y int) (s screen) {
	s.pixels = make([][]string, y)
	for i := range s.pixels {
		s.pixels[i] = make([]string, x)
		for j := range s.pixels[i] {
			s.pixels[i][j] = "."
		}
	}
	return
}

func (s *screen) do(d string) {
	if strings.HasPrefix(d, "rect") {
		re := regexp.MustCompile(`rect (\d+)x(\d+)`)
		m := re.FindStringSubmatch(d)

		a, err := strconv.Atoi(m[1])
		if err != nil {
			panic(err)
		}

		b, err := strconv.Atoi(m[2])
		if err != nil {
			panic(err)
		}

		s.rect(a, b)
	} else if strings.HasPrefix(d, "rotate row") {
		re := regexp.MustCompile(`rotate row y=(\d+) by (\d+)`)
		m := re.FindStringSubmatch(d)

		a, err := strconv.Atoi(m[1])
		if err != nil {
			panic(err)
		}

		b, err := strconv.Atoi(m[2])
		if err != nil {
			panic(err)
		}

		s.rotateRow(a, b)
	} else if strings.HasPrefix(d, "rotate column") {
		re := regexp.MustCompile(`rotate column x=(\d+) by (\d+)`)
		m := re.FindStringSubmatch(d)

		a, err := strconv.Atoi(m[1])
		if err != nil {
			panic(err)
		}

		b, err := strconv.Atoi(m[2])
		if err != nil {
			panic(err)
		}

		s.rotateColumn(a, b)
	} else {
		panic("Invalid instructin")
	}
}

func (s *screen) countLit() (c int) {
	for i := 0; i < len(s.pixels); i++ {
		for j := 0; j < len(s.pixels[i]); j++ {
			if s.pixels[i][j] == "#" {
				c += 1
			}
		}
	}
	return
}

func (s *screen) readyToPrint() (p string) {
	for i := 0; i < len(s.pixels); i++ {
		for j := 0; j < len(s.pixels[i]); j++ {
			p += s.pixels[i][j]
		}
		p += "\n"
	}
	p = strings.TrimSpace(p)
	return
}

func (s *screen) rect(a, b int) {
	for i := 0; i < b; i++ {
		for j := 0; j < a; j++ {
			s.pixels[i][j] = "#"
		}
	}
}

func (s *screen) rotateColumn(a, b int) {
	for b > 0 {
		tmp := s.pixels[0][a]
		for i := 0; i < len(s.pixels); i++ {
			iNew := (i + 1) % len(s.pixels)
			tmp, s.pixels[iNew][a] = s.pixels[iNew][a], tmp
		}
		b -= 1
	}
}

func (s *screen) rotateRow(a, b int) {
	for b > 0 {
		tmp := s.pixels[a][0]
		for i := 0; i < len(s.pixels[a]); i++ {
			iNew := (i + 1) % len(s.pixels[a])
			tmp, s.pixels[a][iNew] = s.pixels[a][iNew], tmp
		}
		b -= 1
	}
}

func main() {
	s := newScreen(50, 6)

	f, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	sc := bufio.NewScanner(f)
	for sc.Scan() {
		s.do(sc.Text())
	}

	println("Part 1:", s.countLit())
	println("Part 2:")
	println(s.readyToPrint())
}
