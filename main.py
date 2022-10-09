import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter.simpledialog import askinteger, askfloat
from tkinter.messagebox import askyesno
import re

def BMI():
    height = askfloat(title="Height", prompt='请输入您的身高(cm):')
    weight = askfloat(title="Weight", prompt='请输入您的体重(kg):')
    global BMI_result
    BMI_result=round(weight/((height/100)**2),2)
    if BMI_result<18.5:
        state="(过轻)"
    if BMI_result>=18.5 and BMI_result<24:
        state="(健康)"
    if  BMI_result>=24 and BMI_result<28:
        state="(超重)"
    if BMI_result>=28:
        state="(肥胖)"
    info = '您的BMI为:'+str(BMI_result)+state
    BMI_present.set(''.join('BMI:'+str(BMI_result)))
    tk.messagebox.showinfo(title='BMI',message=info)

def BMR():
    sex = askyesno(title="Sex", message="您的性别是女性吗")
    age = askinteger(title="Age", prompt='请输入您的年龄(岁):')
    height = askfloat(title="Height", prompt='请输入您的身高(cm):')
    weight = askfloat(title="Weight", prompt='请输入您的体重(kg):')
    global BMR_result
    if sex:#男性
        BMR_result = int(10*weight+6.25*height-5*age-161)
    else:
        BMR_result = int(10*weight+6.25*height-5*age+5)
    info = '您的基础代谢估计值为:' + str(BMR_result)+'Kcal'
    BMR_present.set(''.join('基础代谢:' + str(BMR_result))+' Kcal')
    tk.messagebox.showinfo(title='基础代谢', message=info)

def run():
    weight = askfloat(title="Weight", prompt='请输入您的体重(kg):')
    distance = askfloat(title="Distance", prompt="请输入跑步总距离(km):")
    time = askfloat(title="Time", prompt='请输入跑步总时长(min):')
    global run_result
    run_result=int(weight*(time/60)*30/(time/distance/2.5))
    info = '您的跑步热量消耗估计值为:' + str(run_result) + 'Kcal'
    run_present.set(''.join('跑步:' + str(run_result)) + ' Kcal')
    tk.messagebox.showinfo(title='跑步', message=info)

def jump():
    weight = askfloat(title="Weight", prompt='请输入您的体重(kg):')
    count = askfloat(title="Count", prompt="请输入跳绳数量(个):")
    time = askfloat(title="Time", prompt='请输入跳绳总时长(min):')
    v=count/time
    if v<100:
        MET=8.8
    elif v>=100 and v<120:
        MET=11.8
    else:
        MET=12.3
    global jump_result
    jump_result = int(time*MET*weight*3.5/200)
    info = '您的跳绳热量消耗估计值为:' + str(jump_result) + 'Kcal'
    jump_present.set(''.join('跳绳:' + str(jump_result)) + ' Kcal')
    tk.messagebox.showinfo(title='跳绳', message=info)
def bike():
    weight = askfloat(title="Weight", prompt='请输入您的体重(kg):')
    distance= askfloat(title="Distance", prompt="请输入骑行距离(km):")
    time = askfloat(title="Time", prompt='请输入骑行总时长(min):')
    v = distance/time*60 #km/h
    if v < 10:
        HET = 300
    elif v >=10 and v < 15:
        HET = 380
    elif v>=15 and v<20:
        HET = 600
    elif v>=20 and v<25:
        HET = 820
    elif v>=25:
        HET = 1050
    global bike_result
    bike_result = int(weight/65*HET*time/60)
    info = '您的骑行热量消耗估计值为:' + str(bike_result) + 'Kcal'
    bike_present.set(''.join('骑行:' + str(bike_result)) + ' Kcal')
    tk.messagebox.showinfo(title='骑行', message=info)
def sportsum():
    global sportsum_kcal
    run = re.findall("\d+\.?\d*", run_present.get())
    jump = re.findall("\d+\.?\d*", jump_present.get())
    bike = re.findall("\d+\.?\d*", bike_present.get())
    sportsum_kcal = int(run[0]) + int(jump[0]) + int(bike[0])
    sportsum_present.set(''.join('运动日计:' + str(sportsum_kcal)) + ' Kcal')


