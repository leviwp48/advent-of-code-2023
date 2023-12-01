

int_mapping = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

FILENAME = "input.txt"

def find_nums() -> []:
    num_list = []
    with open(FILENAME, 'r') as f:
        for content in f:
            num = ""
            front_num = ()
            front_word = ""
            back_num = ""
            back_word = ""

            # find front_num
            for i in range(len(content)):
                try:
                    if type(int(content[i])) == int and not front_num:
                       front_num = (i, content[i])
                except:
                    pass

            # find back_num
            for i in range(len(content) - 1, -1, -1):
                try:
                    if type(int(content[i])) == int and not back_num:
                       back_num = (i, content[i])
                except:
                    pass
            # find front_word
            front_word = find_word_front(content)

            # find back_word
            back_word = find_word_back(content)

            if front_num:
                if front_word[0] == -1 or front_num[0] < front_word[0]:
                    num += front_num[1]
                else:
                    num += front_word[1]
            else:
                num += front_word[1]       

            if back_num:
                if back_word[0] == -1 or back_num[0] > back_word[0]:
                    num += back_num[1]
                else:
                    num += back_word[1]
            else:
                num += back_word[1]

            if num != "":
                # print("adding this num: ", num)
                num_list.append(int(num))

    return num_list


def find_word_front(word) -> str:
    index = ()
    for key in int_mapping.keys():
        temp = word.find(key)
        if not index or index[0] == -1:
            index = (temp, int_mapping[key])
        if temp < index[0] and temp != -1:
            index = (temp, int_mapping[key])
    return index

def find_word_back(word) -> str:
    index = ()
    for key in int_mapping.keys():
        start_index = 0
        temp = 0
        while temp != -1:
            temp = word.find(key, start_index)
            if not index or index[0] == -1:
                index = (temp, int_mapping[key])
            if temp > index[0] and temp != -1:
                index = (temp, int_mapping[key])
            start_index = temp + 1
    return index


print(sum(find_nums()))

