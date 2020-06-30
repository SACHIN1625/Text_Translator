from tkinter import *
from tkinter.ttk import Combobox
import googletrans
from tkinter import messagebox
from textblob import TextBlob

root=Tk()
root.geometry('1000x1000+250+50')
root.title("Text Translator created by Sachin")
root.resizable(0,0)
root.iconbitmap('icon.ico')
root.config(bg='grey')

lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}


def clickfunc(event=None):
    try:
        word=TextBlob(varname1.get())
        lan=word.detect_language()
        lan_todict=language.get()
        lang_to=lan_dict[lan_todict]
        word=word.translate(from_lang=lan,to=lang_to)
        varname2.set(word)
        label3.config(text=word)

    except:
        varname2.set("Try another word")
def main_exit():
    rr=messagebox.askyesnocancel("Notification","Do You Want To Exit",parent=root)
    if rr:
        root.destroy()
################################binding functions

def on_enterentryy1(e):
    entry1['bg']='springgreen'

def on_leaveentryy1(e):
    entry1['bg']='white'


def on_enterentryy2(e):
    entry2['bg'] = 'springgreen'


def on_leaveentryy2(e):
    entry2['bg'] = 'white'


def on_enterbutton1(e):
    clickbtn1['bg'] = 'springgreen'


def on_leavebutton1(e):
    clickbtn1['bg'] = 'yellow'


def on_enterbutton2(e):
    exitbtn2['bg'] = 'springgreen'


def on_leavebutton2(e):
    exitbtn2['bg'] = 'yellow'




language=StringVar()
font_box=Combobox(root,width=30,textvariable=language,state='readonly')
font_box['values']=[e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)
#####################################Pics
logopic=PhotoImage(file='translation.png')
exitpic=PhotoImage(file='exit.png')
clickpic=PhotoImage(file='touch.png')

###########################################entry
varname1=StringVar()
entry1=Entry(root,width=30,textvariable=varname1,font=("times",15,'italic bold'),relief=RIDGE)
entry1.place(x=150,y=170)

varname2=StringVar()
entry2=Entry(root,width=30,textvariable=varname2,font=("times",15,'italic bold'),relief=RIDGE)
entry2.place(x=150,y=220)
########################################labels
label1=Label(root,text='Enter word :',font=("times",18,'bold'),bg='white')
label1.place(x=5,y=170)

label2=Label(root,text='Translated :',font=("times",18,'bold'),bg='white')
label2.place(x=5,y=220)

label3=Label(root,text='',font=("times",15,'italic bold'),bg='white')
label3.place(x=50,y=280)

label4=Label(image=logopic,bg='grey')
label4.place(x=150,y=10)

###############################################buttons
clickbtn1=Button(root,text='Click',bd=10,bg='yellow',activebackground='red',width=100,
                 font=("times",15,'italic bold'),image=clickpic,compound=LEFT,command=clickfunc)
clickbtn1.place(x=220,y=330)
exitbtn2=Button(root,text='Exit',bd=10,bg='yellow',activebackground='red',width=100,
                font=("times",15,'italic bold'),image=exitpic,compound=LEFT,command=main_exit)
exitbtn2.place(x=360,y=330)

####################################button binding for hover effect
entry1.bind('<Enter>',on_enterentryy1)
entry1.bind('<Leave>',on_leaveentryy1)

entry2.bind('<Enter>',on_enterentryy2)
entry2.bind('<Leave>',on_leaveentryy2)

clickbtn1.bind('<Enter>',on_enterbutton1)
clickbtn1.bind('<Leave>',on_leavebutton1)
exitbtn2.bind('<Enter>',on_enterbutton2)
exitbtn2.bind('<Leave>',on_leavebutton2)



root.bind('<Return>',clickfunc)
root.mainloop()