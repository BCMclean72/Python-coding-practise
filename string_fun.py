def string_diamond(full_string):
    num_letters = len(full_string)
    outstring = ""
    for i in range (0,num_letters):
        outstring += full_string[0:i+1]+"\n"
    for j in range (0,num_letters):
        outstring += " "*j + full_string[j:num_letters] +"\n"
    return outstring


def string_triangle(full_string):
    num_letters = len(full_string)
    outstring = ""
    for i in range (0,num_letters):
        outstring += full_string[0:i+1]+"\n"
    for j in range (0,num_letters):
        outstring += full_string[j:num_letters] +"\n"
    return outstring
            

fun_string = input("Insert a fun string: ")
for i in range(0,5):
    out = string_diamond(fun_string) + string_triangle(fun_string)
    print(out)
    # string_triangle(fun_string)
