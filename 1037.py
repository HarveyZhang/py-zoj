t = int(raw_input())

for i in range(t):
  m, n = map(int, raw_input().split())
  print "Scenario #%d:" % (i+1)
  if m&1 and n&1:
    print "%.2f" % (m*n+0.41)
  else:
    print "%.2f" % float(m*n)
  print ""