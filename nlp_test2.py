filepath = "/Users/apple/Downloads/ce2.txt"
mylist = []
global maxlength


#正向最大匹配
def FMM(input):
    sentence= input
    split_list = []
    len_line = len(sentence)
    while len_line > 0:
        tryword = sentence[0:maxlength]
        while tryword not in mylist:
            if len(tryword) == 1:
                break
            tryword = tryword[0:len(tryword)-1]
        split_list.append(tryword)
        sentence = sentence[len(tryword):]
        len_line = len(sentence)
    return split_list



#逆向最大匹配
def RMM():
    print("b")


#装载字典到数据结构中
def loadDictionary():
    global maxlength
    maxlength = 0
    with open(filepath, encoding = "utf-8") as f:
        for eachline in f.readlines():
            eachword = eachline.strip().split(",")
            #print(eachword)
            mylist.append(eachword[0])
    #print(mylist)
    for everyword in mylist:
        if len(everyword) > maxlength:
            maxlength = len(everyword)

if __name__ == '__main__':
    #maxlength = 0
    loadDictionary()
    #print(maxlength)
    inputstr = input("请输入一句汉语语句：")
    list_out = FMM(inputstr)
    print(list_out)

