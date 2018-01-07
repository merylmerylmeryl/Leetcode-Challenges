class Solution(object):
    def reverse(self, x):
        # its place in the string should be the length
        tempStr = str(x)
        result = ''
        sign = 1
        
        for c in tempStr:
            result = c + result

        if result[-1] in '+-':
            if result[-1] == '-':
                sign = -1
            result = result[:-1]
                
        num = sign * int(result)
        
        if num >= 2**31 - 1 or num <= - (2**31) - 1:
            return 0
        
        return num

# for a faster solution, don't use strings.
# use % and //
# check for overflow inside the loop
