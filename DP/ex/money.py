import numpy as np
import matplotlib.pyplot as plt
import random

initial_balance = 100000  # 初期資金の設定
initial_bets = 1000  # 初期掛け金の設定
trials = 100  # 試行回数の設定
limit = 3  # 取引制限値の設定

payout = 1.85  # ペイアウトの設定

result_balance = np.array([])  # 残高の試行結果
result_tarade_count = np.array([])  # 取引回数の試行結果

for i in range(trials):  # trails回実行する

    balance = initial_balance  # 残高の初期化
    bets = initial_bets  # 掛け金の初期化

    win_count = 0  # 勝った回数の初期化
    lose_count = 0  # 負けた回数の初期化

    while True:  # 取引を繰り返す

        if balance < initial_bets:  # 残高が初期掛け金を下回ったら終了する
            break
        if balance < bets:  # 残高が現在の掛け金を下回ったら終了する
            break
        if lose_count >= 100:  # 負けた回数がn回以上のとき終了する
            break

        losing_streak_count = 0  # 連敗記録の初期化

        while True:  # 勝つまで繰り返す

            if balance < bets:  # 掛け金が残高を超えたら終了する。
                bets = initial_bets  # 掛け金を初期化してから終了する。
                break

            k = random.randint(1, 100)  # ランダム値の生成

            balance -= bets  # 掛け金分を支払う（取引開始）

            if k <= 50:  # 勝ったのとき
                win_count += 1  # 回数の加算
                balance += int(bets * payout)  # 残高に(掛け金*payout)が加算される。
                bets = initial_bets  # 掛け金の初期化
                losing_streak_count = 0  # 連敗カウントの初期化
                break  # その日の取引の終了

            else:  # 負けのとき
                lose_count += 1  # 回数の加算
                losing_streak_count += 1  # 連敗カウントの加算

                if losing_streak_count == limit:  # limit連敗のとき終了する
                    bets = initial_bets  # 掛け金の初期化
                    break

                # マーチンゲール法（改良）　負けた額の２倍ではなくpayout率に応じて勝ち分が+になるように調整
                parallel_balance = balance + int(bets * payout)  # もし勝っていた場合の残高
                # 掛け金を次に勝ったときに勝ち分が(initial_bets * (1-payout))円となるよう調整する
                bets = int((parallel_balance - balance)/(payout - 1))

    print("result:{} win:{} 取引回数:{} 勝ち:{} 負け:{}".format(
        balance, balance - initial_balance, win_count + lose_count, win_count, lose_count))  # 結果の出力
    result_balance = np.append(result_balance, balance)  # 残高を記録する。
    result_tarade_count = np.append(
        result_tarade_count, win_count+lose_count)  # 試行回数を記録する
