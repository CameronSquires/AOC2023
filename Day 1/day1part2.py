with open('day1.txt') as filetoread:
    lines = filetoread.readlines()
    summ = 0
    for x in lines:
        x = x.replace('one', 'o 1 e')
        x = x.replace('two', 't 2 o')
        x = x.replace('three', 't 3 e')
        x = x.replace('four', '4')
        x = x.replace('five', '5 e')
        x = x.replace('six', 's 6')
        x = x.replace('seven', '7 n')
        x = x.replace('eight', 'e 8 t')
        x = x.replace('nine', 'n 9 e')
        #since excess characters will be removed regardless, I kept all possible overlapping letters which could be used for a digit. for example: nineight would be '9 8' instead of 'nin8'
        nums = ''.join(y for y in x if y.isdigit())
        nums = nums[0] + nums[-1]
        summ += int(nums)
    print(summ)