import random

def hangman():
    words = ["php", "ruby", "python", "java", "swift", "scala", "perl"]
    random_num = random.randint(0,6)
    word = words[random_num]
    wrong = 0
    stages = ["",
              "----------",
              "|    |    ",
              "|    |    ",
              "|    0    ",
              "|   /|\   ",
              "|    /\   ",
              "|         ",
              ]
    letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        guess_num = input("文字を入力してください！：")
        if guess_num in letters:
            chara_index = letters.index(guess_num)
            letter_board[chara_index] = guess_num
            letters[chara_index] = '$'
        else:
            wrong += 1
        print(" ".join(letter_board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in letter_board:
            print("あなたの勝ち！")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
         print("あなたの負け！")
         print("正解は{}".format(word))

hangman()
