import re

message = "To be, or not to be, that is the question"
words = re.findall('\w+',message)
print(f'number of words is: {len(words)}')

