num = eval(input("Enter a number between 0-10 to convert it to words  "))

num_in_words = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

if(num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(num_in_words.get(num))
else:
    print(f" Entered number {num} is not in the range of 0-10. Please enter the number within 0-10")

