package main

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func increasingBST(root *TreeNode) *TreeNode {
	var left *TreeNode
	var result *TreeNode = root
	if root.Left != nil {
		left = increasingBST(root.Left)

		if left != nil {
			var last **TreeNode = &left
			for (*last).Right != nil {
				last = &(*last).Right
			}
			(*last).Right = root
		}
		result = left
	}

	var right *TreeNode
	if root.Right != nil {
		right = increasingBST(root.Right)
		if right != nil {
			root.Right = right
		}
	}
	return result
}
