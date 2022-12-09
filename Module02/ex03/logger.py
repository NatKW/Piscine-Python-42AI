import time
from random import randint
import os

def log(func):
	user = os.environ['USER']
	task = func.__name__.replace('_', " ").title()
	def inner(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		elapsed_time = time.time() - start_time
		unit = 's'
		if elapsed_time < 0.001:
			elapsed_time *= 1000
			unit = 'ms'
		with open("machine_log", "a") as f:
			ret =  f'({user})Running: {task:<15} [exec-time = {elapsed_time:.3f} {unit}]\n'
			f.write(ret)
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