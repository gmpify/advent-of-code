package main

import (
	"bufio"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"unicode"

	"golang.org/x/exp/slices"
)

type room struct {
	nameEncrypted string
	sectorID      int
	checksum      string
	name          string
}

func NewFromString(encryptedName string) room {
	re := regexp.MustCompile(`(?P<Name>[\w-]+)-(?P<SectorID>\d{3})\[(?P<Checksum>\w{5})\]`)
	matches := re.FindStringSubmatch(encryptedName)

	name := matches[re.SubexpIndex("Name")]
	sectorIDRaw := matches[re.SubexpIndex("SectorID")]
	sectorID, err := strconv.Atoi(sectorIDRaw)
	if err != nil {
		panic(err)
	}
	checksum := matches[re.SubexpIndex("Checksum")]

	return room{
		nameEncrypted: name,
		sectorID:      sectorID,
		checksum:      checksum,
	}
}

func (r room) IsValid() bool {
	charCountMap := make(map[rune]int)
	for _, ru := range r.nameEncrypted {
		if !unicode.IsLetter(ru) {
			continue
		}

		if _, ok := charCountMap[ru]; !ok {
			charCountMap[ru] = 0
		}
		charCountMap[ru] += 1
	}

	keys := make([]rune, 0, len(charCountMap))

	for key := range charCountMap {
		keys = append(keys, key)
	}

	slices.Sort(keys)
	sort.SliceStable(keys, func(i, j int) bool {
		return charCountMap[keys[i]] > charCountMap[keys[j]]
	})

	checksumRunes := []rune(r.checksum)
	for i := range 5 {
		if keys[i] != checksumRunes[i] {
			return false
		}
	}

	return true
}

func process(filename string) []room {
	f, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	var rooms []room

	s := bufio.NewScanner(f)
	for s.Scan() {
		r := NewFromString(s.Text())
		if r.IsValid() {
			rooms = append(rooms, r)
		}
	}

	return rooms
}

func sumSectorIDs(rooms []room) int {
	s := 0
	for _, r := range rooms {
		s += r.sectorID
	}
	return s
}

func decryptName(nameEncrypted string, shift int) string {
	numRunesAlphabet := 26
	space := rune(' ')
	dash := rune('-')
	a := rune('a')
	name := ""

	for _, letter := range nameEncrypted {
		if letter == dash {
			letter = space
		} else {
			letter -= a
			letter += int32(shift)
			letter %= int32(numRunesAlphabet)
			letter += a
		}
		name += string(letter)
	}
	return name
}

func decryptNames(rooms []room) {
	for i, room := range rooms {
		room.name = decryptName(room.nameEncrypted, room.sectorID)
		rooms[i] = room
	}
}

func main() {
	rooms := process("input.txt")
	println("Part 1:", sumSectorIDs(rooms))

	decryptNames(rooms)
	for _, r := range rooms {
		if strings.Contains(r.name, "north") {
			println("Room name:", r.name, "; Sector ID:", r.sectorID)
		}
	}
}
