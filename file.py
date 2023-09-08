
class utils:
    def reversed(self, num):
        if type(num) is not int:
            raise TypeError("input not an int") 
        return int("".join(reversed(str(num))))

    def formatter(self, num):
        if type(num) is not int:
            raise TypeError("input not an int")
        return '{:b}'.format(num), '{:o}'.format(num)
    