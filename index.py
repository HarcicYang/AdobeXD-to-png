#用于提取adobe xd 中的png图片文件
import os,zipfile,shutil,sys
from tkinter import filedialog as fileloader
from win10toast import ToastNotifier
#选择文件
command=sys.argv #接收命令行参数
if len(command) == 1:
    path=fileloader.askopenfilename(title="选择一个Adobe XD文件",filetypes=(("Adobe XD设计文件","*.xd"),))
    output=fileloader.askdirectory(title="选择保存位置")
    cmdtype=0
else:
    path=command[1]
    output=command[2]
    cmdtype=1
#处理文件
def process(path):
    global output
    #创建临时目录
    os.mkdir("./temp")
    os.mkdir("./temp/files")
    #文件转换并拷贝
    with open(path,"rb") as read:
        info=read.read()
    with open("./temp/temp.zip","wb") as write:
         write.write(info)
    #提取
    zip=zipfile.ZipFile("./temp/temp.zip")
    zipfile.ZipFile.extractall(zip,'./temp/files/')
    zip.close()
    #将文件拷贝到output文件夹
    filename1=os.listdir("./temp/files/renditions/")[0]
    filename2=os.listdir("./temp/files/renditions/")[1]
    shutil.copy("./temp/files/renditions/"+filename1,output)
    shutil.copy("./temp/files/renditions/"+filename2,output)
    #删除临时目录
    shutil.rmtree("./temp")
    #完成
    if cmdtype == 0:
        # easygui.msgbox("操作完成。\ndone.")
        ToastNotifier().show_toast("操作完成","done.",duration=5)
    elif cmdtype == 1:
        ToastNotifier().show_toast("操作完成","done.",duration=5)

process(path)