# 2022.02.17 팀 프로젝트 - 초기 화면

import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.font as tkFont
import tkinter.ttk
import customtkinter
from PIL import Image, ImageDraw, ImageFont, ImageTk
from openpyxl import load_workbook
import random as r
import csv

#---- 변수모음
load_wb = load_workbook("menu (1).xlsx",data_only=True)
load_ws = load_wb['menu']

xpos,ypos,num = 0,0,0
new_id,new_pw = '',''
fv_food_set = {}
fv_food_list = []
user_info_list = []
count = []
user_food_list = []
max_count=0
a=[]           #리스트화시킨 엑셀의 정보를 담을 리스트들
b=[]
c=[]
d=[]
f=[]
g=[]
rand=[]
equal=[]

for i in range(0,21):
    count.append(0)
login_success_user_info = ''

button_select_list = ['떡볶이','닭볶음탕','고기','밥','국밥','햄버거/치킨','피자','카레','초밥','돈까스','라멘','밥','부대찌개','닭갈비','보쌈','찜닭','꿔바로우','짜장면/짬뽕','브리또','마라탕','햄버거'] #메뉴 선택창에서 활용

    
get_cells1 = load_ws['A2' : 'A38']            #엑셀 파일 종류별로 리스트화
for row in get_cells1:
    for cell in row:
        a.append(cell.value)

get_cells2 = load_ws['B2' : 'B38']
for row in get_cells2:
    for cell in row:
        b.append(cell.value)

get_cells3 = load_ws['C2' : 'C38']
for row in get_cells3:
    for cell in row:
        c.append(cell.value)

get_cells4 = load_ws['D2' : 'D38']
for row in get_cells4:
    for cell in row:
        d.append(cell.value)
        
    
get_cells5 = load_ws['F2' : 'F38']
for row in get_cells5:
    for cell in row:
        f.append(cell.value)

get_cells6 = load_ws['G2' : 'G38']
for row in get_cells6:
    for cell in row:
        g.append(cell.value)

get_cells7 = load_ws['H2' : 'H38']      #음식이 카운팅된 갯수를 표현하는 엑셀을 리스트화 시킨 것 (H열에 0만 들어잇음)
for row in get_cells7:
    for cell in row:
        count.append(cell.value)

get_cells8 = load_ws['I2' : 'I38']      #음식이 카운팅된 갯수를 표현하는 엑셀을 리스트화 시킨 것 (H열에 0만 들어잇음)
for row in get_cells8:
    for cell in row:
        equal.append(cell.value)

#----함수모음


def switch_frame(frame):
    frame.tkraise()

def make_maincanvas(frame):
    canvas_main = tk.Canvas(frame, width=1000, height=1000, bg='ivory',relief ='flat')
    canvas_main.pack()

    canvas_main.create_image(360,400, image=backImg)
    canvas_main.create_image(370,220, image=mainImg)
    canvas_main.create_text(360,50,text = "Every Meal Hamlet", font=('Tmon몬소리Black', 50, "bold"))

def make_signup2canvas(frame):
    canvas_signup2 = tk.Canvas(frame, width=1000, height=1000, bg='ivory',relief ='flat')
    canvas_signup2.pack()

    canvas_signup2.create_image(360,400, image=backImg)
    canvas_signup2.create_text(360,50,text = "선호하는 음식을 골라주세요(1/2)",font=('Tmon몬소리Black', 20, "bold"))

def make_signup3canvas(frame):
    canvas_signup2 = tk.Canvas(frame, width=1000, height=1000, bg='ivory',relief ='flat')
    canvas_signup2.pack()

    canvas_signup2.create_image(360,400, image=backImg)
    canvas_signup2.create_text(360,50,text = "선호하는 음식을 골라주세요(2/2)",font=('Tmon몬소리Black', 20, "bold"))
    
def func_confirm():
    pass

def f_signUp2(frame):
    frame.tkraise()


def f_signUp(frame):
    global  new_id, new_pw
    new_id = en_input_id.get()
    new_pw = en_input_pw.get()
    messagebox.showinfo("안내","다음창으로 넘어가 선호하는 메뉴를 선택해주세요.")

    en_input_id.delete(0,END)
    en_input_pw.delete(0,END)
    ent_pwconfirm.delete(0,END)
    switch_frame(frame_signup2)


