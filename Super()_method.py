class Parent():
	def show(self):
		print("conform")
		
class Child(Parent):
	def show(self):
		super().show()
		print("too")
			
c=Child()
c.show()
