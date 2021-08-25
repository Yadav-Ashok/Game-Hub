import tkinter
# Setup

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")

# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a lion.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
def Left():
        if response == "left":
            print("Lion is near you " + name + ".")


        #def left_part_layer1():
            # 1 Layer
            option1 = ('1.Act like Die')
            option2 = ('2.Climb on Tree')
            option3 = ('3.Try to Es-Cape From Lion')
            option4 = ('4.Lost The Hope')
            print(option1)
            print(option2)
            print(option3)
            print(option4)
            a = input('Enter Your Choice')
            if (a == '2'):
                print('lion Eats You Game--Over')
                quit()
            if (a == '3'):
                print('Lion Cached You Game--Over')
                quit()
            if (a == '4'):
                print('You Are Backwader Game--Over')
                quit()
            if (a == '1'):
                print('Welcome to Next Level')
                print('******* Next Level *******', '\n')

            # left_part_Layer1()


        #def left_part_layer2():
            # 2 Layer
            option1 = ('1.Wait For Lion To Go')
            option2 = ('2.Disturb Lion')
            option3 = ('3.Try to kill lion')
            option4 = ('4.Shout for Help')
            print(option1)
            print(option2)
            print(option3)
            print(option4)
            b = input('Enter Next Level  Choice')
            if (b == '1'):
                print('Lion Kill You Because you Cannot Hold Your Breath Game--Over')
                quit()
            if (b == '2'):
                print('You Fail To Disturb Lion Game--Over')
                quit()
            if (b == '4'):
                print('Idea Does Not Worked Game--Over')
                quit()
            if (b == '3'):
                print('Welcome To Next Level')
                print('******* Next Level *******', '\n')

            # left_part_layer2()


        #def left_part_layer3():
            # 3 Layer
            option1 = ('1.Hit on Face')
            option2 = ('2.Through Dust on Face')
            option3 = ('3.Face To Face Fight')
            option4 = ('4.Let Lion Eat you')
            print(option1)
            print(option2)
            print(option3)
            print(option4)
            c = input('Enter Next Level  Choice')
            if (c == '1'):
                print('Lion Hited on Yor Face and Killed You Game--Over')
                quit()
            if (c == '4'):
                print('You Are A Backwader  Game--Over')
                quit()
            if (c == '2'):
                print(' You Through Dust on Face Lion But You Failed and Lion Killed You Game--Over')
                quit()

            if (c == '3'):
                print('Welcome To Next Level')
                print('******* Next Level *******', '\n')



        #def left_part_layer4():
            # 4 Layer
            option1 = ('1.Cache Neck Of Lion')
            option2 = ('2.Rore Like Lion')
            option3 = ('3.Cache Mouth of Lion')
            option4 = ('4.Lost The Hope')
            print(option1)
            print(option2)
            print(option3)
            print(option4)
            d = input('Enter Next Level  Choice')
            if (d == '2'):
                print('Failed To Be Safe From Lion Game--Over')
                quit()
            if (d == '3'):
                print('Lion Caches You And Killed you Game--Over')
                quit()
            if (d == '4'):
                print('You Are A Bacwared')
                quit()
            if (d == '1'):
                print('Welcome to Next Level')
            print('******* Next Level *******', '\n')


        #def left_part_layer5():
            print('Island Mystry !!!')
            option1 = ('1.Step Behind Due To Fear')
            option2 = ('2.Stay There ')
            option3 = ('3.Step Ahead Into Island')
            option4 = ('4.Lost The Hope And Find For Help')
            print(option1)
            print(option2)
            print(option3)
            print(option4)
            f = input('Enter Next Level Island Mystry Choice')
            if (f == '1'):
                print('You Steped Backward You are Backwarder Game--Over')
                quit()
            if (f == '2'):
                print('You Stayed There  Game--Over')
                quit()
            if (f == '3'):

                print('******* Next Level Of Island Mystry *******', '\n')
            if (f == '4'):
                print('Losted Hope Game--Over');
                quit()

            print('Wonderful Well Played ')
            option1 = ('1. You Liked This Game ')
            option2 = ('2. Should I Implement More In Adventure--Game')
            option3 = ('3. Want To Give  *  * ')
            option4 = ('4. Want To Give *  *  *  * ')
            option5 = ('5. You Dont Like This Game')
            print(option1)
            print(option2)
            print(option3)
            print(option4)
            print(option5)
            m = input('Enter You Faith And True Choice')
            if (m == '1'):
                print('Thank You For You Feedback')
                print('Thank For Playing Adventure--Game')
            if (m == '2'):
                print('Thank You For You Feedback')
                print('Thank For Playing Adventure--Game')
            if (m == '3'):
                print('Thank You For You Feedback')
                print('Thank For Playing Adventure--Game')
            if (m == '4'):
                print('Thank You For You Feedback')
                print('Thank For Playing Adventure--Game')
            if (m == '5'):
                print('Really Sorry I Will Implement This Game')
                print('Thank For Playing Adventure--Game')





