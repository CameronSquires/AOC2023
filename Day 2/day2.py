with open('day2.txt') as filetoread:
    lines = filetoread.readlines()
    sum = 0
    
    for x in lines:
        x=x.split(" ")
        x.pop(0)
        bluesum = 0
        redsum = 0
        greensum = 0
        game_id = ''.join(y for y in x[0] if y.isdigit())
        possible = True
        while (len(x) > 1):
            

            num=x[1]
            colour = x[2]
            #print(x)
            if "blue" in colour:
                bluesum += int(num)
            elif "green" in colour:
                greensum += int(num)
            elif "red" in colour:
                redsum += int(num)
            if ";" in colour:
                if bluesum > 14 or redsum > 12 or greensum > 13:
                    possible = False
                bluesum, redsum, greensum = 0, 0, 0
            x.pop(1)
            x.pop(1)
        if bluesum > 14 or redsum > 12 or greensum > 13:
                    possible = False

            

        if possible:
            sum += int(game_id)
        
    print(sum)

            