def f_login(frame):
    global login_success_user_info
    accord_id = False
    accord_pw = False
    user_num = -1
    f = open('information_of_users.csv', mode='r', encoding="cp949")
    reader = csv.reader(f)

    for line in reader:
        user_info_list.append(line)

    user_id = en_user_id.get()
    user_pw = en_user_pw.get()
    for i in range(1,len(user_info_list)):
        if user_id == user_info_list[i][0]:
            accord_id = True
            user_num = i
            break
    for i in range(1,len(user_info_list)):
        print(user_info_list[i][0])


    for i in range(1,len(user_info_list)):
        if user_pw == user_info_list[i][1]:
            accord_pw = True
            user_num = i
            break

    if (accord_id == True) and (accord_pw == True):
        messagebox.showinfo("안내","환영합니다")
        login_success_user_info =  user_info_list[i][2]

    else:
        messagebox.showwarning("안내","id 또는 비밀번호를 확인해주세요")

    en_user_id.delete(0,END)
    en_user_pw.delete(0,END)
    switch_frame(frame_rec)
    f.close()


def f_menu_select(n):
    if n == 0:
        fv_food_list.append("떡볶이")
    elif n ==1 :
        fv_food_list.append("닭볶음탕")
    elif n == 2 :
        fv_food_list.append("고기")
    elif n == 3 :
        fv_food_list.append("밥")
    elif n == 4:
        fv_food_list.append("국밥")
    elif n == 5:
        fv_food_list.append("햄버거/치킨")
    elif n == 6:
        fv_food_list.append("피자")
    elif n == 7:
        fv_food_list.append("카레")
    elif n == 8:
        fv_food_list.append("초밥")
    elif n == 9 :
        fv_food_list.append("돈까스")
    elif n == 10 :
        fv_food_list.append("라멘")
    elif n ==11 :
        fv_food_list.append("밥")

        
def f_make_set():
    fv_food_set = set(fv_food_list)
    print(fv_food_set)
    f = open('information_of_users.csv', mode='a', encoding="cp949", newline='')
    writer = csv.writer(f)
    writer.writerow([new_id,new_pw,list(fv_food_set)])
    f.close()
    messagebox.showinfo("안내","선호하는 메뉴선택을 완료했습니다. 계속하시려면 로그인 해주세요")
    switch_frame(frame_login)

def user_select(n):
    if n == 1 :
        spicy = 2
        for i in range(len(f)):
            if f[i] == spicy:
                count[i] += 1
    elif n == 2:
        vet = 'o'
        if vet=='o':
            for i in range(len(c)):
                if c[i]=='o':
                    count[i]+=1
    elif n==3:
        ga = 'o'
        if ga=='o':
            for i in range(len(g)):
                if g[i]=='o':
                    count[i]+=1
            return count


def login_list():
    global count,user_food_list
    for j in range(len(user_food_list)):
        for i in range(len(d)):
            if str(user_food_list[j]).strip() in str(d[i]):
                count[i]+=1
                     
'''def counting_zero():                                         
    for i in range(len(count)):
        count[i]=0
        equal[i]=0
    return count


def restart():
    Spicy()
    print(count)
    Ga()
    print(count)
    Vet()
    print(count)
    Like()
    print(count)
    Max()
    print(max_count)
    total()
    
def Like():
    like=input('좋아하는 분야는?')             #좋아하는 분야,맵기,가성비,채식여부에 관한 함수들
                                               #만약 맵기는(1~3),가성비,채식여부에 o를 대입하면, o가 있는 음식점들이 count +1
                                               #o가아닌 다른 문자를 대입할시 o가 없는 음식점들에 count +1 
    if like in b:
        for i in range(len(a)):        
            if b[i]==like:
                count[i]+=3            
        return count
    elif like==None or not( like in b):
        return count


def Spicy():
    
    spicy=int(input('맵기를 선택하세요'))
    
    if 1<=spicy<=3:
        
        for i in range(len(f)):        
            if f[i]==spicy:
                count[i]+=1
        return count
        

           
def Ga():
    ga=input('가성비있게?')
    if ga=='o':
        for i in range(len(g)):
            if g[i]=='o':
                count[i]+=1
        return count

    elif not ga=='o':
        for i in range(len(g)):
            if g[i]!='o':
                count[i]+=1        
        return count

def Vet():
    vet=input('채식가능하게?')
    if vet=='o':
        for i in range(len(c)):
            if c[i]=='o':
                count[i]+=1
        return count

    elif not vet=='o':
        for i in range(len(c)):
            if c[i]=='o':
                count[i]+=1
        return count'''
    
