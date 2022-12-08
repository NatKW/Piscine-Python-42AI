import time
from random import randint
import os

def log(func):
	user = os.environ['USER']
	task = func.__name__.replace('_', " ").capitalize()
	def inner(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		with open("machine_log", "a") as f:
			f.write(user)
			f.write('Running: ')
			f.write(task)
			f.write(str(end-start))
			f.write('\n')
		return result
	return inner

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)