BZ='X-Token'
BY='categories'
BX='gofile'
BW='Accept'
BV='Content-Range'
BU='.version'
BT='GTA5.exe'
BS='CitizenFX.ini'
BR='FiveM.app'
BQ='image/jpeg'
BP='Modium'
BO=reversed
BN=ImportError
At='background'
As='Content-Type'
Ar='http'
Aq='gdrive_folder'
Ap='file'
Ao='Content-Length'
An='status'
Am='_dirs'
Al='x64'
Ak='.ini'
Aj='replace'
Ai='FiveM'
Ah='packs'
Ag='LOCALAPPDATA'
AN='size'
AM='application/json'
AL='le téléchargement'
AK='purged'
AJ='.rpf'
AI='.asi'
AH='plugins'
AG='citizen'
AF='.png'
AE=enumerate
AD=sorted
AC=getattr
A6='custom'
A5='backups'
A4='update'
A3='mods'
A2=next
y='https://'
x='http://'
w='packs_key'
v=list
u=bool
q='files'
n='{a}'
m='User-Agent'
l='.'
k='packs_url'
j=dict
e='categorie'
g=str
f=isinstance
d='url'
c='version'
b='preview'
a=open
Y='/'
X='loaded'
W=int
U='utf-8'
S='image'
R='gta'
Q=ValueError
P=RuntimeError
O='name'
N='fivem'
M=OSError
K='ok'
H=False
G=Exception
F='err'
E=len
D=None
C=''
B=True
import base64 as Au,json as L,os as A,re as I,secrets as Av,shutil as J,struct as A7,subprocess as AO,sys as r,tempfile as Ba,threading as h,time,urllib.error,urllib.parse,urllib.request,zipfile as Aw
from http.server import BaseHTTPRequestHandler as Bb,ThreadingHTTPServer as Bc
import webview as Ax
Bd=BP
A8='3.1.0'
s=f"Modium/{A8}"
Ay='ImSerial/modium'
Be='FiveMPackManager'
def Bf():
	if not AC(r,'frozen',H):return A.path.dirname(A.path.abspath(__file__))
	E=A.environ.get(Ag)or A.path.dirname(r.executable);C=A.path.join(E,BP);D=A.path.join(E,Be)
	if A.path.isdir(D)and not A.path.isdir(C):
		try:A.rename(D,C)
		except M:return D
	A.makedirs(C,exist_ok=B);return C
i=Bf()
T=A.path.join(i,Ah)
Az=A.path.join(i,'_backups')
AP=A.path.join(i,'state.json')
AQ=A.path.join(i,'config.json')
Bg={k:'https://modium.xyz/packs-096759e8/packs.json',w:'glt7ExuP7EBzBc56fUzoAmHy618FWBhT'}
def Bh():
	B=j(Bg);C=[A.path.dirname(A.path.abspath(__file__))]
	if AC(r,'_MEIPASS',D):C.insert(0,r._MEIPASS)
	for F in C:
		E=A.path.join(F,'embedded_config.json')
		if A.path.exists(E):
			try:
				with a(E,'r',encoding=U)as G:B.update(L.load(G))
				break
			except(M,L.JSONDecodeError):pass
	return B
Bi=Bh()
AR=AF,'.jpg','.jpeg','.webp','.gif'
A_={AF:'image/png','.jpg':BQ,'.jpeg':BQ,'.webp':'image/webp','.gif':'image/gif'}
def B0(path,data):
	C=path+'.tmp'
	with a(C,'w',encoding=U)as B:L.dump(data,B,indent=2,ensure_ascii=H);B.flush();A.fsync(B.fileno())
	A.replace(C,path)
def A9():
	B=j(Bi)
	if A.path.exists(AQ):
		try:
			with a(AQ,'r',encoding=U)as C:B.update(L.load(C))
		except(M,L.JSONDecodeError):pass
	return B
def V(**B):A=A9();A.update(B);B0(AQ,A)
def Bj():
	F='fivem_path';D=[];E=A9()
	if E.get(F):D.append(E[F])
	G=A.environ.get(Ag,C);D.append(A.path.join(G,Ai,BR))
	for B in D:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,BS))or A.path.isdir(A.path.join(B,AG))):return B
def Bk(fivem=D):
	I=fivem;N=A9();E=[N.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(Ag,C),Ai,BR))
	for K in J:
		G=A.path.join(K,BS)if K else D
		if G and A.path.exists(G):
			try:
				with a(G,'r',encoding=U,errors=Aj)as O:
					for L in O:
						if L.strip().lower().startswith('ivpath='):E.append(L.split('=',1)[1].strip())
			except M:pass
	try:
		import winreg as H
		for P in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,P)as Q:E.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except M:pass
	except BN:pass
	for B in('C:','D:','E:','F:'):E+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in E:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,BT)):return F
def B1():
	if A.path.exists(AP):
		try:
			with a(AP,'r',encoding=U)as B:return L.load(B)
		except(M,L.JSONDecodeError):pass
	return{X:{}}
