from tkinter import *

import tkinter as tk
from tkinter import simpledialog

# Setup
Yes_No = ["Yes", "No"]
directions = ["Left", "Right", "Forward", "Backward"]

# Introduction
name = input("What is Your Name?\n")
Adventure = input("What is your Adventurer?\n")
print("Greetings, " + name + ". Let us go on a Quest!")
print("You Find YourSelf on the Edge of a Dark Forest.")
print("Can You Find Your Way Through?\n")

# Start of game
response = ""
while response not in Yes_No:
    response = input("Would You Like To Step Into The Forest?\tYes/No\t")
    if response == "Yes":
        print("You Head Into The Forest. You Hear Crows Cawwing in the Distance.\n")
    elif response == "No":
        print("You Are Not Ready For This Quest. Goodbye, " + name + ".")
        quit()
    else:
        print("I Didn't Understand That,\n Please Input Proper Information\n")

# Next part of game
response = ""
while response not in directions:
    print("To Your Left, You See A Lion.")
    print("To Your Right, There is More Forest.")
    print("There Is A Rock Wall Directly In Front Of You.")
    print("Behind you is the Forest exit.\n")
    response = input("What Direction Do You Want To Move?\nLeft/Right/Forward/Backward\n")


def Left():
        if response == "Left":
            # LEFT PART ADVENTURE--GAME
            print("Lion is near you " + name + ".")
            # First Layer Left Part
            option1 = ('1.Act like Die')
            option2 = ('2.Climb on Tree')
            option3 = ('3.Try to Es-Cape From Lion')
            option4 = ('4.Lost The Hope')

            master = Tk()
            var = IntVar()
            var.set(0)

            def quit_loop():
                print("Selection:", var.get())
                global selection
                selection = var.get()
                master.quit()

            Label(master, text="Lion is Near You "+ name + ".").grid(row=0, sticky=W)
            Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
            Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
            Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
            Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
            Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

            master.mainloop()

            if selection == 2:
                Label(master, text='lion Eats You Game--Over').grid(row=8, sticky=W)

            if selection == 1:
                Label(master, text='Welcome To Next Level').grid(sticky=W)
                Label(master, text='******* Next Level *******').grid(sticky=W)

            if selection == 3:
                Label(master, text='Lion Cached You Game--Over').grid(row=9, sticky=W)

            if selection == 4:
                Label(master, text='You Are Backwader Game--Over ').grid(row=10, sticky=W)
            master.mainloop()

            # Second Layer Left Part

            option1 = ('1.Wait For Lion To Go')
            option2 = ('2.Disturb Lion')
            option3 = ('3.Try to kill lion')
            option4 = ('4.Shout for Help')

            master = Tk()
            var = IntVar()
            var.set(0)

            def quit_loop():
                print("Selection:", var.get())
                global selection
                selection = var.get()
                master.quit()

            Label(master, text="Welcome To Next LeveL Adventure-Game" + name + ".").grid(row=0, sticky=W)
            Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
            Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
            Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
            Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
            Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

            master.mainloop()

            if selection == 3:
                Label(master, text='Welcome To Next Level').grid(sticky=W)
                Label(master, text='******* Next Level *******').grid(sticky=W)
            if selection == 1:
                Label(master, text='Failed To Be Safe From Lion Game--Over').grid(row=8, sticky=W)

            if selection == 2:
                Label(master, text='Lion kills You').grid(row=9, sticky=W)

            if selection == 4:
                Label(master, text='You Are A Bacwared').grid(row=10, sticky=W)

            master.mainloop()
            # Third Layer Left Part
            option1 = ('1.Hit on Face')
            option2 = ('2.Through Dust on Face')
            option3 = ('3.Face To Face Fight')
            option4 = ('4.Let Lion Eat you')

            master = Tk()
            var = IntVar()
            var.set(0)

            def quit_loop():
                print("Selection:", var.get())
                global selection
                selection = var.get()
                master.quit()

            Label(master, text="Welcome To  Next LeveL of Adventure-Game"+ name + ".").grid(row=0, sticky=W)
            Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
            Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
            Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
            Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
            Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

            master.mainloop()
            if selection == 3:
                Label(master, text='Welcome To Next Level').grid(sticky=W)
                Label(master, text='******* Next Level *******').grid(sticky=W)
            if selection == 2:
                Label(master, text='Failed To Throw Dust on Lion And Game--Over').grid(row=8, sticky=W)

            if selection == 1:
                Label(master, text='Lion Caches You And Killed you Game--Over').grid(row=9, sticky=W)

            if selection == 4:
                Label(master, text='You Are A Bacwared').grid(row=10, sticky=W)

            master.mainloop()
            # Fourth Layer Left Part
            option1 = ('1.Cache Neck Of Lion')
            option2 = ('2.Rore Like Lion')
            option3 = ('3.Cache Mouth of Lion')
            option4 = ('4.Lost The Hope')

            master = Tk()
            var = IntVar()
            var.set(0)

            def quit_loop():
                print("Selection:", var.get())
                global selection
                selection = var.get()
                master.quit()

            Label(master, text="Welcome To Next LeveL Of Adventure-Game" + name + ".").grid(row=0, sticky=W)
            Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
            Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
            Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
            Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
            Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

            master.mainloop()
            if selection == 1:
                Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
                Label(master, text='******* Next Level *******').grid(row=7, sticky=W)
            if selection == 2:
                Label(master, text='Failed To Be Safe From Lion Game--Over').grid(row=8, sticky=W)

            if selection == 3:
                Label(master, text='Lion Caches You And Killed you Game--Over').grid(row=9, sticky=W)

            if selection == 4:
                Label(master, text='You Are A Bacwared').grid(row=10, sticky=W)

            master.mainloop()
            print('Island Mystry !!!')
            # Fifth Layer Left Part
            option1 = ('1.Step Behind Due To Fear')
            option2 = ('2.Stay There ')
            option3 = ('3.Step Ahead Into Island')
            option4 = ('4.Lost The Hope And Find For Help')

            master = Tk()
            var = IntVar()
            var.set(0)

            def quit_loop():
                print("Selection:", var.get())
                global selection
                selection = var.get()
                master.quit()

            Label(master, text="Welcome To Adventure-Game"+ name + ".").grid(row=0, sticky=W)
            Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
            Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
            Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
            Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
            Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

            master.mainloop()
            if selection == 3:
                Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
                Label(master, text='******* Next Level *******').grid(row=7, sticky=W)
            if selection == 1:
                Label(master, text='You Steped Backward You are Backwarder Game--Over').grid(row=8, sticky=W)

            if selection == 2:
                Label(master, text='You Stayed There  Game--Over').grid(row=8, sticky=W)

            if selection == 4:
                Label(master, text='Losted Hope Game--Over').grid(row=10, sticky=W)

            master.mainloop()



            option1 = ('1.Did You Liked This Game ')
            option2 = ('2.Should I Implement More In Adventure--Game')
            option3 = ('3.Want To Give * * ')
            option4 = ('4.Want To Give Some Comments')
            option5 = ('5.You Dont Like This Game')

            master = Tk()
            var = IntVar()
            var.set(1)
            var.set(2)
            var.set(3)
            var.set(4)
            var.set(5)

            def quit_loop():
                print("Selection: work", var.get())
                global selection
                selection = var.get()
                master.quit()

            Label(master, text="Welcome To Adventure-Game" + name + ".").grid(row=0, sticky=W)
            Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
            Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
            Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
            Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
            Radiobutton(master, text=option5, variable=var, value=5).grid(row=5, sticky=W)
            Button(master, text="Submit", command=quit_loop).grid(row=6, sticky=W)

            master.mainloop()
            if selection == 1:
                Label(master, text='Thank You For You Feedback'+ name + ".").grid(row=7, sticky=W)

            if selection == 2:
                Label(master, text='Thank You For You Feedback'+ name + "." ).grid(row=8, sticky=W)

            if selection == 3:
                Label(master, text='Thank You For You Feedback'+ name + "." ).grid(row=9, sticky=W)
            if selection == 5:
                Label(master, text='Sorry For That Next Time I Will Implement More '+ name + ".").grid(row=10, sticky=W)


            if selection == 4:


                application_window = tk.Tk()

            answer = simpledialog.askstring("Input", "What is your  Name?",
                                            parent=application_window)
            if answer is not None:
                print("Your Name is ", answer)

            else:
                 print("Please Enter Name?")

            answer = simpledialog.askstring("Input", "Enter Your Comment",
                                            parent=application_window)

            if answer is not None:
                print("Your Comment is  ", answer)
            else:
                print("No Comment Written?")

            answer = simpledialog.askstring("Input", "How Many Star You Want To Add?",
                                            parent=application_window, )

            if answer is not None:
                print("You Have Entered  ", answer)
            else:
                print("You Didnt Added Stars?")

            master.mainloop()

            master.mainloop()

            master.mainloop()

            master.mainloop()
            master.mainloop()


