# encoding: utf-8
# __author__: mgcheng date:2017-9-1

#   美   德   英   法   俄   意
#A                            1
#B                       1
#C             1
#D        1
#E                  1
#F   1

def times(n):
    i = 0
    while(n>>(i+1)):
        i += 1
    return i

A = (1, 8)
B = (2,)
C = (8,)
D = (1,)
E = (1, 4, 8, 0x10, 0x20)
F = (1, 2, 4, 8, 0x20)

L = ['意大利', '俄国', '法国', '英国', '德国', '美国']

for a in A:
    for b in B:
        for c in C:
            for d in D:
                for e in E:
                    for f in F:
                        if (a+b+c+d+e+f==0x3f) :
                            print "*************************{"
                            print "A =", a, L[times(a)]
                            print "B =", b, L[times(b)]
                            print "C =", c, L[times(c)]
                            print "D =", d, L[times(d)]
                            print "E =", e, L[times(e)]
                            print "F =", f, L[times(f)]
                            print "}*************************"