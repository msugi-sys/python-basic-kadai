# 14章_課題_グローバルスコープとローカルスコープ
"""
# 下記エラーコードを修正
price1 = 100
price2 = 200

def total()
	tax = 1.1
	return price1 + price2

print(total() * tax)
"""

price1 = 100
price2 = 200

def total(x,y):
	return x + y

tax = 1.1
print(total(price1,price2) * tax)
