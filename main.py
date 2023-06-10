import random
import string

def remove_first_letter(n):
    rfl1 = n[0]
    return n.replace(n[0],'',1),rfl1

def adding_3_letters():
    al1 = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
    al2 = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
    return al1,al2

def remove_last_letter(n):
    rll1 = n[-1]
    return n.replace(n[-1],'',1),rll1

def encoding():
    r_message = input("enter the string you want to be encoded: ")
    r_list = r_message.split()
    r_length= len(r_list)
    for i in range(r_length):
        if len(r_list[i]) <3:
            r_list[i] = r_list[i][::-1]
        else:
            e1,e2 = remove_first_letter(r_list[i])
            r_list[i] = e1
            r_list[i] = r_list[i] + e2
            e3,e4 = adding_3_letters()
            r_list[i] = e3 + r_list[i] + e4
    print("your encoded message is:",*r_list)
            
def decoding():
    d_message = input("enter the string you want to be decoded: ")
    d_list = d_message.split()
    d_length = len(d_list)
    for i in range(d_length):
        if len(d_list[i]) <3:
            d_list[i] = d_list[i][::-1]
        else:
            d_list[i] = d_list[i][3:-3]
            e5,e6 = remove_last_letter(d_list[i])
            d_list[i] = e5
            d_list[i] = e6 + d_list[i]
    print("your decoded message is:",*d_list)

while True:
    choice = int(input(("what action do you want to perform:\n1.Encode\n2.Decode\n3.End\n--> ")))
    if choice == 1:
        encoding()
    elif choice == 2:
        decoding()
    elif choice == 3:
        print("Task has been successfully completed")
        break
    