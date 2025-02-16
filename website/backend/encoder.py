import random
""" 12 = 2,3,8
    10 = 2,2,10
    8 = 3,2,12
    11 = 3,4,9
    9 = 4,3,11"""


def encoder(password):
    length_of_password = len(password)
    length_of_random = 20 - len(password)
    rand = ""
    for i in range(length_of_random):
        rand = rand + chr(int(random.randint(32, 127)))
    encoded_password = ""
    number_of_group = 0
    counter1 = 0
    counter2 = 0
    if length_of_password%2 == 0:
        if length_of_password == 12:
            rand = rand + "234e"
            while number_of_group < 5:
                if number_of_group < 4:
                    for i in range(2):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                    for j in range(3):
                        encoded_password = encoded_password + password[counter2]
                        counter2 += 1
                else:
                    for i in range(4):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                number_of_group += 1
        elif length_of_password == 10:
            rand = rand + "225e"
            while number_of_group < 6:
                if number_of_group < 5:
                    for i in range(2):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                    for j in range(2):
                        encoded_password = encoded_password + password[counter2]
                        counter2 += 1
                else:
                    for i in range(4):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                number_of_group += 1
        elif length_of_password == 8:
            rand = rand + "324e"
            while number_of_group < 5:
                if number_of_group < 4:
                    for i in range(3):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                    for j in range(2):
                        encoded_password = encoded_password + password[counter2]
                        counter2 += 1
                else:
                    for i in range(4):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                number_of_group += 1
    else:
        if length_of_password == 9:
            rand = rand + "433o"
            while number_of_group < 4:
                if number_of_group < 3:
                    if number_of_group == 0 or number_of_group == 2:
                        for i in range(4):
                            encoded_password = encoded_password + rand[counter1]
                            counter1 += 1
                    else:
                        for k in range(3):
                            encoded_password = encoded_password + rand[counter1]
                            counter1 += 1
                    for j in range(3):
                        encoded_password = encoded_password + password[counter2]
                        counter2 += 1
                else:
                    for i in range(4):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                number_of_group += 1
        if length_of_password == 11:
            rand = rand + "343v"
            while number_of_group < 4:
                if number_of_group < 3:
                    for i in range(3):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                    if number_of_group == 0 or number_of_group == 2:
                        for j in range(4):
                            encoded_password = encoded_password + password[counter2]
                            counter2 += 1
                    else:
                        for k in range(3):
                            encoded_password = encoded_password + password[counter2]
                            counter2 += 1
                else:
                    for i in range(4):
                        encoded_password = encoded_password + rand[counter1]
                        counter1 += 1
                number_of_group += 1
    return encoded_password


def decoder(password):
    type_of_password = password[23]
    number_of_group = 0
    max_group = int(password[22])
    max_len_of_pass_group = int(password[21])
    max_len_of_random = int(password[20])
    decoded_password = ""
    counter = 0
    if type_of_password == "e":
            while number_of_group < max_group:
                for i in range(max_len_of_random):
                    counter += 1
                for j in range(max_len_of_pass_group):
                    decoded_password = decoded_password + password[counter]
                    counter += 1
                number_of_group +=1
    elif type_of_password == "o":
        while number_of_group <max_group:
            if number_of_group == 0 or number_of_group == 2:
                for i in range(max_len_of_random):
                    counter += 1
            else:
                for k in range(max_len_of_random - 1):
                    counter += 1
            for j in range(max_len_of_pass_group):
                decoded_password = decoded_password + password[counter]
                counter += 1
            number_of_group += 1
    elif type_of_password == "v":
        while number_of_group < max_group:
            for i in range(max_len_of_random):
                counter += 1
            if number_of_group == 0 or number_of_group == 2:
                for j in range(max_len_of_pass_group):
                    decoded_password = decoded_password + password[counter]
                    counter += 1
            else:
                for k in range(max_len_of_pass_group-1):
                    decoded_password = decoded_password + password[counter]
                    counter += 1
            number_of_group += 1
    return decoded_password

encrypted = encoder("Password") ; print(encrypted)