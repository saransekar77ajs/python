import sys

print(sys.argv)

total = 0


# def sum(argv):
#     global total
#     for num in argv:
#         if not num.isdigit():
#             pass
#         else:
#             total += int(num)


# def sum(argv):
#     global total
#     for num in argv[1:]:
#         total += int(num)


def sum(argv):
    total = 0
    for num in argv[1:]:
        total += int(num)
    return total


# sum(sys.argv)
result = sum(sys.argv)
# print("The total sum:", total)
print("The total sum:", result)
