import tkinter


def add_to_f_file(pat_info): #opens file to append and adds to it and closes it
    file_out_name = "data"
    output_file = open (file_out_name, "a")
    output_file.write(pat_info)

    output_file.close()

#-----------------------------------------------------------------------------#

def read_f_file(): #opens file to read takes text from file and prints it out
    file_in_name = "data"
    input_file = open (file_in_name, "r")
    line_read = input_file.readline() #reads line

    while line_read != "":
        print("\n",line_read) #prints read line
        line_read = input_file.readline () #reads next line

    input_file.close()

#-----------------------------------------------------------------------------#

def search(): #tkae all item and puts it into a list to make a record
    global all_info_list
    all_info_list = []
    file_in_name = "data"
    input_file = open (file_in_name, "r")
    line_read = input_file.readline()
    
    while line_read != "":
        line_read = line_read.split() #makes single line into list
        all_info_list += [line_read] #adds list to records
        line_read = input_file.readline() #reads next line

    return all_info_list #stores list until list function is called

#-----------------------------------------------------------------------------#
def registration():
    global records
    records = []

    records.append(name.get())
    records.append(birthday.get())
    records.append(gender.get())
    records.append(p_number.get())
    records.append(address.get())

    info_string = ""

    for element in records:
        info_string = info_string + element + " "

    info_string = info_string + "\n"
    add_to_f_file(info_string)

    info_string = []

        
#-----------------------------------------------------------------------------#
        
def doctor_data():
    num = ""
    read_f_file()
    pat_num = input("which patient would you like to find (enter patient number): ")
    if (pat_num != num):
        for element in search():
            num = element[0]
            if(pat_num == num):
                print(element)
                num = ""
                
                
#-----------------------------------------------------------------------------#  


def register_button_clicked():
    global name
    global birthday
    global gender
    global p_number
    global address
    global records
    destroy()
    canvas = tkinter.Canvas(window, width = 1000, height = 700)

    message = tkinter.Label(window,
                text="Please enter the following patient information", anchor='w')
    canvas.create_window(150,50, window=message)
    
    name = tkinter.Entry(window)
    canvas.create_window(400, 100, window=name)
    name_label = tkinter.Label(window, text="Full Name:", anchor='w')
    canvas.create_window(100, 100, window=name_label)


    birthday = tkinter.Entry(window)
    canvas.create_window(400, 150, window=birthday)
    birth_label = tkinter.Label(window, text="Birthday (dd/mm/yyyy): ",anchor='w')
    canvas.create_window(100, 150, window=birth_label)
   
    
    gender = tkinter.Entry(window)
    canvas.create_window(400, 200, window=gender)
    gender_label = tkinter.Label(window, text="Gender(female/male/other): ", anchor='w')
    canvas.create_window(100, 200, window=gender_label)
     

    p_number = tkinter.Entry(window)
    canvas.create_window(400, 250, window=p_number)
    p_number_label = tkinter.Label(window, text="Phone number(10-digits): ")
    canvas.create_window(100, 250, window=p_number_label)
  

    address = tkinter.Entry(window)
    canvas.create_window(400, 300, window=address)
    address_label = tkinter.Label(window, text="Address: ")
    canvas.create_window(100, 300, window=address_label)
 

    enter = tkinter.Button (window, text = "ENTER", command = registration)
    canvas.create_window(400, 400, window=enter)

    
    canvas.pack()
    window.mainloop()

#-----------------------------------------------------------------------------#  
    
def destroy():
    canvas.destroy()
    return

#-----------------------------------------------------------------------------#  

def doctor_button_clicked():
    destroy()
    canvas = tkinter.Canvas(window, width = 1000, height = 700)
    
    num = tkinter.Entry(window)
    canvas.create_window(400, 100, window=num)
    pat_num_label = tkinter.Label(window, text="Patient Number:",anchor='w',font=(30))
    canvas.create_window(100, 100, window=pat_num_label)

    pat_data = tkinter.Label(window, text="Patient Number:",anchor='w',font=(30))
    canvas.create_window(100, 100, window=pat_data)

    pat_num = num.get()

    

    while (pat):

    canvas.pack()
    window.mainloop()

#-----------------------------------------------------------------------------#  

def exit_button_clicked():
    exit()

#-----------------------------------------------------------------------------#  

def patient_button_clicked():
    exit()
    
#-----------------------------------------------------------------------------#  

def main_screen():
    doctor_button = tkinter.Button (window, text = "Doctor",command = doctor_button_clicked)
    
    canvas.create_window(200, 200, window=doctor_button)

    patient_button = tkinter.Button (window, text = "Patient",
                                   command = patient_button_clicked)
    canvas.create_window(500, 200, window=patient_button)
    
    register_button = tkinter.Button (text = "Register", 
                                          command = register_button_clicked)
    canvas.create_window(800, 200, window = register_button)

    exit_button = tkinter.Button (window, text = "Exit",
                                          command = exit_button_clicked)
    canvas.create_window(500, 400, window=exit_button)

#-----------------------------------------------------------------------------#  

def main():
    global window
    global canvas
    
    window = tkinter.Tk()
    window.title ("Hospital Program")
    window.geometry("1000x700")
    canvas = tkinter.Canvas(window, width = 1000, height = 700)

    main_screen()
    
    canvas.pack()
    window.mainloop()
   
main()