def Max():                                #count가 가장 높은 음식점의 리스트 번호 출력
    global max_count,rand,equal
    for i in range(len(count)):        
        if count[i]==max(count):
            max_count=i
            

    return max_count

def Remove():                           #결과가 맘에 안들시, count가 가장 높은 음식점의 count를 없애고, 그 다음으로 높은 음식점 출력
    global max_count,rand
    count[max_count]=0

    for i in range(len(count)):
        if count[i]==max(count):
            max_count=i


    return max_count


def total():                                
    sum = 0
    messagebox.showinfo("안내","당신을 위한 추천 가게는 " +a[max_count]+"입니다.")


def menu_recommand():
    global user_food_list,login_success_user_info
    temp_user_food_list = login_success_user_info
    temp_user_food_list_2 = ""
    temp_user_food_list_3 = ""
    temp_user_food_list_4 = ""
    for i in range(len(temp_user_food_list)):
        if temp_user_food_list[i] != '\'':
            temp_user_food_list_2 += temp_user_food_list[i]
    temp_user_food_list_3 = temp_user_food_list_2.strip('\[')
    temp_user_food_list_4 = temp_user_food_list_3.strip('\]')
    temp_user_food_list_4 = temp_user_food_list_4.strip('\[')
    temp_user_food_list_4 = temp_user_food_list_4.strip('\]')
    user_food_list = temp_user_food_list_4.split(',')
    login_list()
    print(count)
    Max()
    total()
    Remove()


#----메인 윈도우 생성    
window = Tk()
window.title('Every Meal Hamlet')
window.geometry('720x940+500+0')
window.configure(bg='white')
#window.resizable(False, False)

mainImg = PhotoImage(file='coco2.png')
backImg = PhotoImage(file='back.png')

#----프레임 모음
frame_main = tk.Frame(window)
frame_login = tk.Frame(window)
frame_signup1 = tk.Frame(window)
frame_signup2 = tk.Frame(window)
frame_signup3 = tk.Frame(window)
frame_question = tk.Frame(window)
frame_rec = tk.Frame(window) 

frame_main.grid(row=0, column=0, sticky='nsew')
frame_login.grid(row=0, column=0, sticky='nsew')
frame_signup1.grid(row=0, column=0, sticky='nsew')
frame_signup2.grid(row=0, column=0, sticky='nsew')
frame_signup3.grid(row=0, column=0, sticky='nsew')
frame_question.grid(row=0, column=0, sticky='nsew')
frame_rec.grid(row=0, column=0, sticky='nsew')


#----메인 프레임 시작
make_maincanvas(frame_main)

#메인프레임 - 로그인 버튼
btn_gotologin = customtkinter.CTkButton(master=frame_main, text_font = ('Tmon몬소리Black', 30, 'bold'),
                                            text = '로그인', width = 300,
                                         fg_color=('white'), bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command=lambda: switch_frame(frame_login))
btn_gotologin.place(x=230, y=350)

#메인프레임 - 회원가입 버튼
btn_sign = customtkinter.CTkButton(master=frame_main, text_font = ('Tmon몬소리Black', 30, 'bold'),
                                            text = '회원가입', width = 300,
                                         fg_color=('white'), bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command=lambda: switch_frame(frame_signup1))
btn_sign.place(x=230, y=450)

#메인프레임 - 문의 버튼
btn_question = customtkinter.CTkButton(master=frame_main, text_font = ('Tmon몬소리Black', 30, 'bold'),
                                            text = '문의하기', width = 300,
                                         fg_color=('#85837F'), bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command=lambda: switch_frame(frame_question))
btn_question.place(x=230, y=550)

#----로그인프레임 시작
make_maincanvas(frame_login)

#아이디, 비밀번호 입력(함수 필요)
en_user_id = customtkinter.CTkEntry(master=frame_login,fg_color='white', text_font=('Tmon몬소리Black', 20, 'bold'),
                                        bg_color='#85837F',
                                        text_color = 'black', width=500, height=50, corner_radius=40)
en_user_id.place(x=110, y=350)

en_user_pw = customtkinter.CTkEntry(master=frame_login,fg_color='white', text_font=('Tmon몬소리Black', 20, 'bold'),
                                        bg_color='#85837F', 
                                        text_color = 'black', width=500, height=50, corner_radius=40, show = '*')
en_user_pw.place(x=110, y=450)

lb_id = tk.Label(frame_login, text = 'ID를 입력하세요', bg='#85837F', font=('Tmon몬소리Black',20,'bold'))
lb_id.place(x=270, y=310)

