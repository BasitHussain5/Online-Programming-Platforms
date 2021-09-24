#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

#Read the number of test cases.
total_no_of_test = int(input())
for i in range(total_no_of_test):
    a, b = map(int, input().split(" ")) 
    addition = a + b
    print(addition)