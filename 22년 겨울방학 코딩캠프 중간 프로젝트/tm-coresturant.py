# 2022.02.09 8일차 팀 프로젝트(GUI만들기)

# gui 버전  기능구현
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import csv
import tkinter.font as tkFont
import datetime

price = {'Salad': 8000, 'Soup': 6000, 'Bread': 3000, 'Han-u Steak': 110000, 'Rib': 60000}
key_list = list(price.keys())
value_list = list(price.values())
menu_count_list= [0,0,0,0,0]
csv_list = []
sum,coupon_code,use_coupon,excel_non_exist = 0 , 12345,'n',True
empty = False


# 메뉴추가
def storeOpen():
    global sum,use_coupon
    for i in range(len(menu_count_list)):
        menu_count_list[i] =0
    sum = 0
    use_coupon = 'n'
    if check_list():
        listbox.delete(0, END)
        ent_cupon.delete(0, END)
        for j in range(len(lb_list)):
            lb_list[j].config(text = menu_count_list[i])
    label = messagebox.showinfo("주문화면", "주문을 초기화 합니다.")

def custopen():
    label = messagebox.showinfo("고객조회", "준비중입니다.")

def fexit():
    label = messagebox.showinfo("Quit", "Quit?")
    window.destroy()

def fabout():
    label = messagebox.showinfo("About", "Co'resturant")

def save():
    pass

def btn_sub(n):  # 메뉴 수량 감소 함수
    global sum
    if n == 1:
        if menu_count_list[0] <= 0:
            return
        menu_count_list[0] -= 1
        sum -= value_list[0]
        lbl_cnt1.config(text=menu_count_list[0])
    elif n == 2:
        if menu_count_list[1] <= 0:
            return
        menu_count_list[1] -= 1
        sum -= value_list[1]
        lbl_cnt2.config(text=menu_count_list[1])
    elif n == 3:
        if menu_count_list[2] <= 0:
            return
        menu_count_list[2] -= 1
        sum -= value_list[2]
        lbl_cnt3.config(text=menu_count_list[2])
    elif n == 4:
        if menu_count_list[3] <= 0:
            return
        menu_count_list[3] -= 1
        sum -= value_list[3]
        lbl_cnt4.config(text=menu_count_list[3])
    elif n == 5:
        if menu_count_list[4] <= 0:
            return
        menu_count_list[4] -= 1
        sum -= value_list[4]
        lbl_cnt5.config(text=menu_count_list[4])
    print(sum)
    print(menu_count_list)
def btn_plus(n):  # 메뉴 수량 추가 함수
    global sum
    if n == 1:
        menu_count_list[0] += 1
        sum += value_list[0]
        lbl_cnt1.config(text=menu_count_list[0])
    elif n == 2:
        menu_count_list[1] += 1
        sum += value_list[1]
        lbl_cnt2.config(text=menu_count_list[1])
    elif n == 3:
        menu_count_list[2] += 1
        sum += value_list[2]
        lbl_cnt3.config(text=menu_count_list[2])
    elif n == 4:
        menu_count_list[3] += 1
        sum += value_list[3]
        lbl_cnt4.config(text=menu_count_list[3])
    elif n == 5:
        menu_count_list[4] += 1
        sum += value_list[4]
        lbl_cnt5.config(text=menu_count_list[4])
    print(sum)
    print(menu_count_list)
def check_list(): # 리스트가 전부 비어 있는지 확인하는 함수 비이있다면 True 반환
    for j in menu_count_list:
        if j != 0:
            return
    return True

def lbl_cnt():  # 주문내역을 보여주는 함수
    listbox.delete(0,END)
    if check_list():
        messagebox.showinfo("안내", "메뉴를 선택해 주세요.")
        listbox.delete(0, END)
        ent_cupon.delete(0, END)
        return
    j = 0
    for i in menu_count_list:
        if i == 0:
            j += 1
            continue
        s = key_list[j] +' '+ str(i) + '개 : ' + str(value_list[j] * i) + '원'
        listbox.insert(END,s)
        j+=1
    listbox.insert(END,"총 "+str(sum)+"원 입니다.")

def func_cupon_use():# 쿠폰 사용 확인 함수
    global sum,empty,use_coupon
    if check_list():
        messagebox.showinfo("안내", "메뉴를 선택해 주세요.")
        ent_cupon.delete(0, END)
        listbox.delete(0, END)
        return
    if use_coupon == 'y':
        messagebox.showinfo("안내", "이미 쿠폰할인이 적용되었습니다.")
        return
    if str(coupon_code) == ent_cupon.get():
        use_coupon ='y'
        sum *= 0.8
        sum = int(sum)
        listbox.delete(0, END)
        j = 0
        for i in menu_count_list:
            if i == 0:
                j += 1
                continue
            s = key_list[j] + ' ' + str(i) + '개 : ' + str(value_list[j] * i) + '원'
            listbox.insert(END, s)
            j += 1
        listbox.insert(END, "총 " + str(sum) + "원 입니다.")
        messagebox.showinfo("안내","20% 할인이 적용되었습니다!!")
    else :
        messagebox.showinfo("안내", "쿠폰코드가 일치하지 않습니다.")
        ent_cupon.delete(0,END)
        use_coupon ='n'


