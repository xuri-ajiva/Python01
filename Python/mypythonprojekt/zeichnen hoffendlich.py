from tkinter import *
from tkinter import messagebox
from sys import *


mfx =1000
mfy=700


class Malflaeche(object):
    def __init__(self,breite,hoehe):
        self.fenster = Tk()
        self.fenster.title("rechteck")
        self.ramen  = Frame(self.fenster,relief=RIDGE,bd=5)
        self.ramen100  = Frame(self.ramen,relief=RIDGE,bd=5)
        self.ramen0 = Frame(self.ramen,relief=RIDGE,bd=5)
        self.ramen1 = Frame(self.ramen,relief=RIDGE,bd=2)
        self.ramen2 = Frame(self.ramen,relief=RIDGE,bd=2)
        self.ramen3 = Frame(self.ramen,relief=RIDGE,bd=2)
        self.ramen4 = Frame(self.ramen,relief=RIDGE,bd=2)
        self.ramen5 = Frame(self.ramen,relief=RIDGE,bd=2)
        self.eingabe1 = Entry(self.ramen1)
        self.label1 =Label (self.ramen1,text = "posx1",font=("Arial",15))
        self.eingabe2 = Entry(self.ramen2)
        self.label2 =Label (self.ramen2,text = "posy1",font=("Arial",15))
        self.eingabe3 = Entry(self.ramen3)
        self.label3 =Label (self.ramen3,text = "posx2",font=("Arial",15))
        self.eingabe4 = Entry(self.ramen4)
        self.label4 =Label (self.ramen4,text = "posy2",font=("Arial",15))
        self.eingabe5 = Entry(self.ramen5)
        self.label5 =Label (self.ramen5,text = "Farbe",font = ("Arial",15))
        self.knopf6 =Button(self.ramen,text="          los           ", bg="green", font=("Arial",15),relief = RAISED, justify = CENTER , command = self.los)
        self.w2 = Scale(self.ramen100, from_=0, to=300,tickinterval=100,length=500)

