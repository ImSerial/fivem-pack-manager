Bf='X-Token'
Be='categories'
Bd='gofile'
Bc='Accept'
Bb='Content-Range'
Ba='.version'
BZ='GTA5.exe'
BY='CitizenFX.ini'
BX='FiveM.app'
BW='image/jpeg'
BV='Modium'
BU=reversed
BT=ImportError
Ay='background'
Ax='Content-Type'
Aw='http'
Av='gdrive_folder'
Au='setup'
At='file'
As='Content-Length'
Ar='status'
Aq='_dirs'
Ap='x64'
Ao='.ini'
An='replace'
Am='FiveM'
Al='packs'
Ak='LOCALAPPDATA'
AQ='size'
AP='application/json'
AO='le téléchargement'
AN='purged'
AM='.rpf'
AL='.asi'
AK='plugins'
AJ='citizen'
AI='.png'
AH=enumerate
AG=sorted
AF=getattr
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
r='files'
n='{a}'
m='User-Agent'
l='.'
k='packs_url'
j='categorie'
i=str
h=isinstance
g=dict
d='url'
c='preview'
a='/'
Z='loaded'
Y=open
W='version'
V='utf-8'
U=int
S='image'
R='gta'
Q=ValueError
P='fivem'
O=RuntimeError
N=OSError
L='name'
I='ok'
H=Exception
G='err'
F=False
E=len
D=None
C=''
B=True
import base64 as Az,json as M,os as A,re as J,secrets as A_,shutil as K,struct as A7,subprocess as A8,sys as o,tempfile as Bg,threading as e,time as A9,urllib.error,urllib.parse,urllib.request,zipfile as B0
from http.server import BaseHTTPRequestHandler as Bh,ThreadingHTTPServer as Bi
import webview as B1
AR=BV
AA='3.2.0'
s=f"Modium/{AA}"
AS='ImSerial/modium'
Bj='FiveMPackManager'
def Bk():
	if not AF(o,'frozen',F):return A.path.dirname(A.path.abspath(__file__))
	E=A.environ.get(Ak)or A.path.dirname(o.executable);C=A.path.join(E,BV);D=A.path.join(E,Bj)
	if A.path.isdir(D)and not A.path.isdir(C):
		try:A.rename(D,C)
		except N:return D
	A.makedirs(C,exist_ok=B);return C
f=Bk()
T=A.path.join(f,Al)
B2=A.path.join(f,'_backups')
AT=A.path.join(f,'state.json')
AU=A.path.join(f,'config.json')
Bl={k:'https://modium.xyz/packs-096759e8/packs.json',w:'glt7ExuP7EBzBc56fUzoAmHy618FWBhT'}
def Bm():
	B=g(Bl);C=[A.path.dirname(A.path.abspath(__file__))]
	if AF(o,'_MEIPASS',D):C.insert(0,o._MEIPASS)
	for F in C:
		E=A.path.join(F,'embedded_config.json')
		if A.path.exists(E):
			try:
				with Y(E,'r',encoding=V)as G:B.update(M.load(G))
				break
			except(N,M.JSONDecodeError):pass
	return B
Bn=Bm()
AV=AI,'.jpg','.jpeg','.webp','.gif'
B3={AI:'image/png','.jpg':BW,'.jpeg':BW,'.webp':'image/webp','.gif':'image/gif'}
def B4(path,data):
	C=path+'.tmp'
	with Y(C,'w',encoding=V)as B:M.dump(data,B,indent=2,ensure_ascii=F);B.flush();A.fsync(B.fileno())
	A.replace(C,path)
def AB():
	B=g(Bn)
	if A.path.exists(AU):
		try:
			with Y(AU,'r',encoding=V)as C:B.update(M.load(C))
		except(N,M.JSONDecodeError):pass
	return B
def X(**B):A=AB();A.update(B);B4(AU,A)
def Bo():
	F='fivem_path';D=[];E=AB()
	if E.get(F):D.append(E[F])
	G=A.environ.get(Ak,C);D.append(A.path.join(G,Am,BX))
	for B in D:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,BY))or A.path.isdir(A.path.join(B,AJ))):return B
def Bp(fivem=D):
	I=fivem;M=AB();E=[M.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(Ak,C),Am,BX))
	for K in J:
		G=A.path.join(K,BY)if K else D
		if G and A.path.exists(G):
			try:
				with Y(G,'r',encoding=V,errors=An)as O:
					for L in O:
						if L.strip().lower().startswith('ivpath='):E.append(L.split('=',1)[1].strip())
			except N:pass
	try:
		import winreg as H
		for P in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,P)as Q:E.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except N:pass
	except BT:pass
	for B in('C:','D:','E:','F:'):E+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in E:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,BZ)):return F
def B5():
	if A.path.exists(AT):
		try:
			with Y(AT,'r',encoding=V)as B:return M.load(B)
		except(N,M.JSONDecodeError):pass
	return{Z:{}}
