import json,os,random,sys,urllib.request,urllib.error
an=os.environ.get("MAKEFUN_ENV_URL")or sys.exit(1)
B=40000
U=100000
ar=[82,337,365,477,1025,0]
am=[94,281,297,512,936,0]
ao=[0,1,1,2,4,0]
ap=[[0,0,0,0,0,0,0,0,98,134,61,95,68,126,34,-11,-6,7,26,31,65,56,25,-20,-14,13,6,21,23,12,17,-23,-27,-2,-5,12,17,6,10,-25,-26,-4,-4,-10,3,3,33,-12,-35,-1,-20,-23,-15,24,38,-22,0,0,0,0,0,0,0,0],[-167,-89,-34,-49,61,-97,-15,-107,-73,-41,72,36,23,62,7,-17,-47,60,37,65,84,129,73,44,-9,17,19,53,37,69,18,22,-13,4,16,13,28,19,21,-8,-23,-9,12,10,19,17,25,-16,-29,-53,-12,-3,-1,18,-14,-19,-105,-21,-58,-33,-17,-28,-19,-23],[-29,4,-82,-37,-25,-42,7,-8,-26,16,-18,-13,30,59,18,-47,-16,37,43,40,35,50,37,-2,-4,5,19,50,37,37,7,-2,-6,13,13,26,34,12,10,4,0,15,15,15,14,27,18,10,4,15,16,0,7,21,33,1,-33,-3,-14,-21,-13,-12,-39,-21],[32,42,32,51,63,9,31,43,27,32,58,62,80,67,26,44,-5,19,26,36,17,45,61,16,-24,-11,7,26,24,35,-8,-20,-36,-26,-12,-1,9,-7,6,-23,-45,-25,-16,-17,3,0,-5,-33,-44,-16,-20,-9,-1,11,-6,-71,-19,-13,1,17,16,7,-37,-26],[-28,0,29,12,59,44,43,45,-24,-39,-5,1,-16,57,28,54,-13,-17,7,8,29,56,47,57,-27,-27,-16,-16,-1,17,-2,1,-9,-26,-9,-10,-2,-4,3,-3,-14,2,-11,-2,-5,2,14,5,-35,-8,11,2,8,15,-3,1,-1,-18,-9,10,-15,-25,-31,-50],[-65,23,16,-15,-56,-34,2,13,29,-1,-20,-7,-8,-4,-38,-29,-9,24,2,-16,-20,6,22,-22,-17,-20,-12,-27,-30,-25,-14,-36,-49,-1,-27,-39,-46,-44,-33,-51,-14,-14,-22,-46,-44,-30,-15,-27,1,7,-8,-64,-43,-16,9,8,-15,36,12,-54,8,-28,24,14]]
al=[[0,0,0,0,0,0,0,0,178,173,158,134,147,132,165,187,94,100,85,67,56,53,82,84,32,24,13,5,-2,4,17,17,13,9,-3,-7,-7,-8,3,-1,4,7,-6,1,0,-5,-1,-8,13,8,8,10,13,0,2,-7,0,0,0,0,0,0,0,0],[-74,-35,-18,-18,-11,15,4,-17,-12,17,14,17,17,38,23,11,10,17,23,15,20,45,44,13,-8,22,24,27,26,33,26,3,-18,-4,21,24,27,23,9,-11,-19,-3,11,21,23,16,7,-9,-27,-11,4,13,14,4,-5,-17,-53,-34,-21,-11,-28,-14,-24,-43]]
S=[al[0],ap[1],ap[2],ap[3],ap[4],al[1]]
T=[am[0],ar[1],ar[2],ar[3],ar[4],am[5]]
bx=[dm for dm in range(128)if not dm&0x88]
def av(bm,bp):
 return([[bp[dg]+bm[dg][(7-(dm>>4))*8+(dm&7)]for dm in range(128)]for dg in range(6)],[[bp[dg]+bm[dg][(dm>>4)*8+(dm&7)]for dm in range(128)]for dg in range(6)])
au,ak=av(ap,ar)
at,aj=av(S,T)
bv=[33,31,18,14,-14,-18,-31,-33]
bu=[1,-1,16,-16,15,17,-15,-17]
br=[15,17,-15,-17]
bw=[1,-1,16,-16]
bt={6:(7,5,3),2:(0,3,3),118:(119,117,9),114:(112,115,9)}
bs=((0,2),(7,1),(4,3),(112,8),(119,4),(116,12))
def cu(dj):
 return(dj-1)if dj>0 else(5-dj)
