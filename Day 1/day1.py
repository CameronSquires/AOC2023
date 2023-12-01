with open('day1.txt') as filetoread:
    lines = filetoread.readlines()
    summ = 0
    for x in lines:
        nums = ''.join(y for y in x if y.isdigit())
        nums = nums[0] + nums[-1]
        summ += int(nums)
    print(summ)