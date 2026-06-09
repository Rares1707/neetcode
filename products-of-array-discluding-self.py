class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * (len(nums))
        for i in range(1, len(nums)):  # first element has prefix_product 1
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        postfix_product = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):  # last element has postfix_product 1
            postfix_product[i] = postfix_product[i + 1] * nums[i + 1]

        output = [prefix_product[i] * postfix_product[i] for i in range(0, len(nums))]
        return output