class aq:
 def __init__(self,bb):
  self.cz=[0]*128
  self.bl=1
  self.Y=0
  self.cc=-1
  self.cf=[0,0]
  self.ck=0
  self.cj=0
  P=bb.split()
  for dl,bj in enumerate(P[0].split('/')):
   de=0
   for da in bj:
    if da.isdigit():
     de+=int(da)
    else:
     cp=(7-dl)*16+de
     dp='pnbrqk'.index(da.lower())+1
     self.cz[cp]=dp if da.isupper()else-dp
     if dp==6:
      self.cf[0 if da.isupper()else 1]=cp
     if dp==1:
      self.cj+=1
     else:
      self.ck+=ao[dp-1]
     de+=1
  self.bl=1 if P[1]=='w'else-1
  if len(P)>2:
   for da in P[2]:
    self.Y|={'K':1,'Q':2,'k':4,'q':8}.get(da,0)
  if len(P)>3 and P[3]!='-':
   self.cc=(ord(P[3][0])-97)+(int(P[3][1])-1)*16
  bi=random.Random(1)
  self.cv=[[bi.getrandbits(64)for cx in range(128)]for cx in range(12)]
  self.cw=bi.getrandbits(64)
  self.cs=[bi.getrandbits(64)for cx in range(16)]
  self.ct=[bi.getrandbits(64)for cx in range(8)]
  dh=0
  for dm in bx:
   dj=self.cz[dm]
   if dj:
    dh^=self.cv[cu(dj)][dm]
  if self.bl<0:
   dh^=self.cw
  dh^=self.cs[self.Y]
  if self.cc>=0:
   dh^=self.ct[self.cc&7]
  self.key=dh
 def o(self,cp,bz):
  cz=self.cz
  for dn in(cp-15*bz,cp-17*bz):
   if not dn&0x88 and cz[dn]==bz:
    return True
  for db in bv:
   dn=cp+db
   if not dn&0x88 and cz[dn]==2*bz:
    return True
  for db in bu:
   dn=cp+db
   if not dn&0x88 and cz[dn]==6*bz:
    return True
  for db in br:
   dn=cp+db
   while not dn&0x88:
    dj=cz[dn]
    if dj:
     if dj==3*bz or dj==5*bz:
      return True
     break
    dn+=db
  for db in bw:
   dn=cp+db
   while not dn&0x88:
    dj=cz[dn]
    if dj:
     if dj==4*bz or dj==5*bz:
      return True
     break
    dn+=db
  return False
 def bd(self,caps_only=False):
  cz,bl=self.cz,self.bl
  M=[]
  for dm in bx:
   dj=cz[dm]
   if not dj or(dj>0)!=(bl>0):
    continue
   dn=abs(dj)
   if dn==1:
    db=16*bl
    bf=dm+db
    if not caps_only and not cz[bf]:
     dl=bf>>4
     if dl==0 or dl==7:
      for cl in(5,4,3,2):
       M.append(dm|(bf<<7)|(cl<<14))
     else:
      M.append(dm|(bf<<7))
      if(bl>0 and(dm>>4)==1)or(bl<0 and(dm>>4)==6):
       bn=dm+2*db
       if not cz[bn]:
        M.append(dm|(bn<<7)|(1<<17))
    for ca in(db-1,db+1):
     cq=dm+ca
     if cq&0x88:
      continue
     dk=cz[cq]
     if dk and(dk>0)!=(bl>0):
      dl=cq>>4
      if dl==0 or dl==7:
       for cl in(5,4,3,2):
        M.append(dm|(cq<<7)|(cl<<14))
      else:
       M.append(dm|(cq<<7))
     elif cq==self.cc:
      M.append(dm|(cq<<7)|(2<<17))
   elif dn==2 or dn==6:
    for db in(bv if dn==2 else bu):
     cq=dm+db
     if cq&0x88:
      continue
     dk=cz[cq]
     if not dk or(dk>0)!=(bl>0):
      if caps_only and not dk:
       continue
      M.append(dm|(cq<<7))
   else:
    for db in(br if dn==3 else bw if dn==4 else br+bw):
     cq=dm+db
     while not cq&0x88:
      dk=cz[cq]
      if not dk:
       if not caps_only:
        M.append(dm|(cq<<7))
      else:
       if(dk>0)!=(bl>0):
        M.append(dm|(cq<<7))
       break
      cq+=db
  if not caps_only:
   for ax,ce,cg,cm,bk,aw in((1,4,6,7,(5,6),(4,5,6)),(2,4,2,0,(3,2,1),(4,3,2)),(4,116,118,119,(117,118),(116,117,118)),(8,116,114,112,(115,114,113),(116,115,114))):
    if self.Y&ax and all(not cz[dm]for dm in bk)and cz[cm]==(4 if ax<4 else-4)and all(not self.o(cy,-bl)for cy in aw):
     M.append(ce|(cg<<7)|(4<<17))
  return M
 def ac(self,di):
  cz=self.cz
  bc,cq=di&127,(di>>7)&127
  cl,cd=(di>>14)&7,(di>>17)&7
  dj=cz[bc]
  ay,E=0,cq
  if cd==2:
   E=cq-16*self.bl
   ay=cz[E]
   cz[E]=0
  else:
   ay=cz[cq]
  ai=(di,ay,self.Y,self.cc,self.ck,self.cj,self.key)
  dh=self.key^self.cv[cu(dj)][bc]^self.cw^self.cs[self.Y]
  if self.cc>=0:
   dh^=self.ct[self.cc&7]
  if ay:
   dh^=self.cv[cu(ay)][E]
  be=cl if cl else abs(dj)
  dh^=self.cv[(be-1)if self.bl>0 else(5+be)][cq]
  cz[cq]=cl*self.bl if cl else dj
  cz[bc]=0
  if abs(dj)==6:
   self.cf[0 if self.bl>0 else 1]=cq
  if cd==4:
   cm,cn,bq=bt[cq]
   cz[cn]=cz[cm];cz[cm]=0
   dh^=self.cv[bq][cm]^self.cv[bq][cn]
  if ay:
   self.ck-=ao[abs(ay)-1]
   if abs(ay)==1:
    self.cj-=1
  if cl:
   self.ck+=ao[cl-1]
   self.cj-=1
  Z=15
  for cp,ax in bs:
   if bc==cp or cq==cp:
    Z&=~ax
  self.Y&=Z
  self.cc=(bc+cq)//2 if cd==1 else-1
  dh^=self.cs[self.Y]
  if self.cc>=0:
   dh^=self.ct[self.cc&7]
  self.bl=-self.bl
  self.key=dh
  return ai
 def H(self,ai):
  di,ay,Y,cc,ck,cj,key=ai
  cz=self.cz
  bc,cq=di&127,(di>>7)&127
  cl,cd=(di>>14)&7,(di>>17)&7
  self.bl=-self.bl
  dj=cz[cq]
  cz[bc]=(1 if cl else abs(dj))*self.bl
  if cd==2:
   cz[cq-16*self.bl]=ay
   cz[cq]=0
  else:
   cz[cq]=ay
  if abs(dj)==6:
   self.cf[0 if self.bl>0 else 1]=bc
  if cd==4:
   cm,cn,cx=bt[cq]
   cz[cm]=cz[cn];cz[cn]=0
  self.Y,self.cc,self.ck,self.cj,self.key=Y,cc,ck,cj,key
 def x(self):
  ch=cb=0
  cz=self.cz
  for dm in bx:
   dj=cz[dm]
   if dj:
    dn=abs(dj)-1
    if dj>0:
     ch+=au[dn][dm];cb+=at[dn][dm]
    else:
     ch-=ak[dn][dm];cb-=aj[dn][dm]
  ck=min(self.ck,24)
  co=(ch*ck+cb*(24-ck))//24
  return co*self.bl
 def bo(self,di):
  bc,cq=di&127,(di>>7)&127
  dm="abcdefgh"[bc&7]+str((bc>>4)+1)+"abcdefgh"[cq&7]+str((cq>>4)+1)
  cl=(di>>14)&7
  return dm+("pnbrqk"[cl-1]if cl else"")
