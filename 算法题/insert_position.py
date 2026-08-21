class InsertPosition:
    def insert_position(self):
        nums = [1,3,5,7]
        target = 5
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return l

if __name__ == '__main__':
    result = InsertPosition().insert_position()
    print(result)