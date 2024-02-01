import math as m
import time as t
from os import get_terminal_size as e
g,j,k,f=(m.sin,m.radians,m.cos,round)
d,c=(lambda i,s:(f(w/2+g(j(i))*g(s*m.pi)*20*2),f(h/2+k(j(i))*20))
     ,lambda s,c:[print(f"\033[{d(i,r)[1]};{d(i,r)[0]}H{c}",end="",flush=1)for i in
range(360)])
r=a=t.time()
while 1:
    w,h,s=(e()[0],e()[1],((t.time()-a)%5)/5)
    ([(c(r,i),r:=s)for i in".#"],t.sleep(0.07))