from pygame import mixer
from tkinter import *
from sys import exit as ex
from tkinter import colorchooser
from os import listdir, getcwd, path
import webbrowser
from time import sleep
from tkinter import messagebox
import tkinter.ttk as ttko
from tkinter import ttk
from mutagen.mp3 import MP3


def main():
    numfw = 1
    while numfw == 1 or numfw == 2:
        player = Tk()
        try:
            icp = PhotoImage(file =  "Audio_File_icon.ico")
            player.iconphoto(True, icp)
        except:
            pass

        player.title("Audio Player")
        player.geometry("260x310+20+20")
        player.maxsize(260, 310)
        player.minsize(260, 310)
        player.resizable(0, 0)
        global f
        global n
        global p
        global dis
        global sop
        n = 0
        f = 0
        p = True
        dis = False
        sop = 2

                   
        def play():
            button3["state"] = "normal"
            global nums
            global f
            f += 1
            if (f%2) == 1:
                global p
                global n
                global dis
                dis = True
                p = True
                button3["text"] = "| |"
                button3["font"] = "bold"
                button1["bg"] = "red"
                button1["text"] = "STOP"
                    
                try:
                   file = box.get()
                   mixer.pre_init(44100, -16, 2, 2048)
                   mixer.init()
                   mixer.music.load(file)
                   try:
                       mixer.music.set_volume(volume)
                       try:
                           if playtimes == "Infinity":
                               mixer.music.play(loops = -1)
                               
                           else:
                               mixer.music.play()
                               
                               
                               
                       except NameError:
                           mixer.music.play()
                           
                           
                   except:
                       mixer.music.set_volume(1.0)
                       
                       
                       try:
                           if playtimes == "Infinity":
                               mixer.music.play(loops = -1)
                           else:
                               mixer.music.play()
                               
                               
                       except NameError:
                           mixer.music.play()
                           
                except:
                   messagebox.showerror("ERROR!", "Choose an allowed Song first!")
                   button3["state"] = "disabled"
                   numfw = 2
                   f += 1
                   button3["text"] = "| |"
                   button3["font"] = "bold"
                   button1["bg"] = "green"
                   button1["text"] = "START"
                   
            else:
                
                if box.get() != "Select Song:":
                    button1["bg"] = "green"
                    button3["text"] = "| |"
                    button3["font"] = "bold"
                    button1["text"] = "START"
                    p = False
                    button3["text"] = ""
                    global n
                    try:
                        if stops == "stop":
                            mixer.music.stop()
                        elif stops == "fadeout":
                            mixer.music.fadeout(2000)
                        else:
                            mixer.music.stop()
                    except:
                        mixer.music.stop()
                else:
                    messagebox.showerror("ERROR!", "Choose an allowed Song first!")
                    numfw = 2 
                    button3["text"] = "| |"
                    button3["font"] = "bold"
                    button1["bg"] = "green"
                    button1["text"] = "START"
        def pause():
            try:
                global n
                n = n + 1
                if dis != True:
                    pass
                elif (n%2) == 1 and p == True and box.get() != "Select Song:":
                    button3["text"] = ""
                    mixer.music.pause()
                elif (n%2) == 0 and p == True and box.get() != "Select Song:":
                    button3["text"] = "| |"
                    button3["font"] = "bold"
                    mixer.music.unpause()
                elif box.get() == "Select Song:":
                    button3["state"] = "disabled"
            except:
                    button3["state"] = "disabled"
        def exit_():
            player.destroy()
            ex()
        def ins():
            global playtimes
            window = Tk()
            window.title("INSTUCTIONS")
            w = window.winfo_screenwidth()
            h = window.winfo_screenheight()
            window.geometry("%dx%d+0+0" % (w, h))
            window.state("zoomed")
            window.resizable(0,0)
            player.iconify()
            def cbcc():
                global lcs1
                lcs1 =colorchooser.askcolor()
                window["bg"] = lcs1[1]
                a["bg"] = lcs1[1]
                b["bg"] = lcs1[1]
                se["bg"] = lcs1[1]
                vol["bg"] =lcs1[1]
                Playt["bg"] = lcs1[1]
                playt1["bg"] = lcs1[1]
                playt23["bg"] = lcs1[1]
                playo["bg"] = lcs1[1]
                playo1["bg"] = lcs1[1]
                leer1["bg"] = lcs1[1]
                leer["bg"] = lcs1[1]
            menubar1= Menu(window)
            file1 = Menu(menubar1,  tearoff = 0)
            file1.add_command(label = "Change background color", command = cbcc)
            menubar1.add_cascade(label = "File", menu = file1)
            window.config(menu=menubar1)
            def gotolink(event):
                url = webbrowser.open('https://audio.online-convert.com/convert-to-wav')
                window.iconify()
                player.iconify()
                b["fg"] = "purple"
            def un(event):
                b["font"] = "bold 15 underline"
            def nun(event):
                b["font"] = "bold 15"
            a = Label(window, text = "This is an Audio player.\n\nHow to use it: store all your .wav files in the same folder as the Python file. Then open the file and start!\nHint: This Programm only supports .wav files.\nIf you want to record and convert your files; Check this Link:", font = "bold 15")
            b = Label(window, text = "Go to the Link", font = "bold 15", fg = "blue", width = 14, cursor = "leftbutton")
            a.pack()
            b.pack()
            b.bind("<Enter>", un)
            b.bind("<Leave>", nun)
            b.bind("<Button-1>", gotolink)
            se = Label(window, text = "\n\n\nSETTINGS\n", font ="bold 17 underline")
            se.pack()
            vol = Label(window, text = "Volume", font = "bold 14")
            vol.pack()
            scala = Scale(window, from_ = 0, to =100, length = 400, orient = HORIZONTAL, bd = 3, cursor = "sb_h_double_arrow", troughcolor = "#00ffff", relief = "groove", tickinterval = 25, font= "bold", repeatdelay = 250, fg  = "#000fff000")
            scala.pack()
            scala["state"] = "active"
            try:
                scala.set(volume*100)
            except:
                scala.set(100)
            def feed():
                window.destroy()
                player.deiconify()
            def po():
                global stops
                stops = playo2.get()
                global playtimes
                playtimes = playt2a.get()
                global volume
                volume = scala.get()
                volume = volume/100
            Playt = Label(window, text = "\nPlaying times", font = "bold 14")
            Playt.pack()
            playt1 = Label(window, text = "The song will play:")
            playt1.pack()
            listplay = [1, 'Infinity']
            playt2a = ttk.Combobox(window, value = listplay, cursor = "leftbutton")
            try:
                if playtimes == 1:
                    playt2a.current(0)
                elif playtimes == "Infinity":
                    playt2a.current(1)
                else:
                    playt2a.current(0)
            except NameError:
                playt2a.current(0)
            playt2a.pack()
            playt23 = Label(window, text = "times\n")
            playt23.pack()
            playo = Label(window, text = "Stop Setting", font = "bold 14")
            playo.pack()
            playo1 = Label(window, text = "When pressed Stop, the song will:")
            playo1.pack()
            listo = ["stop", "fadeout"]
            playo2 = ttk.Combobox(window, value = listo, cursor = "leftbutton")
            try:
                if stops == "stop":
                    playo2.current(0)
                elif stops == "fadeout":
                    playo2.current(1)
                else:
                    playoo2.current(0)
            except:
                playo2.current(0)
            def icono(event):
                window.iconify()
                player.deiconify()
            playo2.pack()
            leer1 = Label(window, text = "\n")
            leer1.pack()
            playo3 = Button(window, text = "SAVE", command = po, bg = "green", cursor = "leftbutton")
            playo3.pack()
            leer = Label(window)
            leer.pack()
            bottonf = Button(window, text = "CLOSE",command = feed, bg = "red", cursor = "leftbutton")
            bottonf.pack()
            window.attributes('-topmost', 1)
            window.bind("<Unmap>", icono)
            def exit_p():
                window.destroy()
                player.deiconify()
            window.protocol('WM_DELETE_WINDOW', exit_p)


        def ref():
            mes = Tk()
            mes.geometry("+320+100")
            mes.title("See Code")
            def en(event):
                lmes["font"] = "bold 10 underline"
            def el(event):
                lmes["font"] = "bold 10"
            def cl(event):
                webbrowser.open("https://github.com/Tams-Tams/python/blob/master/Audio_Player.pyw")
                lmes["font"] = "bold 10"
                lmes["fg"] = "purple"
                mes.destroy()
            lmes = Label(mes, text ="To see the code, visit this Link: https://github.com/Tams-Tams/python/blob/master/Audio_Player.pyw", fg = "blue", font = "bold 10")
            lmes.bind("<Enter>", en)
            lmes.bind("<Leave>", el)
            lmes.bind("<Button-1>", cl)
            lmes.pack()
            
        player.protocol('WM_DELETE_WINDOW', exit_)
        label0 = LabelFrame(player, text = "Song Name", bg = "yellow")
        label0.pack(fill = "y")
        button1 = Button(width = 39, height = 3, text = "START", bg = "green", command = play, font = "bold 9", cursor = "leftbutton")
        button1.pack(fill = "y")
        button3 = Button(width = 30, height = 3, text = "| |", bg = "orange", font = "bold 12", command = pause, cursor = "leftbutton")
        button3.pack(fill = "y")
        button7 = Button(width = 30, height = 3, text = "INSTRUCTIONS and SETTINGS", bg = "blue", fg = "yellow", command = ins, font = "bold 12", cursor = "leftbutton")
        button7.pack(fill = "y")
        button6 = Button(width = 39, height = 3, text = "EXIT", bg = "darkred", command = exit_, font = "bold 9", cursor = "leftbutton")
        button6.pack(fill = "y")
        button3["state"] = "disabled"

        menubar = Menu(player)
        file = Menu(menubar,  tearoff = 0)
        file.add_command(label = "See code", command = ref)
        menubar.add_cascade(label = "File", menu = file)
        
        
        player.config(menu=menubar)
        
        listr = list()
        list1 = listdir()
        for i in list1:
            if (not(i[-3:0] == ".mp3"))and(not("."in i)):
                list1.remove(i)
        if len(list1) == 0:
            list1.append("Go to Instructions")
        list1.sort()
        box = StringVar(label0)
        box.set("Select Song:")
        content1 = ttko.OptionMenu(label0, box, "Select Song:", *list1)
        content1.pack(fill = "y")
        ldd = Label(label0, width = 39, bg  = "yellow")
        ldd.pack()
        if numfw == 2:
             break
            
        player.attributes("-topmost", 1)
        mixer.init()
        
        player.mainloop()

if __name__ == "__main__":
    main()
