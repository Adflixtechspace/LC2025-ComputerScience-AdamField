from random import randint
def main():
    words = make_words()
    wdsize = len(words[0])
    answer_list = make_parameters(words, wdsize)[0]
    record = make_parameters(words, wdsize)[1]
    record = single_turn(answer_list, record)
    display_result(record)
def make_words():
    words=["bat","cat","dog","stop","hat","rat","run","sit","top"]
    return words
def make_parameters(words, wdsize):
    #answer_index = randint(0,6)
    answer_index =len(words)-1
    answer = words[answer_index]
    answer_list = []
    for number in range(wdsize):
        answer_list.append(answer[number])
    record=[]
    for mumber in range(wdsize):
        record.append("_")
    return answer_list, record
def get_guess():
    guess = input("Please choose a 3 letter word ")
    guess_list=[guess[0], guess[1], guess[2]]
    print(guess_list)
    return guess_list
    get_guess()
def check_4_green(answer_list, guess_list, record):
    for i in range(3):
        if answer_list[i] == guess_list[i]:
            record[i] = "X"
    return(record)
def display_result(record):
    print(record)
def single_turn(answer_list, record):
    guess_list = get_guess()
    record = check_4_green(answer_list, guess_list, record)
    return(record)
main()