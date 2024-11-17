package main

import (
	"crypto/md5"
	"encoding/hex"
	"strconv"
	"strings"
)

func findNextInterestingHash(salt string, startingIndex int) (i int, hash string) {
	i = startingIndex
	for {
		it := salt + strconv.Itoa(i)
		itHashed := md5.Sum([]byte(it))
		hash = hex.EncodeToString(itHashed[:])
		i += 1

		if strings.HasPrefix(hash, "00000") {
			return
		}
	}
}

func findPassword1(salt string) string {
	password := ""
	i := 0
	for j := 0; j < 8; j++ {
		iOut, hash := findNextInterestingHash(salt, i)
		i = iOut
		password += string(hash[5])
	}
	return password
}

func findPassword2(salt string) string {
	password := []string{"_", "_", "_", "_", "_", "_", "_", "_"}
	foundChars := 0
	i := 0
	for {
		iOut, hash := findNextInterestingHash(salt, i)
		i = iOut

		position := string(hash[5])
		char := string(hash[6])

		pos, err := strconv.Atoi(position)
		if err != nil || pos >= len(password) || password[pos] != "_" {
			continue
		}

		password[pos] = char
		foundChars += 1

		if foundChars == 8 {
			break
		}
	}
	return strings.Join(password, "")
}

func main() {
	println("Part 1:", findPassword1("ojvtpuvg"))

	println("Part 2:", findPassword2("ojvtpuvg"))
}
