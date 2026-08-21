class tow_number:
    def tow_num(self):
        nums = [1,2,11,4,5,6,7,8,9,10]
        targit = 8
        d1 = dict()
        for i in range(len(nums)):
            if targit - nums[i] in d1:
                return [d1[targit - nums[i]],i]
            d1[nums[i]] = i
        return [d1[targit - nums[i]],i]

if __name__ == '__main__':
    result = tow_number().tow_num()
    print(result)