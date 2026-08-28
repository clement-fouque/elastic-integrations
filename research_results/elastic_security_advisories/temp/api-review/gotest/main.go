package main

import (
	"encoding/base64"
	"fmt"
	"strings"
)

func try(name, s string) {
	b, err := base64.StdEncoding.DecodeString(s)
	if err != nil {
		fmt.Printf("%-46s ERROR: %v\n", name, err)
		return
	}
	fmt.Printf("%-46s OK  -> %q (%d bytes)\n", name, string(b), len(b))
}

func main() {
	fmt.Println("go base64.StdEncoding.DecodeString behaviour")
	plain := "hello world this is a longer test string for base64 wrapping"
	enc := base64.StdEncoding.EncodeToString([]byte(plain))
	fmt.Printf("unwrapped encoding (%d chars): %s\n\n", len(enc), enc)

	try("no whitespace", enc)

	// MIME-style wrap every 60 chars with \n (what GitHub does)
	var wrapped strings.Builder
	for i := 0; i < len(enc); i += 60 {
		e := i + 60
		if e > len(enc) {
			e = len(enc)
		}
		wrapped.WriteString(enc[i:e])
		wrapped.WriteString("\n")
	}
	try("wrapped every 60 with \\n (GitHub style)", wrapped.String())

	crlf := strings.ReplaceAll(wrapped.String(), "\n", "\r\n")
	try("wrapped with \\r\\n", crlf)

	try("leading + trailing \\n", "\n"+enc+"\n")
	try("space in the middle", enc[:10]+" "+enc[10:])
	try("tab in the middle", enc[:10]+"\t"+enc[10:])
	try("vertical tab in the middle", enc[:10]+"\v"+enc[10:])
	try("form feed in the middle", enc[:10]+"\f"+enc[10:])
	try("NUL in the middle", enc[:10]+"\x00"+enc[10:])
	try("'-' (url-safe alphabet char)", enc[:10]+"-"+enc[10:])

	// RawStdEncoding (no padding) - what base64_raw_decode maps to
	rawEnc := base64.RawStdEncoding.EncodeToString([]byte(plain))
	b, err := base64.RawStdEncoding.DecodeString(strings.ReplaceAll(rawEnc, "", ""))
	_ = b
	fmt.Printf("\n%-46s err=%v\n", "RawStdEncoding no whitespace", err)
	var rw strings.Builder
	for i := 0; i < len(rawEnc); i += 60 {
		e := i + 60
		if e > len(rawEnc) {
			e = len(rawEnc)
		}
		rw.WriteString(rawEnc[i:e])
		rw.WriteString("\n")
	}
	_, err2 := base64.RawStdEncoding.DecodeString(rw.String())
	fmt.Printf("%-46s err=%v\n", "RawStdEncoding wrapped \\n", err2)
}
