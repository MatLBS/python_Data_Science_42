def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args: any, **kwds: any):
			print(args)



def main():
	try:
		@callLimit(3)
		def f():
			print("f()")


		@callLimit(1)
		def g():
			print("g()")


		for i in range(3):
			f()
			g()
	except AssertionError as error:
		print("AssertionError:", error)


if __name__ == "__main__":
	main()
