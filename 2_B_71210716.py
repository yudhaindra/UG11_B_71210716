str = ""
int = 123

def check_data_type(input1,input2):
    input2 = input2.lower()
    if (type(input1) == type(str)) and (input2 == "str"):
        print("Jawaban anda benar")
        return "True"

    elif (type(input1) == type(str)) and (input2 == "int"):
        print("Jawaban anda benar")
        return "True"

    elif (type(input1) == type(int)) and (input2 == "str"):
        print("Jawaban anda salah, seharusnya adalah: int")
        return "False"

    elif (type(input1) == type(str)) and (input2 == "int"):
        print("Jawaban anda salah, seharusnya adalah: str")
        return "False"
        
    else:
        print("Jawaban anda tidak valid")
        return "False"

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))