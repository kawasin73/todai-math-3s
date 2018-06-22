package main

import (
	"sort"
	"fmt"
)

type pair struct {
	i int
	a float64
	b float64
	v float64
}

type pairs []pair

func (p pairs) Len() int {
	return len(p)
}

func (p pairs) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p pairs) Less(i, j int) bool {
	return p[i].v > p[j].v
}

var queue = make([][]bool, 0)
var tmpMax float64
var tmpPair []bool

type Result struct {
	i int
	v int
}

type ResultList []Result

func (r ResultList) Len() int {
	return len(r)
}

func (r ResultList) Swap(i, j int) {
	r[i], r[j] = r[j], r[i]
}

func (r ResultList) Less(i, j int) bool {
	return r[i].i < r[j].i
}

func main() {
	a := []float64{4, 5, 12, 14} // maximize
	b := []float64{2, 3, 5, 6}   // strict
	var max float64 = 9

	list := make(pairs, 4)
	for i, _ := range list {
		list[i] = pair{
			i: i,
			a: a[i],
			b: b[i],
			v: (b[i] / a[i]),
		}
	}

	sort.Sort(list)

	tmpMax, tmpPair = ketiketi(list, max)
	queue = append(queue, []bool{})
	branchMethod(list, max)

	result := make(ResultList, len(list))
	for i, p := range list {
		result[i].i = p.i
		if tmpPair[i] {
			result[i].v = 1
		}
	}

	sort.Sort(result)

	fmt.Println("max :", tmpMax)
	fmt.Print("(")
	for _, r := range result {
		fmt.Print("x", r.i+1, ", ")
	}
	fmt.Print(") = (")
	for _, r := range result {
		fmt.Print(r.v, ", ")
	}
	fmt.Println(")")
}

func branchMethod(list pairs, max float64) {
	for (len(queue) > 0) {
		state := queue[0]
		queue = queue[1:]

		var sumA float64
		var sumB float64
		for i, b := range state {
			if b {
				sumA += list[i].a
				sumB += list[i].b
			}
		}
		result, ok, enable, resultList := mitigationMethod(list[len(state):], max, sumA, sumB)
		if !ok {
			continue
		}
		if enable {
			if result > tmpMax {
				tmpMax = result
				tmpPair = append(state, resultList...)
			}
			continue
		}
		queue = append(queue, append(state, true), append(state, false))
	}
}

func mitigationMethod(list pairs, max float64, sumA, sumB float64) (result float64, ok bool, enable bool, resultList []bool) {
	if sumB > max {
		return sumA, false, false, nil
	}
	resultList = make([]bool, len(list))
	for i, p := range list {
		if sumB == max {
			return sumA, true, true, resultList
		} else if sumB+p.b > max {
			return sumA + (max - sumB/p.b), true, false, resultList
		} else {
			sumA += p.a
			sumB += p.b
			resultList[i] = true
		}
	}
	return sumA, true, true, resultList
}

func ketiketi(list pairs, max float64) (float64, []bool) {
	var sumA float64
	var sumB float64

	result := make([]bool, len(list))
	for i, p := range list {
		sumA += p.a
		sumB += p.b
		result[i] = true
	}
	for i := len(list) - 1; i > 0; i-- {
		if sumB <= max {
			break
		}
		sumB -= list[i].b
		sumA -= list[i].a
		result[i] = false
	}
	return sumA, result
}

func yokubari(list pairs, max float64) float64 {
	var sumA float64
	var sumB float64
	for _, p := range list {
		if sumB+p.b > max {
			continue
		}
		sumB += p.b
		sumA += p.a
	}
	return sumA
}
