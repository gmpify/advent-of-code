package main

import (
	"bufio"
	"os"
)

func findABATerms(term string) []string {
	abas := []string{}
	for i := 0; i <= len(term)-3; i++ {
		runes := []rune(term)
		if runes[i] == runes[i+2] && runes[i] != runes[i+1] {
			abas = append(abas, string(runes[i:i+2]))
		}
	}
	return abas
}

func supportSSL(ip string) bool {
	terms := []string{}
	termsHypernet := []string{}

	termStart := 0
	runes := []rune(ip)
	for i := 0; i < len(ip); i++ {
		if runes[i] == ']' {
			termsHypernet = append(termsHypernet, string(runes[termStart:i]))
			termStart = i + 1
		}
		if runes[i] == '[' {
			terms = append(terms, string(runes[termStart:i]))
			termStart = i + 1
		}
		if i == len(ip)-1 {
			terms = append(terms, string(runes[termStart:]))
		}
	}

	abaInTerms := []string{}
	for _, t := range terms {
		abaInTerms = append(abaInTerms, findABATerms(t)...)
	}

	abaInTermsHypernet := []string{}
	for _, t := range termsHypernet {
		abaInTermsHypernet = append(abaInTermsHypernet, findABATerms(t)...)
	}

	for _, t := range abaInTerms {
		inverseABA := t[1:] + t[0:1]
		for _, tt := range abaInTermsHypernet {
			if inverseABA == tt {
				return true
			}
		}
	}

	return false
}

func countIPsWithSSLFromFile(filename string) (count int) {
	f, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)
	for s.Scan() {
		if supportSSL(s.Text()) {
			count += 1
		}
	}
	return
}

func hasABBA(term string) bool {
	for i := 0; i <= len(term)-4; i++ {
		runes := []rune(term)
		if runes[i] == runes[i+3] && runes[i+1] == runes[i+2] && runes[i] != runes[i+1] {
			return true
		}
	}
	return false
}

func supportTLS(ip string) bool {
	termsShouldHaveABBA := []string{}
	termsShouldNotHaveABBA := []string{}

	termStart := 0
	runes := []rune(ip)
	for i := 0; i < len(ip); i++ {
		if runes[i] == ']' {
			termsShouldNotHaveABBA = append(termsShouldNotHaveABBA, string(runes[termStart:i]))
			termStart = i + 1
		}
		if runes[i] == '[' {
			termsShouldHaveABBA = append(termsShouldHaveABBA, string(runes[termStart:i]))
			termStart = i + 1
		}
		if i == len(ip)-1 {
			termsShouldHaveABBA = append(termsShouldHaveABBA, string(runes[termStart:]))
		}
	}

	for _, t := range termsShouldNotHaveABBA {
		if hasABBA(t) {
			return false
		}
	}

	for _, t := range termsShouldHaveABBA {
		if hasABBA(t) {
			return true
		}
	}

	return false
}

func countIPsWithTLSFromFile(filename string) (count int) {
	f, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	s := bufio.NewScanner(f)
	for s.Scan() {
		if supportTLS(s.Text()) {
			count += 1
		}
	}
	return
}

func main() {
	println("Part 1:", countIPsWithTLSFromFile("input.txt"))
	println("Part 2:", countIPsWithSSLFromFile("input.txt"))
}