lb_pw = tk.Label(frame_login, text = 'PW를 입력하세요', bg='#85837F', font=('Tmon몬소리Black',20,'bold'))
lb_pw.place(x=270, y=410)
        
btn_login = customtkinter.CTkButton(master=frame_login, text_font = ('Tmon몬소리Black', 20, 'bold'),
                                            text = '로그인하기',
                                         fg_color=('#D9D9D9'), bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda: f_login(frame_rec))
btn_login.place(x=180, y=550)
        
btn_sign = customtkinter.CTkButton(master=frame_login, text_font = ('Tmon몬소리Black', 20, 'bold'),
                                            text = '메인으로 이동',
                                         fg_color='#85837F', bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda: switch_frame(frame_main))
btn_sign.place(x=350, y=550)


#----회원가입1 프레임 시작
make_maincanvas(frame_signup1)

#회원가입1 아이디
lb_id = tk.Label(frame_signup1, text = 'ID', bg='#85837F', font=('Tmon몬소리Black',20,'bold'))
lb_id.place(x=130, y=180)
        
en_input_id = customtkinter.CTkEntry(frame_signup1,fg_color='white', text_font=('Tmon몬소리Black', 20, 'bold'),
                                        bg_color='#85837F', 
                                        text_color = 'black', width=500, height=50, corner_radius=100)
en_input_id.place(x=110, y=220)

#회원가입1 비밀번호
lb_pw = tk.Label(frame_signup1, text = 'Passward', bg='#85837F', font=('Tmon몬소리Black',20,'bold'))
lb_pw.place(x=130, y=290)

en_input_pw = customtkinter.CTkEntry(frame_signup1,fg_color='white', text_font=('Tmon몬소리Black', 20, 'bold'),
                                        bg_color='#85837F', 
                                        text_color = 'black', width=500, height=50, corner_radius=40, show = '*')
en_input_pw.place(x=110, y=340)

#회원가입1 중복확인
lb_pw_confirm = tk.Label(frame_signup1, text = 'Passward Confirm', bg='#85837F', font=('Tmon몬소리Black',20,'bold'))
lb_pw_confirm.place(x=130, y=400)

ent_pwconfirm = customtkinter.CTkEntry(frame_signup1,fg_color='white', text_font=('Tmon몬소리Black', 20, 'bold'),
                                        bg_color='#85837F', 
                                        text_color = 'black', width=500, height=50, corner_radius=40, show = '*')
ent_pwconfirm.place(x=110, y=450)

#중복확인 버튼
btn_gotologin = customtkinter.CTkButton(master=frame_signup1, text_font = ('Tmon몬소리Black', 15, 'bold'),
                                            text = '중복확인',
                                         fg_color=('#85837F'), bg_color='white', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda: func_confirm())
btn_gotologin.place(x=480, y=230)

# 패스워드 확인 오류 레이블 - 적용함수 필요 / 현재는 구현이 힘들듯?
lb_confirm = tk.Label(frame_signup1, text = '', bg='#85837F',fg = 'orange',
                              font=('Tmon몬소리Black',12,'bold'))
lb_confirm.place(x=380, y=500)

# 기입 확인 버튼(확인을 눌렀을 때 패스워드 확인 오류 레이블에 비밀번호가 일치하지 않습니다.)
btn_confirm_next = customtkinter.CTkButton(master=frame_signup1, text_font = ('Tmon몬소리Black', 20, 'bold'),
                                            text = '확인',
                                         fg_color=('#D9D9D9'), bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda : f_signUp(frame_signup2))
btn_confirm_next.place(x=300, y=580)


#----회원가입2 프레임 시작
make_signup2canvas(frame_signup2)

food1_1 = tk.Button(frame_signup2, text = '떡볶이 img', width=30, height = 10, command = lambda:f_menu_select(0))
food1_1.place(x=100, y=150)

food1_2 = tk.Button(frame_signup2, text = '닭볶음탕 img', width=30, height = 10,command = lambda:f_menu_select(1))
food1_2.place(x=400, y=150)

food1_3 = tk.Button(frame_signup2, text = '고기 img',width=30, height = 10,command = lambda:f_menu_select(2))
food1_3.place(x=100, y=350)

food1_4 = tk.Button(frame_signup2, text = '밥 img', width=30, height = 10,command = lambda:f_menu_select(3))
food1_4.place(x=400, y=350)

food1_5 = tk.Button(frame_signup2, width=30, text = '국밥 img', height = 10,command = lambda:f_menu_select(4))
food1_5.place(x=100, y=550)

