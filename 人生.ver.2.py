# 2023/02/21作成

import random


# 19個の数字から成るデッキを作る関数。
def make_deck():
    made_deck = []
    print("【プレイヤー1】\n数字を19枚分、入力してください。\
    \nルール1：数字は何桁でも構いません。\
    \nルール2：同じ数字を2回以上入力しないでください。\n")

    while len(made_deck) < 4:
        try:
            num = int(input("{}枚目: ".format(len(made_deck)+1)))
        except:
            num = print("数字を入力してください。")
            continue
        if num in made_deck:
            print("同じ数字は入力できません。")
            continue
        else:
            made_deck.append(int(num))

    return made_deck


# 19個の数字の中から数字を1つ選ぶ関数。
def choose(deck):
    passed_deck = deck
    resisted_deck = []
    count = 0
    print("\n【プレイヤー2】\n「抵抗」または「運命」を選んでください。\
    \n「抵抗」は \"r\" 、「運命」は \"d\" を入力します。")

    while count < len(deck)-1:
        draw_num = random.choice(passed_deck)
        if draw_num == "$":
            continue
        dind = passed_deck.index(draw_num)
        passed_deck[dind] = "$"
        resisted_deck.append(draw_num)
        done = False
        correct = False

        print("\n{}回目の選択です。".format(str(count+1)))
        print("引いた数字は {} です。".format(str(draw_num)))
        while not correct:
            pl2_choose = input("「抵抗」または「運命」を選んでください。: ")
            if pl2_choose == "r":
                correct = True
            elif pl2_choose == "d":
                correct = True
                break
            else:
                pl2_choose = print("\n入力が間違っています。\n")
        if pl2_choose == "d":
            done = True
            break
        count += 1

    passed_deck = [j for j in passed_deck if j != "$"]
    if not done:
        draw_num = passed_deck[0]
        print("\n最後の1枚になりました。")

    print("\nあなたの「運命」は {} です。".format(str(draw_num)))

    passed_deck = passed_deck + resisted_deck

    return passed_deck, draw_num


# 選んだ数字が、19枚の中で何番目に大きいかを特定する関数。
def judge(choosed):
    deck, choosed_num = choosed
    deck = sorted(deck, reverse=True)
    dind_2 = deck.index(choosed_num)
    print(deck)
    print("\n{}番目に大きい数字でした。".format(str(dind_2+1)))


# ゲームを実行する関数。
def the_life():
    deck = make_deck()
    choosed = choose(deck)
    judge(choosed)


the_life()
