import json,os
from urllib.request import urlopen as U
ENV=os.environ.get("MAKEFUN_ENV_URL") or exit(1)
MATE=99999
VAL=dict(zip('PNBRQKpnbrqk',[100,320,330,500,900,0]*2))
P="aaaakkkkccegbbcfaaaeb98abcc6aaaa"
N="024426aa4acd4bde4ade4bcd26ab0244"
def mk(s):
 v=[int(c,36)*5-50 for c in s]
 r=[]
 for i in range(0,32,4):r+=v[i:i+4]+v[i:i+4][::-1]
 return ([r[(7-i//8)*8+i%8] for i in range(64)],r)
W=[mk(s) for s in (P,N,N,N,N,N)]
KN=[-21,-19,-12,-8,8,12,19,21]
KI=[-11,-10,-9,-1,1,9,10,11]
BI=[-11,-9,9,11]
RI=[-10,-1,1,10]
CB=((25,12),(28,4),(21,8),(95,3),(98,1),(91,2))
CT=[0];BM=[None,-MATE]
class Pos:
 def __init__(s,b,stm,cast,ep,kg):
  s.b=b;s.stm=stm;s.cast=cast;s.ep=ep;s.kg=kg
 def atk(s,q,by):
  b=s.b
  C='PNBRQK' if by>0 else 'pnbrqk'
  d=-10*by
  if b[q-d-1]==C[0] or b[q-d+1]==C[0]:return 1
  for D,v in ((KN,1),(KI,5)):
   for x in D:
    if b[q+x]==C[v]:return 1
  for x in BI+RI:
   y=q+x
   while b[y]!=' ':
    c=b[y]
    if c!='.':
     if c==C[4] or c==C[2+(abs(x) in (1,10))]:return 1
     break
    y+=x
 def gen(s,cp=0):
  b,stm=s.b,s.stm
  m=[];A=m.append
  def ap(f,t):
   for pr in (('QRBN' if stm>0 else 'qrbn') if (t//10) in (2,9) else ('',)):A((f,t,pr,0))
  for q in range(21,99):
   c=b[q]
   if c==' ' or c=='.':continue
   if (c.isupper())!=(stm>0):continue
   u=c.upper()
   if u=='P':
    d=-10*stm;o=q+d
    if not cp and b[o]=='.':
     ap(q,o)
     if (q//10)==(8 if stm>0 else 3) and b[q+2*d]=='.':A((q,q+2*d,'',1))
    for y in (o-1,o+1):
     v=b[y]
     if v!=' ' and v!='.' and (v.isupper())!=(stm>0):ap(q,y)
     elif y==s.ep:A((q,y,'',2))
   else:
    for x in (KN,KI,BI,RI,BI+RI)['NKBRQ'.index(u)]:
     y=q+x
     while b[y]!=' ':
      v=b[y]
      if v!='.':
       if (v.isupper())!=(stm>0):A((q,y,'',0))
       break
      if not cp:A((q,y,'',0))
      if u in 'NK':break
      y+=x
  if not cp:
   for kf,kt,bit in ((25,27,4),(25,23,8),(95,97,1),(95,93,2)):
    if s.cast&bit:
     d=(kt-kf)//2
     if all(b[kf+d*i]=='.' for i in (1,2,3) if i<3 or d<0) and all(not s.atk(kf+d*i,-stm) for i in range(3)):A((kf,kt,'',3))
  return m
 def make(s,m):
  f,t,pr,fl=m
  b=s.b[:]
  p=b[f]
  kg=s.kg[:]
  if fl==2:b[t+10*s.stm]='.'
  b[t]=pr if pr else p
  b[f]='.'
  if p in 'Kk':kg[p=='k']=t
  if fl==3:
   rf,rt=(t+1,t-1) if t%10==7 else (t-2,t+1)
   b[rt]=b[rf];b[rf]='.'
  k=15
  for q,bit in CB:
   if f==q or t==q:k&=~bit
  return Pos(b,-s.stm,s.cast&k,(f+t)//2 if fl==1 else -1,kg)
 def ev(s):
  b=s.b
  v=0
  for i in range(64):
   q=91-(i//8)*10+i%8
   c=b[q]
   if c=='.':continue
   t='PNBRQK'.index(c.upper())
   w=W[t][c.islower()]
   v+=(VAL[c]+w[i])*(c.isupper()*2-1)
  return v*s.stm
 def uci(s,m):
  return chr(96+m[0]%10)+str(10-m[0]//10)+chr(96+m[1]%10)+str(10-m[1]//10)+m[2].lower()
def parse(f):
 b=list(' '*20+(' '+'.'*8+' ')*8+' '*20)
 p=f.split()
 i=0
 kg=[0,0]
 for c in p[0]:
  if c.isdigit():i+=int(c)
  elif c!='/':
   q=21+(i//8)*10+i%8
   b[q]=c
   if c in 'Kk':kg[c=='k']=q
   i+=1
 cast=sum(1<<'KQkq'.index(c) for c in p[2] if c!='-')
 ep=-1
 if p[3]!='-':ep=(10-int(p[3][1]))*10+ord(p[3][0])-96
 return Pos(b,1 if p[1]=='w' else -1,cast,ep,kg)
def search(p,d,a,be,rt=0):
 CT[0]+=1
 if CT[0]>40000:raise StopIteration
 c=p.atk(p.kg[p.stm<0],-p.stm)
 if d<=0 and not c:
  v=p.ev()
  if v>=be:return be
  a=max(a,v)
 mv=p.gen(d<=0 and not c)
 b=p.b
 mv.sort(key=lambda m:-VAL.get(b[m[1]],0))
 n=0
 for m in mv:
  p2=p.make(m)
  if p2.atk(p2.kg[p2.stm>0],p2.stm):continue
  n+=1
  sc=-search(p2,d-1,-be,-a)
  if rt and sc>BM[1]:BM[1],BM[0]=sc,m
  if sc>a:
   a=sc
   if a>=be:break
 if n==0:return -MATE if c else (a if d<=0 else 0)
 return a
def root(p,lu):
 best=None
 try:
  for d in range(1,64):
   CT[0]=0;BM[0]=best;BM[1]=-MATE
   search(p,d,-MATE,MATE,1)
   best=BM[0]
 except StopIteration:pass
 return p.uci(best) if best else lu[0]
def main():
 g=json.load(U(ENV+"/game",b'{}'))
 while g["status"]!="done":
  if g["status"]=="your_move":
   g=json.load(U(ENV+"/move",json.dumps({"game":g["game"],"move":root(parse(g["fen"]),g["legal_moves"])}).encode()))
  else:
   g=json.load(U(ENV+"/game",b'{}'))
main()
