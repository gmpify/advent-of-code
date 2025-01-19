package main

import (
	"bufio"
	"os"
	"slices"
	"strconv"
	"strings"
)

type chip int

type bot struct {
	chips []chip

	lowReceiverType  string
	lowReceiverID    string
	highReceiverType string
	highReceiverID   string
}

type bin struct {
	chip chip
}

type factory struct {
	bots map[string]bot
	bins map[string]bin
}

func newFactory() factory {
	f := factory{
		bots: make(map[string]bot),
		bins: make(map[string]bin),
	}
	return f
}

func (f *factory) parseInstruction(in string) {
	if strings.HasPrefix(in, "value") {
		m := strings.Split(in, " ")
		botID := m[5]

		b, ok := f.bots[botID]
		if !ok {
			b = bot{}
		}
		c, err := strconv.Atoi(m[1])
		if err != nil {
			panic(err)
		}

		b.chips = append(b.chips, chip(c))
		f.bots[botID] = b
	} else if strings.HasPrefix(in, "bot") {
		m := strings.Split(in, " ")

		botID := m[1]
		b, ok := f.bots[botID]
		if !ok {
			b = bot{}
		}

		b.lowReceiverType = m[5]
		b.lowReceiverID = m[6]
		b.highReceiverType = m[10]
		b.highReceiverID = m[11]
		f.bots[botID] = b
	} else {
		panic("Invalid instruction")
	}
}

func (f *factory) give(receiverType, receiverID string, c chip) {
	if receiverType == "bot" {
		b, ok := f.bots[receiverID]
		if !ok {
			b = bot{}
		}
		b.chips = append(b.chips, c)
		f.bots[receiverID] = b
	} else if receiverType == "output" {
		b, ok := f.bins[receiverID]
		if !ok {
			b = bin{}
		}
		b.chip = c
		f.bins[receiverID] = b
	} else {
		panic("Invalid receiver type")
	}
}

func (f *factory) resolve(botID string) {
	b := f.bots[botID]
	if len(b.chips) != 2 {
		return
	}

	f.give(b.lowReceiverType, b.lowReceiverID, slices.Min(b.chips))
	f.resolve(b.lowReceiverID)

	f.give(b.highReceiverType, b.highReceiverID, slices.Max(b.chips))
	f.resolve(b.highReceiverID)
}

func (f *factory) work() {
	for i, b := range f.bots {
		if len(b.chips) == 2 {
			f.resolve(i)
			break
		}
	}
}

func main() {
	fa := newFactory()

	fi, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer fi.Close()

	sc := bufio.NewScanner(fi)
	for sc.Scan() {
		fa.parseInstruction(sc.Text())
	}

	fa.work()

	for i, b := range fa.bots {
		if slices.Contains(b.chips, 17) && slices.Contains(b.chips, 61) {
			println("Part 1:", i)
			break
		}
	}

	println("Part 2:", fa.bins["0"].chip*fa.bins["1"].chip*fa.bins["2"].chip)
}