#        self.fenster = Tk()
 #       self.fenster.title('Malen')
        self.flaeche = Canvas(self.fenster, width=breite,height=hoehe)
        self.flaeche.bind('<Button-1>',self.klicken)
        self.flaeche.bind('<Motion>',self.bewegen)
        self.flaeche.bind('<ButtonRelease-1>',self.loslassen)
        self.farbe = 'black'
        self.geklickt = False
        self.rot=Label(self.ramen100,width=6,height=3,bg='red',relief=GROOVE)
        self.gruen=Label(self.ramen100,width=6,height=3,bg='green',relief=GROOVE)
        self.blau=Label(self.ramen100,width=6,height=3,bg='blue',relief=GROOVE)
        self.schwarz=Label(self.ramen100,width=6,height=3,bg='black',relief=GROOVE)
        self.weiß=Label(self.ramen100,width=6,height=3,bg='gray94',relief=GROOVE)
        self.rot.bind('<1>',self.roterStift)
        self.gruen.bind('<1>',self.gruenerStift)
        self.blau.bind('<1>',self.blauerStift)
        self.schwarz.bind('<1>',self.schwarzerStift)
        self.weiß.bind('<1>',self.weißerStift)
    #    print("Bitte eine Zahl nicht --> %%D " ,eingabe.get())
        self.ramen100.pack(side=LEFT)
        self.w2.pack(side=BOTTOM)
        self.rot.pack(side=BOTTOM)
        self.gruen.pack(side=BOTTOM)
        self.blau.pack(side=BOTTOM)
        self.schwarz.pack(side=BOTTOM)
        self.weiß.pack(side=BOTTOM)
   #     self.flaeche = Canvas (self.fenster,width=1000,height=700)
        self.flaeche.pack(side=RIGHT)
        self.flaeche.create_line(0,350,1000,350)
        self.flaeche.create_line(500,0,500,700)
        self.ramen0.pack(side=LEFT,padx = 0 ,pady = 25)
        self.ramen5.pack(side=TOP,pady = 20)
        self.label5.pack()
        self.ramen.pack(side=LEFT,pady = 20, padx = 20)
        self.eingabe1.pack(padx = 20 ,pady = 20)                  # sichtbarmachen   1
        self.ramen1.pack(side=TOP,padx = 5 ,pady = 5)
        self.label1.pack()
        self.eingabe2.pack(padx = 20 ,pady = 20)                  # sichtbarmachen   2
        self.ramen2.pack(side=TOP,padx = 5 ,pady = 5)
        self.label2.pack()
        self.eingabe3.pack(padx = 20 ,pady = 20)                  # sichtbarmachen   3
        self.ramen3.pack(side=TOP,padx = 5 ,pady = 5)
        self.label3.pack()
        self.eingabe4.pack(padx = 20 ,pady = 20)                  # sichtbarmachen   4
        self.ramen4.pack(side=TOP,padx = 5 ,pady = 5)
        self.label4.pack()
        self.eingabe5.pack(padx = 20 ,pady = 20)                  # sichtbarmachen   5
        self.knopf6.pack(side=TOP,padx = 20 ,pady = 20)            # sichtbarmachen
        self.menubar = Menu(self.fenster)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="neues kreutz", command=self.nk)
        self.filemenu.add_command(label="neues kreutz", command=self.nk)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.fenster.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.fenster.config(menu=self.menubar)
        self.flaeche.pack()
        self.fenster.mainloop()
        #self.fenster.mainloop()



    def donothing():
       self.filewin = Toplevel(fenster)
       self.button = Button(filewin, text="Do nothing button")
       self.button.pack()



    def klicken(self,event):
        self.geklickt = True
        self.flaeche.create_oval(event.x-self.w2.get(),event.y-self.w2.get(),event.x+self.w2.get(),event.y+self.w2.get(),
                                 fill=self.farbe,outline=self.farbe)
    def bewegen(self,event):
        if self.geklickt:
            self.flaeche.create_oval(event.x-self.w2.get(),event.y-self.w2.get(),event.x+self.w2.get(),event.y+self.w2.get(),
                                     fill=self.farbe,outline=self.farbe)
    def loslassen(self,event):
        self.geklickt = False
    def roterStift(self,event):
        self.farbe = 'red'
        self.fenster.title('roter Stift')
    def gruenerStift(self,event):
        self.farbe = 'green'
        self.fenster.title('gruener Stift')
    def blauerStift(self,event):
        self.farbe = 'blue'
        self.fenster.title('blauer Stift')
    def schwarzerStift(self,event):
        self.farbe = 'black'
    def weißerStift(self,event):
        self.farbe = 'gray94'

    def nk(self):
        y = mfy / 2
        x = mfx / 2
        self.flaeche.create_line(0,y,mfx,y)
        self.flaeche.create_line(x,0,x,mfy)

    def donothing(self):
        self.filewin = Toplevel(fenster)
        self.button = Button(filewin, text="Do nothing button")
        self.button.pack()

    def rechteck(self):
        self.menubar = Menu(self.fenster)
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="neues kreutz", command=nk)
        #self.filemenu.add_command(label="neues kreutz", command=nk)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=fenster.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)
        self.fenster.config(menu=menubar)

    def ende():
        quit()
 
    def los (self):
    
        try:
            self.label5.configure(text="Farbe", fg="black")
            self.label1.configure(text="posx1", fg="black")
            self.label2.configure(text="posy1", fg="black")
            self.label3.configure(text="posx2", fg="black")
            self.label4.configure(text="posy2", fg="black")
   
            co = self.eingabe5.get()                 # farbe
        except:
            self.label5.configure(text="Farbe" , fg="red",font=("Arial",20))
        try:
            x1 = float(self.eingabe1.get())          # x1 pos
        except: 
            self.label1.configure(text="posx1" , fg="red",font=("Arial",20))
        try:
            x2 = float(self.eingabe2.get())          # x2 pos
        except:
            self.label2.configure(text="posx1" , fg="red",font=("Arial",20))
        try:
            y1 = float(self.eingabe3.get())          # y1 pos
        except:
            self.label3.configure(text="posx2" , fg="red",font=("Arial",20))
        try:
            y2 = float(self.eingabe4.get())          # y2 pos
        except:
            self.label4.configure(text="posy2" , fg="red",font=("Arial",20))
        try:
            y = mfy / 2
            x = mfx / 2
            self.flaeche.create_rectangle(-x1+x,-x2+y,-y2+x,-y1+y,fill = co ,width=2)
        except:
            try:
                self.knopf7.forget()
                print("xxx")
            except:
                
                self.label5.configure(text="Es ist etwas schiefgelaufen!",wraplength = 200 , fg="red",font=("Arial",15))
                self.knopf7 =Button(self.ramen,text="          quit          ", bg="green", font=("Arial",15),relief = RAISED, justify = CENTER , command = self.fenster.quit)
                self.knopf7.pack(side=TOP,padx = 20 ,pady = 10)



m = Malflaeche(mfx,mfy)
