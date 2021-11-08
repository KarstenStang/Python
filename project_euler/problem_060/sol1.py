def extendPrimes(primes, newPrimeCount):	
	newPrime = primes[-1]
	while(len(primes) < newPrimeCount):
		newPrime += 2
		while isPrime(primes, newPrime) == False:
			newPrime += 2

		primes.append(newPrime)

	return primes

def isPrime(primes, number):
	while number > primes[-1] ** 2:
		primes = extendPrimes(primes, len(primes) * 2)

	for prime in primes:
		if prime ** 2 > number:
			return True
		else:
			if number % prime == 0:					
				return False

primes = [2, 3, 5, 7, 11, 13, 17, 19]
n = 2
primeSets = [[]]
while True:
	for primeSet in primeSets:
		for prime in primeSet:
			if isPrime(primes, int(str(prime) + str(primes[n]))) == False or isPrime(primes, int(str(primes[n]) + str(prime))) == False:
				break
		else:
			newPrimeSet = primeSet + [primes[n]]
			primeSets.append(newPrimeSet)

			if len(newPrimeSet) >= 5:
				print(sum(newPrimeSet))
				exit(0)

	n += 1