def func_order():  # 주문하기 함수
    global sum,empty
    if check_list():
        messagebox.showinfo("안내","메뉴를 선택해 주세요.")
        listbox.delete(0, END)
        ent_cupon.delete(0, END)
    else:
        messagebox.showinfo("안내", "총 " + str(sum) + "원 입니다.")
        for i in range(len(menu_count_list)):
            csv_list.append([key_list[i], menu_count_list[i], value_list[i] * menu_count_list[i]])
            menu_count_list[i] = 0
            lb_list[i].config(text=menu_count_list[i])
        d_csv(csv_list)
        sum = 0
        listbox.delete(0, END)
        ent_cupon.delete(0, END)



def func_exit():  # 종료하기  함수
    messagebox.showinfo("안내", "프로그램을 종료합니다.")
    exit()

def d_csv(pr_csv_list):
    global sum,use_coupon,excel_non_exist
    if excel_non_exist:
        f = open('매출기록.csv', mode='wt', encoding="cp949", newline='')
        writer = csv.writer(f)
        writer.writerow(["Date", "품명","수량", "가격", "할인율"])
        f.close()
        excel_non_exist = False

    f = open('매출기록.csv', mode='a', encoding="cp949", newline='')
    writer = csv.writer(f)
    now_time = datetime.datetime.now()
    for i in pr_csv_list:
        i.insert(0,now_time)
        if use_coupon =='y':
            i.insert(4,'20')
        writer.writerow(i)
    f.close()
    use_coupon = 'n'
    csv_list.clear()

def sal(event):
    messagebox.showinfo("salad", """신선한 양상추, 아보카도와 발사믹 베이스 소스.""")

def soup(event):
    messagebox.showinfo("soup", """송로버섯 슬라이스를 곁들인 수프""")

def br(event):
    messagebox.showinfo("bread", """갓 구운 또르띠야에 토마토와 양상추, 양파를 넣고
돼지고기를 듬뿍 넣어 만든 타코""")

def best(event):
    messagebox.showinfo("Han-u steak", """-기본 시즈닝에 특제 소스를 곁들인 1++한우 스테이크,
그런데 레드와인 숙성을 곁들인...""")

def reco(event):
    messagebox.showinfo("Rib", """버터에 구운 옥수수와 3가지 종류의 디핑소스,
신선한 토마토로 장식한 오픈에서 갓 구운 립.
그런데 특제 시즈닝에 장시간 훈연을 한...""")




window = Tk()
window.title('Co Resturant')
window.geometry("400x770")
window.configure(bg='white')
window.resizable(False, False)

# ----메뉴 추가
fmenu = Menu(window)
window.config(menu=fmenu)

filemenu = Menu(fmenu)
fmenu.add_cascade(label="Home",  menu=filemenu)
filemenu.add_command(label="매장주문화면", command=storeOpen)
filemenu.add_command(label="고객목록화면", command=custopen)
filemenu.add_command(label="주문내역저장", command=save)
filemenu.add_command(label="Quit", command=fexit)

helpmenu = Menu(fmenu)
fmenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=fabout)

# ----레스토랑 배너
welcome = PhotoImage(file='welcome.png')
lbl_img_wel = Label(window, image=welcome, background='white', relief='solid')
lbl_img_wel.place(x=5, y=0)

# ---- 메뉴 이름 레이블
menu_font = tkFont.Font(family='나눔고딕코딩', size=12, weight='bold')

lbl_menu1 = Label(window, text='1. Salad', justify='right', background='white', font=menu_font)
lbl_menu2 = Label(window, text='2. Soup', justify='left', background='white', font=menu_font)
lbl_menu3 = Label(window, text='3. Bread', justify='left', background='white', font=menu_font)
lbl_menu4 = Label(window, text='4. Han-u Steak', justify='left', background='white', font=menu_font)
lbl_menu5 = Label(window, text='5. Rib', justify='left', background='white', font=menu_font)
lbl_menu1.place(x=100, y=70)
lbl_menu2.place(x=100, y=170)
lbl_menu3.place(x=100, y=270)
lbl_menu4.place(x=100, y=370)
lbl_menu5.place(x=100, y=470)

# ---- 메뉴 가격 레이블
price_font = tkFont.Font(family='나눔고딕코딩', size=12)

lbl_price1 = Label(window, text='8.0', justify='right', background='white', font=price_font)
lbl_price2 = Label(window, text='6.0', justify='left', background='white', font=price_font)
lbl_price3 = Label(window, text='3.0', justify='left', background='white', font=price_font)
lbl_price4 = Label(window, text='110.0', justify='left', background='white', font=price_font)
lbl_price5 = Label(window, text='60.0', justify='left', background='white', font=price_font)
lbl_price1.place(x=125, y=95)
lbl_price2.place(x=125, y=195)
lbl_price3.place(x=125, y=295)
lbl_price4.place(x=125, y=395)
lbl_price5.place(x=125, y=495)

