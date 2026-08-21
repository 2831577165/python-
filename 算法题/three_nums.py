class ThreeNums:
    def three_nums(self):
        nums = [-1,0,1,-7,2,5,6,8,4,-3]
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l , r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
        return ans

if __name__ == '__main__':
    print(ThreeNums().three_nums())