def n(do):
 bc=(ord(do[0])-97)+(int(do[1])-1)*16
 cq=(ord(do[2])-97)+(int(do[3])-1)*16
 cl={"q":5,"r":4,"b":3,"n":2}.get(do[4:5],0)
 return bc,cq,cl
class C:
 def __init__(self,bh):
  self.bh=bh
  self.cr={}
  self.N=0
  self.I=False
  self.ae=[]
 def O(self,M,A,bg):
  cz=self.bh.cz
  def co(di):
   if di==A:
    return 1<<24
   cq=(di>>7)&127
   dk=cz[cq]
   dp=0
   if dk:
    dp=10*ar[abs(dk)-1]-ar[abs(cz[di&127])-1]+10000
   elif(di>>17)&7==2:
    dp=10738
   if(di>>14)&7:
    dp+=9000
   return dp
  M.sort(key=co,reverse=True)
  return M
 def z(self,J,W,bg):
  self.N+=1
  if self.N>B:
   self.I=True
   return 0
  bh=self.bh
  if bh.ck<=1 and bh.cj==0:
   return 0
  y=bh.o(bh.cf[0 if bh.bl>0 else 1],-bh.bl)
  if not y:
   Q=bh.x()
   if Q>=W:
    return W
   if Q>J:
    J=Q
  M=bh.bd(caps_only=not y)
  self.O(M,0,bg)
  L=0
  for di in M:
   do=bh.ac(di)
   if bh.o(bh.cf[0 if-bh.bl>0 else 1],bh.bl):
    bh.H(do)
    continue
   L+=1
   co=-self.z(-W,-J,bg+1)
   bh.H(do)
   if self.I:
    return 0
   if co>=W:
    return W
   if co>J:
    J=co
  if y and L==0:
   return-U+bg
  return J
 def G(self,K,J,W,bg):
  self.N+=1
  if self.N>B:
   self.I=True
   return 0
  bh=self.bh
  if bh.ck<=1 and bh.cj==0:
   return 0
  if self.ae.count(bh.key)>=2:
   return 0
  ad=J
  ba=self.cr.get(bh.key)
  A=0
  if ba and ba[0]>=K:
   cx,cd,co,ci=ba
   co+=-bg if co>U-1000 else bg if co<-U+1000 else 0
   if cd==0:
    return co
   if cd==1 and co>=W:
    return co
   if cd==2 and co<=J:
    return co
   A=ci
  if K<=0:
   return self.z(J,W,bg)
  y=bh.o(bh.cf[0 if bh.bl>0 else 1],-bh.bl)
  M=bh.bd()
  self.O(M,A,bg)
  V=-U
  D=0
  L=0
  self.ae.append(bh.key)
  try:
   for di in M:
    do=bh.ac(di)
    if bh.o(bh.cf[0 if-bh.bl>0 else 1],bh.bl):
     bh.H(do)
     continue
    L+=1
    co=-self.G(K-1,-W,-J,bg+1)
    bh.H(do)
    if self.I:
     return 0
    if co>V:
     V=co
     D=di
    if co>J:
     J=co
     if J>=W:
      break
   if L==0:
    return-U+bg if y else 0
   if V<=ad:
    cd=2
   elif V>=W:
    cd=1
   else:
    cd=0
   R=V+(-bg if V>U-1000 else bg if V<-U+1000 else 0)
   if len(self.cr)>300000:
    self.cr.clear()
   self.cr[bh.key]=(K,cd,R,D)
   return V
  finally:
   self.ae.pop()
 def ag(self,l):
  bh=self.bh
  M=bh.bd()
  L=[]
  for di in M:
   do=bh.ac(di)
   if bh.o(bh.cf[0 if-bh.bl>0 else 1],bh.bl):
    bh.H(do)
    continue
   bh.H(do)
   L.append(di)
  if not L:
   return l[0]if l else None
  D=L[0]
  for K in range(1,64):
   self.N=0
   self.I=False
   J,W=-U,U
   w,F=D,-U
   for di in L:
    do=bh.ac(di)
    co=-self.G(K-1,-W,-J,1)
    bh.H(do)
    if self.I:
     break
    if co>F:
     F,w=co,di
    if co>J:
     J=co
   if self.I:
    break
   D=w
  do=bh.bo(D)
  return do if do in l else l[0]
def af(ae,X):
 try:
  with urllib.request.urlopen(an+ae,json.dumps(X).encode())as dl:
   return json.load(dl)
 except urllib.error.HTTPError as dc:
  sys.exit(f"{ae}: HTTP {dc.code}")
j="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
def h(M):
 dj=aq(j)
 aa=[dj.key]
 for do in M:
  bc,cq,cl=n(do)
  for di in dj.bd():
   if(di&127)==bc and((di>>7)&127)==cq and((di>>14)&7)==cl:
    dj.ac(di)
    aa.append(dj.key)
    break
 return aa
def ah(dc,df):
 dc.bh=aq(df["fen"])
 dc.ae=h(df.get("moves",[]))[:-1]
def ab():
 while True:
  df=af("/game",{})
  if df["status"]=="done":
   break
  az=C(aq(df["fen"]))
  ah(az,df)
  while df["status"]=="your_move":
   ci=az.ag(df["legal_moves"])
   df=af("/move",{"game":df["game"],"move":ci})
   if df["status"]=="your_move":
    ah(az,df)
ab()
