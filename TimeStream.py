import numpy as np
step_size = 1

class TimeStream:
	past = np.array([]) # index 0 is t = 0, index 1 is t = -1, etc.
	memo = {}

	def __init__(p):
		past = p

	def nth_derivative(n):
		if n in memo:
			return memo[n]
		memo[n] = sum([
			math.pow(-1, n) * math.choose(n, i) * past[i * step_size]
			for i in range(n + 1)
		])
		return memo[n]

	def project(duration, degree):
		projection = [past[0] for _ in range(duration)]
		for t in range(duration):
			for n in range(1, degree + 1):
				projection[i] += t * np.pow(self.nth_derivative(n), n) / math.factorial(n)
		return projection