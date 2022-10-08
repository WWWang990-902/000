import tkinter as tk
import tkinter.messagebox
from tkinter.simpledialog import askinteger, askfloat
from tkinter.messagebox import askyesno

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
    BMR_present.set(''.join('基础代谢:' + str(BMR_result))+'Kcal')
    tk.messagebox.showinfo(title='基础代谢', message=info)

def run():
    pass
def jump():
    pass
def biking():
    pass




# 界面
root = tk.Tk()
root.title('健康计算器')
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

button_run=tk.Button(root,text="跑步:/",width=20,font=("宋体",16),background='#C0C0C0', command=lambda: run())
button_jump=tk.Button(root,text="跳绳:/",width=20,font=("宋体",16),background='#C0C0C0', command=lambda: jump())
button_biking=tk.Button(root,text="骑行:/",width=20,font=("宋体",16),background='#C0C0C0', command=lambda: biking())
button_sportsum=tk.Button(root,text="运动日计:/",width=20,font=("宋体",16),background='#C0C0C0')

button_moring=tk.Button(root,text="早餐:/",width=16,font=("宋体",16),background='#C0C0C0')
button_noon=tk.Button(root,text="午餐:/",width=16,font=("宋体",16),background='#C0C0C0')
button_night=tk.Button(root,text="晚餐:/",width=16,font=("宋体",16),background='#C0C0C0')
button_eatsum=tk.Button(root,text="餐食日计:/",width=16,font=("宋体",16),background='#C0C0C0')

button_num=tk.Button(root,text="健康指数:/",width=25,font=("宋体",16),background='#C0C0C0',command=lambda: num())

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
button_num.grid(ipadx=4,row=7,column=0,columnspan=2)

#循环消息
root.mainloop()
