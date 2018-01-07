"""P     I     N
A   L S   I G
Y A   H R   
P     I


P   A   H   N
A P L S I I G
Y   I   R

1st row, 2nd row, 3rd row, 4th row, 3rd row, 2nd row, 1st row, 2nd row,
3rd row, 4th row, 3rd row, 2nd row, 1st row, 2nd row

1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1...

hash map

1 2 3 2 1 2 3 2 1 2 3
12321232123212
PAYPALISHIRING
PAHNAPLSIIGYIR

['PAHN','APLSIIG','YIR']
PAHNAPLSIIGYIR

12343212343212
PAYPALISHIRING

123
PAYPALISHIRING


UNICORNS

U   O
N C R S
I   N

12321232
UNICORNS

13742586
UNICORNS

how many rows = how many strings we need
4 rows means 4 strings

['', '', '', '']
"""

class Solution(object):

    def convert(self, string, numRows):
        if not numRows or not string:
            return ''
        if numRows == 1:
            return string
        
        result = ''
        
        strList = ['' for i in range(numRows)]
        i = 0
        direction = 1
        maxIndex = numRows
        
        for c in string:
            strList[i] += c
            i += direction * 1
            
            # when we reach the max, change direction
            if i == maxIndex:
                i = maxIndex - 2
                direction *= -1
            if i == -1:
                i = 1
                direction *= -1

        for item in strList:
            result = result + item

        return result
