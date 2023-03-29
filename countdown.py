def countdown(word):
    wrong = 0
    stages = ["8",
              "7",
              "6",
              "5",
              "4",
              "3",
              "2",
              "1",
              "0",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("カウントダウンへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は {}/".format(word))

countdown("cat")