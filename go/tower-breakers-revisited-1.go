package main

import (
	"bufio"
	"os"
	"strings"
	"strconv"
	"fmt"
)

func sum(heights []int) int {
	sum := 0
	for i := range heights {
		sum += heights[i]
	}
	return sum
}

//Algo to solve the problem
func findWinner(n int, heights []int) {
	//fmt.Println(fmt.Sprintf("Checking data for n=%d and heights=%v",n,heights))
	//For all the inputs being same height 1, player 2 auto wins
	sumOfHeights := sum(heights)
	//fmt.Println(fmt.Sprintf("Sum of all heights is %d",sumOfHeights))
	if sumOfHeights == n {
		fmt.Println(2)
	} else {
		//odd sum makes player 2 win
		if sumOfHeights%2 == 0 && n%2 == 0 {
			fmt.Println(2)
		} else {
			fmt.Println(1)
		}
	}
}

func readInputStringToInt(reader *bufio.Reader) (int, error) {
	dataStr, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println(fmt.Sprintf("Error in reading data : %s", err.Error()))
	}
	dataInt, err := strconv.Atoi(strings.TrimSpace(dataStr))
	if err != nil {
		fmt.Println(fmt.Sprintf("Error in parsing data : %s", err.Error()))
	}
	return dataInt, nil
}
func readInputStrArrAsIntArr(reader *bufio.Reader) ([]int, error) {
	val, _ := reader.ReadString('\n')
	numArrStr := strings.Split(strings.TrimSpace(val), " ")
	h := make([]int, len(numArrStr))
	for k := range numArrStr {
		h[k], _ = strconv.Atoi(numArrStr[k])
	}
	return h, nil
}
func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	reader := bufio.NewReader(os.Stdin)
	t, _ := readInputStringToInt(reader)
	for i := 0; i < t; i++ {
		n, _ := readInputStringToInt(reader)

		findWinner(n, h)
	}
}
