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
        blue_low, red_low, green_low = 0,0,0
        if game_id == "100":
            x[-1] += ";"
        while (len(x) > 1):
            
            

            num=x[1]
            colour = x[2]
            
            if "blue" in colour:
                bluesum += int(num)
            elif "green" in colour:
                greensum += int(num)
            elif "red" in colour:
                redsum += int(num)
            if ";" in colour or "\n" in colour:
                if blue_low == 0 or bluesum > blue_low:
                    blue_low = bluesum
                if green_low == 0 or greensum > green_low:
                    green_low = greensum
                if red_low == 0 or redsum > red_low:
                    red_low = redsum

                bluesum, redsum, greensum = 0, 0, 0    
                
            x.pop(1)
            x.pop(1)
        print(game_id)
        print(red_low,green_low,blue_low)
        sum += green_low * red_low * blue_low

            

        
    print(sum)

            