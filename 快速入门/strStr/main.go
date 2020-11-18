package main

/**
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从 0 开始)。如果不存在，则返回 -1。
https://leetcode-cn.com/problems/implement-strstr/
 */

func strStr(haystack, needle string) int {
	if len(needle) == 0 {
		return 0
	}

	var i, j int
	for i = 0; i < len(haystack) - len(needle) + 1; i++ {
		for j = 0; j < len(needle); j++ {
			if haystack[i + j] != needle[j] {
				break
			}
		}
		if len(needle) == j {
			return i
		}
	}

	return -1
}


func main() {
	print(strStr("mississippi", "issip"))
}
