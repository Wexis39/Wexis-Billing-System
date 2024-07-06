import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import datetime
import time

form = tk.Tk()

form.title('Login App')

form.geometry('550x400+650+300')

form.resizable(width=False,height=False)

form.configure(bg='#76e698')

currentDate = datetime.datetime.now().date()

values = {}

valuesX = {}

def toplevel1():
    toplevelform = tk.Toplevel(form)
    toplevelform.title('Wexis Biling System')
    toplevelform.geometry('1300x650')
    toplevelform.configure(bg='#a4e8e5')

####################### MAIN COMBO #######################

    combobox1 = Combobox(toplevelform,font='sans 16')
    combobox1.place(x=580,y=213)

####################### MAIN COMBO #######################

    def add():
        global name
        global billno
        name = customer_nameE.get()
        billno = customer_billnoE.get()
        current_values = combobox1.cget("values")
        new_value = 'name: '+ name + ' no: ' + billno
        new_value = new_value
        updated_values = list(current_values) + [new_value]
        combobox1.config(values=updated_values)
        
    def delete():  
        selected_value = combobox1.get()
        current_values = list(combobox1.cget('values'))
        if selected_value in current_values:
            current_values.remove(selected_value)
        combobox1.config(values=current_values)
    
    ###############  PRICE  #################### 

    def Prices():
        ##### FOOD #####
        global chipsPrice , toastPrice , hamburgerPrice , cheesecakePrice , pizzaPrice , saladPrice , steakPrice
        ##### DRINKS #####
        global frozenPrice , mochaPrice , teaPrice , lattePrice , americanoPrice , espressoPrice , colaPrice

        colaPrice = float(cola.get())
        colaPrice *= 2.5
        steakPrice = int(steak.get())
        steakPrice *= 42
        espressoPrice = float(espresso.get())
        espressoPrice *= 3.5
        saladPrice = float(salad.get())
        saladPrice *= 8.5
        americanoPrice = int(americano.get())
        americanoPrice *= 3
        lattePrice = int(latte.get())
        lattePrice *= 4
        hamburgerPrice = int(hamburger.get())
        hamburgerPrice *= 6
        toastPrice = float(toast.get())
        toastPrice *= 1.5
        teaPrice = int(tea.get())
        teaPrice *= 1
        cheesecakePrice = int(cheesecake.get())
        cheesecakePrice *= 9
        mochaPrice = int(mocha.get())
        mochaPrice *= 4
        frozenPrice = int(frozen.get())
        frozenPrice *= 5
        chipsPrice = float(chips.get())
        chipsPrice *= 3.5
        pizzaPrice = int(pizza.get())
        pizzaPrice *= 15


    ###############  PRICE  #################### 

    def priceLog():
        Prices()
        areaLog.delete('6.0',tk.END)
        if int(hamburger.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Hamburger Price: {}$'.format(hamburger.get(),hamburgerPrice))
        if int(latte.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Latte Price: {}$'.format(latte.get(),lattePrice))
        if float(toast.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Toast Price: {}$'.format(toast.get(),toastPrice))
        if int(tea.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Tea Price: {}$'.format(tea.get(),teaPrice))
        if int(cheesecake.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Cheesecake Price: {}$'.format(cheesecake.get(),cheesecakePrice))
        if int(mocha.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Mocha Price: {}$'.format(mocha.get(),mochaPrice))
        if int(frozen.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Frozen Price: {}$'.format(frozen.get(),frozenPrice))
        if int(chips.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Chips Price: {}$'.format(chips.get(),chipsPrice))
        if int(pizza.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Pizza Price: {}$'.format(pizza.get(),pizzaPrice))
        if int(americano.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Americano Price: {}$'.format(americano.get(),americanoPrice))
        if int(salad.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Salad Price: {}$'.format(salad.get(),saladPrice))
        if int(espresso.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Espresso Price: {}$'.format(espresso.get(),espressoPrice))
        if int(steak.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Steak Price: {}$'.format(steak.get(),steakPrice))
        if int(cola.get()) == 0:
            pass
        else:
            areaLog.insert(tk.END,'\n* {} Cola Price: {}$'.format(cola.get(),colaPrice))

    def updateBill():
        global profiles , profilesX
        global logs , totalX
        Prices()
        priceLog()
        total()
        logs = areaLog.get('6.0',tk.END)
        profiles = combobox1.get()
        values.update({
            profiles : logs
        })
        totalX = totalPrice
        profilesX = combobox1.get()
        valuesX.update({
            profilesX : totalX
        })

    def resetM():
        cola.delete(0, tk.END)
        cola.insert(0, 0)               
        steak.delete(0, tk.END)
        steak.insert(0, 0)       
        espresso.delete(0, tk.END)
        espresso.insert(0, 0)
        salad.delete(0, tk.END)
        salad.insert(0, 0)
        hamburger.delete(0, tk.END)
        hamburger.insert(0, 0)
        latte.delete(0,tk.END)
        latte.insert(0, 0)
        toast.delete(0,tk.END)
        toast.insert(0, 0)       
        tea.delete(0,tk.END)
        tea.insert(0, 0)
        cheesecake.delete(0,tk.END)
        cheesecake.insert(0, 0)
        mocha.delete(0,tk.END)
        mocha.insert(0, 0)
        frozen.delete(0,tk.END)
        frozen.insert(0, 0)
        chips.delete(0,tk.END)
        chips.insert(0, 0)
        pizza.delete(0,tk.END)
        pizza.insert(0, 0)
        americano.delete(0,tk.END)
        americano.insert(0, 0)

    def total():
        global totalPrice
        totalPrice = (colaPrice+steakPrice+espressoPrice+saladPrice+americanoPrice+lattePrice+hamburgerPrice+toastPrice
                                                             +teaPrice+cheesecakePrice+mochaPrice+frozenPrice+chipsPrice+pizzaPrice)

    def printTotal():
        try:
            areaLog.insert(tk.END,'\n\nTOTAL PRICE = {}$'.format(valuesX[combobox1.get()]))
        except:
            areaLog.insert(tk.END,'\n\nPlease choose order first')

    def showBill():
        Prices()
        global selected_value
        selected_value = combobox1.get()
        try:
            if selected_value == 'name:  no: ':
                areaLog.delete('1.0',tk.END)
                areaLog.insert(tk.END,'Select a valid customer')
            else:
                selected_value = selected_value.split()
                areaLog.delete('1.0',tk.END)
                areaLog.insert(tk.END,'* Customer Name: {}\n* Customer bill no: {}'.format(selected_value[1],selected_value[3]))
                areaLog.insert(tk.END,"\n\n----------Customers's Order----------")
                areaLog.insert(tk.END,'\n')
                try:
                    areaLog.insert(tk.END,'\n{}'.format(values[combobox1.get()]))
                except:
                    areaLog.insert(tk.END,"\n* No order")
        except:
            areaLog.insert(tk.END,'Please enter a valid name and bill number')    

    def on_selectCombo(event):
        showBill()
        
    combobox1.bind("<<ComboboxSelected>>",on_selectCombo)


    def exitQuestion():
        ask = messagebox.askquestion('QUIT','Do you want to exit')
        if ask == 'yes':
            form.quit()
            toplevelform.quit()

###############################

    titlelabel = tk.Label(toplevelform,text='Wexis Billing System',bg='#3c4f4e',fg='#fc4424',font='sans 40 bold')
    titlelabel.pack(fill=tk.X)

    customer_details = tk.Label(toplevelform,text='',bg='#836c68',font='sans 30')
    customer_details.pack(fill=tk.X)

###############################

    bill_bg = tk.Label(toplevelform,text='    ',bg='#69e1dc',font='sans 240 bold')
    bill_bg.place(x=580,y=340)

    customer_nameL = tk.Label(toplevelform,text='Name',fg='white',font='sans 24 bold',bg='#836c68')
    customer_nameL.place(x=35,y=80)

    customer_nameE = tk.Entry(toplevelform,font='sans 12')
    customer_nameE.place(x=145,y=92)
    
    customer_billnoL = tk.Label(toplevelform,font='sans 24 bold',text='Bill Number',bg='#836c68',fg='white')
    customer_billnoL.place(x=400,y=80)

    customer_billnoE = tk.Entry(toplevelform,font='sans 12')
    customer_billnoE.place(x=620,y=92)

    searchB = tk.Button(toplevelform,text='ADD',font='sans 24 bold',bg='white',fg='red',command=add)
    searchB.place(x=860,y=76)

    deleteB = tk.Button(toplevelform,text='DELETE',font='sans 24 bold',bg='white',fg='red',command=delete)
    deleteB.place(x=990,y=76)

    customer_box = tk.Label(toplevelform,text='Customers',fg='red',font='sans 24 bold',bg='#a4e8e5')
    customer_box.place(x=620,y=148)
    
    drinksL = tk.Label(toplevelform,text='Drinks',font='sans 22 bold',bg='#a4e8e5')
    drinksL.place(x=105,y=155)

    foodsL = tk.Label(toplevelform,text='Foods',font='sans 22 bold',bg='#a4e8e5')
    foodsL.place(x=416,y=155)

    hamburgerL = tk.Label(toplevelform,text='Hamburger',font='sans 14 bold',bg='#a4e8e5',fg='red')
    hamburgerL.place(x=266,y=215)

    hamburger = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    hamburger.place(x=388,y=220)

    toastL = tk.Label(toplevelform,text='Toast',font='sans 14 bold',bg='#a4e8e5',fg='red')
    toastL.place(x=295,y=255)

    toast = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    toast.place(x=388,y=260)

    cheesecakeL = tk.Label(toplevelform,text='Cheesecake',font='sans 14 bold',bg='#a4e8e5',fg='red')
    cheesecakeL.place(x=265,y=298)

    cheesecake = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    cheesecake.place(x=388,y=302)

    chipsL = tk.Label(toplevelform,text='Chips',font='sans 14 bold',bg='#a4e8e5',fg='red')
    chipsL.place(x=295,y=342)

    chips = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    chips.place(x=388,y=346)

    pizzaL = tk.Label(toplevelform,text='Pizza',font='sans 14 bold',bg='#a4e8e5',fg='red')
    pizzaL.place(x=300,y=386)

    pizza = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    pizza.place(x=388,y=388)

    saladL = tk.Label(toplevelform,text='Salad',font='sans 14 bold',bg='#a4e8e5',fg='red')
    saladL.place(x=300,y=427)

    salad = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    salad.place(x=388,y=430)

    steakL = tk.Label(toplevelform,text='Steak',font='sans 14 bold',bg='#a4e8e5',fg='red')
    steakL.place(x=300,y=468)

    steak = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    steak.place(x=388,y=472)

    latteL = tk.Label(toplevelform,text='Latte',font='sans 14 bold',bg='#a4e8e5',fg='red')
    latteL.place(x=14,y=215)

    latte = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    latte.place(x=80,y=220)

    teaL = tk.Label(toplevelform,text='Tea',font='sans 14 bold',bg='#a4e8e5',fg='red')
    teaL.place(x=14,y=259)

    tea = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    tea.place(x=80,y=261)

    mochaL = tk.Label(toplevelform,text='Mocha',font='sans 14 bold',bg='#a4e8e5',fg='red')
    mochaL.place(x=10,y=298)

    mocha = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    mocha.place(x=80,y=302)

    frozenL = tk.Label(toplevelform,text='Frozen',font='sans 14 bold',bg='#a4e8e5',fg='red')
    frozenL.place(x=10,y=342)

    frozen = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    frozen.place(x=80,y=347)

    americanoL = tk.Label(toplevelform,text='Americano',font='sans 10 bold',bg='#a4e8e5',fg='red')
    americanoL.place(x=3,y=387)

    americano = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    americano.place(x=80,y=388)

    espressoL = tk.Label(toplevelform,text='Espresso',font='sans 12 bold',bg='#a4e8e5',fg='red')
    espressoL.place(x=3,y=425)

    espresso = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    espresso.place(x=80,y=429)

    colaL = tk.Label(toplevelform,text='Cola',font='sans 14 bold',bg='#a4e8e5',fg='red')
    colaL.place(x=13,y=467)

    cola = tk.Spinbox(toplevelform,font='sans 10 bold',bg='white',from_=0,to=50)
    cola.place(x=80,y=471)

    areaL = tk.Label(toplevelform,text='    ',bg='#cecece',font='sans 320 bold')
    areaL.pack(side=tk.RIGHT,fill=tk.Y) 

    areaText = tk.Label(toplevelform,text='Bill Area',bg='#cecece',font='sans 36 bold',fg='#19b0f6')
    areaText.place(x=980,y=134) 

    areaLog = tk.Text(toplevelform,wrap=tk.WORD,width=50,height=25)
    areaLog.place(x=874,y=200)

    total_area = tk.Button(toplevelform,text='Total',font='sans 28 bold',bg='#6e6c66',command=printTotal,fg='#37d643')
    total_area.place(x=651,y=560)

    clear_bill_area = tk.Button(toplevelform,text='Reset Menu',font='sans 20 bold',bg='#ffa0a0',command=resetM)
    clear_bill_area.place(x=623,y=480)
    
    exitB = tk.Button(toplevelform,text='EXIT',font='sans 24 bold',bg='#e3f3b0',command=exitQuestion,fg='red')
    exitB.place(x=1180,y=76)
     
    update_bill = tk.Button(toplevelform,text='Update Bill',font='sans 20 bold',bg='#ffa0a0',command=updateBill)
    update_bill.place(x=629,y=400)

    dateL = tk.Label(toplevelform,text='Date: {}'.format(currentDate),font='sans 20 bold',bg='#a4e8e5',fg='#ff59d2')
    dateL.place(x=22,y=600)

    timeL = tk.Label(toplevelform,font='sans 20 bold',bg='#a4e8e5',fg='#e626b2')
    timeL.place(x=22,y=562)

    def timer():
        currentTime = time.strftime('%H:%M:%S')
        timeL.config(text=f'Time: {currentTime}')
        timeL.after(1000,timer)
    timer()

################################################################# TOP LEVEL #################################################################

def registerSystem():
    global nickname
    global password
    nickname = nickname_entry.get().strip()
    password = password_entry.get().strip()
    if len(nickname) > 7 and len(password) > 7:
        if nickname.strip() == '' or password.strip() == '':
            check_label.config(text='Registration Failed',fg='red')
            check_label.place(x=200,y=200)
        else:
            check_label.config(text='Registration Successful', fg='green')
            check_label.place(x=180, y=200)
            password_entry.delete(0,'end')
            nickname_entry.delete(0,'end')
    else:
        check_label.config(text='Must be 7 digits',fg='red')
        check_label.place(x=210,y=200)
        password_entry.delete(0,'end')
        nickname_entry.delete(0,'end')

def loginSystem():
    try:
        if len(nickname) > 7 and len(password) > 7:
            if nickname.strip() == '' or password.strip() == '':
                check_label.config(text='Login Failed',fg='red')
                check_label.place(x=225,y=200)
                password_entry.delete(0,'end')
                nickname_entry.delete(0,'end')

            if nickname == nickname_entry.get() and password == password_entry.get():
                check_label.config(text='Login Successful',fg='green')
                check_label.place(x=208,y=200)
                toplevel1()
                form.withdraw()

            else:
                check_label.config(text='Login Failed',fg='red')
                check_label.place(x=225,y=200)
                password_entry.delete(0,'end')
                nickname_entry.delete(0,'end')
    except:
            check_label.config(text='Login Failed',fg='red')
            check_label.place(x=225,y=200)
            password_entry.delete(0,'end')
            nickname_entry.delete(0,'end')

#BUTTONS
login_buton = tk.Button(form,text='Login',bg='blue',fg='white',font='sans 20 bold',command=loginSystem)
login_buton.place(x=224,y=260)

register_buton = tk.Button(form,text='Register',bg='blue',fg='white',font='sans 20 bold',command=registerSystem)
register_buton.place(x=204,y=320)

#ENTRYS
nickname_entry = tk.Entry(form)
nickname_entry.place(x=195,y=70)

password_entry = tk.Entry(form,show='*')
password_entry.place(x=195,y=150)

#LABELS
nickname_label = tk.Label(form,text='Nickname',font='sans 14 bold',bg='#76e698')
nickname_label.place(x=230,y=40)

password_label = tk.Label(form,text='Password',font='sans 14 bold',bg='#76e698')
password_label.place(x=230,y=120)

check_label = tk.Label(form,text='',font='sans 12 bold',fg='green',bg='#76e698')
check_label.place(x=200,y=200)


form.mainloop()