food1_6 = tk.Button(frame_signup2, width=30, text = '햄버거/치킨 img', height = 10,command = lambda:f_menu_select(5))
food1_6.place(x=400, y=550)

btn_confirm_next = customtkinter.CTkButton(master=frame_signup2, text_font = ('Tmon몬소리Black', 10, 'bold'),
                                            text = '다음',
                                         fg_color=('#D9D9D9'), bg_color='white', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda : switch_frame(frame_signup3))
btn_confirm_next.place(x=300, y=800)

#----회원가입3 프레임 시작
make_signup3canvas(frame_signup3)

food2_1 = tk.Button(frame_signup3, text = '피자 img', width=30, height = 10,command = lambda:f_menu_select(6))
food2_1.place(x=100, y=150)

food2_2 = tk.Button(frame_signup3, text = '카레 img', width=30, height = 10,command = lambda:f_menu_select(7))
food2_2.place(x=400, y=150)

food2_3 = tk.Button(frame_signup3, width=30, text = '초밥 img', height = 10,command = lambda:f_menu_select(8))
food2_3.place(x=100, y=350)

food2_4 = tk.Button(frame_signup3, width=30, text = '돈까스 img', height = 10,command = lambda:f_menu_select(9))
food2_4.place(x=400, y=350)

food2_5 = tk.Button(frame_signup3, width=30, text = '라멘 img', height = 10,command = lambda:f_menu_select(10))
food2_5.place(x=100, y=550)

food2_6 = tk.Button(frame_signup3, width=30, text = '밥 img', height = 10,command = lambda:f_menu_select(11))
food2_6.place(x=400, y=550)

btn_confirm_ok = customtkinter.CTkButton(master=frame_signup3, text_font = ('Tmon몬소리Black', 10, 'bold'),
                                            text = '완료',
                                         fg_color=('#D9D9D9'), bg_color='white', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda : f_make_set())

btn_confirm_ok.place(x=300, y=800)

#----추천 프레임
make_maincanvas(frame_rec)

cb1 = tk.Checkbutton(frame_rec,text="맵게",command = lambda : user_select(1),
                     width = 300)
cb2 = tk.Checkbutton(frame_rec,text="채식",command = lambda : user_select(2),
                     )
cb3 = tk.Checkbutton(frame_rec,text="가성비",command = lambda : user_select(3),
                     )
cb1.place(x=300, y=300)
cb2.place(x=300, y=400)
cb3.place(x=300, y=500)
btn_select = tk.Button(frame_rec,text = '추천',command = menu_recommand )
btn_select.place(x=300, y=600)

#----문의프레임
make_maincanvas(frame_question)
name1 = customtkinter.CTkLabel(frame_question, text="최형욱", text_font = ('Tmon몬소리Black', 30, 'bold'), width = 300, height = 50, fg_color='white', text_color = 'black', bg_color='#85837F')
name1.place(x=30,y=300)
name1 = customtkinter.CTkLabel(frame_question, text="최창은", text_font = ('Tmon몬소리Black', 30, 'bold'), width = 300, height = 50, fg_color='white', text_color = 'black', bg_color='#85837F')
name1.place(x=380,y=300)
name1 = customtkinter.CTkLabel(frame_question, text="유수현", text_font = ('Tmon몬소리Black', 30, 'bold'), width = 300, height = 50, fg_color='white', text_color = 'black', bg_color='#85837F')
name1.place(x=30,y=400)
name1 = customtkinter.CTkLabel(frame_question, text="김유섭", text_font = ('Tmon몬소리Black', 30, 'bold'), width = 300, height = 50, fg_color='white', text_color = 'black', bg_color='#85837F')
name1.place(x=380,y=400)
name1 = customtkinter.CTkLabel(frame_question, text="천진희", text_font = ('Tmon몬소리Black', 30, 'bold'), width = 300, height = 50, fg_color='white', text_color = 'black', bg_color='#85837F')
name1.place(x=220,y=500)

btn_confirm_back = customtkinter.CTkButton(master=frame_question, text_font = ('Tmon몬소리Black', 20, 'bold'),
                                            text = '돌아가기',
                                         fg_color=('white'), bg_color='#85837F', text_color = 'black', hover_color='skyblue',
                                         corner_radius=40, command = lambda : switch_frame(frame_main))

btn_confirm_back.place(x=300, y=600)

#----실행
switch_frame(frame_main)
window.mainloop()
