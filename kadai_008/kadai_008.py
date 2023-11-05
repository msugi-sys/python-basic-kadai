# 8章_課題_if文で条件分岐、値はprint関数で出力

"""
変数varが、3の倍数の場合は「Fizz」を出力
変数varが、5の倍数の場合は「Buzz」を出力
変数varが、3の倍数と5の倍数の両方に該当する場合は「FizzBuzz」を出力
上記のどの場合にも該当しない場合は、変数varの値を出力
ただし、変数varは正の整数とします。
"""

var = int(input('正の整数：'))

if var <= 0:
	print('正の整数ではありません。')
elif var % 3 == 0 and var % 5 == 0:
	print('FizzBuzz')
elif var % 3 == 0:
	print('Fizz')
elif var % 5 == 0:
	print('Buzz')
else:
	print(var)
