class Delete:
    def delete(self):
        nums = [0,0,1,2,2,2,3,4,5,5,6,6,6]
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l+1


if __name__ == '__main__':
    result = Delete().delete()
    print(result)