#============================3===============================
# file1 = open("MyFile.txt","w")
# file1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
# file1.close()
 
# file1 = open("myfile.txt","r+")
# sign = input("Enter a sign: ")
# text = file1.read()
# count =0
# for word in text:
#     if word.startswith(sign):
#         count +=1

# file1.close()
# print(f"Number of words, startwith {sign}: {count}")
#===================================4==============================
# file1 = open("MyFile.txt","w")
# file2 = open("MyFile2.txt","w")
# file1.write("* * * *")
# file1.close()
# file1 = open("myfile.txt","r+")
# text = file1.read()
# for sign in text:
#     if sign == '*':
#         sign = '&'
#         file2.write(sign)
# file2.close()
# file2 = open("MyFile2.txt","r+")
# text2 = file2.read()
# print(text2)
# file2.close()
#========================5==================================
# file1 = open("MyFile.txt","w")
# file1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
# file1.close()
 
# file1 = open("myfile.txt","r+")
# text = file1.read()
# count =0
# for letter in text:
#         count +=1
# print(count)
#====================6============================
# file1 = open("MyFile.txt","w")
# file1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
# file1.close()
 
# file1 = open("myfile.txt","r+")
# text = file1.readlines()
# count =0
# for letter in text:
#         count +=1
# print(count)
#==============================7================================
file1 = open("MyFile.txt","w")
file2 = open("MyFile2.txt","w")
file1.write("c++ c# python java kotlin html css")
file2.write("html css")
file2.close()
file1.close()
file1 = open("MyFile.txt","r+")
file2 = open("MyFile2.txt","r+")
text1 = file1.read()
text2 = file2.read()

text1.split()
list = []
for i in text1:
    list.append(i)
text2.split()
file3 = open("MyFile3.txt","w")
for word in list:
    if word in text2:
        file3.write(word)

file3.close()
file3 = open("MyFile3.txt","r+")
text3 = file3.read()
print(text3)
