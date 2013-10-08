from sys import stdin

s = int()
for line in stdin:
  s += float(line)

print "$%.2f" % (s/12)