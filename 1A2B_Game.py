import random

def gennum():
    pos_num = []
    count_Samenum = 0

    for i in range(10000):
    # for i in range(10000,0,-1):
        num_str = "{:04d}".format(i) 

        for j in range(4):
            count_Samenum = num_str.count(num_str[j])
            if count_Samenum > 1:
                check = 1
                break

        if check == 0:
            # print(num_str)
            pos_num.append(num_str)

        check = 0

    return pos_num

def checkAB(frompos_Num, guess_Num):
    A,B=0,0
    for i in range(4):
        for j in range(4):
            if frompos_Num[i] == guess_Num[j]: 
                if i==j: A+=1
                else: B+=1
    return A,B

def get_random_number():
    random_num = ""
    rannum = random.sample(range(10),4)
    for i in rannum:
        random_num += str(i)
    
    return random_num


def play():
    pos_num = list(set(gennum()))
    # pos_num = gennum()
    round = 1
    round_for_player = 0

    # when you use to play by itself or play together
    random_num = get_random_number()

    while True:
        guess_num = pos_num[0]

        if(round == 1):
            print("\nI guess! it's {}".format(guess_num))
        else: 
            print("\nFrom the hints {}A{}B I guess! it's {} {}".format(A, B, guess_num,len(pos_num)))   
        A = int(input("Can you give me a hint A: "))
        B = int(input("Can you give me a hint B: "))

        #//////////////////////////////////////////////////////////////////////////////////////////////////
        #player zone
        Ans = str(input('Your Guess: '))
        A_from_player,B_from_player=0,0 # Collect A and B data
        if len(Ans) != 4: # Alarm when you don't enter the 4 digit
            print("You need to type 4 num!!")
            continue
        else: 
            for i in range(4):
                for j in range(4):
                    if Ans[i] == random_num[j]: # Checker answer function that tell you get how many A and B
                        if i==j: A_from_player+=1
                        else: B_from_player+=1
            round_for_player +=1 # Count round
            
            if A == 4:
                print("I'm win! \nI'm use ",round," Round\nGreat job!")
                break # When you get 4A  that is you win so we will break the loop
            else: print("A: {} B: {}".format(A,B))
        #//////////////////////////////////////////////////////////////////////////////////////////////////

        # when you use to play by itself
        # A,B = checkAB(guess_num, random_num)

        if(A == 4):
            print("OHH! you win. you use only {} round".format(round))
            break

        pos_num = [num for num in pos_num if checkAB(num, guess_num) == (A, B)]
        round+=1
    return round

def main():
    play()

    # for x in range(10):
    #     round_use = [0,0,0,0,0,0,0,0,0,0]
    #     count = 0
    #     for i in range(1000):
    #         data = play()
    #         # count+=1
    #         round_use[data] += 1
    #         # print(count)
    #     print(round_use)

        
main()

'''
Test algo
# for n in pos_num:
#     A, B = checkAB(n,"1234")
#     if(A==1 and B==2):
#         print(n ," ", A," ",B)
#         count += 1
# print(count)
'''



