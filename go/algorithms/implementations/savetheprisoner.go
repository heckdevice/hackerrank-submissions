package main

import (
	"fmt"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var testCases, noOfPrisoners, noOfCandies, startId int
	if _, err := fmt.Scan(&testCases); err != nil {
		fmt.Println("Error in reading input", err)
		return
	}
	for i := 0; i < testCases; i++ {
		if _, err := fmt.Scan(&noOfPrisoners, &noOfCandies, &startId); err != nil {
			fmt.Println("Error in reading input", err)
			return
		}
		//cause startId is inclusive in the count
		startId = startId - 1
		//Count till the last but one candy
		noOfCandies = noOfCandies - 1
		//the basic math !!!
		pos := startId + noOfCandies
		//since we loop when we reach the last prisoner
		//+1 gives the one to be saved
		pos = pos % noOfPrisoners + 1
		fmt.Println(pos)
	}
}