#left_part_layer1()
    #left_part_layer2()
    #left_part_layer3()
    #left_part_layer4()
    #left_part_layer5()

Left()

# /////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////
def Right():
    if response == "right":
        print("You head deeper into the forest," + name + ".")


#def right_part_Layer1():
    # Layer 1
    print('Welcome To Adventure-Game')
    option1 = ('1.Step Backward')
    option2 = ('2.Step By Step Climb On Trees By Hiding  ')
    option3 = ('3.Go Deep In The Forest')
    option4 = ('4.Lost The Hope And Find For Help')
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    p = input('Enter Choice')
    if (p == '3'):
        print('Welcome to Next Level')
        print('******* Next Level *******', '\n')

    if (p == '4'):
        print('You Lost Your Hope Game--Over ')
        quit()
    if (p == '2'):
        print('Welcome To Next Level')
        print('******* Next Level *******', '\n')
    if (p == '1'):
        print('You Steped Backward, You Are Backwader')
        quit()


#def right_part_Layer2():
    print('Snake Ahead')
    option1 = ('1.kill The Snake')
    option2 = ('2.Run From Snake To Save Life ')
    option3 = ('3.Go To Safe Place Like Cave Of Lion')
    option4 = ('4.Lost The Hope Due To Fear Of Snake')
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    q = input('Enter Next Level Choice')
    if (q == '2'):
        print('Welcome To Next Level')
        print('******* Next Level *******', '\n')

    if (q=='1'):
        print('Snake Bits You Game--Over')
        quit()
    if (q=='4'):
        print('You Losted Your Hope Game--Over')
        quit()

    if(q=='3'):
        print('Lion Eats You Game--Over')
        quit()




#def right_part_Layer3():
    print('Well Level')
    option1 = ('1.Jump in Well')
    option2 = ('2.Sit There Due To Fear Of Death ')
    option3 = ('3.Go Back To Forest')
    option4 = ('4.Pray For God To Help You And Sit There')
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    c = input('Enter Next Level Choice')
    if (c == '1'):
        print('Welcome To The Next Level')
        print('******* Next Level *******', '\n')
    if (c == '2'):
        print('You Sited There Losted Hope Game--Over')
        quit()
    if (c == '3'):
        print('In-Forest You Got-stuck Game--Over ')
        quit()
    if (c == '4'):
        print('You didnot Got Any Help Game--Over')
        quit()


