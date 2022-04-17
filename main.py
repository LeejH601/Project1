import os
import re
import exrex


car_re = re.compile(r'''
^
\d{2,3}             
[ ]*
[가-힣]
[ ]*
\d{4}
[ ]*
\d{4,5}
[ ]*
.*
''', re.VERBOSE)

pattern = r'''
^
\d{2,3}             
[ ]*
[가-힣]
[ ]*
\d{4}
[ ]*
\d{4,5}
[ ]*
.*
'''

final_pattern = re.sub(r'[ ]{2,}|\t|\n', '', pattern)

test_str = [exrex.getone(final_pattern, 5) for _ in range(1000)]

for t in test_str:
    print(t)





if __name__ == '__main__':

