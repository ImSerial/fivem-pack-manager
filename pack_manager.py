BX='X-Token'
BW='gofile'
BV='Accept'
BU='Content-Range'
BT='.version'
BS='GTA5.exe'
BR='CitizenFX.ini'
BQ='FiveM.app'
BP='image/jpeg'
BO='Modium'
BN=reversed
BM=ImportError
As='background'
Ar='Content-Type'
Aq='http'
Ap='gdrive_folder'
Ao='file'
An='Content-Length'
Am='status'
Al='_dirs'
Ak='x64'
Aj='.ini'
Ai='replace'
Ah='FiveM'
Ag='packs'
Af='LOCALAPPDATA'
AM='size'
AL='application/json'
AK='le téléchargement'
AJ='purged'
AI='.rpf'
AH='.asi'
AG='plugins'
AF='citizen'
AE='.png'
AD=enumerate
AC=sorted
AB=getattr
A5='custom'
A4='backups'
A3='update'
A2='mods'
A1=next
x='https://'
w='http://'
v='packs_key'
u=list
t=bool
p='files'
m='{a}'
l='url'
k='User-Agent'
j='.'
i='packs_url'
h=str
g=dict
c=isinstance
b='version'
a='preview'
Z=open
X='/'
W='loaded'
V=int
U='utf-8'
S='image'
R='gta'
Q=ValueError
P=RuntimeError
O='name'
N='ok'
M='fivem'
L=OSError
H=False
G=Exception
F='err'
E=len
D=None
C=''
B=True
import base64 as At,json as K,os as A,re as I,secrets as Au,shutil as J,struct as A6,subprocess as AN,sys as q,tempfile as BY,threading as d,time,urllib.error,urllib.parse,urllib.request,zipfile as Av
from http.server import BaseHTTPRequestHandler as BZ,ThreadingHTTPServer as Ba
import webview as Aw
Bb=BO
A7='3.0.0'
r=f"Modium/{A7}"
Ax='ImSerial/modium'
Bc='FiveMPackManager'
def Bd():
	if not AB(q,'frozen',H):return A.path.dirname(A.path.abspath(__file__))
	E=A.environ.get(Af)or A.path.dirname(q.executable);C=A.path.join(E,BO);D=A.path.join(E,Bc)
	if A.path.isdir(D)and not A.path.isdir(C):
		try:A.rename(D,C)
		except L:return D
	A.makedirs(C,exist_ok=B);return C
e=Bd()
T=A.path.join(e,Ag)
Ay=A.path.join(e,'_backups')
AO=A.path.join(e,'state.json')
AP=A.path.join(e,'config.json')
Be={i:'https://uxqt.site/packs-096759e8/packs.json',v:'glt7ExuP7EBzBc56fUzoAmHy618FWBhT'}
def Bf():
	B=g(Be);C=[A.path.dirname(A.path.abspath(__file__))]
	if AB(q,'_MEIPASS',D):C.insert(0,q._MEIPASS)
	for F in C:
		E=A.path.join(F,'embedded_config.json')
		if A.path.exists(E):
			try:
				with Z(E,'r',encoding=U)as G:B.update(K.load(G))
				break
			except(L,K.JSONDecodeError):pass
	return B
Bg=Bf()
AQ=AE,'.jpg','.jpeg','.webp','.gif'
Az={AE:'image/png','.jpg':BP,'.jpeg':BP,'.webp':'image/webp','.gif':'image/gif'}
def A_(path,data):
	C=path+'.tmp'
	with Z(C,'w',encoding=U)as B:K.dump(data,B,indent=2,ensure_ascii=H);B.flush();A.fsync(B.fileno())
	A.replace(C,path)
def A8():
	B=g(Bg)
	if A.path.exists(AP):
		try:
			with Z(AP,'r',encoding=U)as C:B.update(K.load(C))
		except(L,K.JSONDecodeError):pass
	return B
def f(**B):A=A8();A.update(B);A_(AP,A)
def Bh():
	F='fivem_path';D=[];E=A8()
	if E.get(F):D.append(E[F])
	G=A.environ.get(Af,C);D.append(A.path.join(G,Ah,BQ))
	for B in D:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,BR))or A.path.isdir(A.path.join(B,AF))):return B
def Bi(fivem=D):
	I=fivem;N=A8();E=[N.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(Af,C),Ah,BQ))
	for K in J:
		G=A.path.join(K,BR)if K else D
		if G and A.path.exists(G):
			try:
				with Z(G,'r',encoding=U,errors=Ai)as O:
					for M in O:
						if M.strip().lower().startswith('ivpath='):E.append(M.split('=',1)[1].strip())
			except L:pass
	try:
		import winreg as H
		for P in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,P)as Q:E.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except L:pass
	except BM:pass
	for B in('C:','D:','E:','F:'):E+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in E:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,BS)):return F
def B0():
	if A.path.exists(AO):
		try:
			with Z(AO,'r',encoding=U)as B:return K.load(B)
		except(L,K.JSONDecodeError):pass
	return{W:{}}
