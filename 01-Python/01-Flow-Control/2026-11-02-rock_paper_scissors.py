# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてくださいn = int(input())

n = int(input())

win_count = 0

for i in range(n):
    r_c_p = input().split()

    if r_c_p[0] == "G" and r_c_p[1] == "C":
        win_count += 1

    elif r_c_p[0] == "C" and r_c_p[1] == "P":
        win_count += 1

    elif r_c_p[0] == "P" and r_c_p[1] == "G":
        win_count += 1

print(win_count)