def B2(state):B0(AP,state)
def AS():A.makedirs(T,exist_ok=B);return AD(B for B in A.listdir(T)if A.path.isdir(A.path.join(T,B))and not B.startswith(l))
def CO(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(l)or G and A.path.splitext(E)[0]==b:continue
			yield A.path.relpath(A.path.join(C,D),B)
def Bl(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(T,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except M:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
B3={}
def Bm(pack_name):
	G=A.path.join(T,pack_name)
	for E in AR:
		B=A.path.join(G,b+E)
		try:C=A.stat(B)
		except M:continue
		D=B3.get(B)
		if D and D[0]==C.st_mtime and D[1]==C.st_size:return D[2]
		try:
			with a(B,'rb')as H:I=Au.b64encode(H.read()).decode('ascii')
		except M:return
		F=f"data:{A_[E]};base64,{I}";B3[B]=C.st_mtime,C.st_size,F;return F
def B4(name):
	B=A.path.join(T,name,BU)
	if A.path.exists(B):
		try:
			with a(B,'r',encoding=U)as C:return C.read().strip()
		except M:pass
def Z(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise Q(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
Bn=I.compile('[<>:"/\\\\|?*\\x00-\\x1f]')
def AA(name):
	D=name;B=(D or C).strip().strip('. ')
	if not B or Bn.search(B)or B in(l,'..')or A.path.isabs(D or C):raise Q(f"Nom de pack invalide : {D!r}")
	return B
def B5(path):
	try:return u(A.lstat(path).st_file_attributes&1024)
	except(M,AttributeError):return A.path.islink(path)
def AT():
	try:
		D=AO.run(['tasklist','/FO','CSV'],capture_output=B,text=B,creationflags=BJ,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			C=A.split('","',1)[0].strip('"')
			if C.startswith(('modium','fivempackmanager')):continue
			if C.startswith((N,'gta5')):return B
		return H
	except G:return H
def z(path,need_bytes,what):
	B=need_bytes;C=J.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise P(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def CP(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except M:pass
	return B
AU={AG,A3,AH}
B6={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto 5','grand theft auto v legacy','gta v legacy','gtav legacy','gta 5 legacy','gta5 legacy','singleplayer','single player',R}
AV={'enbseries','enbcache'}
Bo=I.compile('^(enb[\\w .()-]*\\.(ini|dll|asi|fx|fxh|dds|bmp|cfg)|d3d(9|10|11|12)\\.dll|d3dcompiler[\\w.]*\\.dll|dxgi\\.dll)$',I.I)
Bp={'.dll',AI,Ak,'.fx','.fxh','.cfg','.json','.yml','.xml'}
def Bq(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=A3]
		for D in G:
			if D.lower().endswith(AJ):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def Br(src,pack_path,rpf_index,log):
	B=A.path.basename(src);C=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in C]
	for(F,G)in AE(H[:-1]):
		if G in(A4,Al):return A.path.join(*C[F:])
		if G=='dlcpacks':return A.path.join(A4,Al,*C[F:])
	D=rpf_index.get(B.lower(),[])
	if E(D)==1:return D[0]
	if E(D)>1:log(f"{B} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return B
def AW(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(l):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
AX={N,'five m','five-m','fivem.app','fivem app','fivem files','five m files','fivem folder'}
AY={'reshade-shaders','reshade-presets'}
def Bs(pack_path,log,gta_base=D):
	D=pack_path;I=log;B=[];T=Bq(gta_base);F={}
	def G(key,n=1):F[key]=F.get(key,0)+n
	def O(src):B.append((src,N,A.path.join(A3,Br(src,D,T,I))));G('rpf vers mods')
	def P(gta_dir,label,prefix=C):
		F=prefix;E=gta_dir
		for(I,K,J)in A.walk(E):
			for C in J:
				if C.startswith(l):continue
				D=A.path.join(I,C)
				if C.lower().endswith(AJ):O(D)
				else:H=A.path.relpath(D,E);B.append((D,R,A.path.join(F,H)if F else H));G(f"{label} vers GTA V")
	def Q(dirpath,in_fivem=H,depth=0):
		V='asi vers plugins';S=depth;J=in_fivem;H=dirpath
		if S>12:I(f"Profondeur maximale atteinte, dossier ignoré : {H}");return
		K=AD(A.listdir(H));T={B.lower()for B in K if A.path.isdir(A.path.join(H,B))};U=A.path.basename(H).lower();J=J or U in AX;W=U in AX or u(T&(AU|AY));X=not J and(u(T&AV)or any(A.lower().startswith('enb')and A.lower().endswith(Ak)for A in K));Y={A.path.splitext(B)[0].lower()for B in K if B.lower().endswith(AI)}
		for F in K:
			C=A.path.join(H,F);D=F.lower()
			if B5(C):I(f"Lien/jonction ignoré dans le pack : {F}");continue
			if A.path.isdir(C):
				if D in AU or D in AY:M=E(B);AW(B,C,N,D);G(f"{D} vers FiveM",E(B)-M)
				elif D in B6:P(C,B7(F))
				elif D in AV:
					if J:M=E(B);AW(B,C,N,D);G(f"{D} vers FiveM",E(B)-M)
					else:P(C,B7(F),prefix=D)
				else:Q(C,J,S+1)
			elif not D.startswith(l):
				L=A.path.splitext(D)[1]
				if L==AJ:O(C)
				elif X and Bo.match(F):B.append((C,R,F));G('ENB vers GTA V')
				elif L==AI:B.append((C,N,A.path.join(AH,F)));G(V)
				elif L==Ak and A.path.splitext(D)[0]in Y:B.append((C,N,A.path.join(AH,F)));G(V)
				elif W and L in Bp:B.append((C,N,F));G('racine FiveM')
	Q(D)
	if not B:I("Structure standard non détectée — copie de l'archive telle quelle.");AW(B,D,N,C)
	B=[(E,D,B)for(E,D,B)in B if not(D==N and A.path.dirname(B)==C and A.path.splitext(B)[0].lower()==b)];J,K=set(),[]
	for(U,L,M)in B:
		S=L,M.lower()
		if S not in J:J.add(S);K.append((U,L,M))
	V=', '.join(f"{A} : {B}"for(A,B)in F.items())or'rien à installer';I(f"Structure détectée — {V}.");return K
def B7(name):A=name;return A if E(A)<=20 else A[:17]+'...'
def A0(e):return(N,e)if f(e,g)else(e[0],e[1])
def AZ(target,rel):return f"{target}|{rel}"
def Bt(bases,backup_root,manifest,log):
	M=bases;K=manifest;I=backup_root
	for O in BO(K[q]):
		D,L=A0(O);E=M.get(D)
		if not E:continue
		try:
			C=Z(E,L)
			if A.path.exists(C):A.remove(C)
			if K[A5].get(AZ(D,L)):
				H=A.path.join(I,D,L)
				if A.path.exists(H):J.move(H,C)
		except G:pass
	for(D,N)in BO(K.get(AK,[])):
		E=M.get(D)
		if not E:continue
		try:
			C=Z(E,N);H=A.path.join(I,Am,D,N)
			if A.path.exists(H):
				if A.path.isdir(C):J.rmtree(C,ignore_errors=B)
				J.move(H,C)
		except G:pass
	J.rmtree(I,ignore_errors=B);log("Installation annulée — jeu restauré dans son état d'origine.",F)
o={N:Ai,R:'GTA V'}
Bu={N:{AG},R:{A4,Al,'redistributables','installers','dlc','_commonredist',A3}}
def B8(plan):
	C={}
	for(G,D,F)in plan:
		B=F.replace(Y,A.sep).split(A.sep)
		if E(B)>1:C.setdefault((D,B[0].lower()),B[0])
	return C
def Bv(pack_name,bases,state,log,progress):
	e=state;W=pack_name;S=bases;L=log
	if W in e[X]:raise Q('Ce pack est déjà chargé.')
	if AT():raise P('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	v=Z(T,AA(W));I=Bs(v,L,S.get(R))
	if not I:raise Q('Pack vide — aucun fichier à installer.')
	p=[1 for(B,A,C)in I if A==R and not S.get(R)]
	if p:L(f"Dossier GTA V introuvable — {E(p)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);I=[(B,A,C)for(B,A,C)in I if not(A==R and not S.get(R))]
	if not I:raise Q('Rien à installer (dossier GTA V non configuré).')
	i={}
	for(w,Y,A7)in I:
		try:i[Y]=i.get(Y,0)+A.path.getsize(w)
		except M:pass
	for(Y,x)in i.items():
		if S.get(Y):z(S[Y],x,f"l'installation ({o[Y]})")
	a={q:[],A5:{},AK:[]};b={}
	for(c,y)in e[X].items():
		if c!=W:
			for r in y[q]:b[A0(r)[0]+'|'+A0(r)[1].lower()]=c
	L(f"Installation de « {W} » — {E(I)} fichiers...");j=A.path.join(Az,W);k=0;s=E(I)<=60;A1=max(1,E(I)//10)
	try:
		for((H,f),U)in B8(I).items():
			O=S.get(H)
			if H!=N or not O or not A.path.isdir(O):continue
			g=A2((A for A in A.listdir(O)if A.lower()==f),D)
			if g and g!=U:
				try:A.rename(A.path.join(O,g),A.path.join(O,U));L(f"Dossier {g} renommé en {U}.")
				except M:pass
		for((H,f),U)in B8(I).items():
			O=S.get(H)
			if not O or f in Bu.get(H,set()):continue
			t=Z(O,U)
			if not A.path.isdir(t):continue
			A3=f"{H}|{f}{A.sep}";c=A2((B for(A,B)in b.items()if A.startswith(A3)),D)
			if c:L(f"Dossier {U} : contient des fichiers du pack « {c} » — fusion au lieu du remplacement.");continue
			d=A.path.join(j,Am,H,U);A.makedirs(A.path.dirname(d),exist_ok=B);J.move(t,d);a[AK].append([H,U]);L(f"Dossier existant mis de côté ({o[H]}) : {U} — remplacé proprement. Ton contenu précédent est sauvegardé et sera remis au déchargement du pack.")
		for(l,(A4,H,V))in AE(I):
			O=S[H];h=Z(O,V);m=H+'|'+V.lower()
			if m in b:L(f"Attention : {V} appartient déjà au pack « {b[m]} » — écrasé.")
			A.makedirs(A.path.dirname(h),exist_ok=B)
			if A.path.exists(h)and m not in b:
				d=A.path.join(j,H,V);A.makedirs(A.path.dirname(d),exist_ok=B);J.copy2(h,d);a[A5][AZ(H,V)]=B;k+=1
				if s:L(f"Sauvegarde de l'original ({o[H]}) : {V}")
			J.copy2(A4,h);a[q].append([H,V])
			if s:L(f"Copie ({o[H]}) : {V}")
			elif(l+1)%A1==0:L(f"{l+1}/{E(I)} fichiers copiés ({k} originaux sauvegardés)...")
			progress(l+1,E(I))
	except G as n:L(f"Erreur pendant l'installation : {n}",F);Bt(S,j,a,L);raise P(f"Installation échouée ({n}) — tout a été annulé.")from n
	e[X][W]=a;B2(e);u=sum(1 for A in a[q]if A0(A)[0]==R);A6=f" (dont {u} dans GTA V)"if u else C;L(f"« {W} » chargé : {E(I)} fichiers copiés{A6}, {k} originaux sauvegardés.",K)
def Bw(pack_name,bases,state,log,progress):
	c=bases;V=state;O=pack_name;G=log;R=V[X].get(O)
	if not R:raise Q("Ce pack n'est pas chargé.")
	if AT():raise P('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	S=A.path.join(Az,O);I=R[q];d=set();G(f"Désinstallation de « {O} » — {E(I)} fichiers...");U=0;W=E(I)<=60;i=max(1,E(I)//10)
	for(Y,e)in AE(I):
		C,H=A0(e);N=c.get(C)
		if not N:G(f"Cible {o.get(C,C)} introuvable — {H} laissé en place.",F);continue
		try:D=Z(N,H)
		except Q as j:G(f"Entrée ignorée : {j}",F);continue
		if A.path.exists(D):
			A.remove(D)
			if W:G(f"Suppression ({o[C]}) : {H}")
		h,k=A.path.join(S,C,H),A.path.join(S,H);l=R[A5].get(AZ(C,H))or f(e,g)and R[A5].get(H)
		if l:
			T=h if A.path.exists(h)else k
			if A.path.exists(T):
				A.makedirs(A.path.dirname(D),exist_ok=B);J.move(T,D);U+=1
				if W:G(f"Original restauré : {H}")
		if not W and(Y+1)%i==0:G(f"{Y+1}/{E(I)} fichiers retirés ({U} originaux restaurés)...")
		a=A.path.realpath(N);L=A.path.dirname(D)
		while A.path.commonpath([a,L])==a and L!=a:d.add(L);L=A.path.dirname(L)
		progress(Y+1,E(I))
	for L in AD(d,key=E,reverse=B):
		try:A.rmdir(L)
		except M:pass
	for(C,b)in R.get(AK,[]):
		N=c.get(C)
		if not N:continue
		try:D=Z(N,b)
		except Q:continue
		T=A.path.join(S,Am,C,b)
		if A.path.exists(T):
			if A.path.isdir(D):J.rmtree(D,ignore_errors=B)
			J.move(T,D);U+=1;G(f"Dossier original restauré ({o[C]}) : {b}")
	if A.path.isdir(S):J.rmtree(S,ignore_errors=B)
	del V[X][O];B2(V);G(f"« {O} » déchargé : {E(I)} fichiers retirés, {U} originaux restaurés.",K)
class Aa(G):0
AB=D
def Bx(fn):global AB;AB=fn
def Ab():
	if AB is not D and AB():raise Aa('Téléchargement annulé.')
By=262144
Ac=4
Bz=3
class B9(P):0
def B_(exc):
	A=exc
	if f(A,B9):return H
	if f(A,urllib.error.HTTPError):return A.code in(408,429)or A.code>=500
	return B
def C0(url,headers,offset):
	A=offset;B=j(headers)
	if A:B['Range']=f"bytes={A}-"
	return urllib.request.urlopen(urllib.request.Request(url,headers=B),timeout=60)
def Ad(url,out_path,log,progress,headers=D,make_transform=D,align=1,check_space=B,quiet=H):
	X=check_space;V=make_transform;U=out_path;O=log;K=headers;K=j(K or{});K.setdefault(m,s);Z=A.path.dirname(U)or l;H,I,Q,L=0,0,D,0
	while B:
		Ab()
		try:
			with C0(url,K,H)as J:
				if H and AC(J,An,200)!=206:O('Le serveur ne gère pas la reprise — reprise depuis le début.');H=0
				if Q is D:Q=J.headers.get_filename()
				if H==0 and J.headers.get_content_type().startswith('text/'):raise B9('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				if not I:
					R=J.headers.get(BV,C)
					if Y in R and R.rsplit(Y,1)[1].isdigit():I=W(R.rsplit(Y,1)[1])
					else:S=J.headers.get(Ao);I=W(S)+H if S and S.isdigit()else 0
					if I and X and H==0:z(Z,W(I*2.3),AL)
				b=V(H)if V else D
				with a(U,'r+b'if H else'wb')as T:
					T.seek(H);T.truncate(H);c=H
					while B:
						Ab();M=J.read(By)
						if not M:break
						T.write(b(M)if b else M);H+=E(M)
						if I:progress(H,I)
						elif H-c>=256*1024**2:
							c=H
							if X:z(Z,512*1024**2,AL)
							if not quiet:O(f"{H/1048576:.0f} Mo téléchargés...")
			return Q,I or H
		except Aa:raise
		except G as N:
			if not B_(N):raise
			L+=1
			if L>Ac:raise P(f"Téléchargement échoué après {Ac} reprises ({N})")from N
			H-=H%align;d=Bz*L;O(f"Coupure réseau ({N}) — reprise dans {d}s à {H/1048576:.0f} Mo (essai {L}/{Ac}).",F);time.sleep(d)
def Ae(url,key):
	A=url
	if not key:return A
	B='&'if'?'in A else'?';return f"{A}{B}key={urllib.parse.quote(key)}"
def BA(url,key):A=urllib.request.Request(Ae(url,key),headers={m:s});return urllib.request.urlopen(A,timeout=30)
def C1(cfg):
	C=cfg.get(k)
	if not C:return[]
	D=cfg.get(w)
	with BA(C,D)as G:B=L.loads(G.read().decode(U))
	E=C.rsplit(Y,1)[0]+Y;H=B.get(Ah,B)if f(B,j)else B;F=[]
	for A in H:
		if not f(A,j)or not A.get(O):continue
		try:
			AA(A[O])
			if not A.get(d):A[d]=Ae(urllib.parse.urljoin(E,A[Ap]),D)
			if A.get(S)and not A[S].startswith((x,y,'data:')):A[S]=Ae(urllib.parse.urljoin(E,A[S]),D)
		except(KeyError,Q,TypeError):continue
		F.append(A)
	return F
def BB(v):return tuple(W(A)for A in I.findall('\\d+',v or C))or(0,)
def C2():
	D=urllib.request.Request(f"https://api.github.com/repos/{Ay}/releases/latest",headers={m:s,BW:'application/vnd.github+json'})
	with urllib.request.urlopen(D,timeout=15)as E:A=L.loads(E.read().decode(U))
	B=(A.get('tag_name')or C).strip()
	if not B:return
	return B,A.get('html_url')or f"https://github.com/{Ay}/releases"
def BC(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return BX,A
	if D in B and'/folders/'in B:
		C=I.search('/folders/([\\w-]+)',A)
		if C:return Aq,C.group(1)
	if D in B:
		C=I.search('/file/d/([\\w-]+)',A)or I.search('[?&]id=([\\w-]+)',A)
		if C:return Ar,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if'?'in A else'?')+'confirm=t'
	return Ar,A
BD='Mozilla/5.0'
C3=I.compile('data-id="([\\w-]{20,})"')
C4=I.compile('<title>([^<]*)</title>')
def BE(url,rng=D):
	A={m:BD}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def BF(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def BG(fid):
	with BE(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(U,Aj)
def C5(html,fallback):
	B=fallback;D=C4.search(html)
	if not D:return B
	A=D.group(1).replace('\xa0',' ');A=I.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',C,A).strip();return A or B
def C6(html,self_id):
	B,C=[],{self_id}
	for A in C3.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def C7(fid):
	for K in range(2):
		try:
			with BE(BF(fid),'bytes=0-0')as A:E=A.headers.get('Content-Disposition',C);L=A.headers.get_content_type();F=A.headers.get(BV,C)
			if'attachment'in E and not L.startswith('text/html'):J=I.search('filename="([^"]+)"',E)or I.search("filename\\*=UTF-8''(.+)",E);M=urllib.parse.unquote(J.group(1))if J else D;N=W(F.split(Y)[-1])if Y in F else 0;return B,M,N
			return H,D,0
		except urllib.error.HTTPError as O:
			if O.code in(403,429)and K==0:continue
			return D,D,0
		except G:return D,D,0
	return D,D,0
def C8(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def Af(seg):A=seg;A=I.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def C9(folder_id,log):
	B=folder_id;E=[]
	def D(cid,fname,size,prefix):D=prefix;C=fname;B=cid;F=A.path.join(D,Af(C or B))if D else Af(C or B);E.append((F,B,size))
	def I(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in C6(html,fid):
			L,E,F=C7(B)
			if L:D(B,E,F,C);continue
			try:H=BG(B)
			except G:D(B,E,F,C);continue
			if not C8(H):D(B,E,F,C);continue
			K=Af(C5(H,B));I(B,H,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');I(B,BG(B),C,0);return E
def CA(folder_id,dest,log,progress):
	I=dest;G=log;C=C9(folder_id,G)
	if not C:raise P('Dossier Drive vide ou illisible (accès restreint ?).')
	F=sum(A for(B,C,A)in C);G(f"{E(C)} fichiers dans le dossier"+(f" ({F/1048576:.0f} Mo)."if F else l))
	if F:z(I,F,AL)
	A.makedirs(I,exist_ok=B);K=0;N=max(1,E(C)//20)
	for(J,(O,Q,S))in AE(C):
		Ab();L=Z(I,O);A.makedirs(A.path.dirname(L),exist_ok=B);M=K;T,R=Ad(BF(Q),L,G,lambda cur,tot,_b=M:progress(_b+cur,F)if F else D,headers={m:BD},check_space=H,quiet=B);K=M+R
		if(J+1)%N==0 or J+1==E(C):G(f"{J+1}/{E(C)} fichiers téléchargés...")
def CB(url,log):
	J='data';M=url.rstrip(Y).split(Y)[-1].split('?')[0]
	def B(u,data=D,headers=D):
		A=data;B={m:s,BW:AM};B.update(headers or{})
		if A is not D:B[As]=AM;A=L.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return L.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[J]['token']
	try:N=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={m:s}),timeout=30).read().decode();Q=I.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',N).group(1)
	except G as E:raise P(f"Gofile ne fonctionne plus avec ce type de lien ({E}). Ré-héberge le pack sur Google Drive ou Mega.")from E
	A=B(f"https://api.gofile.io/contents/{M}?wt={Q}",headers={'Authorization':f"Bearer {C}"})
	if A.get(An)!=K:raise P(f"Gofile a refusé le lien ({A.get(An)}).")
	R=A[J];S=R.get('children')or{};F=[A for A in S.values()if A.get('type')==Ap]
	if not F:raise P('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	H=max(F,key=lambda c:c.get(AN,0));return H['link'],{'Cookie':f"accountToken={C}"},H.get(O)
def BH(s):s=s.replace('-','+').replace('_',Y);return Au.b64decode(s+'='*(-E(s)%4))
def CC(url,out_path,log,progress):
	K='g';J=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as M,algorithms as N,modes as O
	except BN as U:raise P('Support Mega indisponible (module cryptography manquant).')from U
	E=I.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or I.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not E:raise P('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	V,X=E.group(1),E.group(2);A=A7.unpack('>8I',BH(X));Q=A7.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);Y=A7.pack('>2I',A[4],A[5])+J*8;Z=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=L.dumps([{'a':K,K:1,'p':V}]).encode(),headers={As:AM,m:s});B=L.loads(urllib.request.urlopen(Z,timeout=30).read().decode())
	if f(B,W)or f(B,v)and f(B[0],W):raise P('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	B=B[0];a,D=B[K],W(B.get('s',0));F='mega_pack'
	try:
		R=M(N.AES(Q),O.CBC(J*16)).decryptor();S=R.update(BH(B['at']))+R.finalize()
		if S.startswith(b'MEGA'):F=L.loads(S[4:].split(J)[0].decode())['n']
	except G:pass
	if D:z(T,W(D*2.3),AL)
	log(f"Fichier Mega : {F}"+(f" ({D/1048576:.0f} Mo)"if D else C))
	def b(offset):A=Y[:8]+A7.pack('>Q',offset//16);return M(N.AES(Q),O.CTR(A)).decryptor().update
	Ad(a,out_path,log,progress,make_transform=b,align=16,check_space=H);return F
def BI(pack,cfg,log,progress):
	V=progress;I=pack;H=log;W=AA(I[O]);P=Z(T,W);F=P+'.part';A.makedirs(T,exist_ok=B);k,M=Ba.mkstemp(suffix='.pack',dir=T);A.close(k);N=D
	try:
		H(f"Téléchargement de « {I[O]} »...")
		if AT():H("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		N,Q=BC(I[d]);L=I.get(Ap)
		if A.path.isdir(F):J.rmtree(F,ignore_errors=B)
		if N==Aq:CA(Q,F,H,V);BM(F,H)
		elif N=='mega':L=CC(Q,M,H,V)or L
		else:
			if N==BX:H('Résolution du lien Gofile...');X,f,l=CB(Q,H);L=L or l
			else:X,f=Q,{}
			m,h=Ad(X,M,H,V,headers=f);L=m or L or A.path.basename(urllib.parse.urlparse(X).path)
			if L:H(f"Fichier : {L}"+(f" ({h/1048576:.0f} Mo)"if h else C))
		if N!=Aq:
			H(f"Extraction dans le cache local ({W})...");BL(M,F,H);R=A.listdir(F)
			if E(R)==1 and A.path.isdir(A.path.join(F,R[0]))and R[0].lower()not in(AG,A3,AH):
				Y=A.path.join(F,R[0])
				for i in A.listdir(Y):J.move(A.path.join(Y,i),A.path.join(F,i))
				A.rmdir(Y)
			if not CG(F):BM(F,H)
		if I.get(c):
			with a(A.path.join(F,BU),'w',encoding=U)as e:e.write(g(I[c]))
		if I.get(S):
			try:
				with BA(I[S],D)as n:
					j=A.path.splitext(urllib.parse.urlparse(I[S]).path)[1]or AF
					if j.lower()in AR:
						with a(A.path.join(F,b+j.lower()),'wb')as e:e.write(n.read())
			except G:pass
		if A.path.isdir(P):J.rmtree(P)
		A.replace(F,P);H(f"« {W} » téléchargé et extrait.",K)
	except BaseException:J.rmtree(F,ignore_errors=B);raise
	finally:
		if A.path.exists(M):A.remove(M)
BJ=134217728
BK=3600
CD={'.zip','.rar','.7z'}
t=I.compile('\\.part(\\d+)\\.rar$',I.I)
A1=I.compile('\\.r\\d{2}$',I.I)
p=I.compile('\\.(\\d{3})$')
def CE():K='-o{d}';J='7-Zip';I='-inul';H='-ibck';G='WinRAR';F='UnRAR';E='{d}\\';D='-p-';C='-y';B='x';L=[(F,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,D,n,E]),(F,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,D,n,E]),(G,['C:\\Program Files\\WinRAR\\WinRAR.exe',B,H,I,C,D,n,E]),(G,['C:\\Program Files (x86)\\WinRAR\\WinRAR.exe',B,H,I,C,D,n,E]),(J,['C:\\Program Files\\7-Zip\\7z.exe',B,C,'-p',K,n]),(J,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,'-p',K,n]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',n,'-C','{d}'])];return[(C,B)for(C,B)in L if A.path.exists(B[0])]
def BL(archive,dest,log):
	H=log;E=archive;C=dest;A.makedirs(C,exist_ok=B)
	if Aw.is_zipfile(E):
		try:
			with Aw.ZipFile(E)as L:
				for M in L.namelist():
					O=A.path.realpath(A.path.join(C,M))
					if not O.startswith(A.path.realpath(C)+A.sep):raise Q(f"Chemin suspect dans l'archive : {M}")
				L.extractall(C)
			return
		except Q:raise
		except G as R:H(f"Zip non lisible en natif ({R}) — essai d'un extracteur externe...")
	N=CE()
	if not N:raise P('Aucun extracteur trouvé — installe WinRAR ou 7-Zip.')
	I=[]
	for(D,J)in N:
		H(f"Extraction avec {D}...");J=[A.replace(n,E).replace('{d}',C)for A in J]
		try:K=AO.run(J,capture_output=B,text=B,creationflags=BJ,timeout=BK)
		except AO.TimeoutExpired:I.append(f"{D} : abandon après {BK//60} min (archive protégée par mot de passe ?)");H(f"{D} ne répond plus — abandon.",F);continue
		if K.returncode==0:CF(C);return
		I.append(f"{D} : {(K.stderr or K.stdout).strip()[:200]}")
	raise P('Échec extraction — '+' | '.join(I))
def CF(dest):
	for(E,B,F)in A.walk(dest):
		for C in v(B)+v(F):
			D=A.path.join(E,C)
			if B5(D):
				if C in B:B.remove(C);A.rmdir(D)
				else:A.remove(D)
def BM(dest,log):
	L=log;M=set()
	for S in range(3):
		D=[]
		for(P,T,Q)in A.walk(dest):D+=[A.path.join(P,B)for B in Q if A.path.splitext(B)[1].lower()in CD or p.search(B)or A1.search(B)]
		D=[A for A in D if A not in M]
		if not D:return
		H=[]
		for B in D:
			E=A.path.basename(B)
			if A1.search(E):continue
			J=p.search(E)
			if J and J.group(1)!='001':continue
			K=t.search(E)
			if K and W(K.group(1))>1:continue
			if K:N=t.sub(C,E)
			elif J:O=p.sub(C,E);N=A.path.splitext(O)[0]or O
			else:N=A.path.splitext(E)[0]
			L(f"Archive dans le pack : {E} — extraction...")
			try:BL(B,A.path.join(A.path.dirname(B),N),L)
			except G as R:L(f"Extraction de {E} impossible : {R}",F);M.add(B);continue
			H.append(B)
			if K:I=t.sub(C,B).lower();H+=[A for A in D if A!=B and t.search(A)and t.sub(C,A).lower()==I]
			elif J:I=p.sub(C,B).lower();H+=[A for A in D if A!=B and p.search(A)and p.sub(C,A).lower()==I]
			elif E.lower().endswith('.rar'):I=B[:-4].lower();H+=[A for A in D if A1.search(A)and A1.sub(C,A).lower()==I]
		for B in D:
			if B in H:
				if A.path.exists(B):A.remove(B)
			elif t.search(B)or A1.search(B)or p.search(B):M.add(B)
def CG(dest):
	C=AU|B6|AX|AY|AV
	for(F,D,E)in A.walk(dest):
		if any(A.lower()in C for A in D):return B
		if any(A.lower().endswith((AJ,AI))for A in E):return B
	return H
def CH():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except G:pass
class CI:
	def __init__(A):A.state=B1();A.cfg=A9();A.fivem=Bj();A.gta=Bk(A.fivem);A.remote_packs=[];A.custom_packs=v(A.cfg.get('custom_packs',[]));A.categories=[g(A)for A in A.cfg.get(BY,[])];A.background=A.cfg.get(At);A.busy=H;A._maj=D;A._cancel=h.Event();Bx(A._cancel.is_set);A._lock=h.Lock();A._buf_lock=h.Lock();A._logs=[];A._prog=0,0;A._dirty=H
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=B
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,H
		return{'logs':B,'prog':v(A._prog),'busy':A.busy,'dirty':C,'maj':A._maj}
	def _all_remote(C):
		D={A[O]:j(A)for A in C.remote_packs}
		for E in C.custom_packs:A=j(E);A[A6]=B;D[A[O]]=A
		return v(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((x,y)):return B
		C=A.path.join(i,B);return f"/bg?{W(A.path.getmtime(C))}"if A.path.exists(C)else D
	def get_state(A):
		Q='remote';P='image_link';M='nfiles';J=[];K={A[O]:A for A in A._all_remote()}
		for I in AS():F=K.pop(I,D);L=B4(I);J.append({O:I,AN:Bl(I),c:L,X:I in A.state[X],M:E(A.state[X].get(I,{}).get(q,[])),S:(F or{}).get(S)or Bm(I),P:(F or{}).get(S),d:(F or{}).get(d),b:(F or{}).get(b),Q:H,A6:u(F and F.get(A6)),e:(F or{}).get(e,C),A4:u(F and F.get(c)and g(F[c])!=(L or C))})
		for G in K.values():J.append({O:G[O],AN:G.get(AN,C),c:G.get(c),X:H,M:0,S:G.get(S),P:G.get(S),d:G.get(d),b:G.get(b),Q:B,A6:u(G.get(A6)),e:G.get(e,C),A4:H})
		return{N:A.fivem,R:A.gta,Ah:J,At:A.background_url(),k:A.cfg.get(k,C),w:A.cfg.get(w,C),'background_setting':A.background or C,'busy':A.busy,c:A8,BY:A.categories}
	def open_site(B):A.startfile('https://modium.xyz')
	def ouvrir_maj(C):
		B=(C._maj or{}).get(d)
		if B and B.startswith('https://github.com/'):A.startfile(B)
	def ignorer_maj(A):A._maj=D
	def add_custom_pack(A,name,url,image,preview=C,old_name=C,categorie=C):
		M=image;L=categorie;I=preview;H=url;E=old_name;D=name;D,H,M=D.strip(),H.strip(),M.strip();I,E=I.strip(),E.strip();L=L.strip()
		if not D or not H:A._log('Nom et lien requis pour ajouter un pack.',F);return
		try:D=AA(D);BC(H)
		except G as P:A._log(f"Refusé : {P}",F);return
		if not H.lower().startswith((x,y)):A._log('Lien refusé : il faut une URL http(s).',F);return
		if I and not I.startswith((x,y)):A._log('Lien preview refusé (il faut un lien http).',F);return
		R={D,E}-{C};A.custom_packs=[A for A in A.custom_packs if A[O]not in R];N={O:D,d:H}
		if M:N[S]=M
		if I:N[b]=I
		if L:
			N[e]=L
			if L not in A.categories:A.categories.append(L);V(categories=A.categories)
		A.custom_packs.append(N);V(custom_packs=A.custom_packs)
		if E and E!=D and E in AS():
			try:J.rmtree(Z(T,E),ignore_errors=B)
			except Q:pass
		A._log(f"Pack « {D} » {"modifié"if E else"ajouté"}.",K);A._refresh_ui()
	def add_categorie(B,nom):
		A=nom;A=' '.join(A.split())[:40]
		if not A:return
		if A in B.categories:B._log(f"La catégorie « {A} » existe déjà.",F);return
		B.categories.append(A);V(categories=B.categories);B._log(f"Catégorie « {A} » créée.",K);B._refresh_ui()
	def remove_categorie(A,nom):
		B=nom
		if B not in A.categories:return
		A.categories=[A for A in A.categories if A!=B];E=0
		for F in A.custom_packs:
			if F.get(e)==B:F.pop(e,D);E+=1
		V(categories=A.categories,custom_packs=A.custom_packs);G=f" — {E} pack(s) sans catégorie"if E else C;A._log(f"Catégorie « {B} » supprimée{G}.",K);A._refresh_ui()
	def rename_categorie(A,ancien,nouveau):
		C=ancien;B=nouveau;B=' '.join(B.split())[:40]
		if not B or C not in A.categories or B==C:return
		if B in A.categories:A._log(f"La catégorie « {B} » existe déjà.",F);return
		A.categories=[B if A==C else A for A in A.categories]
		for D in A.custom_packs:
			if D.get(e)==C:D[e]=B
		V(categories=A.categories,custom_packs=A.custom_packs);A._log(f"Catégorie renommée en « {B} ».",K);A._refresh_ui()
	def preview(C,name):
		E=A2((A for A in C._all_remote()if A[O]==name),D);B=(E or{}).get(b)
		if B and B.startswith((x,y)):A.startfile(B)
		else:C._log('Pas de preview pour ce pack.',F)
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if C in B.state[X]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[O]!=C];V(custom_packs=B.custom_packs)
		try:E=Z(T,C)
		except Q:E=D
		if E and A.path.isdir(E):
			try:J.rmtree(E);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",K)
			except M as G:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {G}",F)
		else:B._log(f"Pack « {C} » retiré.",K)
		B._refresh_ui()
	def choose_background(A):return CH()or C
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=D;V(background=D);C._log('Image de fond retirée.',K)
		elif B.startswith((x,y)):C.background=B;V(background=B);C._log('Image de fond (lien) enregistrée.',K)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(i,H))
				except M:pass
			E=A.path.splitext(B)[1].lower();E=E if E in AR else AF;G=At+E;J.copy2(B,A.path.join(i,G));C.background=G;V(background=G);C._log('Image de fond enregistrée.',K)
		else:C._log(f"Image introuvable : {B}",F)
	def save_settings(B,url,key,fivem,gta,bg):
		E=fivem;D=gta;B.cfg[k]=url.strip();B.cfg[w]=key.strip();V(packs_url=B.cfg[k],packs_key=B.cfg[w]);E=E.strip()
		if E:
			if A.path.isdir(E):B.fivem=E;V(fivem_path=E);B._log(f"Dossier FiveM : {E}",K)
			else:B._log(f"Dossier introuvable : {E}",F)
		D=D.strip()
		if D:
			if A.path.isdir(D)and A.path.exists(A.path.join(D,BT)):B.gta=D;V(gta_path=D);B._log(f"Dossier GTA V : {D}",K)
			else:B._log(f"Dossier GTA V invalide (GTA5.exe absent) : {D}",F)
		if(bg or C).strip()!=(B.background or C):B._set_background(bg or C)
		B._log('Paramètres enregistrés.',K)
		if B.cfg[k]:B.fetch_remote()
		else:B.remote_packs=[];B._refresh_ui()
	def check_update(C):
		def A():
			try:
				A=C2()
				if A and BB(A[0])>BB(A8):C._maj={c:A[0],d:A[1],'actuelle':A8};C._refresh_ui()
			except G:pass
		h.Thread(target=A,daemon=B).start()
	def fetch_remote(A):
		if not A.cfg.get(k):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def C():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=C1(A.cfg);A._log(f"{E(A.remote_packs)} pack(s) disponibles en ligne.",K)
			except G as B:A.remote_packs=[];A._log(f"Serveur inaccessible : {B}",F)
			A._refresh_ui()
		h.Thread(target=C,daemon=B).start()
	def _run(A,fn):
		def C():
			if not A._lock.acquire(blocking=H):A._log('Une opération est déjà en cours.',F);return
			try:
				A._cancel.clear();A.busy=B;A._refresh_ui()
				try:fn()
				except Aa as C:A._log(f"{C} Rien n'a été installé.",F)
				except G as C:A._log(f"Erreur : {C}",F)
				finally:A._cancel.clear();A.busy=H;A._prog=0,0;A._refresh_ui()
			finally:A._lock.release()
		h.Thread(target=C,daemon=B).start()
	def cancel(A):
		if not A.busy:return{K:H}
		if not A._cancel.is_set():A._cancel.set();A._log('Annulation demandée, arrêt en cours...')
		return{K:B}
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return H
		return B
	def load(A,name):
		E=name
		if not A._need_fivem():return
		def B():
			B=A2((A for A in A._all_remote()if A[O]==E),D);F=E in AS();G=B and B.get(c)and g(B[c])!=(B4(E)or C)
			if B and(not F or G):BI(B,A.cfg,A._log,A._progress)
			elif not F:raise Q('Pack introuvable (ni local, ni sur le serveur).')
			Bv(E,{N:A.fivem,R:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:Bw(name,{N:A.fivem,R:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=A2((A for A in A._all_remote()if A[O]==name),D)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:BI(B,A.cfg,A._log,A._progress))
CJ='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que le site : noir pur, verre translucide,\n     lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow: hidden; }\n  /* ---- colonne des catégories ---- */\n  main { display: flex; gap: 0; }\n  #cotes {\n    width: 176px; flex-shrink: 0; padding: 20px 12px 20px 22px;\n    border-right: 1px solid var(--line); overflow-y: auto;\n  }\n  .cote-t {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted); padding: 0 10px 10px;\n  }\n  .cote {\n    display: flex; align-items: center; gap: 8px; width: 100%;\n    background: none; border: 1px solid transparent; border-radius: 8px;\n    color: var(--muted); cursor: pointer; text-align: left;\n    padding: 8px 10px; margin-bottom: 3px; font-size: 12px;\n    transition: background 0.2s, color 0.2s, border-color 0.2s, transform 0.2s;\n  }\n  .cote:hover { background: var(--glass); color: var(--text); transform: translateX(2px); }\n  .cote.on { background: var(--glass); color: var(--text); border-color: var(--line); }\n  .cote .n {\n    margin-left: auto; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted);\n  }\n  .zone { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  main > .zone { min-width: 0; }\n  #cotes:empty { display: none; }\n\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  /* le bouton annuler prend le margin auto, "vider" se colle à sa droite */\n  #console-head #btn-cancel + button { margin-left: 14px; }\n  #console-head #btn-cancel { color: var(--err); }\n  #console-head #btn-cancel:hover { color: var(--err); text-decoration: underline; }\n  #console-head #btn-cancel:disabled { color: var(--muted); cursor: default;\n                                       text-decoration: none; }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n\n  /* ---- fenêtre de mise à jour ---- */\n  #maj {\n    position: fixed; inset: 0; z-index: 200; display: none;\n    align-items: center; justify-content: center;\n    background: rgba(0, 0, 0, 0.82); backdrop-filter: blur(6px);\n  }\n  #maj.show { display: flex; animation: majFond .45s ease-out; }\n  @keyframes majFond { from { opacity: 0 } to { opacity: 1 } }\n  #maj-fond { position: absolute; inset: 0; width: 100%; height: 100%; }\n  .maj-box {\n    position: relative; text-align: center; padding: 46px 54px;\n    border: 1px solid var(--line); border-radius: 18px;\n    background: rgba(10, 10, 12, 0.72); backdrop-filter: blur(14px);\n    box-shadow: 0 30px 80px -20px rgba(0, 0, 0, 0.9);\n    animation: majBoite .55s cubic-bezier(.2, .8, .25, 1);\n  }\n  @keyframes majBoite {\n    from { opacity: 0; transform: translateY(22px) scale(.94) }\n    to { opacity: 1; transform: none }\n  }\n  .maj-pastille {\n    display: inline-block; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.24em; text-transform: uppercase;\n    color: #ff6a6a; border: 1px solid rgba(216, 26, 26, 0.45);\n    background: rgba(216, 26, 26, 0.1); border-radius: 999px; padding: 6px 16px;\n    animation: majPouls 2.2s ease-in-out infinite;\n  }\n  @keyframes majPouls {\n    0%, 100% { box-shadow: 0 0 10px rgba(216, 26, 26, .25) }\n    50% { box-shadow: 0 0 26px rgba(216, 26, 26, .6) }\n  }\n  .maj-v {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 62px; font-weight: 700; letter-spacing: -0.02em; margin: 18px 0 6px;\n    background-image: linear-gradient(100deg, #fff 20%, #9a9aa4 55%, #fff 85%);\n    background-size: 220% 100%;\n    -webkit-background-clip: text; background-clip: text; color: transparent;\n    animation: majBrille 6s linear infinite;\n    filter: drop-shadow(0 0 18px rgba(255, 255, 255, .3))\n            drop-shadow(0 0 44px rgba(216, 26, 26, .45));\n  }\n  @keyframes majBrille { to { background-position: -220% 0 } }\n  .maj-de {\n    font-family: ui-monospace, Consolas, monospace; font-size: 10px;\n    letter-spacing: 0.18em; text-transform: uppercase; color: var(--muted);\n    margin-bottom: 30px;\n  }\n  .maj-de b { color: var(--text); font-weight: 400; }\n  .maj-actions { display: flex; gap: 10px; justify-content: center; }\n  .maj-actions .btn { flex: 0 0 auto; padding: 0 26px; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal select {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n    cursor: pointer; appearance: none;\n    /* chevron dessiné en fond : la flèche native est grise et hors charte */\n    background-image: url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'10\' height=\'6\'%3E%3Cpath d=\'M1 1l4 4 4-4\' fill=\'none\' stroke=\'%238a8a8e\' stroke-width=\'1.5\' stroke-linecap=\'round\'/%3E%3C/svg%3E");\n    background-repeat: no-repeat; background-position: right 12px center;\n    padding-right: 30px;\n  }\n  #modal select:focus { outline: none; border-color: var(--accent); }\n  #modal select option { background: #101012; color: var(--text); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>Modium</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">modium.xyz &#8599;</button>\n  </header>\n\n  <main>\n    <aside id="cotes">\n      <div class="cote-t">Catégories</div>\n      <div id="cote-liste"></div>\n    </aside>\n    <div class="zone">\n      <div class="grid" id="grid"></div>\n      <div class="empty" id="empty" style="display:none">\n        Aucun pack disponible.<br>\n        Vérifie la connexion au serveur (bouton Actualiser)<br>\n        ou l\'URL configurée dans Options.\n      </div>\n    </div>\n  </main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button id="btn-cancel" style="display:none"\n              onclick="cancelDownload()">annuler le téléchargement</button>\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n\n  <div id="maj">\n    <canvas id="maj-fond"></canvas>\n    <div class="maj-box">\n      <div class="maj-pastille">Mise à jour disponible</div>\n      <div class="maj-v"><span id="maj-num">—</span></div>\n      <div class="maj-de">tu utilises la <b id="maj-old">—</b></div>\n      <div class="maj-actions">\n        <button class="btn load" onclick="api(\'ouvrir_maj\')">Télécharger</button>\n        <button class="btn unload" onclick="fermerMaj()">Plus tard</button>\n      </div>\n    </div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="cats">Catégories</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <select id="cp-cat" style="margin-top:6px"></select>\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="cats" style="display:none">\n        <label>Nouvelle catégorie</label>\n        <div class="row" style="margin-top:0">\n          <input id="cat-nom" placeholder="Ex : ENB, Thèmes, Réalistes...">\n          <button class="btn dl" style="flex:0 0 120px" onclick="addCat()">Créer</button>\n        </div>\n        <div id="cat-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n\n  // ---- sons ----------------------------------------------------------\n  // Synthétisés à la volée : aucun fichier à embarquer dans l\'exe. Le\n  // contexte audio ne peut naître qu\'après un geste de l\'utilisateur, règle\n  // des navigateurs — et pywebview embarque un vrai moteur de rendu.\n  const Son = (() => {\n    let ctx = null, master = null, dernier = 0;\n    const demarrer = () => {\n      if (ctx) return;\n      const AC = window.AudioContext || window.webkitAudioContext;\n      if (!AC) return;\n      ctx = new AC();\n      master = ctx.createGain(); master.gain.value = .5;\n      const f = ctx.createBiquadFilter();\n      f.type = \'lowpass\'; f.frequency.value = 5200;\n      master.connect(f); f.connect(ctx.destination);\n    };\n    const note = (f0, f1, duree, vol, forme = \'sine\') => {\n      if (!ctx) return;\n      const t = ctx.currentTime;\n      const o = ctx.createOscillator(), g = ctx.createGain();\n      o.type = forme;\n      o.frequency.setValueAtTime(f0, t);\n      if (f1 !== f0) o.frequency.exponentialRampToValueAtTime(f1, t + duree);\n      // attaque courte mais jamais nulle : à zéro on entend un clic parasite\n      g.gain.setValueAtTime(.0001, t);\n      g.gain.exponentialRampToValueAtTime(vol, t + .006);\n      g.gain.exponentialRampToValueAtTime(.0001, t + duree);\n      o.connect(g); g.connect(master);\n      o.start(t); o.stop(t + duree + .02);\n    };\n    const limite = () => {                 // évite l\'effet mitraillette\n      const t = performance.now();\n      if (t - dernier < 55) return false;\n      dernier = t; return true;\n    };\n    return {\n      eveiller: demarrer,\n      survol() { if (ctx && limite()) { const d = 1 + (Math.random() - .5) * .06;\n                 note(1240 * d, 1180 * d, .045, .022, \'triangle\'); } },\n      bouton() { if (ctx && limite()) note(700, 940, .07, .03, \'sine\'); },\n      clic()   { if (ctx) { note(540, 300, .085, .045, \'sine\');\n                 note(1120, 880, .07, .022, \'triangle\'); } },\n      ok()     { if (ctx) { note(660, 990, .12, .035, \'sine\'); } },\n      err()    { if (ctx) { note(340, 190, .16, .04, \'triangle\'); } }\n    };\n  })();\n  [\'pointerdown\', \'keydown\'].forEach(e =>\n    addEventListener(e, () => Son.eveiller(), { once: true }));\n\n  // délégation : les cartes sont reconstruites à chaque rafraîchissement,\n  // poser les écouteurs une fois pour toutes évite de les reposer à chaque fois\n  document.addEventListener(\'pointerover\', e => {\n    const b = e.target.closest(\'button, .cote, .cp-row, .tab-btn\');\n    if (!b || b.disabled) return;\n    if (e.relatedTarget && b.contains(e.relatedTarget)) return;\n    (b.matches(\'.btn, .btn-top, .btn-site\') ? Son.bouton : Son.survol)();\n  });\n  document.addEventListener(\'pointerdown\', e => {\n    const b = e.target.closest(\'button, .cote\');\n    if (b && !b.disabled) Son.clic();\n  });\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    if (kind === \'ok\') Son.ok(); else if (kind === \'err\') Son.err();\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  async function cancelDownload() {\n    const b = document.getElementById(\'btn-cancel\');\n    b.disabled = true;\n    b.textContent = \'annulation...\';\n    try { await api(\'cancel\'); } catch (e) { appendLog(\'Annulation : \' + e, \'err\'); }\n  }\n\n  // visible seulement pendant une action ; l\'arrêt n\'est effectif que si on est\n  // encore en phase de téléchargement (l\'installation, elle, va au bout)\n  function setBusyUI(busy) {\n    const b = document.getElementById(\'btn-cancel\');\n    if (!busy) {\n      b.style.display = \'none\';\n      b.disabled = false;\n      b.textContent = \'annuler le téléchargement\';\n    } else if (b.style.display === \'none\') {\n      b.style.display = \'\';\n    }\n  }\n\n\n\n  // ---- fenêtre de mise à jour -----------------------------------------\n  let majVue = false, majAnim = 0;\n\n  function ouvrirMaj(m) {\n    if (majVue) return;                       // une seule fois par session\n    majVue = true;\n    document.getElementById(\'maj-num\').textContent = m.version;\n    document.getElementById(\'maj-old\').textContent = \'v\' + m.actuelle;\n    document.getElementById(\'maj\').classList.add(\'show\');\n    Son.ok();\n    majFond();\n  }\n\n  function fermerMaj() {\n    document.getElementById(\'maj\').classList.remove(\'show\');\n    cancelAnimationFrame(majAnim);\n    api(\'ignorer_maj\');\n  }\n\n  // fond animé de la fenêtre : des traits qui filent vers le haut, façon\n  // transfert de données. Dessiné sur canvas, arrêté dès la fermeture.\n  function majFond() {\n    const c = document.getElementById(\'maj-fond\');\n    const g = c.getContext(\'2d\');\n    let L, H, traits;\n    const semer = () => {\n      L = c.width = c.offsetWidth; H = c.height = c.offsetHeight;\n      traits = Array.from({ length: Math.min(70, Math.round(L / 16)) }, () => ({\n        x: Math.random() * L, y: Math.random() * H,\n        v: 0.6 + Math.random() * 2.6, l: 12 + Math.random() * 60,\n        rouge: Math.random() < 0.25\n      }));\n    };\n    semer();\n    const pas = () => {\n      g.clearRect(0, 0, L, H);\n      for (const t of traits) {\n        t.y -= t.v;\n        if (t.y + t.l < 0) { t.y = H + t.l; t.x = Math.random() * L; }\n        const grad = g.createLinearGradient(t.x, t.y, t.x, t.y + t.l);\n        const col = t.rouge ? \'216,26,26\' : \'255,255,255\';\n        grad.addColorStop(0, `rgba(${col},${t.rouge ? .55 : .3})`);\n        grad.addColorStop(1, `rgba(${col},0)`);\n        g.strokeStyle = grad; g.lineWidth = t.rouge ? 1.6 : 1;\n        g.beginPath(); g.moveTo(t.x, t.y); g.lineTo(t.x, t.y + t.l); g.stroke();\n      }\n      majAnim = requestAnimationFrame(pas);\n    };\n    pas();\n  }\n\n  // ---- catégories -----------------------------------------------------\n  let filtre = localStorage.getItem(\'modium-cat\') || \'\';   // \'\' = tout afficher\n\n  function renderCotes() {\n    const cats = st?.categories || [];\n    const packs = st?.packs || [];\n    const compte = c => packs.filter(p => (p.categorie || \'\') === c).length;\n    const sans = packs.filter(p => !p.categorie).length;\n\n    // une catégorie effacée entre-temps ne doit pas laisser une grille vide\n    if (filtre && filtre !== \'__sans\' && !cats.includes(filtre)) filtre = \'\';\n\n    const item = (val, libelle, n) => `\n      <button class="cote${filtre === val ? \' on\' : \'\'}" data-cat="${esc(val)}">\n        <span>${esc(libelle)}</span><span class="n">${n}</span>\n      </button>`;\n\n    let html = item(\'\', \'Tous\', packs.length);\n    for (const c of cats) html += item(c, c, compte(c));\n    if (sans && cats.length) html += item(\'__sans\', \'Sans catégorie\', sans);\n\n    const box = document.getElementById(\'cote-liste\');\n    box.innerHTML = html;\n    box.querySelectorAll(\'.cote\').forEach(b => b.onclick = () => {\n      filtre = b.dataset.cat;\n      localStorage.setItem(\'modium-cat\', filtre);\n      refresh();\n    });\n    // la colonne ne sert à rien tant qu\'aucune catégorie n\'existe\n    document.getElementById(\'cotes\').style.display = cats.length ? \'\' : \'none\';\n  }\n\n  function visibles(packs) {\n    if (!filtre) return packs;\n    if (filtre === \'__sans\') return packs.filter(p => !p.categorie);\n    return packs.filter(p => (p.categorie || \'\') === filtre);\n  }\n\n  function renderCats() {\n    const box = document.getElementById(\'cat-list\');\n    const cats = st?.categories || [];\n    if (!cats.length) {\n      box.innerHTML = \'<div class="cp-empty">Aucune catégorie. Crée-en une ci-dessus.</div>\';\n      return;\n    }\n    const n = c => (st?.packs || []).filter(p => (p.categorie || \'\') === c).length;\n    box.innerHTML = cats.map(c => `<div class="cp-row">\n      <div class="cp-n">${esc(c)}</div>\n      <div class="cp-u">${n(c)} pack${n(c) > 1 ? \'s\' : \'\'}</div>\n      <button class="edit" data-ren="${esc(c)}" title="Renommer">Renommer</button>\n      <button data-rmc="${esc(c)}" title="Supprimer la catégorie">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-ren]\').forEach(b => b.onclick = () => {\n      const v = prompt(\'Nouveau nom de la catégorie :\', b.dataset.ren);\n      if (v && v.trim()) api(\'rename_categorie\', b.dataset.ren, v);\n    });\n    box.querySelectorAll(\'button[data-rmc]\').forEach(b => b.onclick = () => {\n      if (confirm(\'Supprimer la catégorie « \' + b.dataset.rmc + \' » ?\\n\\n\'\n                + \'Les packs qui y sont rangés ne sont pas supprimés, ils se \'\n                + \'retrouvent simplement sans catégorie.\'))\n        api(\'remove_categorie\', b.dataset.rmc);\n    });\n  }\n\n  function addCat() {\n    const i = document.getElementById(\'cat-nom\');\n    if (!i.value.trim()) return;\n    api(\'add_categorie\', i.value);\n    i.value = \'\';\n  }\n\n  function majListeCats(garder) {\n    const sel = document.getElementById(\'cp-cat\');\n    const choix = garder !== undefined ? garder : sel.value;\n    const cats = st?.categories || [];\n    sel.innerHTML = \'<option value="">Sans catégorie</option>\'\n      + cats.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join(\'\')\n      + \'<option value="__new">+ Nouvelle catégorie...</option>\';\n    // une catégorie supprimée entre-temps ne doit pas laisser une valeur morte\n    sel.value = cats.includes(choix) ? choix : \'\';\n  }\n\n  // « + Nouvelle catégorie » : on la crée sans quitter le formulaire\n  document.getElementById(\'cp-cat\').addEventListener(\'change\', async function () {\n    if (this.value !== \'__new\') return;\n    const nom = prompt(\'Nom de la nouvelle catégorie :\');\n    this.value = \'\';\n    if (!nom || !nom.trim()) return;\n    await api(\'add_categorie\', nom);\n    st = await api(\'get_state\');\n    majListeCats(nom.trim().replace(/\\s+/g, \' \').slice(0, 40));\n  });\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    renderCotes();\n    majListeCats();\n    const liste = visibles(st.packs);\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = liste.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = liste.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) {\n      renderCustomList(); renderCats();\n    }\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    majListeCats(p.categorie || \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    majListeCats(\'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    const cat = document.getElementById(\'cp-cat\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld, cat.value);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    renderCats();\n    majListeCats();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      setBusyUI(r.busy);\n      if (r.maj) ouvrirMaj(r.maj);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    appendLog(\'Modium v\' + (st?.version || \'?\') + \' démarré.\', \'ok\');\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    api(\'check_update\');   // signale une nouvelle version, sans rien installer\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
CK={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',b,'cancel','check_update','add_categorie','remove_categorie','rename_categorie','ouvrir_maj','ignorer_maj'}
def CL(api):
	M=b'forbidden';K='127.0.0.1';F='text/plain';I=Av.token_urlsafe(16);N=CJ.replace('__TOKEN__',I).encode(U)
	class O(Bb):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(As,ctype);A.send_header(Ao,g(E(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def _host_ok(A):B=(A.headers.get('Host')or C).split(']')[-1];return B.split(':')[0]in(K,'localhost')
		def do_GET(B):
			if not B._host_ok():B._send(403,M,F);return
			if B.path in(Y,'/index.html'):B._send(200,N,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;C=A.path.join(i,E)if E and not E.startswith(Ar)else D
				if C and A.path.exists(C):
					G=A.path.splitext(C)[1].lower()
					with a(C,'rb')as H:B._send(200,H.read(),A_.get(G,'application/octet-stream'))
				else:B._send(404,b'no background',F)
			else:B._send(404,b'not found',F)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if not A._host_ok()or B not in CK or not Av.compare_digest(A.headers.get(BZ)or C,I):A._send(403,M,F);return
			try:
				D=W(A.headers.get(Ao,0))
				if D>1024**2:A._send(413,b'too large',F);return
				E=L.loads(A.rfile.read(D)or b'[]');J=AC(api,B)(*E);A._send(200,L.dumps(J,ensure_ascii=H).encode(U),'application/json; charset=utf-8')
			except G as K:A._send(500,L.dumps({'error':g(K)}).encode(U),AM)
	J=Bc((K,0),O);h.Thread(target=J.serve_forever,daemon=B).start();return J,f"http://127.0.0.1:{J.server_address[1]}/",I
def CM():
	A=AD(B1().get(X,{}))
	try:print('\n'.join(A))
	except G:pass
	r.exit(1 if A else 0)
def CN():
	if'--check-loaded'in r.argv:CM()
	H=CI();I,E,J=CL(H);K=[J];D=Ax.create_window(Bd,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def C(*A):C=' '.join(g(A)for A in A);print(C.encode('ascii',Aj).decode(),flush=B)
		def L():
			F.sleep(4)
			try:import urllib.request as B;H=B.Request(E+'api/poll',data=b'[]',method='POST');H.add_header(BZ,K[0]);I=B.urlopen(H,timeout=5).read()[:80];C('SELFTEST urllib POST:',I)
			except G as A:C('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except G as A:C('SELFTEST inject KO:',A)
			F.sleep(4)
			try:C('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));C('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));C('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except G as A:C('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		h.Thread(target=L,daemon=B).start()
	try:Ax.start(gui='edgechromium')
	finally:I.shutdown()
if __name__=='__main__':CN()