import csv

def write_on_csv(info_list):
    with open("student_info.csv",'a',newline="") as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["First Name","Last Name","Age","Contact_Number","E-mail_ID"])

            writer.writerow(info_list)

if __name__=="__main__":
    condition=True
    serial_number=1

    while(condition):
        print("Enter information for student",serial_number,":")
        student_info=input("Use the format(First_Name, Last_Name, Age, Contact_Number, Email-ID)(no comma):")

        data=student_info.split(' ')

        print("The entered information is:\nFirst Name:{}\nLast Name:{}\nAge:{}\nContact Number:{}\nE-mail ID:{}"
        .format(data[0],data[1],data[2],data[3],data[4]))

        confirm=input("Is the information entered by you correct?(yes/no):")

        if confirm=="yes":
            write_on_csv(data)

            new_entry=input("Enter yes/no if you want to enter for another student:")

            if new_entry=='yes':
                condition=True
                serial_number=serial_number+1

            elif new_entry=='no':
                condition=False

        elif confirm=='no':
            print("\n Please re-enter the information!")
