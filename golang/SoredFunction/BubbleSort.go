package SoredFunction

func BubbleSort(nums []int) []int {
	for i := 0; i < len(nums) - 1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[j] < nums[i] {
				nums[j], nums[i] = nums[i], nums[j]
			}
		}
	}
	return nums
}