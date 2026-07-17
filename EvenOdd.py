# jeff schleibaum
# write a function that returns the sum of all even numbers

def even_sum(numbers):

    total = 0 # set total to zero

    for number in numbers: # check a list for numbers
     if number % 2 == 0: # than check the number to see if % is 0 whisch means it was even
         total +=number # add to total when number is even and add all even numbers together

    return total

numbers = [1, 2, 3, 4,]
print(even_sum(numbers))