import tkinter
from tkinter import *
import random

question = [
    "* Which of the following is not a result of cell division?",
    "* Mark the incorrect pair.",
    "* of the following is incrrect for reproductioWhichn ?",
    "* Mark the incrroect statement w.r.t metabolism.",
    "* Non-living objects exhibit/show",
    "* Which statement is false about the growth shown by non-living object.?",
    "* Local names of various plants and animals",
    "* Which of the follwing is incorrect w.r.t Binomial nomencature.?",
    "* What do  A,B and C represent in the given scientific name respectively.?",
    "* Whicg of the following is incorrect regarding scientific names.?"
]

answers_choice = [
    ["Growth","Repair","Metabolism","Reproduction"],
    ["Hydra - Budding","Flatworm - Regeneration","Amoeba - Fragmentation","Yeast - Budding"],
    ["Unicellular organisms reproduce by cell division","reproduction is a characterisitc of all living organisms","In unicellular organisms, reproduction and growth are linked together","Non - living object are incapable of reproducng"],
    ["Microbes exhibit the metabolism","It is the property of all living forms","The metablic reaction can be demonstrated in-vitro","It is not a defining feature of life forms",],
    ["Property of self-replication","Evolution","Self-regulating interactives systems","Reversible growth"],
    ["the growth occurs from outside","The growth is reversible","The growth is due to the accumulation of material on the surface","The growth is intrinsic"],
    ["help in recognizing organisms woldwide","Are used universally","Are specific and distinct names","Vary from place to place"],
    ["Biological names are generally in Latin","The first word in biological name represents the genus","Biological names are printed in italics","The first word of the genus starts with a small letter"],
    ["generic name, specific name and author's name","ecific name, generic name and generic name","Author's name, specific name and generic name","generic name, author name and specific name"],
    ["These are also known as common names","these ensure that each organim has only one name","These have two component - the generic name and specific epithet","These are universally accepted names"],
]
answers = [2,2,1,3,3,3,3,3,2,0]

user_ans= []

indexes = []

def gen():
    global indexes
    while(len(indexes) <10):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            #print(indexes)

def showresult(score):
    lbl_question.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    lbl_new_image = Label(root, bg = "white")
    lbl_new_image.pack(pady = (50,30))
    lbl_result_text = Label(root, font = ("Consolas",20), bg = "white", border = 0)
    lbl_result_text.pack()
    if score >=20:
        img = PhotoImage(file = "img/the.png")
        lbl_new_image.configure(image = img)
        lbl_new_image.image = img
        lbl_result_text.configure(text = "You Are Excellent")
    elif score <20:
        img = PhotoImage(file = "img/t.png")
        lbl_new_image.configure(image = img)
        lbl_new_image.image = img
        lbl_result_text.configure(text = "You Are Can be Better !!")
    elif score <= 10:
        img = PhotoImage(file = "img/sad.png")
        lbl_new_image.configure(image = img)
        lbl_new_image.image = img
        lbl_result_text.configure(text = "You should Work Hard")
        


def calc():
    global indexes,user_ans,answers
    x = 0
    score = 0
    for i in indexes:
        if user_ans[x] == answers[i]:
            score = score + 5
        x +=1
        print(score)
        showresult(score)



ques = 1
def selected():
    global radiovar,user_ans
    global lbl_question,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_ans.append(x)
    radiovar.set(-1)
    if ques <10:
        lbl_question.config(text = question[indexes[ques]])
        r1["text"] = answers_choice[indexes[ques]][0]
        r2["text"] = answers_choice[indexes[ques]][1]
        r3["text"] = answers_choice[indexes[ques]][2]
        r4["text"] = answers_choice[indexes[ques]][3]
        ques +=1
    else:
        print(indexes)
        print(user_ans)
        print(answers)
        calc()
        



def start_quiz():
    global lbl_question,r1,r2,r3,r4
    lbl_question = Label( root, text = question[indexes[0]], font = ("Consolas",16),width = 500, justify = "center", wraplength = 400,bg = "White")
    lbl_question.pack(pady = (100,30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root, text = answers_choice[indexes[0]][0], font = ("Times", 12), value = 0, command = selected,bg = "White")
    r1.pack(pady = 5)

    r2 = Radiobutton(root, text = answers_choice[indexes[0]][1], font = ("Times", 12), value = 1, command = selected,bg = "White")
    r2.pack(pady = 5)

    r3 = Radiobutton(root, text = answers_choice[indexes[0]][2], font = ("Times", 12), value = 2, command = selected,bg = "White")
    r3.pack(pady = 5)

    r4 = Radiobutton(root, text = answers_choice[indexes[0]][3], font = ("Times", 12), value = 3, command = selected,bg = "White")
    r4.pack(pady = 5)

def start_is_press():
    label_image.destroy()
    label_text.destroy()
    label_Instruction.destroy()
    lbl_Rules.destroy()
    btn_Start.destroy()
    gen()
    start_quiz()

root = tkinter.Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(bg = "white")
root.resizable(0,0)


img1 = PhotoImage(file = "img/icon.png")

label_image = Label(root, image = img1, bg = "white")
label_image.pack(pady = (40,0))

label_text = Label(root, text = "Quiz", font = ("Comic sans MS",24,"bold"),bg = "white")
label_text.pack(pady = (0,50))



img2 = PhotoImage(file = "img/exit.png")

btn_Start = Button(root, image = img2, relief = FLAT, border = 0, bg = "white",command = start_is_press,)
btn_Start.pack()

label_Instruction = Label(root, text = "Read The Rules And \n Click Start Once You are Ready", bg = "white", font = ("Consolas",14), justify = "center", fg = "red")
label_Instruction.pack(pady = (10,90))

lbl_Rules = Label(root, text = "This quiz contains 10 questions\n you will get 20 secons to solve a question\nOnce you select a radio button taht willbe a final choice\nheance think before you select", width = 100, font = ("Times",14),bg = "#000000",fg = "yellow",)
lbl_Rules.pack()


root.mainloop()