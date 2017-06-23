package main
import (
	"fmt"
	"bufio"
	"strings"
	"sort"
	"strconv"
	"os"
)
func readInputStringToInt(reader *bufio.Reader)(int,error){
	dataStr,err:=reader.ReadString('\n')
	if err!=nil{
		fmt.Println(fmt.Sprintf("Error in reading data : %s",err.Error()))
	}
	dataInt,err:=strconv.Atoi(strings.TrimSpace(dataStr))
	if err!=nil{
		fmt.Println(fmt.Sprintf("Error in parsing data : %s",err.Error()))
	}
	return dataInt,nil
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
func abs(data int) int{
	if data<0 {
		return -data
	}else{
		return data
	}
}
func findAbsMinimum(n int,numArr []int){
	//first sort the array
	sort.Ints(numArr)
	if n==1 {
		fmt.Println(numArr[0])
		return
	}
	absMin:=abs(numArr[0]-numArr[1])
	for i:=1;i<n-1;i++{
		curDif:=abs(numArr[i]-numArr[i+1])
		if(curDif<absMin){
			absMin=curDif
		}
		//fmt.Println(fmt.Sprintf("curDif=%d,absMin=%d",curDif,absMin))
	}
	fmt.Println(absMin)
}
func main() {
	reader := bufio.NewReader(os.Stdin)
	n,_ :=readInputStringToInt(reader)
	numArr,_:=readInputStrArrAsIntArr(reader)
	findAbsMinimum(n,numArr)
}