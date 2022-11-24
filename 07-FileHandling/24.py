import re

message = "To be, or not to be, that is the question"
vowels = re.findall('[aouei]',message)
print(f'the number of vowels in the text is:  {len(vowels)}')