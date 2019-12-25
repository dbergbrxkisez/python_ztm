def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

# Should do one thing really well.
# Should return something.


# total = 15
# total = sum(10, 5)
total = sum(10, 20)
# print(sum(10, sum(10, 5)))
# print(total(10, 20))
print(total)