#def right_part_Layer4():
    print('Secreate Island')
    option1 = ('1.Go Ahead To Explore Secrate Path')
    option2 = ('2.Due To Fear Stay At Well')
    option3 = ('3.Step Back Due To Fear Of Secreate Path ')
    option4 = ('4.Stay At well Life long')
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    d = input('Enter Next Level Choice')
    if (d == '1'):
        print('Welcome To Next Level')
        print('******* Next Level *******', '\n')
    if (d == '2'):
        print('You Died At Well Game--Over')
        quit()
    if (d == '3'):
        print('You Step back And Got Stuck At Well')
        quit()
    if (d == '4'):
        print('Game--Over')

    print('Wonderful Well Player ')
    option1 = ('1.Did You Liked This Game ')
    option2 = ('2.Should I Implement More In Adventure--Game')
    option3 = ('3.Want To Give  *  * ')
    option4 = ('4.Want To Give  *  *  *  * ')
    option5 = ('5.You Dont Like This Game')
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    print(option5)
    z = input('Enter You Faith And True Choice')
    if (z == '1'):
        print('Thank You For You Feedback')
    if (z == '2'):
        print('Thank You For You Feedback')
    if (z == '3'):
        print('Thank You For You Feedback')
    if (z == '4'):
        print('Thank You For You Feedback')
    if (z == '5'):
        print('Really Sorry I Will Implement This Game'+ name +'')
        quit()

    #right_part_Layer1()
    #right_part_Layer2()
    #right_part_Layer3()
    #right_part_Layer4()
    #Last_Teaser_right()
        Right()


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def Forward():
    if response == "forward":
        print("Rock Big Wall In Front Of You," + name + ".")


        print('Welcome To Adventure-Game')
        option1 = ('1.Climb The Wall')
        option2 = ('2.Break The Wall')
        option3 = ('3.Lost The Hope')
        option4 = ('4.Tossing Head To Wall And Die')
        print(option1)
        print(option2)
        print(option3)
        print(option4)
        a = input('Enter Level Choice')
        if (a == '1'):
            print('Welcome To Next Level')
            print('******* Next Level *******', '\n')
        if (a == '2'):
            print('You Failed To Break The Wall Game--Over')
            quit()
        if (a == '3'):
            print('You Are Backwader')
            quit()
        if (a == '4'):
            print('You Died Game--Over')
            quit()




        print('River Ahead')
        option1 = ('1.Jump in The River')
        option2 = ('2.Wait For Boat')
        option3 = ('3.Shout For Help ')
        option4 = ('4.Step Back At Rock Wall')
        print(option1)
        print(option2)
        print(option3)
        print(option4)
        b = input('Enter Next Level Choice')
        if (b == '1'):
            print('Welcome To Next Level')
            print('******* Next Level *******', '\n')
        if (b == '2'):
            print('You does not Got Boat In River And Game--Over')
            quit()
        if(b == '3'):
            print('Game--Over')
            quit()
        if (b == '4'):
            print('Snake Bits You And You Died Game--Over')
            quit()



        print('Aligator Ahead')
        option1 = ('1.Step Back')
        option2 = ('2.Fight With Aligator')
        option3 = ('3.Shout For Help ')
        option4 = ('4.Run Due To Fear Of Aligator')
        print(option1)
        print(option2)
        print(option3)
        print(option4)
        c = input('Enter Next Level Choice')
        if (c == '1'):
            print('Aligator Eats You ')
            quit()
        if (c == '2'):
            print('You Escape From Aligator')
            print('******* Next Level *******', '\n')
        if (c == '3'):
            print('Game--Over')
            quit()
        if (c == '4'):
            print('Aligator Caches You And  Game--Over')
            quit()



        print('Mystry Of Island')
        option1 = ('1.Step Back')
        option2 = ('2.Due To Fear Of Black Spot Stay There')
        option3 = ('3.Find Another Way From River ')
        option4 = ('4.Go Ahead In Island')
        print(option1)
        print(option2)
        print(option3)
        print(option4)
        d = input('Enter Next Level Choice')
        if (d == '1'):
            print('You Steped Back Game--Over')
            quit()
        if (d == '2'):
            print('Due To Fear You Step back')
            quit()
        if (d == '3'):
            print('No Another Way Found')
            quit()
        if (d == '4'):
            print('Welcome To Next level')
            print('******* Next Level *******', '\n')

        print('Wonderful Well Player ')
        option1 = ('1.Did You Liked This Game ')
        option2 = ('2.Should I Implement More In Adventure--Game')
        option3=  ('3.Want To Give * * ')
        option4=  ('4.Want To Give * *,*,*')
        option5=  ('5.You Dont Like This Game')
        print(option1)
        print(option2)
        print(option3)
        print(option4)
        print(option5)
        A=input('Enter You Faith And True Choice')
        if(A=='1'):
            print()
        if (A == '2'):
            print('Thank You For You Feedback')
        if (A == '3'):
            print('Thank You For You Feedback')
        if (A == '4'):
            print('Thank You For You Feedback')
        if (A == '5'):
            print('Really Sorry I Will Implement This Game'+ name +'')

Forward()
def Backward():
    if response == "backward":
        print("You Are A BACKWADER!!, " + name + ".")
    quit()
    Backward()