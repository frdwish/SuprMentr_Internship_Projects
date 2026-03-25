def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(i)

    print("\nCounts:")
    print("Fizz:", fizz_count)
    print("Buzz:", buzz_count)
    print("FizzBuzz:", fizzbuzz_count)


fizz_buzz()