def morning():
    def choose(i):
        cheakboxs[i] = True
    def send(foods, heats, cheakboxs):
        info = ""
        sum = 0
        numbers = [2,1,1,1,1,1,1]
        for j in cheakboxs.keys():
            info += foods[j] + "\t" + ": " + str(
                heats[j] * numbers[j]) + " Kcal" + "\n"
            sum += heats[j] * numbers[j]
        info = info + "总计\t: " + str(sum) + " Kcal"
        morning_present.set(''.join('早餐:' + str(sum)) + ' Kcal')
        tk.messagebox.showinfo(title='早餐热量明细', message=info)

    morning_window = tk.Tk()
    morning_window.title('早餐')
    label = tk.Label(morning_window,text="请选择您的早餐组成", bg="lightyellow", fg="red",width=18)
    label.grid(row=0)

    foods = {0: "糕团类", 1: "粉面类", 2: "粥汤类", 3: "炸物", 4:"坚果类",5: "奶制品",6: "蛋类"}
    heats = {0:100,1:300,2:75,3:250,4:50,5:30,6:30}
    cheakboxs = {}
    tkinter.Checkbutton(morning_window, text=foods[0],command=lambda:choose(0)).grid(row=0 + 1, sticky=tkinter.W)
    tkinter.Checkbutton(morning_window, text=foods[1],command=lambda: choose(1)).grid(row=1 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(morning_window, text=foods[2],command=lambda: choose(2)).grid(row=2 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(morning_window, text=foods[3],command=lambda: choose(3)).grid(row=3 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(morning_window, text=foods[4],command=lambda: choose(4)).grid(row=4 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(morning_window, text=foods[5],command=lambda: choose(5)).grid(row=5 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(morning_window, text=foods[6], command=lambda: choose(6)).grid(row=6 + 1,sticky=tkinter.W)

    number0 = tk.StringVar()
    combobox0 = ttk.Combobox(morning_window,textvariable=number0,value=('50克','100克','150克','200克','250克'))
    combobox0.grid(row=1, column=1)
    number1 = tk.StringVar()
    combobox1 = ttk.Combobox(morning_window, textvariable=number1,value=("1份", "2份", "3份", "4份", "5份"))
    combobox1.grid(row=2, column=1)
    number2 = tk.StringVar()
    combobox2 = ttk.Combobox(morning_window, textvariable=number2,value=("1份", "2份", "3份", "4份", "5份"))
    combobox2.grid(row=3, column=1)
    number3 = tk.StringVar()
    combobox3 = ttk.Combobox(morning_window, textvariable=number3,value=('50克','100克','150克','200克','250克'))
    combobox3.grid(row=4, column=1)
    number4 = tk.StringVar()
    combobox4 = ttk.Combobox(morning_window, textvariable=number4,value=('20克', '40克', '60克', '80克', '100克'))
    combobox4.grid(row=5, column=1)
    number5 = tk.StringVar()
    combobox5 = ttk.Combobox(morning_window, textvariable=number5,value=('100ml', '200ml', '300ml', '400ml', '500ml'))
    combobox5.grid(row=6, column=1)
    number6 = tk.StringVar()
    combobox6 = ttk.Combobox(morning_window, textvariable=number6,value=("1份", "2份", "3份", "4份", "5份"))
    combobox6.grid(row=7, column=1)

    button = tk.Button(morning_window, text="确定", width=10,command=lambda: send(foods, heats, cheakboxs))
    button.grid(row=len(foods) + 1)
    morning_window.mainloop()

def noon():
    def choose(i):
        cheakboxs[i] = True
    def send(foods, heats, cheakboxs):
        info = ""
        sum = 0
        numbers = [2,1,1,1,1]
        for j in cheakboxs.keys():
            info += foods[j] + "\t" + ": " + str(
                heats[j] * numbers[j]) + " Kcal" + "\n"
            sum += heats[j] * numbers[j]
        info = info + "总计\t: " + str(sum) + " Kcal"
        noon_present.set(''.join('午餐:' + str(sum)) + ' Kcal')
        tk.messagebox.showinfo(title='午餐热量明细', message=info)

    noon_window = tk.Tk()
    noon_window.title('午餐')
    label = tk.Label(noon_window,text="请选择您的午餐组成", bg="lightyellow", fg="red",width=18)
    label.grid(row=0)

    foods = {0: "肉菜", 1: "素菜", 2: "粥汤", 3: "水果", 4:"面食"}
    heats = {0:250,1:100,2:50,3:15,4:120}
    cheakboxs = {}
    tkinter.Checkbutton(noon_window, text=foods[0], command=lambda:choose(0)).grid(row=0 + 1, sticky=tkinter.W)
    tkinter.Checkbutton(noon_window, text=foods[1],command=lambda: choose(1)).grid(row=1 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(noon_window, text=foods[2],command=lambda: choose(2)).grid(row=2 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(noon_window, text=foods[3],command=lambda: choose(3)).grid(row=3 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(noon_window, text=foods[4],command=lambda: choose(4)).grid(row=4 + 1,sticky=tkinter.W)


    number0 = tk.StringVar()
    combobox0 = ttk.Combobox(noon_window,textvariable=number0,value=("1份", "2份", "3份", "4份", "5份"))
    combobox0.grid(row=1, column=1)
    number1 = tk.StringVar()
    combobox1 = ttk.Combobox(noon_window, textvariable=number1,value=("1份", "2份", "3份", "4份", "5份"))
    combobox1.grid(row=2, column=1)
    number2 = tk.StringVar()
    combobox2 = ttk.Combobox(noon_window, textvariable=number2,value=("1份", "2份", "3份", "4份", "5份"))
    combobox2.grid(row=3, column=1)
    number3 = tk.StringVar()
    combobox3 = ttk.Combobox(noon_window, textvariable=number3,value=("50克", "100克", "150克", "200克", "250克"))
    combobox3.grid(row=4, column=1)
    number4 = tk.StringVar()
    combobox4 = ttk.Combobox(noon_window, textvariable=number4,value=("1份", "2份", "3份", "4份", "5份"))
    combobox4.grid(row=5, column=1)



    button = tk.Button(noon_window, text="确定", width=10,command=lambda: send(foods, heats, cheakboxs))
    button.grid(row=len(foods) + 1)
    noon_window.mainloop()

def night():
    def choose(i):
        cheakboxs[i] = True
    def send(foods, heats, cheakboxs):
        info = ""
        sum = 0
        numbers = [2,2,1,2,1]
        for j in cheakboxs.keys():
            info += foods[j] + "\t" + ": " + str(
                heats[j] * numbers[j]) + " Kcal" + "\n"
            sum += heats[j] * numbers[j]
        info = info + "总计\t: " + str(sum) + " Kcal"
        night_present.set(''.join('晚餐:' + str(sum)) + ' Kcal')
        tk.messagebox.showinfo(title='晚餐热量明细', message=info)

    night_window = tk.Tk()
    night_window.title('晚餐')
    label = tk.Label(night_window,text="请选择您的晚餐组成", bg="lightyellow", fg="red",width=18)
    label.grid(row=0)

    foods = {0: "肉菜", 1: "素菜", 2: "粥汤", 3: "水果", 4:"面食"}
    heats = {0:250,1:100,2:50,3:15,4:120}
    cheakboxs = {}
    tkinter.Checkbutton(night_window, text=foods[0], command=lambda:choose(0)).grid(row=0 + 1, sticky=tkinter.W)
    tkinter.Checkbutton(night_window, text=foods[1],command=lambda: choose(1)).grid(row=1 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(night_window, text=foods[2],command=lambda: choose(2)).grid(row=2 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(night_window, text=foods[3],command=lambda: choose(3)).grid(row=3 + 1,sticky=tkinter.W)
    tkinter.Checkbutton(night_window, text=foods[4],command=lambda: choose(4)).grid(row=4 + 1,sticky=tkinter.W)


    number0 = tk.StringVar()
    combobox0 = ttk.Combobox(night_window,textvariable=number0,value=("1份", "2份", "3份", "4份", "5份"))
    combobox0.grid(row=1, column=1)
    number1 = tk.StringVar()
    combobox1 = ttk.Combobox(night_window, textvariable=number1,value=("1份", "2份", "3份", "4份", "5份"))
    combobox1.grid(row=2, column=1)
    number2 = tk.StringVar()
    combobox2 = ttk.Combobox(night_window, textvariable=number2,value=("1份", "2份", "3份", "4份", "5份"))
    combobox2.grid(row=3, column=1)
    number3 = tk.StringVar()
    combobox3 = ttk.Combobox(night_window, textvariable=number3,value=("50克", "100克", "150克", "200克", "250克"))
    combobox3.grid(row=4, column=1)
    number4 = tk.StringVar()
    combobox4 = ttk.Combobox(night_window, textvariable=number4,value=("1份", "2份", "3份", "4份", "5份"))
    combobox4.grid(row=5, column=1)



    button = tk.Button(night_window, text="确定", width=10,command=lambda: send(foods, heats, cheakboxs))
    button.grid(row=len(foods) + 1)
    night_window.mainloop()

def eatsum():
    global eatsum_kcal
    morning=re.findall("\d+\.?\d*", morning_present.get())
    noon=re.findall("\d+\.?\d*", noon_present.get())
    night=re.findall("\d+\.?\d*", night_present.get())
    eatsum_kcal=int(morning[0])+int(noon[0])+int(night[0])
    eatsum_present.set(''.join('餐食日计:' + str(eatsum_kcal)) + ' Kcal')

def zhishu():
    daily_zhishu=int((sportsum_kcal+BMR_result-eatsum_kcal)*(BMI_result-21.2)/9)
    zhishu_present.set(''.join('今日健康指数:' + str(daily_zhishu)))
# 界面
root = tk.Tk()
root.title('健康膳食计算器')
root.geometry("420x285+250+250")#窗口大小和初始位置
root.attributes('-alpha',0.85)#透明度
root['background']='#2F4F4F'#背景颜色/图片

label1 = tk.Label(root, text="",width=40,height=1,font=("宋体",20),justify="center",background="#ABCDEF")
label1.grid(row=2,column=0,columnspan=40)

# 按钮
BMI_present = tk.StringVar()
BMI_present.set("BMI:/")
button_BMI=tk.Button(root,textvariable=BMI_present,width=16,font=("宋体",16),background='#C0C0C0', command=lambda: BMI())

BMR_present = tk.StringVar()
BMR_present.set("基础代谢:/")
button_BMR=tk.Button(root,textvariable=BMR_present,width=20,font=("宋体",16),background='#C0C0C0', command=lambda: BMR())

run_present = tk.StringVar()
run_present.set("跑步:/")
button_run=tk.Button(root,textvariable=run_present,width=20,font=("宋体",16),background='#C0C0C0', command=lambda: run())

jump_present = tk.StringVar()
jump_present.set("跳绳:/")
button_jump=tk.Button(root,textvariable=jump_present,width=20,font=("宋体",16),background='#C0C0C0', command=lambda: jump())

bike_present = tk.StringVar()
bike_present.set("骑行:/")
button_biking=tk.Button(root,textvariable=bike_present,width=20,font=("宋体",16),background='#C0C0C0', command=lambda: bike())

sportsum_present = tk.StringVar()
sportsum_present.set("运动日计:/")
button_sportsum=tk.Button(root,textvariable=sportsum_present,width=20,font=("宋体",16),background='#C0C0C0',command=lambda: sportsum())

morning_present = tk.StringVar()
morning_present.set("早餐:/")
button_moring=tk.Button(root,textvariable=morning_present,width=16,font=("宋体",16),background='#C0C0C0',command=lambda: morning())

noon_present = tk.StringVar()
noon_present.set("午餐:/")
button_noon=tk.Button(root,textvariable=noon_present,width=16,font=("宋体",16),background='#C0C0C0',command=lambda: noon())

night_present = tk.StringVar()
night_present.set("晚餐:/")
button_night=tk.Button(root,textvariable=night_present,width=16,font=("宋体",16),background='#C0C0C0',command=lambda: night())

eatsum_present = tk.StringVar()
eatsum_present.set("餐食日计:/")
button_eatsum=tk.Button(root,textvariable=eatsum_present,width=16,font=("宋体",16),background='#C0C0C0',command=lambda: eatsum())

zhishu_present = tk.StringVar()
zhishu_present.set("今日健康指数:/")
button_zhishu=tk.Button(root,textvariable=zhishu_present,width=25,font=("宋体",16),background='#C0C0C0',command=lambda: zhishu())

button_BMI.grid(ipadx=4,row=1,column=0)
button_BMR.grid(ipadx=4,row=1,column=1)

button_run.grid(ipadx=4,row=3,column=1)
button_jump.grid(ipadx=4,row=4,column=1)
button_biking.grid(ipadx=4,row=5,column=1)
button_sportsum.grid(ipadx=4,row=6,column=1)

button_moring.grid(ipadx=4,row=3,column=0)
button_noon.grid(ipadx=4,row=4,column=0)
button_night.grid(ipadx=4,row=5,column=0)
button_eatsum.grid(ipadx=4,row=6,column=0)

button_zhishu.grid(ipadx=4,row=7,column=0,columnspan=2)

#循环消息
root.mainloop()