Left()


from tkinter import *


def Right():
    if response == "Right":
        print("You head deeper into the forest," + name + ".")
        # Right PART ADVENTURE--GAME
        master = Tk()
        var = IntVar()
        var.set(0)

        def quit_loop():
            print("Selection:", var.get())
            global selections
            selections = var.get()
            master.quit()
            # First Layer Of Right Part

        option1 = ('1.Step Backward')
        option2 = ('2.Step By Step Climb On Trees By Hiding  ')
        option3 = ('3.Go Deep In The Forest')
        option4 = ('4.Lost The Hope And Find For Help')
        Label(master, text="Welcome To Adventure-Game").grid(row=0, sticky=W)
        Label(master, text="You head deeper into the forest" + name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

        master.mainloop()
        if selections == 3:
            Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
            Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

        if selections == 1:
            Label(master, text='You Steped Backward You are Backwarder Game--Over').grid(row=8, sticky=W)
            quit_loop()

        if selections == 2:
            Label(master, text='You Failed To Climb On Trees And Game--Over').grid(row=9, sticky=W)

        if selections == 4:
            Label(master, text='Losted Hope Failed To Receive Help').grid(row=10, sticky=W)

        master.mainloop()
        # second Layer
        master = Tk()
        var = IntVar()
        var.set(0)

        def quit_loop():
            print("Selection:", var.get())
            global selections
            selections = var.get()
            master.quit()
            # Second Layer Of Right Part

        option1 = ('1.kill The Snake')
        option2 = ('2.Run From Snake To Save Life ')
        option3 = ('3.Go To Safe Place Like Cave Of Lion')
        option4 = ('4.Lost The Hope Due To Fear Of Snake')
        Label(master, text='Snake Ahead'+ name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

        master.mainloop()
        if selections == 2:
            Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
            Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

        if selections == 1:
            Label(master, text='You Failed To Kill Snake And Game--Over').grid(row=8, sticky=W)

        if selections == 3:
            Label(master, text='Lion Kills You And Game--Over').grid(row=9, sticky=W)

        if selections == 4:
            Label(master, text=' You Losted Hope Due To Fear Of Snake ').grid(row=10, sticky=W)

        master.mainloop()
        master = Tk()
        var = IntVar()
        var.set(0)

        def quit_loop():
            print("Selection:", var.get())
            global selections
            selections = var.get()
            master.quit()
            # Third Layer Of Right Part
    option1 = ('1.Jump in Well')
    option2 = ('2.Sit There Due To Fear Of Death ')
    option3 = ('3.Go Back To Forest')
    option4 = ('4.Pray For God To Help You And Sit There')
    Label(master, text='Well Ahead' + name + ".").grid(row=0, sticky=W)
    Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
    Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
    Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
    Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
    Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

    master.mainloop()
    if selections == 1:
        Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
        Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

    if selections == 2:
        Label(master, text='You Sited There And Game--Over ').grid(row=8, sticky=W)

    if selections == 3:
        Label(master, text='Lion Kills You And Game--Over').grid(row=9, sticky=W)

    if selections == 4:
        Label(master, text=' You Losted Hope  ').grid(row=10, sticky=W)

    master.mainloop()
    # Fourth Layer
    master = Tk()
    var = IntVar()
    var.set(0)

    def quit_loop():
        print("Selection:", var.get())
        global selections
        selections = var.get()
        master.quit()

        # Fourth Layer Of Right Part

    option1 = ('1.Go Ahead To Explore Secrate Path')
    option2 = ('2.Due To Fear Stay At Well')
    option3 = ('3.Step Back Due To Fear Of Secreate Path ')
    option4 = ('4.Stay At well Life long')
    Label(master, text='Secreate Island Ahead' + name + ".").grid(row=0, sticky=W)
    Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
    Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
    Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
    Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
    Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

    master.mainloop()
    if selections == 1:
        Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
        Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

    if selections == 2:
        Label(master, text='You Sited There And Game--Over ').grid(row=8, sticky=W)

    if selections == 3:
        Label(master, text='No Way To Excitued').grid(row=9, sticky=W)

    if selections == 4:
        Label(master, text=' You Losted Hope  ').grid(row=10, sticky=W)

    master.mainloop()
    option1 = ('1.Did You Liked This Game ')
    option2 = ('2.Should I Implement More In Adventure--Game')
    option3 = ('3.Want To Give * * ')
    option4 = ('4.Want To Give Some Comments')
    option5 = ('5.You Dont Like This Game')

    master = Tk()
    var = IntVar()
    var.set(1)
    var.set(2)
    var.set(3)
    var.set(4)
    var.set(5)

    def quit_loop():
        print("Selection: work", var.get())
        global selection
        selection = var.get()
        master.quit()

    Label(master, text="Welcome To Adventure-Game" + name + ".").grid(row=0, sticky=W)
    Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
    Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
    Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
    Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
    Radiobutton(master, text=option5, variable=var, value=5).grid(row=5, sticky=W)
    Button(master, text="Submit", command=quit_loop).grid(row=6, sticky=W)

    master.mainloop()
    if selection == 1:
        Label(master, text='Thank You For You Feedback' + name + ".").grid(row=7, sticky=W)

    if selection == 2:
        Label(master, text='Thank You For You Feedback' + name + ".").grid(row=8, sticky=W)

    if selection == 3:
        Label(master, text='Thank You For You Feedback' + name + ".").grid(row=9, sticky=W)
    if selection == 5:
        Label(master, text='Sorry For That Next Time I Will Implement More ' + name + ".").grid(row=10, sticky=W)

    if selection == 4:
        application_window = tk.Tk()

    answer = simpledialog.askstring("Input", "What is your  Name?",
                                    parent=application_window)
    if answer is not None:
        print("Your Name is ", answer)

    else:
        print("Please Enter Name?")

    answer = simpledialog.askstring("Input", "Enter Your Comment",
                                    parent=application_window)

    if answer is not None:
        print("Your Comment is  ", answer)
    else:
        print("No Comment Written?")

    answer = simpledialog.askstring("Input", "How Many Star You Want To Add?",
                                    parent=application_window, )

    if answer is not None:
        print("You Have Entered  ", answer)
    else:
        print("You Didnt Added Stars?")

    master.mainloop()

    master.mainloop()
    master.mainloop()
    master.mainloop()

    Right()


from tkinter import *


def Forward():
    # Forward LAYER ADVENTURE--GAME
    if response == "Forward":
        print("Rock Big Wall In Front Of You," + name + ".")
        master = Tk()
        var = IntVar()
        var.set(0)

        def quit_loop():
            print("Selections:", var.get())
            global selections
            selections = var.get()
            master.quit()
            # First Layer Of Forward Part

        option1 = ('1.Climb The Wall')
        option2 = ('2.Break The Wall')
        option3 = ('3.Lost The Hope')
        option4 = ('4.Tossing Head To Wall And Die')

        Label(master, text="Rock Big Wall In Front Of You"  + name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

        master.mainloop()
        if selections == 1:
            Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
            Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

        if selections == 2:
            Label(master, text='You Failed To Break The Wall Game--Over').grid(row=8, sticky=W)

        if selections == 3:
            Label(master, text='You Are Backwader').grid(row=9, sticky=W)

        if selections == 4:
            Label(master, text='You Died Game--Over').grid(row=10, sticky=W)

        master.mainloop()

        # Second Layer Of Forward Part

        option1 = ('1.Jump in The River')
        option2 = ('2.Wait For Boat')
        option3 = ('3.Shout For Help ')
        option4 = ('4.Step Back At Rock Wall')
        master = Tk()
        var = IntVar()
        var.set(0)

        def quit_loop():
            print("Selections:", var.get())
            global selections
            selections = var.get()
            master.quit()

        Label(master, text='River Ahead ' + name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

        master.mainloop()
        if selections == 1:
            Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
            Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

        if selections == 2:
            Label(master, text='You does not Got Boat In River And Game--Over').grid(row=8, sticky=W)
            quit_loop()

        if selections == 3:
            Label(master, text='Game--Over').grid(row=9, sticky=W)

        if selections == 4:
            Label(master, text='Snake Bits You And You Died Game--Over').grid(row=10, sticky=W)
        # Forward Second Layer Ends
        master = Tk()
        var = IntVar()
        var.set(2)

        def quit_loop():
            print("Selection:", var.get())
            global selections
            selections = var.get()
            master.quit()

            # Third Layer Of Forward Part

        option1 = ('1.Step Back')
        option2 = ('2.Fight With Aligator')
        option3 = ('3.Shout For Help ')
        option4 = ('4.Run Due To Fear Of Aligator')

        Label(master, text='Aligator Ahead ' + name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

        master.mainloop()
        if selections == 2:
            Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
            Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

        if selections == 1:
            Label(master, text='Aligator Catches you And Game--Over').grid(row=8, sticky=W)
            quit_loop()

        if selections == 3:
            Label(master, text='Game--Over').grid(row=9, sticky=W)

        if selections == 4:
            Label(master, text='Failed To Be Safe From Aligator').grid(row=10, sticky=W)

        master.mainloop()
        master = Tk()
        var = IntVar()
        var.set(4)

        def quit_loop():
            print("Selection:", var.get())
            global selections
            selections = var.get()
            master.quit()

            # Fourth Layer Of Forward Part

        option1 = ('1.Step Back')
        option2 = ('2.Due To Fear Of Black Spot Stay There')
        option3 = ('3.Find Another Way From River ')
        option4 = ('4.Go Ahead In Island')

        Label(master, text='Mystry Of Island ' + name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=5, sticky=W)

        master.mainloop()
        if selections == 4:
            Label(master, text='Welcome To Next Level').grid(row=6, sticky=W)
            Label(master, text='******* Next Level *******').grid(row=7, sticky=W)

        if selections == 1:
            Label(master, text='You Are A Backwader').grid(row=8, sticky=W)
            quit_loop()

        if selections == 3:
            Label(master, text='Failed To Receive Another Way').grid(row=9, sticky=W)

        if selections == 2:
            Label(master, text='Game--Over').grid(row=10, sticky=W)

        master.mainloop()


        option1 = ('1.Did You Liked This Game ')
        option2 = ('2.Should I Implement More In Adventure--Game')
        option3 = ('3.Want To Give * * ')
        option4 = ('4.Want To Give Some Comments')
        option5 = ('5.You Dont Like This Game')


        master = Tk()
        var = IntVar()
        var.set(0)


        def quit_loop():
            print("Selection: work", var.get())
            global selection
            selection = var.get()
            master.quit()

        Label(master, text="Welcome To Adventure-Game" + name + ".").grid(row=0, sticky=W)
        Radiobutton(master, text=option1, variable=var, value=1).grid(row=1, sticky=W)
        Radiobutton(master, text=option2, variable=var, value=2).grid(row=2, sticky=W)
        Radiobutton(master, text=option3, variable=var, value=3).grid(row=3, sticky=W)
        Radiobutton(master, text=option4, variable=var, value=4).grid(row=4, sticky=W)
        Radiobutton(master, text=option5, variable=var, value=5).grid(row=5, sticky=W)
        Button(master, text="Submit", command=quit_loop).grid(row=6, sticky=W)

        master.mainloop()
        if selection == 1:
            Label(master, text='Thank You For You Feedback' + name + ".").grid(row=7, sticky=W)

        if selection == 2:
            Label(master, text='Thank You For You Feedback' + name + ".").grid(row=8, sticky=W)

        if selection == 3:
            Label(master, text='Thank You For You Feedback' + name + ".").grid(row=9, sticky=W)
        if selection == 5:
            Label(master, text='Sorry For That Next Time I Will Implement More ' + name + ".").grid(row=10, sticky=W)

        if selection == 4:
            application_window = tk.Tk()

        answer = simpledialog.askstring("Input", "What is your  Name?",
                                        parent=application_window)
        if answer is not None:
            print("Your Name is ", answer)

        else:
            print("Please Enter Name?")

        answer = simpledialog.askstring("Input", "Enter Your Comment",
                                        parent=application_window)

        if answer is not None:
            print("Your Comment is  ", answer)
        else:
            print("No Comment Written?")

        answer = simpledialog.askstring("Input", "How Many Star You Want To Add?",
                                        parent=application_window, )

        if answer is not None:
            print("You Have Entered  ", answer)
        else:
            print("You Didnt Added Stars?")


        master.mainloop()
        master.mainloop()
        master.mainloop()
        master.mainloop()
        master.mainloop()
        master.mainloop(quit())


Forward()

from tkinter import *


def Backward():
    if response == "Backward":
        print("You Are A BACKWADER!!, " + name + ".")
        # BACKWARD LAYER ADVENTURE--GAME
        master = Tk()
        var = IntVar()
        var.set(0)

        def quit_loop():
            print("Selections:", var.get())
            global selections
            selections = var.get()
            master.quit()

        Label(master, text="You Are A\n BACKWADER!!" + name + ".").grid(row=9, sticky=W)
        master.mainloop()


Backward()