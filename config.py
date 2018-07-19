import csv
'''
CSV文件列名：商品编号，商品名称，划线价，销售价，税费，利润，高级会员，蓝钻会员，红钻会员。其中最后三列为推荐供应奖的三
个级别，红钻以上与红钻一致。
'''
Array = []
csv_file = csv.reader(open('changeprice.csv', 'r'))


for stu in csv_file:
    Array.append((stu[0], stu[2], stu[3], stu[4], stu[5], stu[6], stu[7], stu[8]))


