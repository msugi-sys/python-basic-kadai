# 15章_課題_クラスを使ったプログラム
"""
名前(name)と年齢(age)の属性を持つHumanクラスを作成
nameとageを標準出力(print)するメソッド(printinfo)を追加
Humanクラスのインスタンスは、変数に代入してプログラム内で使用
"""
class Human:
	def __init__(self, name: str, age: int) -> None:
		"""コンストラクタ"""
		self.name = name
		self.age = age

	def printinfo(self) -> None:
		print('名前は',self.name,'です。')
		print('年齢は',self.age,'です。')

a = str(input('名前：'))
b = int(input('年齢：'))
print('\n')
x = Human(a, b)
x.printinfo()