def B6(state):B4(AT,state)
def AW():A.makedirs(T,exist_ok=B);return AG(B for B in A.listdir(T)if A.path.isdir(A.path.join(T,B))and not B.startswith(l))
def CW(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(l)or G and A.path.splitext(E)[0]==c:continue
			yield A.path.relpath(A.path.join(C,D),B)
def Bq(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(T,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except N:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
B7={}
def Br(pack_name):
	G=A.path.join(T,pack_name)
	for E in AV:
		B=A.path.join(G,c+E)
		try:C=A.stat(B)
		except N:continue
		D=B7.get(B)
		if D and D[0]==C.st_mtime and D[1]==C.st_size:return D[2]
		try:
			with Y(B,'rb')as H:I=Az.b64encode(H.read()).decode('ascii')
		except N:return
		F=f"data:{B3[E]};base64,{I}";B7[B]=C.st_mtime,C.st_size,F;return F
def B8(name):
	B=A.path.join(T,name,Ba)
	if A.path.exists(B):
		try:
			with Y(B,'r',encoding=V)as C:return C.read().strip()
		except N:pass
def b(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise Q(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
Bs=J.compile('[<>:"/\\\\|?*\\x00-\\x1f]')
def AC(name):
	D=name;B=(D or C).strip().strip('. ')
	if not B or Bs.search(B)or B in(l,'..')or A.path.isabs(D or C):raise Q(f"Nom de pack invalide : {D!r}")
	return B
def B9(path):
	try:return u(A.lstat(path).st_file_attributes&1024)
	except(N,AttributeError):return A.path.islink(path)
def AX():
	try:
		D=A8.run(['tasklist','/FO','CSV'],capture_output=B,text=B,creationflags=Aj,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			C=A.split('","',1)[0].strip('"')
			if C.startswith(('modium','fivempackmanager')):continue
			if C.startswith((P,'gta5')):return B
		return F
	except H:return F
def z(path,need_bytes,what):
	B=need_bytes;C=K.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise O(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def CX(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except N:pass
	return B
AY={AJ,A3,AK}
BA={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto 5','grand theft auto v legacy','gta v legacy','gtav legacy','gta 5 legacy','gta5 legacy','singleplayer','single player',R}
AZ={'enbseries','enbcache'}
Bt=J.compile('^(enb[\\w .()-]*\\.(ini|dll|asi|fx|fxh|dds|bmp|cfg)|d3d(9|10|11|12)\\.dll|d3dcompiler[\\w.]*\\.dll|dxgi\\.dll)$',J.I)
Bu={'.dll',AL,Ao,'.fx','.fxh','.cfg','.json','.yml','.xml'}
def Bv(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=A3]
		for D in G:
			if D.lower().endswith(AM):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def Bw(src,pack_path,rpf_index,log):
	B=A.path.basename(src);C=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in C]
	for(F,G)in AH(H[:-1]):
		if G in(A4,Ap):return A.path.join(*C[F:])
		if G=='dlcpacks':return A.path.join(A4,Ap,*C[F:])
	D=rpf_index.get(B.lower(),[])
	if E(D)==1:return D[0]
	if E(D)>1:log(f"{B} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return B
def Aa(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(l):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
Ab={P,'five m','five-m','fivem.app','fivem app','fivem files','five m files','fivem folder'}
Ac={'reshade-shaders','reshade-presets'}
def Bx(pack_path,log,gta_base=D):
	D=pack_path;H=log;B=[];T=Bv(gta_base);I={}
	def G(key,n=1):I[key]=I.get(key,0)+n
	def N(src):B.append((src,P,A.path.join(A3,Bw(src,D,T,H))));G('rpf vers mods')
	def O(gta_dir,label,prefix=C):
		F=prefix;E=gta_dir
		for(I,K,J)in A.walk(E):
			for C in J:
				if C.startswith(l):continue
				D=A.path.join(I,C)
				if C.lower().endswith(AM):N(D)
				else:H=A.path.relpath(D,E);B.append((D,R,A.path.join(F,H)if F else H));G(f"{label} vers GTA V")
	def Q(dirpath,in_fivem=F,depth=0):
		V='asi vers plugins';S=depth;J=in_fivem;I=dirpath
		if S>12:H(f"Profondeur maximale atteinte, dossier ignoré : {I}");return
		K=AG(A.listdir(I));T={B.lower()for B in K if A.path.isdir(A.path.join(I,B))};U=A.path.basename(I).lower();J=J or U in Ab;W=U in Ab or u(T&(AY|Ac));X=not J and(u(T&AZ)or any(A.lower().startswith('enb')and A.lower().endswith(Ao)for A in K));Y={A.path.splitext(B)[0].lower()for B in K if B.lower().endswith(AL)}
		for F in K:
			C=A.path.join(I,F);D=F.lower()
			if B9(C):H(f"Lien/jonction ignoré dans le pack : {F}");continue
			if A.path.isdir(C):
				if D in AY or D in Ac:M=E(B);Aa(B,C,P,D);G(f"{D} vers FiveM",E(B)-M)
				elif D in BA:O(C,BB(F))
				elif D in AZ:
					if J:M=E(B);Aa(B,C,P,D);G(f"{D} vers FiveM",E(B)-M)
					else:O(C,BB(F),prefix=D)
				else:Q(C,J,S+1)
			elif not D.startswith(l):
				L=A.path.splitext(D)[1]
				if L==AM:N(C)
				elif X and Bt.match(F):B.append((C,R,F));G('ENB vers GTA V')
				elif L==AL:B.append((C,P,A.path.join(AK,F)));G(V)
				elif L==Ao and A.path.splitext(D)[0]in Y:B.append((C,P,A.path.join(AK,F)));G(V)
				elif W and L in Bu:B.append((C,P,F));G('racine FiveM')
	Q(D)
	if not B:H("Structure standard non détectée — copie de l'archive telle quelle.");Aa(B,D,P,C)
	B=[(E,D,B)for(E,D,B)in B if not(D==P and A.path.dirname(B)==C and A.path.splitext(B)[0].lower()==c)];J,K=set(),[]
	for(U,L,M)in B:
		S=L,M.lower()
		if S not in J:J.add(S);K.append((U,L,M))
	V=', '.join(f"{A} : {B}"for(A,B)in I.items())or'rien à installer';H(f"Structure détectée — {V}.");return K
def BB(name):A=name;return A if E(A)<=20 else A[:17]+'...'
def A0(e):return(P,e)if h(e,i)else(e[0],e[1])
def Ad(target,rel):return f"{target}|{rel}"
def By(bases,backup_root,manifest,log):
	M=bases;J=manifest;I=backup_root
	for O in BU(J[r]):
		D,L=A0(O);E=M.get(D)
		if not E:continue
		try:
			C=b(E,L)
			if A.path.exists(C):A.remove(C)
			if J[A5].get(Ad(D,L)):
				F=A.path.join(I,D,L)
				if A.path.exists(F):K.move(F,C)
		except H:pass
	for(D,N)in BU(J.get(AN,[])):
		E=M.get(D)
		if not E:continue
		try:
			C=b(E,N);F=A.path.join(I,Aq,D,N)
			if A.path.exists(F):
				if A.path.isdir(C):K.rmtree(C,ignore_errors=B)
				K.move(F,C)
		except H:pass
	K.rmtree(I,ignore_errors=B);log("Installation annulée — jeu restauré dans son état d'origine.",G)
p={P:Am,R:'GTA V'}
Bz={P:{AJ},R:{A4,Ap,'redistributables','installers','dlc','_commonredist',A3}}
def BC(plan):
	C={}
	for(G,D,F)in plan:
		B=F.replace(a,A.sep).split(A.sep)
		if E(B)>1:C.setdefault((D,B[0].lower()),B[0])
	return C
def B_(pack_name,bases,state,log,progress):
	e=state;W=pack_name;S=bases;L=log
	if W in e[Z]:raise Q('Ce pack est déjà chargé.')
	if AX():raise O('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	v=b(T,AC(W));J=Bx(v,L,S.get(R))
	if not J:raise Q('Pack vide — aucun fichier à installer.')
	o=[1 for(B,A,C)in J if A==R and not S.get(R)]
	if o:L(f"Dossier GTA V introuvable — {E(o)} fichiers ENB/jeu non installés (indique le dossier dans Options).",G);J=[(B,A,C)for(B,A,C)in J if not(A==R and not S.get(R))]
	if not J:raise Q('Rien à installer (dossier GTA V non configuré).')
	i={}
	for(w,X,A7)in J:
		try:i[X]=i.get(X,0)+A.path.getsize(w)
		except N:pass
	for(X,x)in i.items():
		if S.get(X):z(S[X],x,f"l'installation ({p[X]})")
	Y={r:[],A5:{},AN:[]};a={}
	for(c,y)in e[Z].items():
		if c!=W:
			for q in y[r]:a[A0(q)[0]+'|'+A0(q)[1].lower()]=c
	L(f"Installation de « {W} » — {E(J)} fichiers...");j=A.path.join(B2,W);k=0;s=E(J)<=60;A1=max(1,E(J)//10)
	try:
		for((F,f),U)in BC(J).items():
			M=S.get(F)
			if F!=P or not M or not A.path.isdir(M):continue
			g=A2((A for A in A.listdir(M)if A.lower()==f),D)
			if g and g!=U:
				try:A.rename(A.path.join(M,g),A.path.join(M,U));L(f"Dossier {g} renommé en {U}.")
				except N:pass
		for((F,f),U)in BC(J).items():
			M=S.get(F)
			if not M or f in Bz.get(F,set()):continue
			t=b(M,U)
			if not A.path.isdir(t):continue
			A3=f"{F}|{f}{A.sep}";c=A2((B for(A,B)in a.items()if A.startswith(A3)),D)
			if c:L(f"Dossier {U} : contient des fichiers du pack « {c} » — fusion au lieu du remplacement.");continue
			d=A.path.join(j,Aq,F,U);A.makedirs(A.path.dirname(d),exist_ok=B);K.move(t,d);Y[AN].append([F,U]);L(f"Dossier existant mis de côté ({p[F]}) : {U} — remplacé proprement. Ton contenu précédent est sauvegardé et sera remis au déchargement du pack.")
		for(l,(A4,F,V))in AH(J):
			M=S[F];h=b(M,V);m=F+'|'+V.lower()
			if m in a:L(f"Attention : {V} appartient déjà au pack « {a[m]} » — écrasé.")
			A.makedirs(A.path.dirname(h),exist_ok=B)
			if A.path.exists(h)and m not in a:
				d=A.path.join(j,F,V);A.makedirs(A.path.dirname(d),exist_ok=B);K.copy2(h,d);Y[A5][Ad(F,V)]=B;k+=1
				if s:L(f"Sauvegarde de l'original ({p[F]}) : {V}")
			K.copy2(A4,h);Y[r].append([F,V])
			if s:L(f"Copie ({p[F]}) : {V}")
			elif(l+1)%A1==0:L(f"{l+1}/{E(J)} fichiers copiés ({k} originaux sauvegardés)...")
			progress(l+1,E(J))
	except H as n:L(f"Erreur pendant l'installation : {n}",G);By(S,j,Y,L);raise O(f"Installation échouée ({n}) — tout a été annulé.")from n
	e[Z][W]=Y;B6(e);u=sum(1 for A in Y[r]if A0(A)[0]==R);A6=f" (dont {u} dans GTA V)"if u else C;L(f"« {W} » chargé : {E(J)} fichiers copiés{A6}, {k} originaux sauvegardés.",I)
def C0(pack_name,bases,state,log,progress):
	c=bases;V=state;P=pack_name;F=log;R=V[Z].get(P)
	if not R:raise Q("Ce pack n'est pas chargé.")
	if AX():raise O('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	S=A.path.join(B2,P);J=R[r];d=set();F(f"Désinstallation de « {P} » — {E(J)} fichiers...");U=0;W=E(J)<=60;g=max(1,E(J)//10)
	for(X,e)in AH(J):
		C,H=A0(e);M=c.get(C)
		if not M:F(f"Cible {p.get(C,C)} introuvable — {H} laissé en place.",G);continue
		try:D=b(M,H)
		except Q as j:F(f"Entrée ignorée : {j}",G);continue
		if A.path.exists(D):
			A.remove(D)
			if W:F(f"Suppression ({p[C]}) : {H}")
		f,k=A.path.join(S,C,H),A.path.join(S,H);l=R[A5].get(Ad(C,H))or h(e,i)and R[A5].get(H)
		if l:
			T=f if A.path.exists(f)else k
			if A.path.exists(T):
				A.makedirs(A.path.dirname(D),exist_ok=B);K.move(T,D);U+=1
				if W:F(f"Original restauré : {H}")
		if not W and(X+1)%g==0:F(f"{X+1}/{E(J)} fichiers retirés ({U} originaux restaurés)...")
		Y=A.path.realpath(M);L=A.path.dirname(D)
		while A.path.commonpath([Y,L])==Y and L!=Y:d.add(L);L=A.path.dirname(L)
		progress(X+1,E(J))
	for L in AG(d,key=E,reverse=B):
		try:A.rmdir(L)
		except N:pass
	for(C,a)in R.get(AN,[]):
		M=c.get(C)
		if not M:continue
		try:D=b(M,a)
		except Q:continue
		T=A.path.join(S,Aq,C,a)
		if A.path.exists(T):
			if A.path.isdir(D):K.rmtree(D,ignore_errors=B)
			K.move(T,D);U+=1;F(f"Dossier original restauré ({p[C]}) : {a}")
	if A.path.isdir(S):K.rmtree(S,ignore_errors=B)
	del V[Z][P];B6(V);F(f"« {P} » déchargé : {E(J)} fichiers retirés, {U} originaux restaurés.",I)
class Ae(H):0
AD=D
def C1(fn):global AD;AD=fn
def Af():
	if AD is not D and AD():raise Ae('Téléchargement annulé.')
C2=262144
Ag=4
C3=3
class BD(O):0
def C4(exc):
	A=exc
	if h(A,BD):return F
	if h(A,urllib.error.HTTPError):return A.code in(408,429)or A.code>=500
	return B
def C5(url,headers,offset):
	A=offset;B=g(headers)
	if A:B['Range']=f"bytes={A}-"
	return urllib.request.urlopen(urllib.request.Request(url,headers=B),timeout=60)
def AE(url,out_path,log,progress,headers=D,make_transform=D,align=1,check_space=B,quiet=F):
	X=check_space;W=make_transform;V=out_path;P=log;K=headers;K=g(K or{});K.setdefault(m,s);Z=A.path.dirname(V)or l;F,I,Q,L=0,0,D,0
	while B:
		Af()
		try:
			with C5(url,K,F)as J:
				if F and AF(J,Ar,200)!=206:P('Le serveur ne gère pas la reprise — reprise depuis le début.');F=0
				if Q is D:Q=J.headers.get_filename()
				if F==0 and J.headers.get_content_type().startswith('text/'):raise BD('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				if not I:
					R=J.headers.get(Bb,C)
					if a in R and R.rsplit(a,1)[1].isdigit():I=U(R.rsplit(a,1)[1])
					else:S=J.headers.get(As);I=U(S)+F if S and S.isdigit()else 0
					if I and X and F==0:z(Z,U(I*2.3),AO)
				b=W(F)if W else D
				with Y(V,'r+b'if F else'wb')as T:
					T.seek(F);T.truncate(F);c=F
					while B:
						Af();M=J.read(C2)
						if not M:break
						T.write(b(M)if b else M);F+=E(M)
						if I:progress(F,I)
						elif F-c>=256*1024**2:
							c=F
							if X:z(Z,512*1024**2,AO)
							if not quiet:P(f"{F/1048576:.0f} Mo téléchargés...")
			return Q,I or F
		except Ae:raise
		except H as N:
			if not C4(N):raise
			L+=1
			if L>Ag:raise O(f"Téléchargement échoué après {Ag} reprises ({N})")from N
			F-=F%align;d=C3*L;P(f"Coupure réseau ({N}) — reprise dans {d}s à {F/1048576:.0f} Mo (essai {L}/{Ag}).",G);A9.sleep(d)
def Ah(url,key):
	A=url
	if not key:return A
	B='&'if'?'in A else'?';return f"{A}{B}key={urllib.parse.quote(key)}"
def BE(url,key):A=urllib.request.Request(Ah(url,key),headers={m:s});return urllib.request.urlopen(A,timeout=30)
def C6(cfg):
	C=cfg.get(k)
	if not C:return[]
	D=cfg.get(w)
	with BE(C,D)as G:B=M.loads(G.read().decode(V))
	E=C.rsplit(a,1)[0]+a;H=B.get(Al,B)if h(B,g)else B;F=[]
	for A in H:
		if not h(A,g)or not A.get(L):continue
		try:
			AC(A[L])
			if not A.get(d):A[d]=Ah(urllib.parse.urljoin(E,A[At]),D)
			if A.get(S)and not A[S].startswith((x,y,'data:')):A[S]=Ah(urllib.parse.urljoin(E,A[S]),D)
		except(KeyError,Q,TypeError):continue
		F.append(A)
	return F
def BF(v):return tuple(U(A)for A in J.findall('\\d+',v or C))or(0,)
def C7():
	G=urllib.request.Request(f"https://api.github.com/repos/{AS}/releases/latest",headers={m:s,Bc:'application/vnd.github+json'})
	with urllib.request.urlopen(G,timeout=15)as H:A=M.loads(H.read().decode(V))
	B=(A.get('tag_name')or C).strip()
	if not B:return
	D=C
	for E in A.get('assets',[]):
		F=(E.get(L)or C).lower()
		if F.endswith('.exe')and Au in F:D=E.get('browser_download_url')or C;break
	I=A.get('html_url')or f"https://github.com/{AS}/releases";return B,I,D
def BG(url):A=f"https://github.com/{AS}/releases/download/";return url.startswith(A)and'..'not in url
def BH(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return Bd,A
	if D in B and'/folders/'in B:
		C=J.search('/folders/([\\w-]+)',A)
		if C:return Av,C.group(1)
	if D in B:
		C=J.search('/file/d/([\\w-]+)',A)or J.search('[?&]id=([\\w-]+)',A)
		if C:return Aw,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if'?'in A else'?')+'confirm=t'
	return Aw,A
BI='Mozilla/5.0'
C8=J.compile('data-id="([\\w-]{20,})"')
C9=J.compile('<title>([^<]*)</title>')
def BJ(url,rng=D):
	A={m:BI}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def BK(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def BL(fid):
	with BJ(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(V,An)
def CA(html,fallback):
	B=fallback;D=C9.search(html)
	if not D:return B
	A=D.group(1).replace('\xa0',' ');A=J.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',C,A).strip();return A or B
def CB(html,self_id):
	B,C=[],{self_id}
	for A in C8.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def CC(fid):
	for K in range(2):
		try:
			with BJ(BK(fid),'bytes=0-0')as A:E=A.headers.get('Content-Disposition',C);L=A.headers.get_content_type();G=A.headers.get(Bb,C)
			if'attachment'in E and not L.startswith('text/html'):I=J.search('filename="([^"]+)"',E)or J.search("filename\\*=UTF-8''(.+)",E);M=urllib.parse.unquote(I.group(1))if I else D;N=U(G.split(a)[-1])if a in G else 0;return B,M,N
			return F,D,0
		except urllib.error.HTTPError as O:
			if O.code in(403,429)and K==0:continue
			return D,D,0
		except H:return D,D,0
	return D,D,0
def CD(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def Ai(seg):A=seg;A=J.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def CE(folder_id,log):
	B=folder_id;E=[]
	def D(cid,fname,size,prefix):D=prefix;C=fname;B=cid;F=A.path.join(D,Ai(C or B))if D else Ai(C or B);E.append((F,B,size))
	def I(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in CB(html,fid):
			L,E,F=CC(B)
			if L:D(B,E,F,C);continue
			try:G=BL(B)
			except H:D(B,E,F,C);continue
			if not CD(G):D(B,E,F,C);continue
			K=Ai(CA(G,B));I(B,G,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');I(B,BL(B),C,0);return E
def CF(folder_id,dest,log,progress):
	I=dest;H=log;C=CE(folder_id,H)
	if not C:raise O('Dossier Drive vide ou illisible (accès restreint ?).')
	G=sum(A for(B,C,A)in C);H(f"{E(C)} fichiers dans le dossier"+(f" ({G/1048576:.0f} Mo)."if G else l))
	if G:z(I,G,AO)
	A.makedirs(I,exist_ok=B);K=0;N=max(1,E(C)//20)
	for(J,(P,Q,S))in AH(C):
		Af();L=b(I,P);A.makedirs(A.path.dirname(L),exist_ok=B);M=K;T,R=AE(BK(Q),L,H,lambda cur,tot,_b=M:progress(_b+cur,G)if G else D,headers={m:BI},check_space=F,quiet=B);K=M+R
		if(J+1)%N==0 or J+1==E(C):H(f"{J+1}/{E(C)} fichiers téléchargés...")
def CG(url,log):
	K='data';N=url.rstrip(a).split(a)[-1].split('?')[0]
	def B(u,data=D,headers=D):
		A=data;B={m:s,Bc:AP};B.update(headers or{})
		if A is not D:B[Ax]=AP;A=M.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return M.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[K]['token']
	try:P=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={m:s}),timeout=30).read().decode();Q=J.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',P).group(1)
	except H as E:raise O(f"Gofile ne fonctionne plus avec ce type de lien ({E}). Ré-héberge le pack sur Google Drive ou Mega.")from E
	A=B(f"https://api.gofile.io/contents/{N}?wt={Q}",headers={'Authorization':f"Bearer {C}"})
	if A.get(Ar)!=I:raise O(f"Gofile a refusé le lien ({A.get(Ar)}).")
	R=A[K];S=R.get('children')or{};F=[A for A in S.values()if A.get('type')==At]
	if not F:raise O('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	G=max(F,key=lambda c:c.get(AQ,0));return G['link'],{'Cookie':f"accountToken={C}"},G.get(L)
def BM(s):s=s.replace('-','+').replace('_',a);return Az.b64decode(s+'='*(-E(s)%4))
def CH(url,out_path,log,progress):
	K='g';I=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as L,algorithms as N,modes as P
	except BT as V:raise O('Support Mega indisponible (module cryptography manquant).')from V
	E=J.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or J.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not E:raise O('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	W,X=E.group(1),E.group(2);A=A7.unpack('>8I',BM(X));Q=A7.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);Y=A7.pack('>2I',A[4],A[5])+I*8;Z=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=M.dumps([{'a':K,K:1,'p':W}]).encode(),headers={Ax:AP,m:s});B=M.loads(urllib.request.urlopen(Z,timeout=30).read().decode())
	if h(B,U)or h(B,v)and h(B[0],U):raise O('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	B=B[0];a,D=B[K],U(B.get('s',0));G='mega_pack'
	try:
		R=L(N.AES(Q),P.CBC(I*16)).decryptor();S=R.update(BM(B['at']))+R.finalize()
		if S.startswith(b'MEGA'):G=M.loads(S[4:].split(I)[0].decode())['n']
	except H:pass
	if D:z(T,U(D*2.3),AO)
	log(f"Fichier Mega : {G}"+(f" ({D/1048576:.0f} Mo)"if D else C))
	def b(offset):A=Y[:8]+A7.pack('>Q',offset//16);return L(N.AES(Q),P.CTR(A)).decryptor().update
	AE(a,out_path,log,progress,make_transform=b,align=16,check_space=F);return G
def BN(pack,cfg,log,progress):
	U=progress;J=pack;G=log;X=AC(J[L]);P=b(T,X);F=P+'.part';A.makedirs(T,exist_ok=B);k,N=Bg.mkstemp(suffix='.pack',dir=T);A.close(k);O=D
	try:
		G(f"Téléchargement de « {J[L]} »...")
		if AX():G("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		O,Q=BH(J[d]);M=J.get(At)
		if A.path.isdir(F):K.rmtree(F,ignore_errors=B)
		if O==Av:CF(Q,F,G,U);BR(F,G)
		elif O=='mega':M=CH(Q,N,G,U)or M
		else:
			if O==Bd:G('Résolution du lien Gofile...');Z,f,l=CG(Q,G);M=M or l
			else:Z,f=Q,{}
			m,g=AE(Z,N,G,U,headers=f);M=m or M or A.path.basename(urllib.parse.urlparse(Z).path)
			if M:G(f"Fichier : {M}"+(f" ({g/1048576:.0f} Mo)"if g else C))
		if O!=Av:
			G(f"Extraction dans le cache local ({X})...");BQ(N,F,G);R=A.listdir(F)
			if E(R)==1 and A.path.isdir(A.path.join(F,R[0]))and R[0].lower()not in(AJ,A3,AK):
				a=A.path.join(F,R[0])
				for h in A.listdir(a):K.move(A.path.join(a,h),A.path.join(F,h))
				A.rmdir(a)
			if not CL(F):BR(F,G)
		if J.get(W):
			with Y(A.path.join(F,Ba),'w',encoding=V)as e:e.write(i(J[W]))
		if J.get(S):
			try:
				with BE(J[S],D)as n:
					j=A.path.splitext(urllib.parse.urlparse(J[S]).path)[1]or AI
					if j.lower()in AV:
						with Y(A.path.join(F,c+j.lower()),'wb')as e:e.write(n.read())
			except H:pass
		if A.path.isdir(P):K.rmtree(P)
		A.replace(F,P);G(f"« {X} » téléchargé et extrait.",I)
	except BaseException:K.rmtree(F,ignore_errors=B);raise
	finally:
		if A.path.exists(N):A.remove(N)
Aj=134217728
BO=6
BP=3600
CI={'.zip','.rar','.7z'}
t=J.compile('\\.part(\\d+)\\.rar$',J.I)
A1=J.compile('\\.r\\d{2}$',J.I)
q=J.compile('\\.(\\d{3})$')
def CJ():K='-o{d}';J='7-Zip';I='-inul';H='-ibck';G='WinRAR';F='UnRAR';E='{d}\\';D='-p-';C='-y';B='x';L=[(F,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,D,n,E]),(F,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,D,n,E]),(G,['C:\\Program Files\\WinRAR\\WinRAR.exe',B,H,I,C,D,n,E]),(G,['C:\\Program Files (x86)\\WinRAR\\WinRAR.exe',B,H,I,C,D,n,E]),(J,['C:\\Program Files\\7-Zip\\7z.exe',B,C,'-p',K,n]),(J,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,'-p',K,n]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',n,'-C','{d}'])];return[(C,B)for(C,B)in L if A.path.exists(B[0])]
def BQ(archive,dest,log):
	F=log;E=archive;C=dest;A.makedirs(C,exist_ok=B)
	if B0.is_zipfile(E):
		try:
			with B0.ZipFile(E)as L:
				for M in L.namelist():
					P=A.path.realpath(A.path.join(C,M))
					if not P.startswith(A.path.realpath(C)+A.sep):raise Q(f"Chemin suspect dans l'archive : {M}")
				L.extractall(C)
			return
		except Q:raise
		except H as R:F(f"Zip non lisible en natif ({R}) — essai d'un extracteur externe...")
	N=CJ()
	if not N:raise O('Aucun extracteur trouvé — installe WinRAR ou 7-Zip.')
	I=[]
	for(D,J)in N:
		F(f"Extraction avec {D}...");J=[A.replace(n,E).replace('{d}',C)for A in J]
		try:K=A8.run(J,capture_output=B,text=B,creationflags=Aj,timeout=BP)
		except A8.TimeoutExpired:I.append(f"{D} : abandon après {BP//60} min (archive protégée par mot de passe ?)");F(f"{D} ne répond plus — abandon.",G);continue
		if K.returncode==0:CK(C);return
		I.append(f"{D} : {(K.stderr or K.stdout).strip()[:200]}")
	raise O('Échec extraction — '+' | '.join(I))
def CK(dest):
	for(E,B,F)in A.walk(dest):
		for C in v(B)+v(F):
			D=A.path.join(E,C)
			if B9(D):
				if C in B:B.remove(C);A.rmdir(D)
				else:A.remove(D)
def BR(dest,log):
	L=log;M=set()
	for S in range(3):
		D=[]
		for(P,T,Q)in A.walk(dest):D+=[A.path.join(P,B)for B in Q if A.path.splitext(B)[1].lower()in CI or q.search(B)or A1.search(B)]
		D=[A for A in D if A not in M]
		if not D:return
		F=[]
		for B in D:
			E=A.path.basename(B)
			if A1.search(E):continue
			J=q.search(E)
			if J and J.group(1)!='001':continue
			K=t.search(E)
			if K and U(K.group(1))>1:continue
			if K:N=t.sub(C,E)
			elif J:O=q.sub(C,E);N=A.path.splitext(O)[0]or O
			else:N=A.path.splitext(E)[0]
			L(f"Archive dans le pack : {E} — extraction...")
			try:BQ(B,A.path.join(A.path.dirname(B),N),L)
			except H as R:L(f"Extraction de {E} impossible : {R}",G);M.add(B);continue
			F.append(B)
			if K:I=t.sub(C,B).lower();F+=[A for A in D if A!=B and t.search(A)and t.sub(C,A).lower()==I]
			elif J:I=q.sub(C,B).lower();F+=[A for A in D if A!=B and q.search(A)and q.sub(C,A).lower()==I]
			elif E.lower().endswith('.rar'):I=B[:-4].lower();F+=[A for A in D if A1.search(A)and A1.sub(C,A).lower()==I]
		for B in D:
			if B in F:
				if A.path.exists(B):A.remove(B)
			elif t.search(B)or A1.search(B)or q.search(B):M.add(B)
def CL(dest):
	C=AY|BA|Ab|Ac|AZ
	for(G,D,E)in A.walk(dest):
		if any(A.lower()in C for A in D):return B
		if any(A.lower().endswith((AM,AL))for A in E):return B
	return F
def CM():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except H:pass
class CN:
	def __init__(A):A.state=B5();A.cfg=AB();A.fivem=Bo();A.gta=Bp(A.fivem);A.remote_packs=[];A.custom_packs=v(A.cfg.get('custom_packs',[]));A.categories=[i(A)for A in A.cfg.get(Be,[])];A.background=A.cfg.get(Ay);A.busy=F;A._maj=D;A._fetch_t=.0;A._fetch_en_cours=F;A._cancel=e.Event();C1(A._cancel.is_set);A._lock=e.Lock();A._buf_lock=e.Lock();A._logs=[];A._prog=0,0;A._dirty=F
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=B
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,F
		return{'logs':B,'prog':v(A._prog),'busy':A.busy,'dirty':C,'maj':A._maj}
	def _all_remote(C):
		D={A[L]:g(A)for A in C.remote_packs}
		for E in C.custom_packs:A=g(E);A[A6]=B;D[A[L]]=A
		return v(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((x,y)):return B
		C=A.path.join(f,B);return f"/bg?{U(A.path.getmtime(C))}"if A.path.exists(C)else D
	def get_state(A):
		Q='remote';O='image_link';N='nfiles';J=[];K={A[L]:A for A in A._all_remote()}
		for I in AW():G=K.pop(I,D);M=B8(I);J.append({L:I,AQ:Bq(I),W:M,Z:I in A.state[Z],N:E(A.state[Z].get(I,{}).get(r,[])),S:(G or{}).get(S)or Br(I),O:(G or{}).get(S),d:(G or{}).get(d),c:(G or{}).get(c),Q:F,A6:u(G and G.get(A6)),j:(G or{}).get(j,C),A4:u(G and G.get(W)and i(G[W])!=(M or C))})
		for H in K.values():J.append({L:H[L],AQ:H.get(AQ,C),W:H.get(W),Z:F,N:0,S:H.get(S),O:H.get(S),d:H.get(d),c:H.get(c),Q:B,A6:u(H.get(A6)),j:H.get(j,C),A4:F})
		return{P:A.fivem,R:A.gta,Al:J,Ay:A.background_url(),k:A.cfg.get(k,C),w:A.cfg.get(w,C),'background_setting':A.background or C,'busy':A.busy,W:AA,Be:A.categories}
	def open_site(B):A.startfile('https://modium.xyz')
	def ouvrir_maj(C):
		B=(C._maj or{}).get(d)
		if B and B.startswith('https://github.com/'):A.startfile(B)
	def installer_maj(D):
		E=g(D._maj or{});F=E.get(Au)or C
		if not BG(F):D._log('Installeur indisponible — ouverture de la page.',G);D.ouvrir_maj();return
		if D.busy:D._log('Une opération est en cours — réessaie après.',G);return
		def H():
			G=A.path.join(f,'_maj');A.makedirs(G,exist_ok=B);C=A.path.join(G,'Modium-Setup.exe');D._log(f"Téléchargement de la version {E.get(W)}...");AE(F,C,D._log,D._progress);H=A.path.getsize(C)
			if H<1000000:A.remove(C);raise O('fichier reçu trop petit, téléchargement invalide')
			with Y(C,'rb')as J:
				if J.read(2)!=b'MZ':A.remove(C);raise O("le fichier reçu n'est pas un exécutable")
			D._log(f"Installation de {E.get(W)} — Modium va se fermer et redémarrer.",I);A9.sleep(1.2);A8.Popen([C,'/SILENT','/NORESTART','/CLOSEAPPLICATIONS','/RESTARTAPPLICATIONS'],creationflags=Aj|8);e.Timer(.8,lambda:A._exit(0)).start()
		D._run(H)
	def ignorer_maj(A):A._maj=D
	def add_custom_pack(A,name,url,image,preview=C,old_name=C,categorie=C):
		N=image;M=categorie;J=preview;F=url;E=old_name;D=name;D,F,N=D.strip(),F.strip(),N.strip();J,E=J.strip(),E.strip();M=M.strip()
		if not D or not F:A._log('Nom et lien requis pour ajouter un pack.',G);return
		try:D=AC(D);BH(F)
		except H as P:A._log(f"Refusé : {P}",G);return
		if not F.lower().startswith((x,y)):A._log('Lien refusé : il faut une URL http(s).',G);return
		if J and not J.startswith((x,y)):A._log('Lien preview refusé (il faut un lien http).',G);return
		R={D,E}-{C};A.custom_packs=[A for A in A.custom_packs if A[L]not in R];O={L:D,d:F}
		if N:O[S]=N
		if J:O[c]=J
		if M:
			O[j]=M
			if M not in A.categories:A.categories.append(M);X(categories=A.categories)
		A.custom_packs.append(O);X(custom_packs=A.custom_packs)
		if E and E!=D and E in AW():
			try:K.rmtree(b(T,E),ignore_errors=B)
			except Q:pass
		A._log(f"Pack « {D} » {"modifié"if E else"ajouté"}.",I);A._refresh_ui()
	def add_categorie(B,nom):
		A=nom;A=' '.join(A.split())[:40]
		if not A:return
		if A in B.categories:B._log(f"La catégorie « {A} » existe déjà.",G);return
		B.categories.append(A);X(categories=B.categories);B._log(f"Catégorie « {A} » créée.",I);B._refresh_ui()
	def remove_categorie(A,nom):
		B=nom
		if B not in A.categories:return
		A.categories=[A for A in A.categories if A!=B];E=0
		for F in A.custom_packs:
			if F.get(j)==B:F.pop(j,D);E+=1
		X(categories=A.categories,custom_packs=A.custom_packs);G=f" — {E} pack(s) sans catégorie"if E else C;A._log(f"Catégorie « {B} » supprimée{G}.",I);A._refresh_ui()
	def rename_categorie(A,ancien,nouveau):
		C=ancien;B=nouveau;B=' '.join(B.split())[:40]
		if not B or C not in A.categories or B==C:return
		if B in A.categories:A._log(f"La catégorie « {B} » existe déjà.",G);return
		A.categories=[B if A==C else A for A in A.categories]
		for D in A.custom_packs:
			if D.get(j)==C:D[j]=B
		X(categories=A.categories,custom_packs=A.custom_packs);A._log(f"Catégorie renommée en « {B} ».",I);A._refresh_ui()
	def preview(C,name):
		E=A2((A for A in C._all_remote()if A[L]==name),D);B=(E or{}).get(c)
		if B and B.startswith((x,y)):A.startfile(B)
		else:C._log('Pas de preview pour ce pack.',G)
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",G);return
		if C in B.state[Z]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",G);return
		B.custom_packs=[A for A in B.custom_packs if A[L]!=C];X(custom_packs=B.custom_packs)
		try:E=b(T,C)
		except Q:E=D
		if E and A.path.isdir(E):
			try:K.rmtree(E);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",I)
			except N as F:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {F}",G)
		else:B._log(f"Pack « {C} » retiré.",I)
		B._refresh_ui()
	def choose_background(A):return CM()or C
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=D;X(background=D);C._log('Image de fond retirée.',I)
		elif B.startswith((x,y)):C.background=B;X(background=B);C._log('Image de fond (lien) enregistrée.',I)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(f,H))
				except N:pass
			E=A.path.splitext(B)[1].lower();E=E if E in AV else AI;F=Ay+E;K.copy2(B,A.path.join(f,F));C.background=F;X(background=F);C._log('Image de fond enregistrée.',I)
		else:C._log(f"Image introuvable : {B}",G)
	def save_settings(D,url,key,fivem,gta,bg):
		F=fivem;E=gta;D.cfg[k]=url.strip();D.cfg[w]=key.strip();X(packs_url=D.cfg[k],packs_key=D.cfg[w]);F=F.strip()
		if F:
			if A.path.isdir(F):D.fivem=F;X(fivem_path=F);D._log(f"Dossier FiveM : {F}",I)
			else:D._log(f"Dossier introuvable : {F}",G)
		E=E.strip()
		if E:
			if A.path.isdir(E)and A.path.exists(A.path.join(E,BZ)):D.gta=E;X(gta_path=E);D._log(f"Dossier GTA V : {E}",I)
			else:D._log(f"Dossier GTA V invalide (GTA5.exe absent) : {E}",G)
		if(bg or C).strip()!=(D.background or C):D._set_background(bg or C)
		D._log('Paramètres enregistrés.',I)
		if D.cfg[k]:D.fetch_remote(force=B)
		else:D.remote_packs=[];D._refresh_ui()
	def check_update(D):
		def A():
			try:
				A=C7()
				if A and BF(A[0])>BF(AA):D._maj={W:A[0],d:A[1],Au:A[2]if BG(A[2])else C,'actuelle':AA};D._refresh_ui()
			except H:pass
		e.Thread(target=A,daemon=B).start()
	def fetch_remote(A,force=F):
		C='attente'
		if not A.cfg.get(k):A._log("Pas d'URL de serveur configurée (voir Options).",G);return{I:F,C:0}
		if A._fetch_en_cours:return{I:F,C:1}
		D=BO-(A9.monotonic()-A._fetch_t)
		if not force and D>0:A._log(f"Patiente {D:.0f} s avant de réactualiser.",G);return{I:F,C:U(D)+1}
		A._fetch_en_cours=B
		def J():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=C6(A.cfg);A._log(f"{E(A.remote_packs)} pack(s) disponibles en ligne.",I)
			except H as B:A.remote_packs=[];A._log(f"Serveur inaccessible : {B}",G)
			finally:A._fetch_t=A9.monotonic();A._fetch_en_cours=F
			A._refresh_ui()
		e.Thread(target=J,daemon=B).start();return{I:B,C:BO}
	def _run(A,fn):
		def C():
			if not A._lock.acquire(blocking=F):A._log('Une opération est déjà en cours.',G);return
			try:
				A._cancel.clear();A.busy=B;A._refresh_ui()
				try:fn()
				except Ae as C:A._log(f"{C} Rien n'a été installé.",G)
				except H as C:A._log(f"Erreur : {C}",G)
				finally:A._cancel.clear();A.busy=F;A._prog=0,0;A._refresh_ui()
			finally:A._lock.release()
		e.Thread(target=C,daemon=B).start()
	def cancel(A):
		if not A.busy:return{I:F}
		if not A._cancel.is_set():A._cancel.set();A._log('Annulation demandée, arrêt en cours...')
		return{I:B}
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',G);return F
		return B
	def load(A,name):
		E=name
		if not A._need_fivem():return
		def B():
			B=A2((A for A in A._all_remote()if A[L]==E),D);F=E in AW();G=B and B.get(W)and i(B[W])!=(B8(E)or C)
			if B and(not F or G):BN(B,A.cfg,A._log,A._progress)
			elif not F:raise Q('Pack introuvable (ni local, ni sur le serveur).')
			B_(E,{P:A.fivem,R:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:C0(name,{P:A.fivem,R:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=A2((A for A in A._all_remote()if A[L]==name),D)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",G);return
		A._run(lambda:BN(B,A.cfg,A._log,A._progress))
CO='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que le site : noir pur, verre translucide,\n     lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.12);\n    --glass: rgba(255, 255, 255, 0.035);\n    --glass-hover: rgba(255, 255, 255, 0.07);\n    --err: #ff7a70;\n    /* rouge de la marque, relevé sur le logo */\n    --red: #d81a1a;\n    --red-hi: #ff3d3d;\n    --red-glow: rgba(216, 26, 26, 0.55);\n    --red-soft: rgba(216, 26, 26, 0.14);\n    --ease: cubic-bezier(.22, .68, .28, 1);\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  /* ---- fond animé ---- */\n  .nappe, #champ, .trame {\n    position: fixed; inset: 0; pointer-events: none; z-index: -1;\n  }\n  .nappe { inset: -30% -20%; filter: blur(80px); z-index: -3; }\n  .nappe.a {\n    background: radial-gradient(ellipse 26% 30% at 32% 38%,\n                rgba(216, 26, 26, .13), transparent 65%);\n    animation: derive-a 38s ease-in-out infinite alternate;\n  }\n  .nappe.b {\n    background: radial-gradient(ellipse 24% 26% at 70% 62%,\n                rgba(255, 255, 255, .05), transparent 65%);\n    animation: derive-b 52s ease-in-out infinite alternate;\n  }\n  @keyframes derive-a {\n    0% { transform: translate3d(-6%, -4%, 0) scale(1); }\n    50% { transform: translate3d(8%, 6%, 0) scale(1.16); }\n    100% { transform: translate3d(-3%, 9%, 0) scale(.95); }\n  }\n  @keyframes derive-b {\n    0% { transform: translate3d(5%, 6%, 0) scale(1.05); }\n    50% { transform: translate3d(-8%, -5%, 0) scale(.9); }\n    100% { transform: translate3d(4%, -8%, 0) scale(1.15); }\n  }\n  .trame {\n    z-index: -2;\n    background-image: linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px),\n                      linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px);\n    background-size: 46px 46px;\n    mask-image: radial-gradient(ellipse 85% 65% at 50% 0%, #000 25%, transparent 92%);\n  }\n  #champ { z-index: -1; opacity: .85; }\n\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n    text-shadow: 0 0 14px rgba(255,255,255,.35), 0 0 34px var(--red-glow);\n  }\n  header { position: relative; }\n  /* filet lumineux sous la barre du haut */\n  header::after {\n    content: \'\'; position: absolute; left: 0; right: 0; bottom: -1px; height: 1px;\n    background: linear-gradient(90deg, transparent, var(--red), transparent);\n    opacity: .55;\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 0; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover:not(:disabled) {\n    border-color: var(--red); transform: translateY(-1px);\n    box-shadow: 0 0 20px -6px var(--red-glow);\n  }\n  .btn-top:disabled { opacity: .4; cursor: default; transform: none; }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 0; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow: hidden; }\n  /* ---- colonne des catégories ---- */\n  main { display: flex; gap: 0; }\n  #cotes {\n    width: 176px; flex-shrink: 0; padding: 20px 12px 20px 22px;\n    border-right: 1px solid var(--line); overflow-y: auto;\n  }\n  .cote-t {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted); padding: 0 10px 10px;\n  }\n  .cote {\n    display: flex; align-items: center; gap: 8px; width: 100%;\n    background: none; border: 1px solid transparent; border-radius: 0;\n    color: var(--muted); cursor: pointer; text-align: left;\n    padding: 8px 10px; margin-bottom: 3px; font-size: 12px;\n    transition: background 0.2s, color 0.2s, border-color 0.2s, transform 0.2s;\n  }\n  .cote:hover { background: var(--glass); color: var(--text); transform: translateX(2px); }\n  .cote { position: relative; }\n  .cote.on {\n    background: var(--glass); color: var(--text);\n    border-color: rgba(216, 26, 26, .35);\n  }\n  .cote.on::before {\n    content: \'\'; position: absolute; left: -12px; top: 6px; bottom: 6px; width: 2px;\n    background: var(--red); border-radius: 0;\n    box-shadow: 0 0 12px var(--red-glow), 0 0 24px var(--red-glow);\n  }\n  .cote .n {\n    margin-left: auto; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted);\n  }\n  .zone { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  main > .zone { min-width: 0; }\n  #cotes:empty { display: none; }\n\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .grid { grid-template-columns: repeat(auto-fill, minmax(238px, 1fr)) !important; }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 0; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px); position: relative;\n    transition: border-color .3s, transform .3s var(--ease), box-shadow .3s;\n    animation: entree .5s var(--ease) both;\n  }\n  @keyframes entree {\n    from { opacity: 0; transform: translateY(14px) scale(.97); }\n    to { opacity: 1; transform: none; }\n  }\n  /* reflet qui suit le curseur, comme sur le site */\n  .card::after {\n    content: \'\'; position: absolute; inset: 0; opacity: 0; pointer-events: none;\n    transition: opacity .35s; border-radius: 0; z-index: 2;\n    background: radial-gradient(300px circle at var(--mx, 50%) var(--my, 50%),\n                rgba(216, 26, 26, .16), transparent 70%);\n  }\n  .card:hover {\n    border-color: rgba(216, 26, 26, .45); transform: translateY(-3px);\n    box-shadow: 0 0 34px -12px var(--red-glow), 0 18px 40px -22px #000;\n  }\n  .card:hover::after { opacity: 1; }\n  /* pack installé : anneau rouge qui respire */\n  .card.on {\n    border-color: rgba(216, 26, 26, .55);\n    box-shadow: 0 0 0 1px rgba(216, 26, 26, .18), 0 0 26px -12px var(--red-glow);\n    animation: entree .5s var(--ease) both, respire 3.4s ease-in-out 1s infinite;\n  }\n  @keyframes respire {\n    0%, 100% { box-shadow: 0 0 0 1px rgba(216,26,26,.16), 0 0 22px -14px var(--red-glow); }\n    50% { box-shadow: 0 0 0 1px rgba(216,26,26,.34), 0 0 40px -10px var(--red-glow); }\n  }\n  .thumb {\n    height: 152px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; overflow: hidden;\n  }\n  /* voile bas : le texte posé sur l\'image reste lisible quelle qu\'elle soit */\n  .thumb::after {\n    content: \'\'; position: absolute; inset: 0; pointer-events: none;\n    background: linear-gradient(180deg, rgba(0,0,0,.05) 40%, rgba(0,0,0,.88));\n  }\n  .card:hover .thumb img { transform: scale(1.06); }\n  .thumb img { transition: transform .55s var(--ease); }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 0;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge { z-index: 1; }\n  .badge.on {\n    color: #ff7a7a; border-color: rgba(216, 26, 26, .5);\n    background: rgba(216, 26, 26, .14);\n    box-shadow: 0 0 14px -3px var(--red-glow);\n  }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body {\n    padding: 0 14px 14px; display: flex; flex-direction: column; gap: 9px;\n    margin-top: -42px; position: relative; z-index: 1;\n  }\n  .name {\n    font-size: 14.5px; font-weight: 650; letter-spacing: 0.01em;\n    text-shadow: 0 2px 12px #000, 0 0 22px rgba(0,0,0,.9);\n  }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 0; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) {\n    transform: translateY(-1px);\n    box-shadow: 0 0 22px rgba(255,255,255,.35), 0 0 44px -8px var(--red-glow);\n  }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) {\n    border-color: var(--red); transform: translateY(-1px);\n    box-shadow: 0 0 18px -6px var(--red-glow);\n  }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress { height: 3px; }\n  #progress div {\n    height: 100%; width: 0%; transition: width .1s;\n    background: linear-gradient(90deg, var(--red), var(--red-hi), #fff);\n    box-shadow: 0 0 14px var(--red-glow), 0 0 30px var(--red-glow);\n  }\n  #console-head.actif { color: #ff8a8a; text-shadow: 0 0 14px var(--red-glow); }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  /* le bouton annuler prend le margin auto, "vider" se colle à sa droite */\n  #console-head #btn-cancel + button { margin-left: 14px; }\n  #console-head #btn-cancel { color: var(--err); }\n  #console-head #btn-cancel:hover { color: var(--err); text-decoration: underline; }\n  #console-head #btn-cancel:disabled { color: var(--muted); cursor: default;\n                                       text-decoration: none; }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 0; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n\n  /* ---- fenêtre de mise à jour ---- */\n  /* Reprend la carte de pack telle quelle : même bordure, même rayon, même\n     vignette. Seule la vignette change de contenu — le numéro de version en\n     néon à la place de l\'image. */\n  #maj {\n    position: fixed; inset: 0; z-index: 200; display: none;\n    align-items: center; justify-content: center;\n    background: rgba(0, 0, 0, 0.86); backdrop-filter: blur(7px);\n  }\n  #maj.show { display: flex; animation: majFond .45s ease-out; }\n  @keyframes majFond { from { opacity: 0 } to { opacity: 1 } }\n  #maj-fond { position: absolute; inset: 0; width: 100%; height: 100%; }\n  .maj-carte {\n    position: relative; width: 290px; cursor: default;\n    box-shadow: 0 30px 80px -18px rgba(0, 0, 0, 0.95),\n                0 0 60px -14px rgba(216, 26, 26, 0.5);\n    animation: majCarte .55s cubic-bezier(.2, .8, .25, 1);\n  }\n  .maj-carte:hover { transform: none; }\n  @keyframes majCarte {\n    from { opacity: 0; transform: translateY(24px) scale(.92) }\n    to { opacity: 1; transform: none }\n  }\n  .maj-carte .thumb { height: 132px; }\n  /* La bannière vient du site : la fenêtre ne s\'ouvre que si la vérification\n     de version a abouti, donc la connexion est forcément là. En cas d\'échec\n     l\'image se masque et le numéro reprend toute la place. */\n  .maj-carte .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .maj-carte .thumb::after {\n    content: \'\'; position: absolute; inset: 0;\n    background: linear-gradient(180deg, rgba(0,0,0,.15), rgba(0,0,0,.78));\n  }\n  .maj-carte .maj-v, .maj-carte .badge { position: absolute; z-index: 1; }\n  .maj-carte .maj-v { bottom: 12px; left: 16px; }\n  .maj-carte .badge.cloud {\n    color: #ff6a6a; border-color: rgba(216, 26, 26, 0.5);\n    background: rgba(216, 26, 26, 0.12);\n    animation: majPouls 2.2s ease-in-out infinite;\n  }\n  @keyframes majPouls {\n    0%, 100% { box-shadow: 0 0 10px rgba(216, 26, 26, .25) }\n    50% { box-shadow: 0 0 26px rgba(216, 26, 26, .6) }\n  }\n  .maj-v {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 30px; font-weight: 700; letter-spacing: -0.02em;\n    background-image: linear-gradient(100deg, #fff 20%, #9a9aa4 55%, #fff 85%);\n    background-size: 220% 100%;\n    -webkit-background-clip: text; background-clip: text; color: transparent;\n    animation: majBrille 6s linear infinite;\n    filter: drop-shadow(0 0 16px rgba(255, 255, 255, .32))\n            drop-shadow(0 0 40px rgba(216, 26, 26, .5));\n  }\n  @keyframes majBrille { to { background-position: -220% 0 } }\n  .maj-carte .name { font-size: 15px; }\n  .maj-carte .actions { margin-top: 2px; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 0; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 0; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal select {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 0; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n    cursor: pointer; appearance: none;\n    /* chevron dessiné en fond : la flèche native est grise et hors charte */\n    background-image: url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'10\' height=\'6\'%3E%3Cpath d=\'M1 1l4 4 4-4\' fill=\'none\' stroke=\'%238a8a8e\' stroke-width=\'1.5\' stroke-linecap=\'round\'/%3E%3C/svg%3E");\n    background-repeat: no-repeat; background-position: right 12px center;\n    padding-right: 30px;\n  }\n  #modal select:focus { outline: none; border-color: var(--accent); }\n  #modal select option { background: #101012; color: var(--text); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 0; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 0; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <div class="nappe a"></div><div class="nappe b"></div>\n  <div class="trame"></div><canvas id="champ"></canvas>\n  <header>\n    <h1>Modium</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" id="btn-refresh" onclick="actualiser()">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">modium.xyz &#8599;</button>\n  </header>\n\n  <main>\n    <aside id="cotes">\n      <div class="cote-t">Catégories</div>\n      <div id="cote-liste"></div>\n    </aside>\n    <div class="zone">\n      <div class="grid" id="grid"></div>\n      <div class="empty" id="empty" style="display:none">\n        Aucun pack disponible.<br>\n        Vérifie la connexion au serveur (bouton Actualiser)<br>\n        ou l\'URL configurée dans Options.\n      </div>\n    </div>\n  </main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button id="btn-cancel" style="display:none"\n              onclick="cancelDownload()">annuler le téléchargement</button>\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n\n  <div id="maj">\n    <canvas id="maj-fond"></canvas>\n    <div class="card maj-carte">\n      <div class="thumb">\n        <img id="maj-img" src="https://modium.xyz/assets/banner.png" alt=""\n             onerror="this.style.display=\'none\'">\n        <span class="maj-v" id="maj-num">—</span>\n        <span class="badge cloud">NOUVELLE VERSION</span>\n      </div>\n      <div class="body">\n        <div class="name">Modium <span id="maj-num2">—</span></div>\n        <div class="meta">tu utilises la v<span id="maj-old">—</span></div>\n        <div class="actions">\n          <button class="btn load" id="maj-go" onclick="lancerMaj()">Mettre à jour</button>\n          <button class="btn unload" onclick="fermerMaj()">Plus tard</button>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="cats">Catégories</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <select id="cp-cat" style="margin-top:6px"></select>\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="cats" style="display:none">\n        <label>Nouvelle catégorie</label>\n        <div class="row" style="margin-top:0">\n          <input id="cat-nom" placeholder="Ex : ENB, Thèmes, Réalistes...">\n          <button class="btn dl" style="flex:0 0 120px" onclick="addCat()">Créer</button>\n        </div>\n        <div id="cat-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n\n\n  // ---- fond animé -----------------------------------------------------\n  // Un seul requestAnimationFrame pour tout. Le champ se met en veille quand\n  // une opération tourne : pendant une installation de 10 Go, la machine a\n  // mieux à faire que dessiner des points.\n  (() => {\n    const cv = document.getElementById(\'champ\');\n    const g = cv.getContext(\'2d\', { alpha: true });\n    let L = 0, H = 0, dpr = 1, pts = [], sx = -999, sy = -999, veille = false;\n\n    const semer = () => {\n      dpr = Math.min(devicePixelRatio || 1, 2);\n      L = innerWidth; H = innerHeight;\n      cv.width = L * dpr; cv.height = H * dpr;\n      cv.style.width = L + \'px\'; cv.style.height = H + \'px\';\n      g.setTransform(dpr, 0, 0, dpr, 0, 0);\n      // densité calculée sur l\'aire : un grand écran n\'hérite pas d\'un nuage\n      // proportionnellement plus dense\n      const n = Math.min(60, Math.round(L * H / 26000));\n      pts = Array.from({ length: n }, () => ({\n        x: Math.random() * L, y: Math.random() * H,\n        vx: (Math.random() - .5) * .14, vy: (Math.random() - .5) * .14,\n        r: Math.random() * 1.4 + .4, rouge: Math.random() < .22\n      }));\n    };\n    semer();\n    let t; addEventListener(\'resize\', () => { clearTimeout(t); t = setTimeout(semer, 200); });\n    addEventListener(\'pointermove\', e => { sx = e.clientX; sy = e.clientY; }, { passive: true });\n\n    const pas = () => {\n      requestAnimationFrame(pas);\n      if (veille || document.hidden) return;\n      g.clearRect(0, 0, L, H);\n      for (const p of pts) {\n        p.x += p.vx; p.y += p.vy;\n        const dx = p.x - sx, dy = p.y - sy, d2 = dx * dx + dy * dy;\n        if (d2 < 20000 && d2 > 1) {\n          const f = (1 - d2 / 20000) * .45, d = Math.sqrt(d2);\n          p.x += dx / d * f; p.y += dy / d * f;\n        }\n        if (p.x < -10) p.x = L + 10; else if (p.x > L + 10) p.x = -10;\n        if (p.y < -10) p.y = H + 10; else if (p.y > H + 10) p.y = -10;\n        g.beginPath(); g.arc(p.x, p.y, p.r, 0, 6.2832);\n        g.fillStyle = p.rouge ? \'rgba(216,26,26,.5)\' : \'rgba(255,255,255,.22)\';\n        g.fill();\n      }\n      for (let i = 0; i < pts.length; i++)\n        for (let j = i + 1; j < pts.length; j++) {\n          const a = pts[i], b = pts[j];\n          const dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy;\n          if (d2 > 13000) continue;\n          const o = (1 - d2 / 13000) * .13;\n          g.strokeStyle = (a.rouge || b.rouge)\n            ? \'rgba(216,26,26,\' + o.toFixed(3) + \')\'\n            : \'rgba(255,255,255,\' + (o * .7).toFixed(3) + \')\';\n          g.lineWidth = 1; g.beginPath();\n          g.moveTo(a.x, a.y); g.lineTo(b.x, b.y); g.stroke();\n        }\n    };\n    pas();\n    window.champVeille = v => { veille = v; if (v) g.clearRect(0, 0, L, H); };\n  })();\n\n  // reflet qui suit le curseur dans les cartes\n  addEventListener(\'pointermove\', e => {\n    const c = e.target.closest(\'.card\');\n    if (!c) return;\n    const r = c.getBoundingClientRect();\n    c.style.setProperty(\'--mx\', (e.clientX - r.left) + \'px\');\n    c.style.setProperty(\'--my\', (e.clientY - r.top) + \'px\');\n  }, { passive: true });\n\n  // ---- sons ----------------------------------------------------------\n  // Synthétisés à la volée : aucun fichier à embarquer dans l\'exe. Le\n  // contexte audio ne peut naître qu\'après un geste de l\'utilisateur, règle\n  // des navigateurs — et pywebview embarque un vrai moteur de rendu.\n  const Son = (() => {\n    let ctx = null, master = null, dernier = 0;\n    const demarrer = () => {\n      if (ctx) return;\n      const AC = window.AudioContext || window.webkitAudioContext;\n      if (!AC) return;\n      ctx = new AC();\n      master = ctx.createGain(); master.gain.value = .5;\n      const f = ctx.createBiquadFilter();\n      f.type = \'lowpass\'; f.frequency.value = 5200;\n      master.connect(f); f.connect(ctx.destination);\n    };\n    const note = (f0, f1, duree, vol, forme = \'sine\') => {\n      if (!ctx) return;\n      const t = ctx.currentTime;\n      const o = ctx.createOscillator(), g = ctx.createGain();\n      o.type = forme;\n      o.frequency.setValueAtTime(f0, t);\n      if (f1 !== f0) o.frequency.exponentialRampToValueAtTime(f1, t + duree);\n      // attaque courte mais jamais nulle : à zéro on entend un clic parasite\n      g.gain.setValueAtTime(.0001, t);\n      g.gain.exponentialRampToValueAtTime(vol, t + .006);\n      g.gain.exponentialRampToValueAtTime(.0001, t + duree);\n      o.connect(g); g.connect(master);\n      o.start(t); o.stop(t + duree + .02);\n    };\n    const limite = () => {                 // évite l\'effet mitraillette\n      const t = performance.now();\n      if (t - dernier < 55) return false;\n      dernier = t; return true;\n    };\n    return {\n      eveiller: demarrer,\n      survol() { if (ctx && limite()) { const d = 1 + (Math.random() - .5) * .06;\n                 note(1240 * d, 1180 * d, .045, .022, \'triangle\'); } },\n      bouton() { if (ctx && limite()) note(700, 940, .07, .03, \'sine\'); },\n      clic()   { if (ctx) { note(540, 300, .085, .045, \'sine\');\n                 note(1120, 880, .07, .022, \'triangle\'); } },\n      ok()     { if (ctx) { note(660, 990, .12, .035, \'sine\'); } },\n      err()    { if (ctx) { note(340, 190, .16, .04, \'triangle\'); } }\n    };\n  })();\n  [\'pointerdown\', \'keydown\'].forEach(e =>\n    addEventListener(e, () => Son.eveiller(), { once: true }));\n\n  // délégation : les cartes sont reconstruites à chaque rafraîchissement,\n  // poser les écouteurs une fois pour toutes évite de les reposer à chaque fois\n  document.addEventListener(\'pointerover\', e => {\n    const b = e.target.closest(\'button, .cote, .cp-row, .tab-btn\');\n    if (!b || b.disabled) return;\n    if (e.relatedTarget && b.contains(e.relatedTarget)) return;\n    (b.matches(\'.btn, .btn-top, .btn-site\') ? Son.bouton : Son.survol)();\n  });\n  document.addEventListener(\'pointerdown\', e => {\n    const b = e.target.closest(\'button, .cote\');\n    if (b && !b.disabled) Son.clic();\n  });\n\n  // Le bouton se verrouille pendant le délai imposé par le back-end et\n  // affiche le décompte : sans retour visible, l\'utilisateur reclique.\n  let refreshTimer = 0;\n  async function actualiser() {\n    const b = document.getElementById(\'btn-refresh\');\n    if (b.disabled) return;\n    const r = await api(\'fetch_remote\');\n    verrouiller(b, (r && r.attente) ? r.attente : 6);\n  }\n\n  function verrouiller(b, secondes) {\n    clearInterval(refreshTimer);\n    b.disabled = true;\n    let reste = secondes;\n    const peindre = () => { b.textContent = reste > 0 ? \'Actualiser (\' + reste + \')\' : \'Actualiser\'; };\n    peindre();\n    refreshTimer = setInterval(() => {\n      reste -= 1;\n      if (reste <= 0) { clearInterval(refreshTimer); b.disabled = false; }\n      peindre();\n    }, 1000);\n  }\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    if (kind === \'ok\') Son.ok(); else if (kind === \'err\') Son.err();\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  async function cancelDownload() {\n    const b = document.getElementById(\'btn-cancel\');\n    b.disabled = true;\n    b.textContent = \'annulation...\';\n    try { await api(\'cancel\'); } catch (e) { appendLog(\'Annulation : \' + e, \'err\'); }\n  }\n\n  // visible seulement pendant une action ; l\'arrêt n\'est effectif que si on est\n  // encore en phase de téléchargement (l\'installation, elle, va au bout)\n  function setBusyUI(busy) {\n    const b = document.getElementById(\'btn-cancel\');\n    if (!busy) {\n      b.style.display = \'none\';\n      b.disabled = false;\n      b.textContent = \'annuler le téléchargement\';\n    } else if (b.style.display === \'none\') {\n      b.style.display = \'\';\n    }\n  }\n\n\n\n  // ---- fenêtre de mise à jour -----------------------------------------\n  let majVue = false, majAnim = 0;\n\n  function ouvrirMaj(m) {\n    if (majVue) return;                       // une seule fois par session\n    majVue = true;\n    const v = String(m.version).replace(/^v/, \'\');\n    document.getElementById(\'maj-num\').textContent = v;\n    document.getElementById(\'maj-num2\').textContent = v;\n    document.getElementById(\'maj-old\').textContent = m.actuelle;\n    document.getElementById(\'maj\').classList.add(\'show\');\n    Son.ok();\n    majFond();\n  }\n\n  async function lancerMaj() {\n    const b = document.getElementById(\'maj-go\');\n    b.disabled = true;\n    b.textContent = \'Téléchargement...\';\n    document.getElementById(\'maj\').classList.remove(\'show\');\n    cancelAnimationFrame(majAnim);\n    // la console reprend la main : la progression y est visible\n    await api(\'installer_maj\');\n  }\n\n  function fermerMaj() {\n    document.getElementById(\'maj\').classList.remove(\'show\');\n    cancelAnimationFrame(majAnim);\n    api(\'ignorer_maj\');\n  }\n\n  // fond animé de la fenêtre : des traits qui filent vers le haut, façon\n  // transfert de données. Dessiné sur canvas, arrêté dès la fermeture.\n  function majFond() {\n    const c = document.getElementById(\'maj-fond\');\n    const g = c.getContext(\'2d\');\n    let L, H, traits;\n    const semer = () => {\n      L = c.width = c.offsetWidth; H = c.height = c.offsetHeight;\n      traits = Array.from({ length: Math.min(70, Math.round(L / 16)) }, () => ({\n        x: Math.random() * L, y: Math.random() * H,\n        v: 0.6 + Math.random() * 2.6, l: 12 + Math.random() * 60,\n        rouge: Math.random() < 0.25\n      }));\n    };\n    semer();\n    const pas = () => {\n      g.clearRect(0, 0, L, H);\n      for (const t of traits) {\n        t.y -= t.v;\n        if (t.y + t.l < 0) { t.y = H + t.l; t.x = Math.random() * L; }\n        const grad = g.createLinearGradient(t.x, t.y, t.x, t.y + t.l);\n        const col = t.rouge ? \'216,26,26\' : \'255,255,255\';\n        grad.addColorStop(0, `rgba(${col},${t.rouge ? .55 : .3})`);\n        grad.addColorStop(1, `rgba(${col},0)`);\n        g.strokeStyle = grad; g.lineWidth = t.rouge ? 1.6 : 1;\n        g.beginPath(); g.moveTo(t.x, t.y); g.lineTo(t.x, t.y + t.l); g.stroke();\n      }\n      majAnim = requestAnimationFrame(pas);\n    };\n    pas();\n  }\n\n  // ---- catégories -----------------------------------------------------\n  let filtre = localStorage.getItem(\'modium-cat\') || \'\';   // \'\' = tout afficher\n\n  function renderCotes() {\n    const cats = st?.categories || [];\n    const packs = st?.packs || [];\n    const compte = c => packs.filter(p => (p.categorie || \'\') === c).length;\n    const sans = packs.filter(p => !p.categorie).length;\n\n    // une catégorie effacée entre-temps ne doit pas laisser une grille vide\n    if (filtre && filtre !== \'__sans\' && !cats.includes(filtre)) filtre = \'\';\n\n    const item = (val, libelle, n) => `\n      <button class="cote${filtre === val ? \' on\' : \'\'}" data-cat="${esc(val)}">\n        <span>${esc(libelle)}</span><span class="n">${n}</span>\n      </button>`;\n\n    let html = item(\'\', \'Tous\', packs.length);\n    for (const c of cats) html += item(c, c, compte(c));\n    if (sans && cats.length) html += item(\'__sans\', \'Sans catégorie\', sans);\n\n    const box = document.getElementById(\'cote-liste\');\n    box.innerHTML = html;\n    box.querySelectorAll(\'.cote\').forEach(b => b.onclick = () => {\n      filtre = b.dataset.cat;\n      localStorage.setItem(\'modium-cat\', filtre);\n      refresh();\n    });\n    // la colonne ne sert à rien tant qu\'aucune catégorie n\'existe\n    document.getElementById(\'cotes\').style.display = cats.length ? \'\' : \'none\';\n  }\n\n  function visibles(packs) {\n    if (!filtre) return packs;\n    if (filtre === \'__sans\') return packs.filter(p => !p.categorie);\n    return packs.filter(p => (p.categorie || \'\') === filtre);\n  }\n\n  function renderCats() {\n    const box = document.getElementById(\'cat-list\');\n    const cats = st?.categories || [];\n    if (!cats.length) {\n      box.innerHTML = \'<div class="cp-empty">Aucune catégorie. Crée-en une ci-dessus.</div>\';\n      return;\n    }\n    const n = c => (st?.packs || []).filter(p => (p.categorie || \'\') === c).length;\n    box.innerHTML = cats.map(c => `<div class="cp-row">\n      <div class="cp-n">${esc(c)}</div>\n      <div class="cp-u">${n(c)} pack${n(c) > 1 ? \'s\' : \'\'}</div>\n      <button class="edit" data-ren="${esc(c)}" title="Renommer">Renommer</button>\n      <button data-rmc="${esc(c)}" title="Supprimer la catégorie">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-ren]\').forEach(b => b.onclick = () => {\n      const v = prompt(\'Nouveau nom de la catégorie :\', b.dataset.ren);\n      if (v && v.trim()) api(\'rename_categorie\', b.dataset.ren, v);\n    });\n    box.querySelectorAll(\'button[data-rmc]\').forEach(b => b.onclick = () => {\n      if (confirm(\'Supprimer la catégorie « \' + b.dataset.rmc + \' » ?\\n\\n\'\n                + \'Les packs qui y sont rangés ne sont pas supprimés, ils se \'\n                + \'retrouvent simplement sans catégorie.\'))\n        api(\'remove_categorie\', b.dataset.rmc);\n    });\n  }\n\n  function addCat() {\n    const i = document.getElementById(\'cat-nom\');\n    if (!i.value.trim()) return;\n    api(\'add_categorie\', i.value);\n    i.value = \'\';\n  }\n\n  function majListeCats(garder) {\n    const sel = document.getElementById(\'cp-cat\');\n    const choix = garder !== undefined ? garder : sel.value;\n    const cats = st?.categories || [];\n    sel.innerHTML = \'<option value="">Sans catégorie</option>\'\n      + cats.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join(\'\')\n      + \'<option value="__new">+ Nouvelle catégorie...</option>\';\n    // une catégorie supprimée entre-temps ne doit pas laisser une valeur morte\n    sel.value = cats.includes(choix) ? choix : \'\';\n  }\n\n  // « + Nouvelle catégorie » : on la crée sans quitter le formulaire\n  document.getElementById(\'cp-cat\').addEventListener(\'change\', async function () {\n    if (this.value !== \'__new\') return;\n    const nom = prompt(\'Nom de la nouvelle catégorie :\');\n    this.value = \'\';\n    if (!nom || !nom.trim()) return;\n    await api(\'add_categorie\', nom);\n    st = await api(\'get_state\');\n    majListeCats(nom.trim().replace(/\\s+/g, \' \').slice(0, 40));\n  });\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    renderCotes();\n    majListeCats();\n    const liste = visibles(st.packs);\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = liste.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = liste.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) {\n      renderCustomList(); renderCats();\n    }\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    majListeCats(p.categorie || \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    majListeCats(\'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    const cat = document.getElementById(\'cp-cat\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld, cat.value);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    renderCats();\n    majListeCats();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      setBusyUI(r.busy);\n    document.getElementById(\'console-head\').classList.toggle(\'actif\', r.busy);\n    if (window.champVeille) window.champVeille(r.busy);\n      if (r.maj) ouvrirMaj(r.maj);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    appendLog(\'Modium v\' + (st?.version || \'?\') + \' démarré.\', \'ok\');\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    verrouiller(document.getElementById(\'btn-refresh\'), 6);\n    api(\'check_update\');   // signale une nouvelle version, sans rien installer\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
CP={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',c,'cancel','check_update','add_categorie','remove_categorie','rename_categorie','ouvrir_maj','ignorer_maj','installer_maj'}
def CQ(api):
	L=b'forbidden';K='127.0.0.1';G='text/plain';I=A_.token_urlsafe(16);N=CO.replace('__TOKEN__',I).encode(V)
	class O(Bh):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(Ax,ctype);A.send_header(As,i(E(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def _host_ok(A):B=(A.headers.get('Host')or C).split(']')[-1];return B.split(':')[0]in(K,'localhost')
		def do_GET(B):
			if not B._host_ok():B._send(403,L,G);return
			if B.path in(a,'/index.html'):B._send(200,N,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;C=A.path.join(f,E)if E and not E.startswith(Aw)else D
				if C and A.path.exists(C):
					F=A.path.splitext(C)[1].lower()
					with Y(C,'rb')as H:B._send(200,H.read(),B3.get(F,'application/octet-stream'))
				else:B._send(404,b'no background',G)
			else:B._send(404,b'not found',G)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if not A._host_ok()or B not in CP or not A_.compare_digest(A.headers.get(Bf)or C,I):A._send(403,L,G);return
			try:
				D=U(A.headers.get(As,0))
				if D>1024**2:A._send(413,b'too large',G);return
				E=M.loads(A.rfile.read(D)or b'[]');J=AF(api,B)(*E);A._send(200,M.dumps(J,ensure_ascii=F).encode(V),'application/json; charset=utf-8')
			except H as K:A._send(500,M.dumps({'error':i(K)}).encode(V),AP)
	J=Bi((K,0),O);e.Thread(target=J.serve_forever,daemon=B).start();return J,f"http://127.0.0.1:{J.server_address[1]}/",I
def CR():
	A=AG(B5().get(Z,{}))
	try:print('\n'.join(A))
	except H:pass
	o.exit(1 if A else 0)
BS=D
def CS():
	global BS
	try:import ctypes as C;A=C.windll.kernel32;BS=A.CreateMutexW(D,F,'Modium.instance.unique');return A.GetLastError()!=183
	except H:return B
def CT():
	try:
		import ctypes as E;A=E.windll.user32;C=A.FindWindowW(D,AR)
		if not C:return F
		A.ShowWindow(C,9);A.SetForegroundWindow(C);return B
	except H:return F
def CU(message):
	try:import ctypes as A;A.windll.user32.MessageBoxW(0,message,AR,64)
	except H:pass
def CV():
	if'--check-loaded'in o.argv:CR()
	if not CS():
		if not CT():CU("Modium est déjà en cours d'exécution.\n\nSi tu ne vois pas la fenêtre, regarde dans la barre des tâches, ou termine le processus Modium.exe depuis le Gestionnaire des tâches.")
		o.exit(0)
	G=CN();I,E,J=CQ(G);K=[J];D=B1.create_window(AR,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def C(*A):C=' '.join(i(A)for A in A);print(C.encode('ascii',An).decode(),flush=B)
		def L():
			F.sleep(4)
			try:import urllib.request as B;G=B.Request(E+'api/poll',data=b'[]',method='POST');G.add_header(Bf,K[0]);I=B.urlopen(G,timeout=5).read()[:80];C('SELFTEST urllib POST:',I)
			except H as A:C('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except H as A:C('SELFTEST inject KO:',A)
			F.sleep(4)
			try:C('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));C('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));C('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except H as A:C('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		e.Thread(target=L,daemon=B).start()
	try:B1.start(gui='edgechromium')
	finally:I.shutdown()
if __name__=='__main__':CV()