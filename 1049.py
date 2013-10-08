n = int(raw_input())

PI = 3.14159

for i in range(1, n+1):
  x, y = map(float, raw_input().split())
  z = (x*x+y*y)*PI/100+1
  print "Property %d: This property will begin eroding in year %d." % (i, int(z))

print "END OF OUTPUT."