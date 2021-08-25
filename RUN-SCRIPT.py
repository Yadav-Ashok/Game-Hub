from tkinter import *


root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)
import wx
import os
class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Launch Scripts")
        panel = wx.Panel(self, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        buttonA = wx.Button(panel, id=wx.ID_ANY, label="NUMBER-BY-OPERATON", name="MYSCRIPT-NUMBER-BY-OPERATON")
        buttonB = wx.Button(panel, id=wx.ID_ANY, label="MATHS-QUIZ", name="MYSCRIPT-MATHS-QUIZ")
        buttonC = wx.Button(panel, id=wx.ID_ANY, label="ADVENTURE-GAME", name="MYSCRIPT-ADVENTURE-GAME-GUI-BASED")
        buttonD = wx.Button(panel, id=wx.ID_ANY, label="ADVENTURE-GAME-TEXT", name="MYSCRIPT-ADVENTURE-GAME-TEXT-BASED")
        buttonE = wx.Button(panel, id=wx.ID_ANY, label="GUESS-THE-WORD", name="MYSCRIPT-GUESS-THE-WORD")
        buttonF = wx.Button(panel, id=wx.ID_ANY, label="TIC-TAC-TOE", name="MYSCRIPT-TIC-TAC-TOE")


        buttonss1 = [buttonA]
        buttonss2 = [buttonB]
        buttonss3 = [buttonC]
        buttonss4 = [buttonD]
        buttonss5 = [buttonE]
        buttonss6 = [buttonF]


        for button in buttonss1:
            self.buildButtonss1(button, sizer)
        for button in buttonss2:
            self.buildButtonss2(button, sizer)
        for button in buttonss3:
            self.buildButtonss3(button, sizer)
        for button in buttonss4:
            self.buildButtonss4(button, sizer)
        for button in buttonss5:
            self.buildButtonss5(button, sizer)
        for button in buttonss6:
            self.buildButtonss6(button, sizer)

        panel.SetSizer(sizer)

    def buildButtonss1(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, 0, )
    def buildButtonss2(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, 1, )
    def buildButtonss3(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, 0, )
    def buildButtonss4(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, 1, )
    def buildButtonss5(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, 0, )
    def buildButtonss6(self, btn, sizer):
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, 1, )

    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed, taking the script from it's name
        """
        button = event.GetEventObject()


        os.system('python {}.py'.format(button.GetName()))

        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print ("The button you pressed was labeled: " + button_by_id.GetLabel())
        print ("The button's name is " + button_by_id.GetName())





# Run the program
if __name__ == "__main__":
    _input = []




    app = wx.App(False)

    frame = MyForm()
    frame.Show()


    app.MainLoop()
