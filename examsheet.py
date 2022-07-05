import tkinter as tk
from tkinter import ttk


def Sett(*args):
    for i in range(len(lickey)):
        answersheet[i + 1] = vars[i].get()
    return answersheet


def count(c1, c2):
    percantile = 0.0
    corcount = 0
    wrocount = 0
    nacount = 0
    t = c2 - c1 + 1
    for k, v in answersheet.items():
        while c1 <= k <= c2:
            for ke, ve in keysheet.items():
                if k == ke:
                    if v == ve and v != 0:
                        corcount += 1
                        index = str(k) + '.' + '0'
                        char = str(k) + '.' + str(v) + '✅\n'
                        resultbox.insert(index, char)
                    elif v == 0:
                        index = str(k) + '.' + '0'
                        char = str(k) + '.' + str(ve) + '⚪\n'
                        resultbox.insert(index, char)
                    elif v != ve and v != 0:
                        wrocount += 1
                        index = str(k) + '.' + '0'
                        char = str(k) + '.' + str(v) + '❌' + \
                            '⟶' + str(ve) + '✅\n'
                        resultbox.insert(index, char)
                else:
                    continue
            break
    nacount = t - (corcount + wrocount)
    percantile = (corcount - (wrocount / 3)) / t 
    #if your exam calcuates the wrongs as a minus(where 3 wrongs, also clears one of your corrects), else use this:
    # percantile = corcount / t
    return str(corcount) + '/' + str(wrocount) + '/' + str(
        nacount) + '⟶ ' + str(percantile * 100)[:4] + '%\n'


def Check():
    resultbox['state'] = 'normal'
    resultbox.delete(0.0, "end")
    if len(lickey) == 235:  #Change these accoring to your exam:
        Farsi = "Farsi: " + count(1, 25)
        Arabi = "Arabic: " + count(26, 50)
        Relig = "Relig: " + count(51, 75)
        Eng = "English: " + count(76, 100)
        Math = "Maths: " + count(101, 155)
        Phys = "Physics: " + count(156, 200)
        Chem = "Chemistry: " + count(201, 235)
        topicres.set(Farsi + Arabi + Relig + Eng + Math + Phys + Chem)
    else:
        Total = "Total: " + count(1, len(lickey))
        topicres.set(Total)
    resultbox['state'] = 'disabled'


seqkey = input("Enter sequential exam key: ") #enter examkey sequentially (e.g: 1243332114213...).
lickey = [key for key in seqkey.strip()]
keysheet = dict()
a = 1
for i in lickey:
    keysheet[a] = int(i)
    a += 1

root = tk.Tk(className=("Exam Checker"))
mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0)

canvas = tk.Canvas(mainframe, width=165, height=431)
canvas.grid(row=0, column=0, sticky="N")
content = ttk.Frame(canvas)
content.grid(row=0, column=0)

lframe = ttk.Frame(content)
lframe.grid(row=0, column=0, sticky=('n'))

exscroll = ttk.Scrollbar(mainframe, orient='vertical', command=canvas.yview)
canvas.config(yscrollcommand=exscroll.set, scrollregion=(
    0, 0, 0, len(lickey) * 23))
exscroll.grid(row=0, column=0, sticky="e")

ttk.Label(lframe, text=("1"), font=("Comic Mono", 15)
          ).grid(row=0, column=1, sticky=("nw"))
ttk.Label(lframe, text=("2"), font=("Comic Mono", 15)
          ).grid(row=0, column=2, sticky=("nw"))
ttk.Label(lframe, text=("3"), font=("Comic Mono", 15)
          ).grid(row=0, column=3, sticky=("nw"))
ttk.Label(lframe, text=("4"), font=("Comic Mono", 15)
          ).grid(row=0, column=4, sticky=("nw"))
ttk.Frame(lframe, width=10).grid(row=0, column=5)
ttk.Label(lframe, text=("N/A"), font=("Comic Mono", 14)
          ).grid(row=0, column=6, sticky=("nw"))

answersheet = dict()
vars = []
for i in range(len(lickey)):
    monokeyholder = tk.IntVar()
    vars.append(monokeyholder)

    ttk.Label(lframe, text=(i + 1)).grid(row=i + 1, column=0, sticky=("NE"))

    ttk.Radiobutton(lframe, value=1, variable=monokeyholder,
                    command=Sett).grid(row=i + 1, column=1, sticky=("NE"))
    ttk.Radiobutton(lframe, value=2, variable=monokeyholder,
                    command=Sett).grid(row=i + 1, column=2, sticky=("NE"))
    ttk.Radiobutton(lframe, value=3, variable=monokeyholder,
                    command=Sett).grid(row=i + 1, column=3, sticky=("NE"))
    ttk.Radiobutton(lframe, value=4, variable=monokeyholder,
                    command=Sett).grid(row=i + 1, column=4, sticky=("NE"))
    ttk.Radiobutton(lframe, value=0, variable=monokeyholder,
                    command=Sett).grid(row=i + 1, column=6, sticky=("NE"))

rframe = ttk.Frame(mainframe)
rframe.grid(row=0, column=2, sticky=("N"))

topicres = tk.StringVar()

donbut = ttk.Button(rframe, text="Result", command=Check)
donbut.grid(row=2, column=2, sticky=("S"))

topiclab = ttk.Label(rframe, textvariable=topicres)
topiclab.grid(row=0, column=2)

resultbox = tk.Text(rframe, width=20, height=17)
resultbox.grid(row=1, column=2, sticky=("N"))

rbscroll = ttk.Scrollbar(rframe, orient="vertical", command=resultbox.yview)
rbscroll.grid(row=1, column=3, sticky="E")
resultbox.configure(yscrollcommand=rbscroll.set)

canvas.create_window(0, 0, anchor='nw', window=content)
root.mainloop()
