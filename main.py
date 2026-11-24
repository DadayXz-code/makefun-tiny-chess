import json as j,os,urllib.request as u
V=[0,100,320,330,500,900,0]
KN=(14,18,31,33,-14,-18,-31,-33)
DG=(15,17,-15,-17);OR=(1,16,-1,-16);KI=DG+OR
DR=[0,0,KN,DG,OR,DG+OR,KI]
W=(0,0,6,5,2,3,0)
RB={0:2,7:1,112:8,119:4}
SQ=[r*16+f for r in range(8) for f in range(8)]
BUD=100000
B=[0]*128;S=1;C=0;E=-1;K=[116,4];N=0
def ok(x):return not x&0x88
def so(m):m.sort(key=mv,reverse=1)
def at(s,by):
 if any(ok(x:=s-d*by) and B[x]==by for d in(15,17)):return 1
 if any(ok(x:=s+d) and B[x]==by*(2 if d in KN else 6) for d in KN+KI):return 1
 for d in DG+OR:
  x=s+d
  while ok(x) and not B[x]:x+=d
  if ok(x) and(B[x]==by*5 or B[x]==by*(3 if d in DG else 4)):return 1
 return 0
def gn(cp=0):
 ms=[]
 def ap(s,x):ms.extend(s|x<<7|q<<14 for q in((5,4,3,2) if x>>4==(7 if S>0 else 0) else(0,)))
 for s in SQ:
  p=B[s]
  if not p or p*S<=0:continue
  a=p if p>0 else -p
  if a==1:
   for dd in(16,15,17):
    x=s+dd*S
    if ok(x) and(dd==16 and not cp and not B[x] or dd!=16 and(B[x]*S<0 or x==E)):ap(s,x)
    if dd==16 and ok(x) and not cp and not B[x] and s>>4==(1 if S>0 else 6) and not B[s+32*S]:ms.append(s|s+32*S<<7)
  else:
   for d in DR[a]:
    x=s+d
    while ok(x):
     if B[x]*S>0:break
     if not cp or B[x]:ms.append(s|x<<7)
     if B[x] or a==2 or a==6:break
     x+=d
   if a==6 and not cp and not at(s,-S):
    for k in(1,-1):
     bt=1<<(2 if S<0 else 0)+(1 if k<0 else 0);a1=s+k;b1=s+2*k
     if C&bt and not(B[a1] or B[b1]) and B[s+3*k]in(0,4*S) and not(at(a1,-S) or at(b1,-S)):ms.append(s|s+2*k<<7)
 return ms
def mk(m):
 global S,C,E
 f=m&127;t=m>>7&127;pr=m>>14&7;p=B[f]
 u=(B[:],S,C,E,K[:]);B[f]=0
 if p==S and t==E and not B[t]:B[t-16*S]=0
 B[t]=pr*S if pr else p
 if abs(p)==6:K[S>0]=t
 if abs(p)==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1) if t>f else(f-4,f-1);B[rt]=B[rf];B[rf]=0
 if p==6*S:C&=(12,3)[S<0]
 for q2 in(f,t):C&=~RB.get(q2,0)
 E=t-16*S if p==S and abs(t-f)==32 else-1;S=-S
 if at(K[S<0],S):unm(u);return None
 return u
def unm(u):
 global S,C,E
 B[:]=u[0];S,C,E=u[1],u[2],u[3];K[:]=u[4]
def ev():
 s=0
 for q in SQ:
  p=B[q]
  if p:
   a=abs(p);w=p//a;f=q&7;r=q>>4
   s+=w*(V[a]+(7*(r if w>0 else 7-r) if a==1 else(6-abs(2*f-7)-abs(2*r-7))*W[a]))
 return s*S
def mv(m):
 f=m&127;t=m>>7&127
 return V[abs(B[t] or(1 if t==E else 0))]*16-V[abs(B[f])]+V[m>>14&7]
class AB(Exception):pass
def qs(a,b,qd):
 global N;N+=1
 if N>BUD:raise AB
 st=ev()
 if st>=b:return b
 if st>a:a=st
 if qd<=0:return a
 ms=gn(1);so(ms)
 for m in ms:
  if(w:=mk(m)):
   s=-qs(-b,-a,qd-1);unm(w)
   if s>=b:return b
   if s>a:a=s
 return a
def sr(a,b,d):
 global N;N+=1
 if N>BUD:raise AB
 if d<=0:return qs(a,b,16)
 ms=gn();so(ms)
 bst=-10**6
 for m in ms:
  if(w:=mk(m)):
   s=-sr(-b,-a,d-1);unm(w)
   if s>bst:bst=s
   if s>a:a=s
   if a>=b:break
 if bst<-99999:return 0 if not at(K[S>0],-S) else -99990-d
 return bst
def th():
 global N
 ms=[m for m in gn() if(w:=mk(m)) and not unm(w)]
 so(ms);bm=ms[0];N=0
 for d in range(1,40):
  try:
   a=-10**6;bb=bm
   for m in ms:
    if(w:=mk(m)):
     s=-sr(-10**6,-a,d-1);unm(w)
     if s>a:a=s;bb=m
   bm=bb
  except AB:break
 return bm
def sf(f):
 global S,C,E
 w=f.split();B[:]=[0]*128;i=112
 for ch in w[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  else:
   p="PNBRQKpnbrqk".find(ch);p=(p%6+1)*(1 if p<6 else -1)
   B[i]=p
   if abs(p)==6:K[p>0]=i
   i+=1
 S=1 if w[1]=="w" else-1;C=0
 for ch in w[2]:C|={"K":1,"Q":2,"k":4,"q":8}.get(ch,0)
 E=-1 if w[3]=="-" else ord(w[3][0])-97+(int(w[3][1])-1)*16
def uc(m):
 f=m&127;t=m>>7&127
 return chr(97+(f&7))+str(1+(f>>4))+chr(97+(t&7))+str(1+(t>>4))+("nbrq"[(m>>14&7)-2]if m>>14 else"")
def po(p,b):
 try:
  with u.urlopen(os.environ["MAKEFUN_ENV_URL"]+p,data=j.dumps(b).encode()) as r:return j.load(r)
 except:return{}
def main():
 while 1:
  g=po("/game",{})
  if g.get("status") not in("your_move","over"):break
  while g.get("status")=="your_move":
   mv=None
   try:sf(g["fen"]);m=th();mv=uc(m) if m else None
   except:mv=None
   if mv not in g["legal_moves"]:mv=g["legal_moves"][0]
   g=po("/move",{"game":g["game"],"move":mv})
if __name__=="__main__":main()
