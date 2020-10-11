# a = False
# if a is True:
#     if 20 % 2 is 0:
#         print("even")
#     if 45 % 3 is 0:
#         print("odd")
# else:
#     print("False")


def messageWithWelcome(str):
    # Nested function
    def addWelcome():
        return "Welcome to "

    # Return concatenation of addWelcome()
    # and str.
    return addWelcome() + str


# To get site name to which welcome is added


def site(site_name):
    return site_name


print(messageWithWelcome(site("GeeksforGeeks")))
