__author__ = 'JeredYang'

def find_secret_message(paragraph):
    #your code here
    paragraph = paragraph.translate(None, "?.!/;:")
    cha_list = paragraph.lower().split(" ")
    a_dict = {}
    a_list = []
    result = ""

    for index in range(len(cha_list)):
        dup = a_dict.keys()
        if cha_list[index] in dup:
            a_list.append(cha_list[index])
        else:
            print cha_list[index]
            a_dict[cha_list[index]] = index

    for index in range(len(a_list)):
        result = result + a_list[index]
        if index != len(a_list) - 1:
             result += " "

    return result