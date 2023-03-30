# 2023/02/21作成
import random

def make_deck():
    deck = []
    print("【プレイヤー1】\n数字を19枚分、入力してください。\
    \nルール1：数字は何桁でも構いません。\
    \nルール2：同じ数字を2回以上入力しないでください。\n")

    while len(deck) < 4:
        try:
            num = int(input("{}枚目: ".format(len(deck)+1)))
        except:
            num = print("数字を入力してください。")
            continue
        if num in deck:
            print("同じ数字は入力できません。")
            continue
        else:
            deck.append(int(num))

    return deck


def the_life():
    deck = make_deck()
    r_deck = []
    count = 0
    print("\n【プレイヤー2】\n「抵抗」または「運命」を選んでください。\
    \n「抵抗」は \"r\" 、「運命」は \"d\" を入力します。")

    while count < len(deck)-1:
        draw_num = random.choice(deck)
        if draw_num == "$":
            continue
        dind = deck.index(draw_num)
        deck[dind] = "$"
        r_deck.append(draw_num)
        judge = False
        correct = False

        print("\n{}回目の選択です。".format(str(count+1)))
        print("引いた数字は {} です。".format(str(draw_num)))
        while not correct:
            pl2_judge = input("「抵抗」または「運命」を選んでください。: ")
            if pl2_judge == "r":
                correct = True
            elif pl2_judge == "d":
                correct = True
                break
            else:
                pl2_judge = print("\n入力が間違っています。\n")
        if pl2_judge == "d":
            judge = True
            break
        count += 1

    deck = [j for j in deck if j != "$"]
    if not judge:
        print("\n最後の1枚になりました。")
        draw_num = deck[0]
    deck = deck + r_deck
    deck = sorted(deck, reverse=True)
    print("\nあなたの「運命」は {} です。".format(str(draw_num)))
    print(deck)
    dind_2 = deck.index(draw_num)
    print("\n{}番目に大きい数字でした。".format(str(dind_2+1)))


the_life()
