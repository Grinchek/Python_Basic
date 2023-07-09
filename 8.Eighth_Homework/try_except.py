# ===============================1=============================
'''my_str = input("Enter number as string: ")
try:
    print(f"The number is {int(my_str)}")
except:
    print("Error")'''
# ================================2=============================
my_str = input("Enter number as string: ")

# ==============chapt1=========


'''def checking(string):
    print(int(string))


try:
    checking(my_str)
    print("Error")'''
# ==============chapt2=========


def checking(string):
    try:
        print(int(string))
    except:
        print("Error")


checking(my_str)