# ----1번 메뉴추가 감소 버튼, 레이블
btn_menu1_sub = Button(window, text='-', command=lambda: btn_sub(1))
btn_menu1_plus = Button(window, text='+', command=lambda: btn_plus(1))
lbl_cnt1 = Label(window, text = menu_count_list[0], background='white')
lbl_cnt1.place(x=323, y=70)
btn_menu1_sub.place(x=300, y=70)
btn_menu1_plus.place(x=340, y=70)

# ----2번 메뉴추가 감소 버튼, 레이블
btn_menu2_sub = Button(window, text='-', command=lambda: btn_sub(2))
btn_menu2_plus = Button(window, text='+', command=lambda: btn_plus(2))
lbl_cnt2 = Label(window, text = menu_count_list[1], background='white')
lbl_cnt2.place(x=323, y=170)
btn_menu2_sub.place(x=300, y=170)
btn_menu2_plus.place(x=340, y=170)

# ----3번 메뉴추가 감소 버튼, 레이블
btn_menu3_sub = Button(window, text='-', command=lambda: btn_sub(3))
btn_menu3_plus = Button(window, text='+', command=lambda: btn_plus(3))
lbl_cnt3 = Label(window, text = menu_count_list[2], background='white')
lbl_cnt3.place(x=323, y=270)
btn_menu3_sub.place(x=300, y=270)
btn_menu3_plus.place(x=340, y=270)

# ----4번 메뉴추가 감소 버튼, 레이블
btn_menu4_sub = Button(window, text='-', command=lambda: btn_sub(4))
btn_menu4_plus = Button(window, text='+', command=lambda: btn_plus(4))
lbl_cnt4 = Label(window, text = menu_count_list[3], background='white')
lbl_cnt4.place(x=323, y=370)
btn_menu4_sub.place(x=300, y=370)
btn_menu4_plus.place(x=340, y=370)

# ----5번 메뉴추가 감소 버튼, 레이블
btn_menu5_sub = Button(window, text='-', command=lambda: btn_sub(5))
btn_menu5_plus = Button(window, text='+', command=lambda: btn_plus(5))
lbl_cnt5 = Label(window, text = menu_count_list[4], background='white')
lbl_cnt5.place(x=323, y=470)
btn_menu5_sub.place(x=300, y=470)
btn_menu5_plus.place(x=340, y=470)

# ---- 메뉴 레이블을 리스트화

lb_list = [lbl_cnt1,lbl_cnt2,lbl_cnt3,lbl_cnt4,lbl_cnt5]

# ----주문 내역, 쿠폰 입력 칸
lbl_oderview = Label(window, text='주문 내역', background='white')
lbl_oderview.place(x=165, y=525)

'''ent_orderview = Text(window, width=45, height=5)
ent_orderview.place(x=40, y=550)'''
listbox = Listbox(window,width=40, height=6)
listbox.place(x=40, y=550)

btn_oderview = Button(window, text='확인', command=lbl_cnt)  # 쿠폰 사용 확인함수 필요
btn_oderview.place(x=340, y=550)



lbl_cupon = Label(window, text='쿠폰을 입력해주세요', background='white')
lbl_cupon.place(x=140, y=650)

btn_cupon_use = Button(window, text='확인', command=func_cupon_use)  # 쿠폰 사용 확인함수 필요
btn_cupon_use.place(x=340, y=675)

ent_cupon = Entry(window, text='', width=40)
ent_cupon.place(x=40, y=675)

# ----주문하기, 종료하기 버튼
helv15 = tkFont.Font(family='나눔고딕코딩', size=15, weight='bold')

btn_order = Button(window, text='주문하기', font=helv15, command=func_order)  # 주문하기 함수 필요
btn_order.place(x=70, y=720)

btn_exit = Button(window, text='종료하기', font=helv15, command=func_exit)  # 종료하기 함수 필요
btn_exit.place(x=230, y=720)


#----메뉴 이미지 클릭
photo1=PhotoImage(file='menu1_salad.png')
label_sal=Label(window, image= photo1)
label_sal.bind("<Double-Button>", sal)
label_sal.config(bg='white')
label_sal.place(x=10, y= 60)

photo2=PhotoImage(file='menu2_soup.png')
label_soup=Label(window, image= photo2)
label_soup.bind("<Double-Button>", soup)
label_soup.config(bg='white')
label_soup.place(x=0, y= 160)


photo3=PhotoImage(file='menu3_bread.png')
label_br=Label(window, image= photo3)
label_br.bind("<Double-Button>", br)
label_br.config(bg='white')
label_br.place(x=10, y= 260)


photo4=PhotoImage(file='menu4_steak.png')
label_best=Label(window, image= photo4)
label_best.bind("<Double-Button>", best)
# label_best.grid(row=22, column=0, columnspan=1)
label_best.config(bg='white')
label_best.place(x=10, y= 360)

photo5=PhotoImage(file='menu5_rib.png')
label_reco=Label(window, image= photo5)
label_reco.bind("<Double-Button>", reco)
# label_reco.grid(row=18, column=0, rowspan=19)
label_reco.config(bg='white')
label_reco.place(x=10, y= 460)


# ----종료
window.mainloop()
