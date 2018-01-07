class Solution():
    def myAtoi(self, str):
        # remove whitespace
        str = str.strip()

        MAX_NEG = (1 << 31)
        MAX_POS = MAX_NEG - 1
        
        # check for null value
        if not str:
            return 0

        negative = False
        
        # check if negative and move index past the sign
        sign = 1
        if str[0] in '+-':
            if str[0] == '-':
                negative = True
            str = str[1:]

        result = 0

        # Iterate through string and convert each digit
        for d in str:
            if not (d.isdigit()):
                break
            
            result = result * 10 + ord(d) - ord('0')
        
        if result >= MAX_POS:
            if not negative:
                return MAX_POS
            elif result > MAX_NEG:
                return -MAX_NEG

        if result == 0: return 0
        else: return -result if negative else result
