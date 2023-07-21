import csv

# CSVファイルのパス
csv_file_path = "random_values.csv"
# 結果のファイルパス
result_file_path = "result.csv"

# 数値の読み込み
numbers = []
with open(csv_file_path, "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        for value in row:
            numbers.append(int(value))

# 数値のソート
numbers.sort()

# セット作成の準備
set1 = []
set2 = []
current_sum = 0

# 数値の配置
for number in numbers:
    if current_sum + number >= 800:
        if len(set1) < 3:
            set1.append(number)
            current_sum += number
        else:
            set2.append(number)
            current_sum += number
    else:
        set1.append(number)
        current_sum += number

# 結果の確認
if len(set1) <= 3 and len(set2) <= 3:
    print("Set1:", set1)
    print("Set2:", set2)
elif len(set1) > 3:
    set2.append(set1.pop())
    print("Set1:", set1)
    print("Set2:", set2)

# 結果のファイルへの書き込み
with open(result_file_path, "w", newline="") as result_file:
    writer = csv.writer(result_file)
    writer.writerow(["Set1"] + set1)
    writer.writerow(["Set2"] + set2)
