import random
import string

def password_generator(password_length:int):
    
        string_1 = string.digits
        string_2 = string.ascii_lowercase
        string_3 = string.ascii_uppercase
        string_4 = string.punctuation

        total_string = string_1 + string_2 + string_3 + string_4
        my_list = []
        my_list.extend(total_string)
        
        # password_length = int(input(password_length))
        while True:
            try:
                password_length = int(input(password_length))
                return "".join(random.sample(my_list,password_length))
            except ValueError:
                print("Password length must be a number.")
            
if __name__ == "__main__":
    password = password_generator("Please enter password length:")
    print(f"Your password is:{password}")