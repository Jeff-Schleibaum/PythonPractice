# jeff schleibaum
# Write a funtion that returns the largest number in a list
# list numbers = [7, 2, 10, 5] answer = 10



def largestnum(numbers): # declare function
    largest = numbers[0] # variable in function assumming first num is the largest

    for number in numbers: # loop through numbers and compare the largest
        if number > largest: # if number is larger than largest found
            largest = number # update largest to the new biggest num

    return largest # return the largest



numbers = [7, 2, 10, 5]
print(largestnum(numbers))

