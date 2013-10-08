dc = ['.', '!', 'X', '#']
ts = int(raw_input())
for t in xrange(ts):
  ds = int(raw_input())
  D = map(int, raw_input().split())
  den = [[0]*22]
  for i in xrange(20):
    den.append(map(int, ("0 "+raw_input()+" 0").split()))
  den.append([0]*22)
  _den = [[0]*22 for i in xrange(22)]

  for d in xrange(ds):
    for i in xrange(1,21):
      for j in xrange(1,21):
        s = den[i][j] + den[i-1][j] + den[i+1][j] + den[i][j-1] + den[i][j+1]
        # print s, " ",
        _den[i][j] = den[i][j] + D[s]
        if _den[i][j] < 0:
          _den[i][j] = 0
        if _den[i][j] > 3:
          _den[i][j] = 3
      # print ""
    den = _den[:]

    outStr = str()
    for i in xrange(1,21):
      for j in xrange(1,21):
        # outStr += str(dc[den[i][j]])
        outStr += str(den[i][j])
      outStr += '\n'
    print outStr