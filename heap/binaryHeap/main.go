package main

import (
	"fmt"
	"log"
	"math/rand"
	"sort"
	"time"
)

type binHeap struct {
	value     int
	leftNode  *binHeap
	rightNode *binHeap
}

type ByInt []int

func (a ByInt) Len() int           { return len(a) }
func (a ByInt) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByInt) Less(i, j int) bool { return a[i] < a[j] }

func main() {
	rand.Seed(time.Now().UTC().UnixNano())

	ih := GenRandIntSlice()
	ih = BuildMaxHeap(ih)
	start := time.Now()
	HeapSort(ih)
	r := ByInt(ih)
	elapsed := time.Since(start)
	log.Printf("Heap Sort took %s", elapsed)
	fmt.Println("sorted ?", sort.IsSorted(r))
}

func GenRandIntSlice() []int {
	var result []int
	for i := 0; i < 100000; i++ {
		result = append(result, rand.Intn(100000))
	}
	return result
}

func BuildMaxHeap(in []int) []int {
	heap := []int{}
	for _, value := range in {
		// insert a new node at the bottom
		heap = append(heap, value)
		// do heapify to make the new node to right position
		heap = MaxHeapifyBottomUp(heap)
	}

	return heap
}

func MaxHeapifyBottomUp(in []int) []int {
	// the index of new node, the latest one element in slice
	newELeIndex := len(in) - 1
	for {
		// get the parent node index
		parentIndex := (newELeIndex+1)/2 - 1
		// break if the node is to the top of heap
		if parentIndex < 0 {
			break
		}
		// if parent node < the new node, swap
		if in[newELeIndex] > in[parentIndex] {
			in[parentIndex], in[newELeIndex] = in[newELeIndex], in[parentIndex]
			newELeIndex = parentIndex
		} else {
			// if not, break here
			break
		}
	}
	return in
}

func MaxHeapifyTopDown(currLastNode int, in []int) {
	currEleIndex := 0
	for {
		child := 2*currEleIndex + 1
		// check left child is out of the bound or not
		if child > currLastNode {
			break
		}
		// check right child is out of the bound or not
		// and if right child > left child, shoose right child
		if child+1 <= currLastNode && in[child] < in[child+1] {
			child++
		}
		// if current root > both right and left child, just return
		if in[child] < in[currEleIndex] {
			return
		}
		// if root < the largest child
		// swap root with the largest child
		in[currEleIndex], in[child] = in[child], in[currEleIndex]
		// keep going to next sub-heap
		currEleIndex = child
	}
}

func HeapSort(in []int) {
	var currLastNode = len(in) - 1
	for {
		if currLastNode <= 0 {
			break
		}
		if currLastNode > 0 {
			// take the final element to the root and do heapify
			in[0], in[currLastNode] = in[currLastNode], in[0]
			currLastNode--
			MaxHeapifyTopDown(currLastNode, in)
		}
	}
}
