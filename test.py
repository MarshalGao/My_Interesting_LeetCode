def test():    
    nums = [3,2,4]
    target = 6
    for i in nums:
        temp = nums[:nums.index(i):] + nums[nums.index(i)+1::]
        for j in temp:
            if i + j == target:
                print(list((nums.index(i), nums.index(j))))
                return

if __name__ == "__main__":
    test()