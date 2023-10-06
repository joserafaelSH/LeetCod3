func mySqrt(x int) int {
    i := 0
	z := 1.0

	for i < 20 {
		z -= (z*z - float64(x)) / (2.0 * z)
		i++
	}

	return int(math.Floor(z))
}