# ==============================1============================
# file_list = []
# while True:
#     file_name = input(
#         "Enter file name (or 'quit' for exit): ")
#     if file_name.lower() == "quit":
#         break
#     else:
#         file = open(file_name, 'w')
#         file.close()
#         file_list.append(file_name)
#         print(f"File '{file_name}' added succesfuly.")
# combined_content = '\n'.join(file_list)
# final_file = open('final_file', 'w')
# final_file.write(combined_content)
# final_file.close()
# print("File saved succesfuly.")
# =============================2============================
file_list2 = []
signes = 'S I G N E S'
while True:
    file_name2 = input(
        "Enter file name (or 'quit' for exit): ")
    if file_name2.lower() == "quit":
        break
    else:
        file = open(file_name2, 'w')
        file.write(signes)
        file.close()
        file = open(file_name2, 'r')
        contents = file.read()
        file_list2.append(contents)
        print(f"File '{file_name2}' added succesfuly.")
combined_content2 = '\n'.join(file_list2)
final_file2 = open('final_file', 'w')
final_file2.write(combined_content2)
final_file2.close()
print("File saved succesfuly.")
