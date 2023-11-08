# 17章_課題
"""
名前(name)と年齢(age)の属性を持つHumanクラスを作成
Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加
	ageが20以上の場合に大人であること
	そうでない場合に大人でないこと
Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出す
"""

list_human = []

class Human:
	def __init__(self, name: str, age: int) -> None:
		"""コンストラクタ"""
		self.name = name
		self.age = age

	def printinfo(self) -> None:
		print('名前は',self.name,'です。')
		print('年齢は',self.age,'です。')

	def check_adult(self):
		if self.age >= 20:
			print(self.name,'は大人です。')
		else:
			print(self.name,'は大人ではありません。')

# 登録人数を入力
num_people = int(input('登録人数：'))

# 入力された人数分だけHumanインスタンスを作成
for i in range(num_people):
	a = str(input('名前：'))
	b = int(input('年齢：'))
	x = Human(a, b)
	list_human.append(x)

# リストの各要素に対してprintinfoとchek_adultを呼び出す
for human in list_human:
	human.printinfo()
	human.check_adult()
