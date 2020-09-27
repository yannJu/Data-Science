import sys
from collections import Counter
import re

pattern = '[^0-9^a-z]'
c = Counter()

for line in sys.stdin:
	lst = re.split(pattern, line.lower())
	c.update(lst)
c.pop("")

for i in c.most_common(n=1000):
	print("{}\t{}".format(i[0], i[1]))
