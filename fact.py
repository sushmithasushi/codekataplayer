class reve:
	def __init__(self):
		self.n=int(input())
		p=1
		for i in range(1,self.n+1):
			p*=i
		print(p)
o=reve()
