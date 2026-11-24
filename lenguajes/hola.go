// hola.go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("Hola desde Go", runtime.Version())
}