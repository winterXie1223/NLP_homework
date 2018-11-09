mydic = {}
filename = 'D:\学习资料\dic_ec.txt'
inputstrs = [] #一组输入



def loadDictionary():
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            attribute = ''
            explanation = {}
            eachline = str(line).strip().split("")  #eachline是用空格分割开的字典每一行具体内容
            # print(eachline[:-1])
            for eachword in eachline[1:-1]:
                if eachword[-1:] == '.':
                    attribute = eachword
                    explanation[attribute] = []
                elif attribute in explanation:
                    explanation[attribute].append(eachword)
            mydic[eachline[0]] = explanation
    # print(mydic)

def judgeIfValiableWord(word, mydic):
    #length = len(word)

    #不规则情况


    flagword = word    #次序一二三 单复数
    if mydic.get(flagword, "not_exist") == "not_exist" and flagword[-1:] == 's':
        flagword = word[:-1]
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if flagword[-2:] == 'es':
        flagword = word[:-2]
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if flagword[-3:] == 'ies':
        flagword = word[:-3] + 'y'
    if mydic.get(flagword, "not_exist") != "not_exist":
        return flagword


    #次序四五六七 进行时
    if mydic.get(flagword, "not_exist") == "not_exist" and word[-3:] == 'ing':
        flagword = word[:-3]
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if flagword[-3:] == 'ing':
        flagword = word[:-3] + 'e'
    if mydic.get(flagword, "not_exist") == "not_exist":
         flagword = word
    else:
        return flagword
    if flagword[-4:] == 'ying':
        flagword = word[:-4] + 'ie'
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if word[-3:] == 'ing':
        flagword = word[:-4]
    if mydic.get(flagword, "not_exist") != "not_exist":
        return flagword

    #次序八九十十一 过去时
    if mydic.get(flagword, "not_exist") == "not_exist" and word[-2:] == 'ed':
        flagword = word[:-2]
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if flagword[-2:] == 'ed':
        flagword = word[:-1]
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if word[-3:] == 'ied':
        flagword = word[:-3] + 'y'
    if mydic.get(flagword, "not_exist") == "not_exist":
        flagword = word
    else:
        return flagword
    if word[-2:] == 'ed':
        flagword = word[:-3]
    if mydic.get(flagword, "not_exist") != "not_exist":
        return flagword

    return "Nothing found"

if __name__ == '__main__':
    loadDictionary()  # 装载字典
    while True:
        inputstr = input("请输入一个英文单词：")
        if inputstr == 'went':
            print("go", mydic["go"])
        if inputstr == 'gone':
            print("go", mydic["go"])
        if inputstr == 'sat':
            print("sit", mydic["sit"])
        if mydic.get(inputstr, "not_exist") != "not_exist":
            print(mydic[inputstr])
        else:
            x = judgeIfValiableWord(inputstr, mydic)# 单词不在字典中，形态还原
            if x != "Nothing found":
                print(x, mydic[x])
            else:
                print("Nothing found")
