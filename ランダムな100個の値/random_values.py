from random import randint
import csv

# 乱数の範囲と生成数
start_range = 200
end_range = 400
num_values = 100

# ランダムな値の生成
random_values = [randint(start_range, end_range) for _ in range(num_values)]

# CSVファイルへの書き込み
with open('random_values.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for value in random_values:
        writer.writerow([value])  # 値の書き込み