def B1(state):A_(AO,state)
def AR():A.makedirs(T,exist_ok=B);return AC(B for B in A.listdir(T)if A.path.isdir(A.path.join(T,B))and not B.startswith(j))
def CM(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(j)or G and A.path.splitext(E)[0]==a:continue
			yield A.path.relpath(A.path.join(C,D),B)
def Bj(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(T,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except L:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
B2={}
def Bk(pack_name):
	G=A.path.join(T,pack_name)
	for E in AQ:
		B=A.path.join(G,a+E)
		try:C=A.stat(B)
		except L:continue
		D=B2.get(B)
		if D and D[0]==C.st_mtime and D[1]==C.st_size:return D[2]
		try:
			with Z(B,'rb')as H:I=At.b64encode(H.read()).decode('ascii')
		except L:return
		F=f"data:{Az[E]};base64,{I}";B2[B]=C.st_mtime,C.st_size,F;return F
def B3(name):
	B=A.path.join(T,name,BT)
	if A.path.exists(B):
		try:
			with Z(B,'r',encoding=U)as C:return C.read().strip()
		except L:pass
def Y(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise Q(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
Bl=I.compile('[<>:"/\\\\|?*\\x00-\\x1f]')
def A9(name):
	D=name;B=(D or C).strip().strip('. ')
	if not B or Bl.search(B)or B in(j,'..')or A.path.isabs(D or C):raise Q(f"Nom de pack invalide : {D!r}")
	return B
def B4(path):
	try:return t(A.lstat(path).st_file_attributes&1024)
	except(L,AttributeError):return A.path.islink(path)
def AS():
	try:
		D=AN.run(['tasklist','/FO','CSV'],capture_output=B,text=B,creationflags=BI,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			C=A.split('","',1)[0].strip('"')
			if C.startswith(('modium','fivempackmanager')):continue
			if C.startswith((M,'gta5')):return B
		return H
	except G:return H
def y(path,need_bytes,what):
	B=need_bytes;C=J.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise P(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def CN(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except L:pass
	return B
AT={AF,A2,AG}
B5={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto 5','grand theft auto v legacy','gta v legacy','gtav legacy','gta 5 legacy','gta5 legacy','singleplayer','single player',R}
AU={'enbseries','enbcache'}
Bm=I.compile('^(enb[\\w .()-]*\\.(ini|dll|asi|fx|fxh|dds|bmp|cfg)|d3d(9|10|11|12)\\.dll|d3dcompiler[\\w.]*\\.dll|dxgi\\.dll)$',I.I)
Bn={'.dll',AH,Aj,'.fx','.fxh','.cfg','.json','.yml','.xml'}
def Bo(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=A2]
		for D in G:
			if D.lower().endswith(AI):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def Bp(src,pack_path,rpf_index,log):
	B=A.path.basename(src);C=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in C]
	for(F,G)in AD(H[:-1]):
		if G in(A3,Ak):return A.path.join(*C[F:])
		if G=='dlcpacks':return A.path.join(A3,Ak,*C[F:])
	D=rpf_index.get(B.lower(),[])
	if E(D)==1:return D[0]
	if E(D)>1:log(f"{B} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return B
def AV(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(j):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
AW={M,'five m','five-m','fivem.app','fivem app','fivem files','five m files','fivem folder'}
AX={'reshade-shaders','reshade-presets'}
def Bq(pack_path,log,gta_base=D):
	D=pack_path;I=log;B=[];T=Bo(gta_base);F={}
	def G(key,n=1):F[key]=F.get(key,0)+n
	def O(src):B.append((src,M,A.path.join(A2,Bp(src,D,T,I))));G('rpf vers mods')
	def P(gta_dir,label,prefix=C):
		F=prefix;E=gta_dir
		for(I,K,J)in A.walk(E):
			for C in J:
				if C.startswith(j):continue
				D=A.path.join(I,C)
				if C.lower().endswith(AI):O(D)
				else:H=A.path.relpath(D,E);B.append((D,R,A.path.join(F,H)if F else H));G(f"{label} vers GTA V")
	def Q(dirpath,in_fivem=H,depth=0):
		V='asi vers plugins';S=depth;J=in_fivem;H=dirpath
		if S>12:I(f"Profondeur maximale atteinte, dossier ignoré : {H}");return
		K=AC(A.listdir(H));T={B.lower()for B in K if A.path.isdir(A.path.join(H,B))};U=A.path.basename(H).lower();J=J or U in AW;W=U in AW or t(T&(AT|AX));X=not J and(t(T&AU)or any(A.lower().startswith('enb')and A.lower().endswith(Aj)for A in K));Y={A.path.splitext(B)[0].lower()for B in K if B.lower().endswith(AH)}
		for F in K:
			C=A.path.join(H,F);D=F.lower()
			if B4(C):I(f"Lien/jonction ignoré dans le pack : {F}");continue
			if A.path.isdir(C):
				if D in AT or D in AX:N=E(B);AV(B,C,M,D);G(f"{D} vers FiveM",E(B)-N)
				elif D in B5:P(C,B6(F))
				elif D in AU:
					if J:N=E(B);AV(B,C,M,D);G(f"{D} vers FiveM",E(B)-N)
					else:P(C,B6(F),prefix=D)
				else:Q(C,J,S+1)
			elif not D.startswith(j):
				L=A.path.splitext(D)[1]
				if L==AI:O(C)
				elif X and Bm.match(F):B.append((C,R,F));G('ENB vers GTA V')
				elif L==AH:B.append((C,M,A.path.join(AG,F)));G(V)
				elif L==Aj and A.path.splitext(D)[0]in Y:B.append((C,M,A.path.join(AG,F)));G(V)
				elif W and L in Bn:B.append((C,M,F));G('racine FiveM')
	Q(D)
	if not B:I("Structure standard non détectée — copie de l'archive telle quelle.");AV(B,D,M,C)
	B=[(E,D,B)for(E,D,B)in B if not(D==M and A.path.dirname(B)==C and A.path.splitext(B)[0].lower()==a)];J,K=set(),[]
	for(U,L,N)in B:
		S=L,N.lower()
		if S not in J:J.add(S);K.append((U,L,N))
	V=', '.join(f"{A} : {B}"for(A,B)in F.items())or'rien à installer';I(f"Structure détectée — {V}.");return K
def B6(name):A=name;return A if E(A)<=20 else A[:17]+'...'
def z(e):return(M,e)if c(e,h)else(e[0],e[1])
def AY(target,rel):return f"{target}|{rel}"
def Br(bases,backup_root,manifest,log):
	M=bases;K=manifest;I=backup_root
	for O in BN(K[p]):
		D,L=z(O);E=M.get(D)
		if not E:continue
		try:
			C=Y(E,L)
			if A.path.exists(C):A.remove(C)
			if K[A4].get(AY(D,L)):
				H=A.path.join(I,D,L)
				if A.path.exists(H):J.move(H,C)
		except G:pass
	for(D,N)in BN(K.get(AJ,[])):
		E=M.get(D)
		if not E:continue
		try:
			C=Y(E,N);H=A.path.join(I,Al,D,N)
			if A.path.exists(H):
				if A.path.isdir(C):J.rmtree(C,ignore_errors=B)
				J.move(H,C)
		except G:pass
	J.rmtree(I,ignore_errors=B);log("Installation annulée — jeu restauré dans son état d'origine.",F)
n={M:Ah,R:'GTA V'}
Bs={M:{AF},R:{A3,Ak,'redistributables','installers','dlc','_commonredist',A2}}
def B7(plan):
	C={}
	for(G,D,F)in plan:
		B=F.replace(X,A.sep).split(A.sep)
		if E(B)>1:C.setdefault((D,B[0].lower()),B[0])
	return C
def Bt(pack_name,bases,state,log,progress):
	e=state;X=pack_name;S=bases;K=log
	if X in e[W]:raise Q('Ce pack est déjà chargé.')
	if AS():raise P('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	v=Y(T,A9(X));I=Bq(v,K,S.get(R))
	if not I:raise Q('Pack vide — aucun fichier à installer.')
	q=[1 for(B,A,C)in I if A==R and not S.get(R)]
	if q:K(f"Dossier GTA V introuvable — {E(q)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);I=[(B,A,C)for(B,A,C)in I if not(A==R and not S.get(R))]
	if not I:raise Q('Rien à installer (dossier GTA V non configuré).')
	i={}
	for(w,Z,A7)in I:
		try:i[Z]=i.get(Z,0)+A.path.getsize(w)
		except L:pass
	for(Z,x)in i.items():
		if S.get(Z):y(S[Z],x,f"l'installation ({n[Z]})")
	a={p:[],A4:{},AJ:[]};b={}
	for(c,A0)in e[W].items():
		if c!=X:
			for r in A0[p]:b[z(r)[0]+'|'+z(r)[1].lower()]=c
	K(f"Installation de « {X} » — {E(I)} fichiers...");j=A.path.join(Ay,X);k=0;s=E(I)<=60;A2=max(1,E(I)//10)
	try:
		for((H,f),U)in B7(I).items():
			O=S.get(H)
			if H!=M or not O or not A.path.isdir(O):continue
			g=A1((A for A in A.listdir(O)if A.lower()==f),D)
			if g and g!=U:
				try:A.rename(A.path.join(O,g),A.path.join(O,U));K(f"Dossier {g} renommé en {U}.")
				except L:pass
		for((H,f),U)in B7(I).items():
			O=S.get(H)
			if not O or f in Bs.get(H,set()):continue
			t=Y(O,U)
			if not A.path.isdir(t):continue
			A3=f"{H}|{f}{A.sep}";c=A1((B for(A,B)in b.items()if A.startswith(A3)),D)
			if c:K(f"Dossier {U} : contient des fichiers du pack « {c} » — fusion au lieu du remplacement.");continue
			d=A.path.join(j,Al,H,U);A.makedirs(A.path.dirname(d),exist_ok=B);J.move(t,d);a[AJ].append([H,U]);K(f"Dossier existant mis de côté ({n[H]}) : {U} — remplacé proprement. Ton contenu précédent est sauvegardé et sera remis au déchargement du pack.")
		for(l,(A5,H,V))in AD(I):
			O=S[H];h=Y(O,V);m=H+'|'+V.lower()
			if m in b:K(f"Attention : {V} appartient déjà au pack « {b[m]} » — écrasé.")
			A.makedirs(A.path.dirname(h),exist_ok=B)
			if A.path.exists(h)and m not in b:
				d=A.path.join(j,H,V);A.makedirs(A.path.dirname(d),exist_ok=B);J.copy2(h,d);a[A4][AY(H,V)]=B;k+=1
				if s:K(f"Sauvegarde de l'original ({n[H]}) : {V}")
			J.copy2(A5,h);a[p].append([H,V])
			if s:K(f"Copie ({n[H]}) : {V}")
			elif(l+1)%A2==0:K(f"{l+1}/{E(I)} fichiers copiés ({k} originaux sauvegardés)...")
			progress(l+1,E(I))
	except G as o:K(f"Erreur pendant l'installation : {o}",F);Br(S,j,a,K);raise P(f"Installation échouée ({o}) — tout a été annulé.")from o
	e[W][X]=a;B1(e);u=sum(1 for A in a[p]if z(A)[0]==R);A6=f" (dont {u} dans GTA V)"if u else C;K(f"« {X} » chargé : {E(I)} fichiers copiés{A6}, {k} originaux sauvegardés.",N)
def Bu(pack_name,bases,state,log,progress):
	d=bases;V=state;O=pack_name;G=log;R=V[W].get(O)
	if not R:raise Q("Ce pack n'est pas chargé.")
	if AS():raise P('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	S=A.path.join(Ay,O);I=R[p];e=set();G(f"Désinstallation de « {O} » — {E(I)} fichiers...");U=0;X=E(I)<=60;i=max(1,E(I)//10)
	for(Z,f)in AD(I):
		C,H=z(f);M=d.get(C)
		if not M:G(f"Cible {n.get(C,C)} introuvable — {H} laissé en place.",F);continue
		try:D=Y(M,H)
		except Q as j:G(f"Entrée ignorée : {j}",F);continue
		if A.path.exists(D):
			A.remove(D)
			if X:G(f"Suppression ({n[C]}) : {H}")
		g,k=A.path.join(S,C,H),A.path.join(S,H);l=R[A4].get(AY(C,H))or c(f,h)and R[A4].get(H)
		if l:
			T=g if A.path.exists(g)else k
			if A.path.exists(T):
				A.makedirs(A.path.dirname(D),exist_ok=B);J.move(T,D);U+=1
				if X:G(f"Original restauré : {H}")
		if not X and(Z+1)%i==0:G(f"{Z+1}/{E(I)} fichiers retirés ({U} originaux restaurés)...")
		a=A.path.realpath(M);K=A.path.dirname(D)
		while A.path.commonpath([a,K])==a and K!=a:e.add(K);K=A.path.dirname(K)
		progress(Z+1,E(I))
	for K in AC(e,key=E,reverse=B):
		try:A.rmdir(K)
		except L:pass
	for(C,b)in R.get(AJ,[]):
		M=d.get(C)
		if not M:continue
		try:D=Y(M,b)
		except Q:continue
		T=A.path.join(S,Al,C,b)
		if A.path.exists(T):
			if A.path.isdir(D):J.rmtree(D,ignore_errors=B)
			J.move(T,D);U+=1;G(f"Dossier original restauré ({n[C]}) : {b}")
	if A.path.isdir(S):J.rmtree(S,ignore_errors=B)
	del V[W][O];B1(V);G(f"« {O} » déchargé : {E(I)} fichiers retirés, {U} originaux restaurés.",N)
class AZ(G):0
AA=D
def Bv(fn):global AA;AA=fn
def Aa():
	if AA is not D and AA():raise AZ('Téléchargement annulé.')
Bw=262144
Ab=4
Bx=3
class B8(P):0
def By(exc):
	A=exc
	if c(A,B8):return H
	if c(A,urllib.error.HTTPError):return A.code in(408,429)or A.code>=500
	return B
def Bz(url,headers,offset):
	A=offset;B=g(headers)
	if A:B['Range']=f"bytes={A}-"
	return urllib.request.urlopen(urllib.request.Request(url,headers=B),timeout=60)
def Ac(url,out_path,log,progress,headers=D,make_transform=D,align=1,check_space=B,quiet=H):
	Y=check_space;W=make_transform;U=out_path;O=log;K=headers;K=g(K or{});K.setdefault(k,r);a=A.path.dirname(U)or j;H,I,Q,L=0,0,D,0
	while B:
		Aa()
		try:
			with Bz(url,K,H)as J:
				if H and AB(J,Am,200)!=206:O('Le serveur ne gère pas la reprise — reprise depuis le début.');H=0
				if Q is D:Q=J.headers.get_filename()
				if H==0 and J.headers.get_content_type().startswith('text/'):raise B8('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				if not I:
					R=J.headers.get(BU,C)
					if X in R and R.rsplit(X,1)[1].isdigit():I=V(R.rsplit(X,1)[1])
					else:S=J.headers.get(An);I=V(S)+H if S and S.isdigit()else 0
					if I and Y and H==0:y(a,V(I*2.3),AK)
				b=W(H)if W else D
				with Z(U,'r+b'if H else'wb')as T:
					T.seek(H);T.truncate(H);c=H
					while B:
						Aa();M=J.read(Bw)
						if not M:break
						T.write(b(M)if b else M);H+=E(M)
						if I:progress(H,I)
						elif H-c>=256*1024**2:
							c=H
							if Y:y(a,512*1024**2,AK)
							if not quiet:O(f"{H/1048576:.0f} Mo téléchargés...")
			return Q,I or H
		except AZ:raise
		except G as N:
			if not By(N):raise
			L+=1
			if L>Ab:raise P(f"Téléchargement échoué après {Ab} reprises ({N})")from N
			H-=H%align;d=Bx*L;O(f"Coupure réseau ({N}) — reprise dans {d}s à {H/1048576:.0f} Mo (essai {L}/{Ab}).",F);time.sleep(d)
def Ad(url,key):
	A=url
	if not key:return A
	B='&'if'?'in A else'?';return f"{A}{B}key={urllib.parse.quote(key)}"
def B9(url,key):A=urllib.request.Request(Ad(url,key),headers={k:r});return urllib.request.urlopen(A,timeout=30)
def B_(cfg):
	C=cfg.get(i)
	if not C:return[]
	D=cfg.get(v)
	with B9(C,D)as G:B=K.loads(G.read().decode(U))
	E=C.rsplit(X,1)[0]+X;H=B.get(Ag,B)if c(B,g)else B;F=[]
	for A in H:
		if not c(A,g)or not A.get(O):continue
		try:
			A9(A[O])
			if not A.get(l):A[l]=Ad(urllib.parse.urljoin(E,A[Ao]),D)
			if A.get(S)and not A[S].startswith((w,x,'data:')):A[S]=Ad(urllib.parse.urljoin(E,A[S]),D)
		except(KeyError,Q,TypeError):continue
		F.append(A)
	return F
def BA(v):return tuple(V(A)for A in I.findall('\\d+',v or C))or(0,)
def C0():
	D=urllib.request.Request(f"https://api.github.com/repos/{Ax}/releases/latest",headers={k:r,BV:'application/vnd.github+json'})
	with urllib.request.urlopen(D,timeout=15)as E:A=K.loads(E.read().decode(U))
	B=(A.get('tag_name')or C).strip()
	if not B:return
	return B,A.get('html_url')or f"https://github.com/{Ax}/releases"
def BB(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return BW,A
	if D in B and'/folders/'in B:
		C=I.search('/folders/([\\w-]+)',A)
		if C:return Ap,C.group(1)
	if D in B:
		C=I.search('/file/d/([\\w-]+)',A)or I.search('[?&]id=([\\w-]+)',A)
		if C:return Aq,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if'?'in A else'?')+'confirm=t'
	return Aq,A
BC='Mozilla/5.0'
C1=I.compile('data-id="([\\w-]{20,})"')
C2=I.compile('<title>([^<]*)</title>')
def BD(url,rng=D):
	A={k:BC}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def BE(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def BF(fid):
	with BD(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(U,Ai)
def C3(html,fallback):
	B=fallback;D=C2.search(html)
	if not D:return B
	A=D.group(1).replace('\xa0',' ');A=I.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',C,A).strip();return A or B
def C4(html,self_id):
	B,C=[],{self_id}
	for A in C1.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def C5(fid):
	for K in range(2):
		try:
			with BD(BE(fid),'bytes=0-0')as A:E=A.headers.get('Content-Disposition',C);L=A.headers.get_content_type();F=A.headers.get(BU,C)
			if'attachment'in E and not L.startswith('text/html'):J=I.search('filename="([^"]+)"',E)or I.search("filename\\*=UTF-8''(.+)",E);M=urllib.parse.unquote(J.group(1))if J else D;N=V(F.split(X)[-1])if X in F else 0;return B,M,N
			return H,D,0
		except urllib.error.HTTPError as O:
			if O.code in(403,429)and K==0:continue
			return D,D,0
		except G:return D,D,0
	return D,D,0
def C6(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def Ae(seg):A=seg;A=I.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def C7(folder_id,log):
	B=folder_id;E=[]
	def D(cid,fname,size,prefix):D=prefix;C=fname;B=cid;F=A.path.join(D,Ae(C or B))if D else Ae(C or B);E.append((F,B,size))
	def I(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in C4(html,fid):
			L,E,F=C5(B)
			if L:D(B,E,F,C);continue
			try:H=BF(B)
			except G:D(B,E,F,C);continue
			if not C6(H):D(B,E,F,C);continue
			K=Ae(C3(H,B));I(B,H,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');I(B,BF(B),C,0);return E
def C8(folder_id,dest,log,progress):
	I=dest;G=log;C=C7(folder_id,G)
	if not C:raise P('Dossier Drive vide ou illisible (accès restreint ?).')
	F=sum(A for(B,C,A)in C);G(f"{E(C)} fichiers dans le dossier"+(f" ({F/1048576:.0f} Mo)."if F else j))
	if F:y(I,F,AK)
	A.makedirs(I,exist_ok=B);K=0;N=max(1,E(C)//20)
	for(J,(O,Q,S))in AD(C):
		Aa();L=Y(I,O);A.makedirs(A.path.dirname(L),exist_ok=B);M=K;T,R=Ac(BE(Q),L,G,lambda cur,tot,_b=M:progress(_b+cur,F)if F else D,headers={k:BC},check_space=H,quiet=B);K=M+R
		if(J+1)%N==0 or J+1==E(C):G(f"{J+1}/{E(C)} fichiers téléchargés...")
def C9(url,log):
	J='data';L=url.rstrip(X).split(X)[-1].split('?')[0]
	def B(u,data=D,headers=D):
		A=data;B={k:r,BV:AL};B.update(headers or{})
		if A is not D:B[Ar]=AL;A=K.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return K.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[J]['token']
	try:M=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={k:r}),timeout=30).read().decode();Q=I.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',M).group(1)
	except G as E:raise P(f"Gofile ne fonctionne plus avec ce type de lien ({E}). Ré-héberge le pack sur Google Drive ou Mega.")from E
	A=B(f"https://api.gofile.io/contents/{L}?wt={Q}",headers={'Authorization':f"Bearer {C}"})
	if A.get(Am)!=N:raise P(f"Gofile a refusé le lien ({A.get(Am)}).")
	R=A[J];S=R.get('children')or{};F=[A for A in S.values()if A.get('type')==Ao]
	if not F:raise P('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	H=max(F,key=lambda c:c.get(AM,0));return H['link'],{'Cookie':f"accountToken={C}"},H.get(O)
def BG(s):s=s.replace('-','+').replace('_',X);return At.b64decode(s+'='*(-E(s)%4))
def CA(url,out_path,log,progress):
	L='g';J=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as M,algorithms as N,modes as O
	except BM as U:raise P('Support Mega indisponible (module cryptography manquant).')from U
	E=I.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or I.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not E:raise P('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	W,X=E.group(1),E.group(2);A=A6.unpack('>8I',BG(X));Q=A6.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);Y=A6.pack('>2I',A[4],A[5])+J*8;Z=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=K.dumps([{'a':L,L:1,'p':W}]).encode(),headers={Ar:AL,k:r});B=K.loads(urllib.request.urlopen(Z,timeout=30).read().decode())
	if c(B,V)or c(B,u)and c(B[0],V):raise P('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	B=B[0];a,D=B[L],V(B.get('s',0));F='mega_pack'
	try:
		R=M(N.AES(Q),O.CBC(J*16)).decryptor();S=R.update(BG(B['at']))+R.finalize()
		if S.startswith(b'MEGA'):F=K.loads(S[4:].split(J)[0].decode())['n']
	except G:pass
	if D:y(T,V(D*2.3),AK)
	log(f"Fichier Mega : {F}"+(f" ({D/1048576:.0f} Mo)"if D else C))
	def b(offset):A=Y[:8]+A6.pack('>Q',offset//16);return M(N.AES(Q),O.CTR(A)).decryptor().update
	Ac(a,out_path,log,progress,make_transform=b,align=16,check_space=H);return F
def BH(pack,cfg,log,progress):
	V=progress;I=pack;H=log;W=A9(I[O]);P=Y(T,W);F=P+'.part';A.makedirs(T,exist_ok=B);j,L=BY.mkstemp(suffix='.pack',dir=T);A.close(j);M=D
	try:
		H(f"Téléchargement de « {I[O]} »...")
		if AS():H("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		M,Q=BB(I[l]);K=I.get(Ao)
		if A.path.isdir(F):J.rmtree(F,ignore_errors=B)
		if M==Ap:C8(Q,F,H,V);BL(F,H)
		elif M=='mega':K=CA(Q,L,H,V)or K
		else:
			if M==BW:H('Résolution du lien Gofile...');X,e,k=C9(Q,H);K=K or k
			else:X,e=Q,{}
			m,f=Ac(X,L,H,V,headers=e);K=m or K or A.path.basename(urllib.parse.urlparse(X).path)
			if K:H(f"Fichier : {K}"+(f" ({f/1048576:.0f} Mo)"if f else C))
		if M!=Ap:
			H(f"Extraction dans le cache local ({W})...");BK(L,F,H);R=A.listdir(F)
			if E(R)==1 and A.path.isdir(A.path.join(F,R[0]))and R[0].lower()not in(AF,A2,AG):
				c=A.path.join(F,R[0])
				for g in A.listdir(c):J.move(A.path.join(c,g),A.path.join(F,g))
				A.rmdir(c)
			if not CE(F):BL(F,H)
		if I.get(b):
			with Z(A.path.join(F,BT),'w',encoding=U)as d:d.write(h(I[b]))
		if I.get(S):
			try:
				with B9(I[S],D)as n:
					i=A.path.splitext(urllib.parse.urlparse(I[S]).path)[1]or AE
					if i.lower()in AQ:
						with Z(A.path.join(F,a+i.lower()),'wb')as d:d.write(n.read())
			except G:pass
		if A.path.isdir(P):J.rmtree(P)
		A.replace(F,P);H(f"« {W} » téléchargé et extrait.",N)
	except BaseException:J.rmtree(F,ignore_errors=B);raise
	finally:
		if A.path.exists(L):A.remove(L)
BI=134217728
BJ=3600
CB={'.zip','.rar','.7z'}
s=I.compile('\\.part(\\d+)\\.rar$',I.I)
A0=I.compile('\\.r\\d{2}$',I.I)
o=I.compile('\\.(\\d{3})$')
def CC():K='-o{d}';J='7-Zip';I='-inul';H='-ibck';G='WinRAR';F='UnRAR';E='{d}\\';D='-p-';C='-y';B='x';L=[(F,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,D,m,E]),(F,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,D,m,E]),(G,['C:\\Program Files\\WinRAR\\WinRAR.exe',B,H,I,C,D,m,E]),(G,['C:\\Program Files (x86)\\WinRAR\\WinRAR.exe',B,H,I,C,D,m,E]),(J,['C:\\Program Files\\7-Zip\\7z.exe',B,C,'-p',K,m]),(J,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,'-p',K,m]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',m,'-C','{d}'])];return[(C,B)for(C,B)in L if A.path.exists(B[0])]
def BK(archive,dest,log):
	H=log;E=archive;C=dest;A.makedirs(C,exist_ok=B)
	if Av.is_zipfile(E):
		try:
			with Av.ZipFile(E)as L:
				for M in L.namelist():
					O=A.path.realpath(A.path.join(C,M))
					if not O.startswith(A.path.realpath(C)+A.sep):raise Q(f"Chemin suspect dans l'archive : {M}")
				L.extractall(C)
			return
		except Q:raise
		except G as R:H(f"Zip non lisible en natif ({R}) — essai d'un extracteur externe...")
	N=CC()
	if not N:raise P('Aucun extracteur trouvé — installe WinRAR ou 7-Zip.')
	I=[]
	for(D,J)in N:
		H(f"Extraction avec {D}...");J=[A.replace(m,E).replace('{d}',C)for A in J]
		try:K=AN.run(J,capture_output=B,text=B,creationflags=BI,timeout=BJ)
		except AN.TimeoutExpired:I.append(f"{D} : abandon après {BJ//60} min (archive protégée par mot de passe ?)");H(f"{D} ne répond plus — abandon.",F);continue
		if K.returncode==0:CD(C);return
		I.append(f"{D} : {(K.stderr or K.stdout).strip()[:200]}")
	raise P('Échec extraction — '+' | '.join(I))
def CD(dest):
	for(E,B,F)in A.walk(dest):
		for C in u(B)+u(F):
			D=A.path.join(E,C)
			if B4(D):
				if C in B:B.remove(C);A.rmdir(D)
				else:A.remove(D)
def BL(dest,log):
	L=log;M=set()
	for S in range(3):
		D=[]
		for(P,T,Q)in A.walk(dest):D+=[A.path.join(P,B)for B in Q if A.path.splitext(B)[1].lower()in CB or o.search(B)or A0.search(B)]
		D=[A for A in D if A not in M]
		if not D:return
		H=[]
		for B in D:
			E=A.path.basename(B)
			if A0.search(E):continue
			J=o.search(E)
			if J and J.group(1)!='001':continue
			K=s.search(E)
			if K and V(K.group(1))>1:continue
			if K:N=s.sub(C,E)
			elif J:O=o.sub(C,E);N=A.path.splitext(O)[0]or O
			else:N=A.path.splitext(E)[0]
			L(f"Archive dans le pack : {E} — extraction...")
			try:BK(B,A.path.join(A.path.dirname(B),N),L)
			except G as R:L(f"Extraction de {E} impossible : {R}",F);M.add(B);continue
			H.append(B)
			if K:I=s.sub(C,B).lower();H+=[A for A in D if A!=B and s.search(A)and s.sub(C,A).lower()==I]
			elif J:I=o.sub(C,B).lower();H+=[A for A in D if A!=B and o.search(A)and o.sub(C,A).lower()==I]
			elif E.lower().endswith('.rar'):I=B[:-4].lower();H+=[A for A in D if A0.search(A)and A0.sub(C,A).lower()==I]
		for B in D:
			if B in H:
				if A.path.exists(B):A.remove(B)
			elif s.search(B)or A0.search(B)or o.search(B):M.add(B)
def CE(dest):
	C=AT|B5|AW|AX|AU
	for(F,D,E)in A.walk(dest):
		if any(A.lower()in C for A in D):return B
		if any(A.lower().endswith((AI,AH))for A in E):return B
	return H
def CF():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except G:pass
class CG:
	def __init__(A):A.state=B0();A.cfg=A8();A.fivem=Bh();A.gta=Bi(A.fivem);A.remote_packs=[];A.custom_packs=u(A.cfg.get('custom_packs',[]));A.background=A.cfg.get(As);A.busy=H;A._cancel=d.Event();Bv(A._cancel.is_set);A._lock=d.Lock();A._buf_lock=d.Lock();A._logs=[];A._prog=0,0;A._dirty=H
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=B
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,H
		return{'logs':B,'prog':u(A._prog),'busy':A.busy,'dirty':C}
	def _all_remote(C):
		D={A[O]:g(A)for A in C.remote_packs}
		for E in C.custom_packs:A=g(E);A[A5]=B;D[A[O]]=A
		return u(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((w,x)):return B
		C=A.path.join(e,B);return f"/bg?{V(A.path.getmtime(C))}"if A.path.exists(C)else D
	def get_state(A):
		Q='remote';P='image_link';N='nfiles';J=[];K={A[O]:A for A in A._all_remote()}
		for I in AR():F=K.pop(I,D);L=B3(I);J.append({O:I,AM:Bj(I),b:L,W:I in A.state[W],N:E(A.state[W].get(I,{}).get(p,[])),S:(F or{}).get(S)or Bk(I),P:(F or{}).get(S),l:(F or{}).get(l),a:(F or{}).get(a),Q:H,A5:t(F and F.get(A5)),A3:t(F and F.get(b)and h(F[b])!=(L or C))})
		for G in K.values():J.append({O:G[O],AM:G.get(AM,C),b:G.get(b),W:H,N:0,S:G.get(S),P:G.get(S),l:G.get(l),a:G.get(a),Q:B,A5:t(G.get(A5)),A3:H})
		return{M:A.fivem,R:A.gta,Ag:J,As:A.background_url(),i:A.cfg.get(i,C),v:A.cfg.get(v,C),'background_setting':A.background or C,'busy':A.busy,b:A7}
	def open_site(B):A.startfile('https://uxqt.site')
	def add_custom_pack(A,name,url,image,preview=C,old_name=C):
		K=image;I=preview;H=url;E=old_name;D=name;D,H,K=D.strip(),H.strip(),K.strip();I,E=I.strip(),E.strip()
		if not D or not H:A._log('Nom et lien requis pour ajouter un pack.',F);return
		try:D=A9(D);BB(H)
		except G as M:A._log(f"Refusé : {M}",F);return
		if not H.lower().startswith((w,x)):A._log('Lien refusé : il faut une URL http(s).',F);return
		if I and not I.startswith((w,x)):A._log('Lien preview refusé (il faut un lien http).',F);return
		P={D,E}-{C};A.custom_packs=[A for A in A.custom_packs if A[O]not in P];L={O:D,l:H}
		if K:L[S]=K
		if I:L[a]=I
		A.custom_packs.append(L);f(custom_packs=A.custom_packs)
		if E and E!=D and E in AR():
			try:J.rmtree(Y(T,E),ignore_errors=B)
			except Q:pass
		A._log(f"Pack « {D} » {"modifié"if E else"ajouté"}.",N);A._refresh_ui()
	def preview(C,name):
		E=A1((A for A in C._all_remote()if A[O]==name),D);B=(E or{}).get(a)
		if B and B.startswith((w,x)):A.startfile(B)
		else:C._log('Pas de preview pour ce pack.',F)
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if C in B.state[W]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[O]!=C];f(custom_packs=B.custom_packs)
		try:E=Y(T,C)
		except Q:E=D
		if E and A.path.isdir(E):
			try:J.rmtree(E);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",N)
			except L as G:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {G}",F)
		else:B._log(f"Pack « {C} » retiré.",N)
		B._refresh_ui()
	def choose_background(A):return CF()or C
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=D;f(background=D);C._log('Image de fond retirée.',N)
		elif B.startswith((w,x)):C.background=B;f(background=B);C._log('Image de fond (lien) enregistrée.',N)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(e,H))
				except L:pass
			E=A.path.splitext(B)[1].lower();E=E if E in AQ else AE;G=As+E;J.copy2(B,A.path.join(e,G));C.background=G;f(background=G);C._log('Image de fond enregistrée.',N)
		else:C._log(f"Image introuvable : {B}",F)
	def save_settings(B,url,key,fivem,gta,bg):
		E=fivem;D=gta;B.cfg[i]=url.strip();B.cfg[v]=key.strip();f(packs_url=B.cfg[i],packs_key=B.cfg[v]);E=E.strip()
		if E:
			if A.path.isdir(E):B.fivem=E;f(fivem_path=E);B._log(f"Dossier FiveM : {E}",N)
			else:B._log(f"Dossier introuvable : {E}",F)
		D=D.strip()
		if D:
			if A.path.isdir(D)and A.path.exists(A.path.join(D,BS)):B.gta=D;f(gta_path=D);B._log(f"Dossier GTA V : {D}",N)
			else:B._log(f"Dossier GTA V invalide (GTA5.exe absent) : {D}",F)
		if(bg or C).strip()!=(B.background or C):B._set_background(bg or C)
		B._log('Paramètres enregistrés.',N)
		if B.cfg[i]:B.fetch_remote()
		else:B.remote_packs=[];B._refresh_ui()
	def check_update(C):
		def A():
			try:
				A=C0()
				if A and BA(A[0])>BA(A7):C._log(f"Nouvelle version disponible : {A[0]} (tu as la {A7}) — {A[1]}",N)
			except G:pass
		d.Thread(target=A,daemon=B).start()
	def fetch_remote(A):
		if not A.cfg.get(i):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def C():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=B_(A.cfg);A._log(f"{E(A.remote_packs)} pack(s) disponibles en ligne.",N)
			except G as B:A.remote_packs=[];A._log(f"Serveur inaccessible : {B}",F)
			A._refresh_ui()
		d.Thread(target=C,daemon=B).start()
	def _run(A,fn):
		def C():
			if not A._lock.acquire(blocking=H):A._log('Une opération est déjà en cours.',F);return
			try:
				A._cancel.clear();A.busy=B;A._refresh_ui()
				try:fn()
				except AZ as C:A._log(f"{C} Rien n'a été installé.",F)
				except G as C:A._log(f"Erreur : {C}",F)
				finally:A._cancel.clear();A.busy=H;A._prog=0,0;A._refresh_ui()
			finally:A._lock.release()
		d.Thread(target=C,daemon=B).start()
	def cancel(A):
		if not A.busy:return{N:H}
		if not A._cancel.is_set():A._cancel.set();A._log('Annulation demandée, arrêt en cours...')
		return{N:B}
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return H
		return B
	def load(A,name):
		E=name
		if not A._need_fivem():return
		def B():
			B=A1((A for A in A._all_remote()if A[O]==E),D);F=E in AR();G=B and B.get(b)and h(B[b])!=(B3(E)or C)
			if B and(not F or G):BH(B,A.cfg,A._log,A._progress)
			elif not F:raise Q('Pack introuvable (ni local, ni sur le serveur).')
			Bt(E,{M:A.fivem,R:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:Bu(name,{M:A.fivem,R:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=A1((A for A in A._all_remote()if A[O]==name),D)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:BH(B,A.cfg,A._log,A._progress))
CH='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que uxqt.site (palette igloo dark) :\n     noir pur, verre translucide, lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  /* le bouton annuler prend le margin auto, "vider" se colle à sa droite */\n  #console-head #btn-cancel + button { margin-left: 14px; }\n  #console-head #btn-cancel { color: var(--err); }\n  #console-head #btn-cancel:hover { color: var(--err); text-decoration: underline; }\n  #console-head #btn-cancel:disabled { color: var(--muted); cursor: default;\n                                       text-decoration: none; }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>Modium</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">uxqt.site &#8599;</button>\n  </header>\n\n  <main><div class="grid" id="grid"></div><div class="empty" id="empty" style="display:none">\n    Aucun pack disponible.<br>\n    Vérifie la connexion au serveur (bouton Actualiser)<br>\n    ou l\'URL configurée dans Options.\n  </div></main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button id="btn-cancel" style="display:none"\n              onclick="cancelDownload()">annuler le téléchargement</button>\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  async function cancelDownload() {\n    const b = document.getElementById(\'btn-cancel\');\n    b.disabled = true;\n    b.textContent = \'annulation...\';\n    try { await api(\'cancel\'); } catch (e) { appendLog(\'Annulation : \' + e, \'err\'); }\n  }\n\n  // visible seulement pendant une action ; l\'arrêt n\'est effectif que si on est\n  // encore en phase de téléchargement (l\'installation, elle, va au bout)\n  function setBusyUI(busy) {\n    const b = document.getElementById(\'btn-cancel\');\n    if (!busy) {\n      b.style.display = \'none\';\n      b.disabled = false;\n      b.textContent = \'annuler le téléchargement\';\n    } else if (b.style.display === \'none\') {\n      b.style.display = \'\';\n    }\n  }\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = st.packs.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = st.packs.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) renderCustomList();\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      setBusyUI(r.busy);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    appendLog(\'Modium v\' + (st?.version || \'?\') + \' démarré.\', \'ok\');\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    api(\'check_update\');   // signale une nouvelle version, sans rien installer\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
CI={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',a,'cancel','check_update'}
def CJ(api):
	M=b'forbidden';L='127.0.0.1';F='text/plain';I=Au.token_urlsafe(16);N=CH.replace('__TOKEN__',I).encode(U)
	class O(BZ):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(Ar,ctype);A.send_header(An,h(E(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def _host_ok(A):B=(A.headers.get('Host')or C).split(']')[-1];return B.split(':')[0]in(L,'localhost')
		def do_GET(B):
			if not B._host_ok():B._send(403,M,F);return
			if B.path in(X,'/index.html'):B._send(200,N,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;C=A.path.join(e,E)if E and not E.startswith(Aq)else D
				if C and A.path.exists(C):
					G=A.path.splitext(C)[1].lower()
					with Z(C,'rb')as H:B._send(200,H.read(),Az.get(G,'application/octet-stream'))
				else:B._send(404,b'no background',F)
			else:B._send(404,b'not found',F)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if not A._host_ok()or B not in CI or not Au.compare_digest(A.headers.get(BX)or C,I):A._send(403,M,F);return
			try:
				D=V(A.headers.get(An,0))
				if D>1024**2:A._send(413,b'too large',F);return
				E=K.loads(A.rfile.read(D)or b'[]');J=AB(api,B)(*E);A._send(200,K.dumps(J,ensure_ascii=H).encode(U),'application/json; charset=utf-8')
			except G as L:A._send(500,K.dumps({'error':h(L)}).encode(U),AL)
	J=Ba((L,0),O);d.Thread(target=J.serve_forever,daemon=B).start();return J,f"http://127.0.0.1:{J.server_address[1]}/",I
def CK():
	A=AC(B0().get(W,{}))
	try:print('\n'.join(A))
	except G:pass
	q.exit(1 if A else 0)
def CL():
	if'--check-loaded'in q.argv:CK()
	H=CG();I,E,J=CJ(H);K=[J];D=Aw.create_window(Bb,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def C(*A):C=' '.join(h(A)for A in A);print(C.encode('ascii',Ai).decode(),flush=B)
		def L():
			F.sleep(4)
			try:import urllib.request as B;H=B.Request(E+'api/poll',data=b'[]',method='POST');H.add_header(BX,K[0]);I=B.urlopen(H,timeout=5).read()[:80];C('SELFTEST urllib POST:',I)
			except G as A:C('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except G as A:C('SELFTEST inject KO:',A)
			F.sleep(4)
			try:C('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));C('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));C('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except G as A:C('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		d.Thread(target=L,daemon=B).start()
	try:Aw.start(gui='edgechromium')
	finally:I.shutdown()
if __name__=='__main__':CL()