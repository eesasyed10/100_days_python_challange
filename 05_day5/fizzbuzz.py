for fizzbuzz in range(1,101):
    if fizzbuzz % 3==0 and fizzbuzz % 5==0:
        fizzbuzz="fizzbuzz"
        
    elif fizzbuzz % 3==0:
        fizzbuzz="fizz"

    elif fizzbuzz % 5==0:
        fizzbuzz = "buzz"

    print(fizzbuzz)