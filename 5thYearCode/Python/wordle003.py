from random import randint
def main():
    words = make_words()
    answer_list = make_parameters(words)[0]
    record = make_parameters(words)[1]
    record = single_turn(answer_list, record)
    display_result(record)
def make_words():
    words=["cat","hat","run","sit","top"]
    return words
def make_parameters(words):
    answer_index = randint(0,4)
    answer = words[answer_index]
    answer_list = [answer[0], answer[1], answer[2]]
    record=["_","_","_"]
    return answer_list, record
def get_guess():
    guess = input("Please choose a 3 letter word ")
    guess_list=[guess[0], guess[1], guess[2]]
    print(guess_list)
    return guess_list
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