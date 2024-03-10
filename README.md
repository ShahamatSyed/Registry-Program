    import tkinter
    import random
    
    def add_to_f_file(pat_info):#opens file to append and adds to it and closes it
        file_out_name = "data.txt"
        output_file = open (file_out_name, "a")
     
        output_file.write(pat_info)
        print("Program Done")
       
        output_file.close()
    
    def write_new_file(pat_info):
        file_out_name = "data.txt"
        output_file = open (file_out_name, "w")
     
        output_file.write("%s\n" % pat_info)
        print("Program Done")
       
        output_file.close()
    
    #-----------------------------------------------------------------------------#
    
    def read_f_file(): #opens file to read takes text from file and prints it out
        file_in_name = "data.txt"
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
        file_in_name = "data.txt"
        input_file = open (file_in_name, "r")
        line_read = input_file.readline()
       
        while line_read != "":
            line_read = line_read.split() #makes single line into list
            all_info_list += [line_read] #adds list to records
            line_read = input_file.readline() #reads next line
    
        return all_info_list #stores list until list function is called
    
    
    #-----------------------------------------------------------------------------#
    
    #Validates registration information
    
    def registration_validation():
        name_rec = str(name.get())
        birth_rec = str(birthday.get())
        gender_rec = str(gender.get())
        p_num_rec= str(p_number.get())
        address_rec = str(address.get())
    
    
    
        p_rec= 0
        full_validation = 0
        
        
        #other validation
        if (p_num_rec == ""):
            name_validation = tkinter.Label(window,
                                            text= "number please", bg="red")
            canvas.create_window(390, 120, window=name_validation)
        else:
            n_validation_accepted = tkinter.Label(window, width = 31)
            canvas.create_window (390,120, window = n_validation_accepted)
            full_validation = full_validation + 1
            p_rec= int(p_num_rec)
            
        if (name_rec == ""):
            name_validation = tkinter.Label(window,
                                            text= "Please write your full name",
                                            bg="red")
            canvas.create_window(390, 120, window=name_validation)
        else:
            n_validation_accepted = tkinter.Label(window, width = 31)
            canvas.create_window (390,120, window = n_validation_accepted)
            full_validation = full_validation + 1
      
            
    
        if (birth_rec == ""):
            birth_validation = tkinter.Label(window,
                                             text= "Please write your birthday",
                                             bg="red")
            canvas.create_window(390, 170, window=birth_validation)
        else:
            b_validation_accepted = tkinter.Label(window, width = 31)
            canvas.create_window (390,170, window = b_validation_accepted)
            full_validation = full_validation + 1
    
        if (address_rec == ""):
            address_validation = tkinter.Label(window,
                                               text= "Please write your address",
                                               bg="red")
            canvas.create_window(390, 320, window=address_validation)
        else:
            a_validation_accepted = tkinter.Label(window, width = 31)
            canvas.create_window (390,320, window = a_validation_accepted)
            full_validation = full_validation + 1
    
    
        
            
            
            
        
        #gender validation 
        if (gender_rec == "male"):
            gender_validated = 1
            
        elif(gender_rec == "female"):
            gender_validated = 1
    
        elif(gender_rec == "other"):
            gender_validated = 1
            
        else:
            gender_validation = tkinter.Label(window,
                         text= "Gender must be male, female, or other", bg="red")
            canvas.create_window(390, 220, window=gender_validation)
            gender_validated = 2
    
         
    
        if (gender_validated == 1):
            validation_accepted = tkinter.Label(window, width = 30)
            canvas.create_window (390,220, window = validation_accepted)
            full_validation = full_validation + 1
    
        #phone number validation
        if (1000000000 < p_rec < 9999999999):
            phone_validated = 1
            
        else:
            phone_validation = tkinter.Label (window,
                    text = "Patient phone number must be 10 digits", bg= "red")
            canvas.create_window(390, 270, window = phone_validation)
            phone_validated = 2
            
    
        if (phone_validated == 1):
            p_validation_accepted = tkinter.Label(window, width = 31)
            canvas.create_window (390,270, window = p_validation_accepted)
            full_validation = full_validation + 1
    
    
        #final validation
        if (full_validation == 6):
            registration()
    
        else:
            full_validation == 0
        
        
    
    
    #-----------------------------------------------------------------------------#
    # Registration main page, makes stuff into strings 
    
    def registration():
        
        patient_num_list = []
        
        name_rec = str(name.get())
        birth_rec = str(birthday.get())
        gender_rec = str(gender.get())
        p_num_rec = str(p_number.get())
        address_rec = str(address.get())
        doc = assign_doctor()
        room = room_num()
        records.append([name_rec, birth_rec, gender_rec, p_num_rec,address_rec, patient_number(),doc, room])
    
        str_patient_number = str(patient_number())
        message=tkinter.Label(text="  Your patient number:" + str_patient_number,
                              anchor='w',font=30, bg="#91CAEB",
                              width = 50, height = 3)
        canvas.create_window(250, 520, window=message)
        str_given_doctor = str(doc)
        message_2=tkinter.Label(text="  Your doctor: " + str_given_doctor,
                              anchor='w',font=30, bg="white",
                                width = 50, height=3)
        canvas.create_window(250, 570, window=message_2)
        str_room_number = str(room)
        message_3=tkinter.Label(text="  Your room number is:" + str_room_number,
                              anchor='w', font=30, bg="#91CAEB",
                                width = 50, height =3)
        canvas.create_window(250, 620, window=message_3)
        info_string = ""
        string = ""
    
        for i in range(1):
            sub_list = records[-1] # takes patient info just entered
            
            for i in range(len(sub_list)):
                a = str(sub_list[i])
                string = string + a + " "
                
            info_string = info_string + string + " "
        print("program started")
        info_string = info_string + "\n"
        add_to_f_file(info_string)
        info_string = []
    
    #------------------------------------------------------------------------------#
        
    def patient_number():
    
        file_in_name = "data.txt"
        input_file = open (file_in_name, "r")
        count = 0
        line_read = input_file.readline()
    
        while (line_read != ""):
            count = count + 1
            line_read = input_file.readline()
            patient_number = str(1000 + count)
        return patient_number
    
    #-----------------------------------------------
    
    def room_num():
        split_lines = store_split()
        i = 0
       
        while (i == 0):
            room = str(random.randrange(100,200))
            print(room)
            count = 0
            for i in range(len(split_lines)):
                line_split = split_lines[i]
                room_number = line_split[-1]
                if (room == room_number):
                    count = count + 1
          
            if (count == 2):
                i = 0
            else:
                i = 1
                print("*",room)
                return room
    
    #------------------------------------------------------------------------------#
    
    def doctor_data():
        global s_pat
        global n_change
        global b_change
        global g_change
        global p_n_change
        global ad_change
        global room_change
        global list_split
        num = ""
        if (pat_num.get() != num):
            for element in store_split():
                num = element[-3]
                if(pat_num.get()== num):
                    s_pat = element
                    n_change = s_pat[0] + " " + s_pat[1]
                    b_change = s_pat[2]
                    g_change = s_pat[3]
                    p_n_change = s_pat[4]
                    ad_change = s_pat[5] + " " + s_pat[6]
                    room_change = s_pat[-1]
                    change_data_text()
        
    #------------------------------------------------------------------------------#
                    
    def all_pat_num():
        pat_nums = ""
        list_split = store_split()
        for pat in list_split:
            pat_nums = pat_nums + pat[-3] + "\n"
        return pat_nums
    
    #------------------------------------------------------------------------------#
    
    def change_data_text():
        n.config(text = "Name:" + n_change)
        b.config(text = "Brithday:" + b_change)
        g.config(text = "Gender:" + g_change)
        p_n.config(text = "Phone number:" + p_n_change)
        ad.config(text = "Address:" + ad_change)
        room_num.config(text = "Room number:" + room_change)
    
    def dis_pat():
        new_full_data_list = []
        num = 0
        is_num = ""
        counter = 0
        run = ""
        string = ""
        list_split = store_split()
        if (pat_num.get() != num):
                for element in list_split:
                    counter += 1
                    print (counter)
                    num = element[-3]
                    print (num)
                    if(pat_num.get()== num):
                        print(counter)
                        index = counter - 1
                        print (index)
                        del list_split[index]
                        new_full_data_list = list_split
                        print(new_full_data_list)
                        counter = 0
                        
                        for x in new_full_data_list:
                            for y in x:
                                y = str(y)
                                string = string + y + " "
                            string = string + "\n"    
                            write_new_file(string)
                        read_f_file()
    
    
    #------------------------------------------------------------------------------#
    
    def doctor_button_clicked():
        global pat_num
        global n
        global b
        global g
        global p_n
        global ad
        global room_num
        canvas.delete('all')
    
        bg_block_1 = canvas.create_polygon(0,0, 20,0,20,700,0,700,0,0, fill='blue')
        bg_block_1 = canvas.create_polygon(500,0, 700,0,700,700,500,700,500,0, fill='blue')
        
        pat_num = tkinter.Entry(window)
        canvas.create_window(400, 100, window=pat_num)
    
        pat_num_label = tkinter.Label(window, text="Please enter patient number:",anchor='w',font=(30))
        canvas.create_window(175, 100, window=pat_num_label)
        
        enter = tkinter.Button (window, text = "ENTER", command =  doctor_data, bg="#16A0F0")
        canvas.create_window(150, 600, window=enter)
    
        pat_num_box = tkinter.Text(window, height = 28, width = 25)
        canvas.create_window(200, 350, window=pat_num_box)
    
        pat_num_box.insert(tkinter.END,all_pat_num())
    
        n = tkinter.Label(window, text="Name:",anchor='w',font=(30))
        canvas.create_window(600, 150, window=n)
        
        b = tkinter.Label(window, text="Brithday:",anchor='w',font=(30))
        canvas.create_window(600, 200, window=b)
    
        g = tkinter.Label(window, text="Gender:",anchor='w',font=(30))
        canvas.create_window(600, 250, window=g)
        
        p_n = tkinter.Label(window, text="Phone number:",anchor='w',font=(30))
        canvas.create_window(600, 300, window=p_n)
    
        ad = tkinter.Label(window, text="Address:",anchor='w',font=(30))
        canvas.create_window(600, 350, window=ad)
    
        room_num = tkinter.Label(window, text="Room number:",anchor='w',font=(30))
        canvas.create_window(600, 400, window=room_num)
        
        exit_pressed = tkinter.Button(window, text = "EXIT",
                                      command = exit_button_clicked, bg="#EB8FEB")
        canvas.create_window(250, 600, window=exit_pressed)
    
        discharge_pressed = tkinter.Button(window, text = "Discharge",
                                      command = dis_pat, bg="red")
        canvas.create_window(350, 600, window=discharge_pressed)
    
        canvas.pack()
        window.mainloop()
    
    
    #-----------------------------------------------------------------------------#
        
    def assign_doctor():
        doctor_list = ["Dr.Syed", "Dr.Thiva","Dr.Mahpara","Dr.Fong", "Dr.Stranger"]
        split_lines = store_split()
        i = 0
       
        while (i == 0):
            count = 0
            doctor = str(doctor_list[random.randrange(0, len(doctor_list))])
            for i in range(len(split_lines)):
                line_split = split_lines[i]
                doctor_in_file = line_split[-2]
                if (doctor == doctor_in_file):
                    count = count + 1
            if (count == 20):
                i = 0
            else:
                i = 1
                return doctor
    
    #-----------------------------------------------------------------------------#
           
    def register_button_clicked():
        global name
        global birthday
        global gender
        global p_number
        global address
        global records
        canvas.delete('all')
    
        message = tkinter.Label(window,
                    text="Please enter the following patient information",
                                anchor='w')
        canvas.create_window(150,50, window=message)
        
        bg_block_1 = canvas.create_polygon(0,0, 20,0,20,700,0,700,0,0, fill='blue')
        bg_block_1 = canvas.create_polygon(550,0, 1000,0,1000,700,
                                           550,700,550,0, fill='blue')
       
        name = tkinter.Entry(window)
        canvas.create_window(400, 100, window=name)
        name_label = tkinter.Label(window, text="First and Last Name:",
                                   anchor='w')
        canvas.create_window(100, 100, window=name_label)
    
    
        birthday = tkinter.Entry(window)
        canvas.create_window(400, 150, window=birthday)
        birth_label = tkinter.Label(window, text="Birthday (dd/mm/yyyy): ",
                                    anchor='w')
        canvas.create_window(100, 150, window=birth_label)
       
       
        gender = tkinter.Entry(window)
        canvas.create_window(400, 200, window=gender)
        gender_label = tkinter.Label(window, text="Gender(female/male/other): ",
                                     anchor='w')
        canvas.create_window(100, 200, window=gender_label)
         
    
        p_number = tkinter.Entry(window)
        canvas.create_window(400, 250, window=p_number)
        p_number_label = tkinter.Label(window, text="Phone number(10-digits): ")
        canvas.create_window(100, 250, window=p_number_label)
     
    
        address = tkinter.Entry(window)
        canvas.create_window(400, 300, window=address)
        address_label = tkinter.Label(window, text="Address: ")
        canvas.create_window(100, 300, window=address_label)
     
    
        enter = tkinter.Button (window, text = "ENTER",
                                command = registration_validation, bg="#16A0F0")
        canvas.create_window(350, 400, window=enter)
     
    
        exit_pressed = tkinter.Button(window, text = "EXIT",
                                      command = exit_button_clicked, bg="#EB8FEB"
                              )
        canvas.create_window(450, 400, window=exit_pressed)
    
       
        canvas.pack()
        window.mainloop()
    
    
    
    #-----------------------------------------------------------------------------# 
    
    def exit_button_clicked():
        canvas.delete('all')
        main_screen()
        canvas.pack()
        window.mainloop()
    #-----------------------------------------------------------------------------#
    
    def patient_button_clicked():
        global pat_num
        
        canvas.delete('all')
        bg_block_1 = canvas.create_polygon(0,0, 20,0,20,700,0,700,0,0, fill='blue')
        bg_block_1 = canvas.create_polygon(500,0, 700,0,700,700,
                                           500,700,500,0, fill='blue')
    
        pat_num = tkinter.Entry(window)
        canvas.create_window(400, 100, window=pat_num)
        pat_num_label = tkinter.Label(window, text="Patient Number:",
                                      anchor='w',font=(30))
        canvas.create_window(100, 100, window=pat_num_label)
        
    
        enter = tkinter.Button (window, text = "ENTER",command=show_edit_buttons,
                                bg="#16A0F0")
        canvas.create_window(400, 150, window=enter)
        exit_pressed = tkinter.Button(window, text = "EXIT",
                                      command = exit_button_clicked,bg="#EB8FEB")
        canvas.create_window(400, 200, window=exit_pressed)
    
    
    def validate_pat_num():
        valid = []
        filtered_list = []
        pat_num_get = pat_num.get()
        split_lines = store_split()
    
        for element in split_lines:
            if element:
                filtered_list.append(element)
        
        for x in filtered_list:
            if pat_num_get == x[-3]:
                valid.append(pat_num)
        if len(valid) == 1:
            return True
        else:
            return False
        
    
    #-----------------------------------------------------------------------------#
    def show_edit_buttons():
        check = validate_pat_num()
        if check == True:
            edit_address = tkinter.Button(window, text="Edit Address", bg="pink",
                                      command=edit_address_clicked)
            canvas.create_window(840, 100, window=edit_address)
            edit_number = tkinter.Button(window,
                                         text="Edit Phone Number", bg="cyan",
                                     command=edit_number_clicked)
            canvas.create_window(840, 200, window=edit_number)
    
            label = tkinter.Label(width=30)
            canvas.create_window(150, 250, window= label)
        elif check == False:
            message = tkinter.Label(text="Invalid patient number",
                                    bg='red')
            canvas.create_window(150, 250, window=message)
    #-----------------------------------------------------------------------------#
        
    def edit_address_clicked():
        global new_address
        
        canvas.delete('all')
        store_split = []
        new_address_get = ""
    
        bg_block_1 = canvas.create_polygon(700,0, 1000,0,1000,700,
                                           700,700,700,0, fill='blue')
        bg_block_2 = canvas.create_polygon(0,0, 300,0,300,700,0,
                                           700,0,0, fill='blue')
        message = tkinter.Label(text="Please enter your new address below:",
                                font=30)
        canvas.create_window(500, 150, window=message)
    
        new_address = tkinter.Entry(window)
        canvas.create_window(500,200, window=new_address)
        new_address_get = new_address.get()
    
        exit_pressed = tkinter.Button(window, text = "EXIT",
                                      command = exit_button_clicked,bg="#EB8FEB")
        canvas.create_window(530, 250, window=exit_pressed)
        enter = tkinter.Button (window, text = "ENTER",command=change_address,
                                bg="#16A0F0")
        canvas.create_window(470, 250, window=enter)
            
    
    def store_split():
        store_split = []
        filtered_list = []
        file_in_name = "data.txt"
        input_file = open (file_in_name, "r")
    
        for line in input_file:
            split_line = line.split()
            store_split.append(split_line)
     
        for element in store_split:
            if element:
                filtered_list.append(element)
        print("T", filtered_list)
        return filtered_list
    
    #-----------------------------------------------------------------------------#
                  
    def change_address():
        
        new_address_get = new_address.get()
        pat_num_get = pat_num.get()
    
        new_line = []
        info_string = ""
        string = ""
    
        split_lines = store_split()
    
        for i in range(len(split_lines)):
            line_split = split_lines[i]
            print("N",line_split)
            number_in_file = line_split[-3]
            if (pat_num_get == number_in_file):
                new_line.append([line_split[0],line_split[1],line_split[2],
                                line_split[3],line_split[4], line_split[-3],
                                line_split[-2], line_split[-1]])
                new_line = new_line[0]
                new_line.insert(5, new_address_get)
                for x in new_line:
                    x = str(x)
                    string = string + x + " "
                string = string + "\n"
            else:
                for x in split_lines[i]:
                    x = str(x)
                    string = string + x + " "
                string = string + "\n"
                    
        info_string = info_string + string + " "
        print(info_string)
        write_new_file(info_string)
        info_string = []
        
    #------------------------------------------------------------------------------#
        
    def edit_number_clicked():
        global new_number
    
        canvas.delete('all')
    
        bg_block_1 = canvas.create_polygon(700,0, 1000,0,1000,700,700,
                                           700,700,0, fill='blue')
        bg_block_2 = canvas.create_polygon(0,0, 300,0,300,700,0,700,
                                           0,0, fill='blue')
    
        message = tkinter.Label(text="Please enter your new phone number below:",
                                font=30)
        canvas.create_window(500, 150, window=message)
        message_2 = tkinter.Label(text="Please ensure number is 10 digits",font=30)
        canvas.create_window(500, 350, window=message_2)
    
        new_number = tkinter.Entry(window)
        canvas.create_window(500,200, window=new_number)
    
        exit_pressed = tkinter.Button(window, text = "EXIT",
                                      command = exit_button_clicked,bg="#EB8FEB")
        canvas.create_window(530, 250, window=exit_pressed)
        enter = tkinter.Button (window, text = "ENTER", command=change_number
                                ,bg="#16A0F0")
        canvas.create_window(470, 250, window=enter)
    
    #------------------------------------------------------------------------------#
    
    def validate_number():
        len_address = len(new_number_get)
        print(len_address)
        if (len_address > 10 or len_address < 10):
            edit_number_clicked()
        else:
            return new_number_get  
        
    #------------------------------------------------------------------------------#
        
    def change_number():
        global new_number_get
        
        new_number_get = new_number.get()
        validate_number()
        new_number_get = validate_number()
        pat_num_get = pat_num.get()
      
        info_string = ""
        string = ""
    
        split_lines = store_split()
                
        for i in range(len(split_lines)):
            line_split = split_lines[i]
            number_in_file = line_split[-3]
            if (pat_num_get == number_in_file):
                line_split.remove(line_split[4])
                line_split.insert(4, new_number_get)
                new_line = str(line_split)
                for x in line_split:
                    x = str(x)
                    string = string + x + " "
                string = string + "\n"
            else:
                for x in line_split:
                    x = str(x)
                    string = string + x + " "
                string = string + "\n"
                    
        info_string = info_string + string + " "
        print("program started")
        write_new_file(info_string)
        info_string = []
    
        
    #-----------------------------------------------------------------------------#
    
    def goodbye():
        canvas.delete('all')
        message = tkinter.Label(window,
                text="Thank you for visiting our site.\nStay healthy and safe!",
                                font=50, height=5, width=25, bg='white')
        canvas.create_window(500,350,window=message)
    
    
    #-----------------------------------------------------------------------------#
    
    def main_screen():
        doctor_button = tkinter.Button (text = "Doctor",
                                        width=10,height =2,font=('Oswald',15),
                                              command = doctor_button_clicked,
                                        bg="#8FA0EB", fg='white')
        canvas.create_window(200, 200, window = doctor_button)
    
        patient_button = tkinter.Button (text = "Patient",width=10,
                                         height =2,font=('Oswald',15),
                                       command = patient_button_clicked,
                                         bg="#8FEB91")
        canvas.create_window(500, 200, window=patient_button)
       
        register_button = tkinter.Button (text = "Register", width=10,height =2,
                                          font=('Oswald',15),
                                              command = register_button_clicked,
                                          bg="orange")
        canvas.create_window(800, 200, window = register_button)
    
        exit_button = tkinter.Button (text = "Exit", width=10,height =2,
                                      fg='white', font=('Oswald',15),
                                              command=goodbye, bg="#D968D7")
        canvas.create_window(500, 400, window=exit_button)
        
    
    #-----------------------------------------------------------------------------#
    
    def main():
        global window
        global canvas
        global records
        
        records = []
        window = tkinter.Tk()
        window.title ("Hospital Program")
        window.geometry("1000x700")
        canvas = tkinter.Canvas(window, width = 1000, height = 700)
        canvas.pack()
    
        main_screen()
       
        window.mainloop()
       
    main()
