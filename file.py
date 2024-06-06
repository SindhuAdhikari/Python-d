file_path="C:/Users/user/Dropbox/My PC (LAPTOP-VKLMLSC8)/Desktop/Python/file.TXT"
# with open(file_path ,"r")as f:
#     for line in f.readlines():
#         print(line)
    
with open(file_path,"w")as f:
    print(type(f))
    for index in range(100):
        f.write("sindhu\n")
    f.close()
    