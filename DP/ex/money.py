#    一日プラス２千円で終了

#     ３連続で負けたら終了

import numpy as  np
import matplotlib.pyplot as plt
import random

n = 300000                          #資金n円

N = np.array([])                    #試行結果の配列

bets = 1000                         #betsの最低金額1,000円

day_count = 0

while True:                  #n日やる
    if n < 1000 or day_count == 365:
        break
    win = 0                         #勝ち分の初期化
    count = 0                           #一日の取引回数

    while True:                     #勝つまでやる
        
        if bets == 16000:            #betsがm円のとき,やめる。
            bets = 1000
            break

        if n <= 0 or bets > n:     #資金が0円、または、bets金額が資金を超える場合は終了する。
            bets = 1000
            break
        
        k = random.randint(1,100)    #確率1/2

        if k <= 55:       #勝ちのとき
            count += 1              #取引回数加算
            #print("勝ち")
            n += int(bets*0.95)  #betsが加算される。
            win += bets             #勝ち分の計算
            bets = 1000             #betsの初期化
            #print("所持金:{} 勝ち分:{}".format(n, win))
            break

        else:                       #負けのとき
            count += 1              #取引回数加算
            #print("負け")
            n -= bets               #betsが没収される。
            win -= bets             #勝ち分の計算（マイナス）
            bets = int(bets * 2)    #betsを2倍にする
            #print("所持金:{} 勝ち分:{} next bets:{}".format(n, win, bets))
    day_count += 1

    N = np.append(N, n)             #一日の取引を記録する。
    print("win:{} 取引回数:{} 資金:{} 日にち:{}".format(win, count, n, day_count))                      #勝ち分を表示する。

print("total win:{}".format(int(N[len(N)-1]-300000)))