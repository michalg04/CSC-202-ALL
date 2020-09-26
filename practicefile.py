def takeoff():
    current = 3
    while True:
        yield current
        if current == 0:
            current = 4
        current = current -1

def main():
    counter = takeoff()
    print(next(counter))  # prints 3
    print(next(counter))  # prints 2
    print(next(counter))  # prints 1
    print(next(counter))  # prints 0
    print(next(counter))  # prints 3
    print(next(counter))  # prints 2
    print(next(counter))  # prints 1
    print(next(counter))  # prints 0
    print(next(counter))  # prints 3
    print(next(counter))  # prints 2
if __name__ == '__main__':
    main()


