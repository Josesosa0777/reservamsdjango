class Solution:
    def romanToInt(self, s: str) -> int:
        if s != None:
            units = 0
            if 'IX' in s:
                s=s.replace('IX', '')
                units = 9
            elif 'IV' in s:
                s=s.replace('IV', '')
                units = 4
            else:
                if 'V' in s:
                    units = 5
                if 'I' in s:
                    units += s.count('I')
            tens = 0
            print(s)
            if 'XC' in s:
                s=s.replace('XC', '')
                tens = 90
            elif 'XL' in s:
                s=s.replace('XL', '')
                tens = 40
            else:
                if 'L' in s:
                    tens = 50
                if 'X' in s:
                    tens += s.count('X') * 10
            hundreds = 0
            print(s)
            if 'CM' in s:
                s=s.replace('CM', '')
                hundreds = 900
            elif 'CD' in s:
                s=s.replace('CD', '')
                hundreds = 400
            if 'D' in s:
                hundreds = 500
            if 'C' in s:
                hundreds += s.count('C') * 100
            thousands = 0
            if 'M' in s:
                thousands = s.count('M') * 1000
            return thousands + hundreds + tens + units

if __name__ == "__main__":
    print(Solution.romanToInt('', 'MMCCCXCIX'))

