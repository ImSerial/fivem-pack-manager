BI='X-Token'
BH='gofile'
BG='.version'
BF='GTA5.exe'
BE='CitizenFX.ini'
BD='FiveM.app'
BC='image/jpeg'
BB=reversed
BA=ImportError
Ap='background'
Ao='Content-Length'
An='Content-Type'
Am='le téléchargement'
Al='http'
Ak='file'
Aj='_dirs'
Ai='x64'
Ah='.ini'
Ag='replace'
Af='FiveM'
Ae='packs'
Ad='LOCALAPPDATA'
Ac=sorted
Ab=getattr
AK='size'
AJ='application/json'
AI='wb'
AH='gdrive_folder'
AG='purged'
AF='.rpf'
AE='.asi'
AD='plugins'
AC='citizen'
AB='.png'
AA=list
A9=enumerate
A8=dict
A3='custom'
A2='https://'
A1='http://'
A0='packs_key'
z='?'
y='backups'
x='update'
w='mods'
v='r'
u=next
t=bool
q='.'
p=isinstance
l='packs_url'
k='User-Agent'
j='files'
g='{a}'
e='url'
f=str
a='version'
Z='/'
Y=int
X='preview'
W='loaded'
V=ValueError
U='utf-8'
T=OSError
S='image'
R='gta'
Q=RuntimeError
P=open
N='ok'
M=False
K='name'
J='fivem'
G=Exception
F='err'
E=None
D=''
C=len
B=True
import base64 as Aq,json as L,os as A,re as H,secrets,shutil as I,struct as AL,subprocess as Ar,sys,tempfile as BJ,threading as h,urllib.parse,urllib.request,zipfile as As
from http.server import BaseHTTPRequestHandler as BK,ThreadingHTTPServer as BL
import webview as At
BM='FiveM Pack Manager'
m='FiveMPackManager/2.0'
def BN():
	if Ab(sys,'frozen',M):C=A.path.join(A.environ.get(Ad,A.path.dirname(sys.executable)),'FiveMPackManager');A.makedirs(C,exist_ok=B);return C
	return A.path.dirname(A.path.abspath(__file__))
b=BN()
O=A.path.join(b,Ae)
Au=A.path.join(b,'_backups')
AM=A.path.join(b,'state.json')
AN=A.path.join(b,'config.json')
def BO():
	B=[A.path.dirname(A.path.abspath(__file__))]
	if Ab(sys,'_MEIPASS',E):B.insert(0,sys._MEIPASS)
	for D in B:
		C=A.path.join(D,'embedded_config.json')
		if A.path.exists(C):
			try:
				with P(C,v,encoding=U)as F:return L.load(F)
			except(T,L.JSONDecodeError):pass
	return{}
BP=BO()
AO=AB,'.jpg','.jpeg','.webp','.gif'
Av={AB:'image/png','.jpg':BC,'.jpeg':BC,'.webp':'image/webp','.gif':'image/gif'}
def A4():
	B=A8(BP)
	if A.path.exists(AN):
		try:
			with P(AN,v,encoding=U)as C:B.update(L.load(C))
		except(T,L.JSONDecodeError):pass
	return B
def c(**B):
	A=A4();A.update(B)
	with P(AN,'w',encoding=U)as C:L.dump(A,C,indent=2)
def BQ():
	F='fivem_path';C=[];E=A4()
	if E.get(F):C.append(E[F])
	G=A.environ.get(Ad,D);C.append(A.path.join(G,Af,BD))
	for B in C:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,BE))or A.path.isdir(A.path.join(B,AC))):return B
def BR(fivem=E):
	I=fivem;M=A4();C=[M.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(Ad,D),Af,BD))
	for K in J:
		G=A.path.join(K,BE)if K else E
		if G and A.path.exists(G):
			try:
				with P(G,v,encoding=U,errors=Ag)as N:
					for L in N:
						if L.strip().lower().startswith('ivpath='):C.append(L.split('=',1)[1].strip())
			except T:pass
	try:
		import winreg as H
		for O in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,O)as Q:C.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except T:pass
	except BA:pass
	for B in('C:','D:','E:','F:'):C+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in C:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,BF)):return F
def BS():
	if A.path.exists(AM):
		try:
			with P(AM,v,encoding=U)as B:return L.load(B)
		except(T,L.JSONDecodeError):pass
	return{W:{}}
def Aw(state):
	with P(AM,'w',encoding=U)as A:L.dump(state,A,indent=2,ensure_ascii=M)
def AP():A.makedirs(O,exist_ok=B);return Ac(B for B in A.listdir(O)if A.path.isdir(A.path.join(O,B))and not B.startswith(q))
def Bz(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(q)or G and A.path.splitext(E)[0]==X:continue
			yield A.path.relpath(A.path.join(C,D),B)
def BT(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(O,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except T:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
def Ax(pack_name):
	D=A.path.join(O,pack_name)
	for B in AO:
		C=A.path.join(D,X+B)
		if A.path.exists(C):
			try:
				with P(C,'rb')as E:F=Aq.b64encode(E.read()).decode('ascii')
				return f"data:{Av[B]};base64,{F}"
			except T:return
def Ay(name):
	B=A.path.join(O,name,BG)
	if A.path.exists(B):
		try:
			with P(B,v,encoding=U)as C:return C.read().strip()
		except T:pass
def d(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise V(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
def AQ():
	try:
		D=Ar.run(['tasklist','/FO','CSV'],capture_output=B,text=B,creationflags=B7,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			C=A.split('","',1)[0].strip('"')
			if C.startswith('fivempackmanager'):continue
			if C.startswith((J,'gta5')):return B
		return M
	except G:return M
def A5(path,need_bytes,what):
	B=need_bytes;C=I.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise Q(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def B_(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except T:pass
	return B
AR={AC,w,AD}
Az={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto 5','grand theft auto v legacy','gta v legacy','gtav legacy','gta 5 legacy','gta5 legacy','singleplayer','single player',R}
AS={'enbseries','enbcache'}
BU=H.compile('^(enb[\\w .()-]*\\.(ini|dll|asi|fx|fxh|dds|bmp|cfg)|d3d(9|10|11|12)\\.dll|d3dcompiler[\\w.]*\\.dll|dxgi\\.dll)$',H.I)
BV={'.dll',AE,Ah,'.fx','.fxh','.cfg','.json','.yml','.xml'}
def BW(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=w]
		for D in G:
			if D.lower().endswith(AF):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def BX(src,pack_path,rpf_index,log):
	B=A.path.basename(src);D=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in D]
	for(F,G)in A9(H[:-1]):
		if G in(x,Ai):return A.path.join(*D[F:])
		if G=='dlcpacks':return A.path.join(x,Ai,*D[F:])
	E=rpf_index.get(B.lower(),[])
	if C(E)==1:return E[0]
	if C(E)>1:log(f"{B} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return B
def AT(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(q):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
AU={J,'five m','five-m','fivem.app','fivem app','fivem files','five m files','fivem folder'}
AV={'reshade-shaders','reshade-presets'}
def BY(pack_path,log,gta_base=E):
	F=log;E=pack_path;B=[];T=BW(gta_base);H={}
	def G(key,n=1):H[key]=H.get(key,0)+n
	def N(src):B.append((src,J,A.path.join(w,BX(src,E,T,F))));G('rpf vers mods')
	def O(gta_dir,label,prefix=D):
		F=prefix;E=gta_dir
		for(I,K,J)in A.walk(E):
			for C in J:
				if C.startswith(q):continue
				D=A.path.join(I,C)
				if C.lower().endswith(AF):N(D)
				else:H=A.path.relpath(D,E);B.append((D,R,A.path.join(F,H)if F else H));G(f"{label} vers GTA V")
	def P(dirpath,in_fivem=M):
		T='asi vers plugins';I=dirpath;H=in_fivem;K=Ac(A.listdir(I));Q={B.lower()for B in K if A.path.isdir(A.path.join(I,B))};S=A.path.basename(I).lower();H=H or S in AU;U=S in AU or t(Q&(AR|AV));V=not H and(t(Q&AS)or any(A.lower().startswith('enb')and A.lower().endswith(Ah)for A in K));W={A.path.splitext(B)[0].lower()for B in K if B.lower().endswith(AE)}
		for F in K:
			E=A.path.join(I,F);D=F.lower()
			if A.path.isdir(E):
				if D in AR or D in AV:M=C(B);AT(B,E,J,D);G(f"{D} vers FiveM",C(B)-M)
				elif D in Az:O(E,A_(F))
				elif D in AS:
					if H:M=C(B);AT(B,E,J,D);G(f"{D} vers FiveM",C(B)-M)
					else:O(E,A_(F),prefix=D)
				else:P(E,H)
			elif not D.startswith(q):
				L=A.path.splitext(D)[1]
				if L==AF:N(E)
				elif V and BU.match(F):B.append((E,R,F));G('ENB vers GTA V')
				elif L==AE:B.append((E,J,A.path.join(AD,F)));G(T)
				elif L==Ah and A.path.splitext(D)[0]in W:B.append((E,J,A.path.join(AD,F)));G(T)
				elif U and L in BV:B.append((E,J,F));G('racine FiveM')
	P(E)
	if not B:F("Structure standard non détectée — copie de l'archive telle quelle.");AT(B,E,J,D)
	B=[(E,C,B)for(E,C,B)in B if not(C==J and A.path.dirname(B)==D and A.path.splitext(B)[0].lower()==X)];I,K=set(),[]
	for(U,L,Q)in B:
		S=L,Q.lower()
		if S not in I:I.add(S);K.append((U,L,Q))
	V=', '.join(f"{A} : {B}"for(A,B)in H.items())or'rien à installer';F(f"Structure détectée — {V}.");return K
def A_(name):A=name;return A if C(A)<=20 else A[:17]+'...'
def r(e):return(J,e)if p(e,f)else(e[0],e[1])
def AW(target,rel):return f"{target}|{rel}"
def BZ(bases,backup_root,manifest,log):
	M=bases;K=manifest;J=backup_root
	for O in BB(K[j]):
		D,L=r(O);E=M.get(D)
		if not E:continue
		try:
			C=d(E,L)
			if A.path.exists(C):A.remove(C)
			if K[y].get(AW(D,L)):
				H=A.path.join(J,D,L)
				if A.path.exists(H):I.move(H,C)
		except G:pass
	for(D,N)in BB(K.get(AG,[])):
		E=M.get(D)
		if not E:continue
		try:
			C=d(E,N);H=A.path.join(J,Aj,D,N)
			if A.path.exists(H):
				if A.path.isdir(C):I.rmtree(C,ignore_errors=B)
				I.move(H,C)
		except G:pass
	I.rmtree(J,ignore_errors=B);log("Installation annulée — jeu restauré dans son état d'origine.",F)
n={J:Af,R:'GTA V'}
Ba={J:{AC},R:{x,Ai,'redistributables','installers','dlc','_commonredist',w}}
def B0(plan):
	D={}
	for(G,E,F)in plan:
		B=F.replace(Z,A.sep).split(A.sep)
		if C(B)>1:D.setdefault((E,B[0].lower()),B[0])
	return D
def Bb(pack_name,bases,state,log,progress):
	c=state;X=pack_name;S=bases;L=log
	if X in c[W]:raise V('Ce pack est déjà chargé.')
	if AQ():raise Q('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	v=A.path.join(O,X);K=BY(v,L,S.get(R))
	if not K:raise V('Pack vide — aucun fichier à installer.')
	o=[1 for(B,A,C)in K if A==R and not S.get(R)]
	if o:L(f"Dossier GTA V introuvable — {C(o)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);K=[(B,A,C)for(B,A,C)in K if not(A==R and not S.get(R))]
	if not K:raise V('Rien à installer (dossier GTA V non configuré).')
	w=sum(A.path.getsize(B)for(B,C,D)in K if A.path.exists(B));A5(S[J],w,"l'installation");Y={j:[],y:{},AG:[]};Z={}
	for(a,x)in c[W].items():
		if a!=X:
			for p in x[j]:Z[r(p)[0]+'|'+r(p)[1].lower()]=a
	L(f"Installation de « {X} » — {C(K)} fichiers...");h=A.path.join(Au,X);i=0;q=C(K)<=60;z=max(1,C(K)//10)
	try:
		for((H,e),P)in B0(K).items():
			M=S.get(H)
			if H!=J or not M or not A.path.isdir(M):continue
			f=u((A for A in A.listdir(M)if A.lower()==e),E)
			if f and f!=P:
				try:A.rename(A.path.join(M,f),A.path.join(M,P));L(f"Dossier {f} renommé en {P}.")
				except T:pass
		for((H,e),P)in B0(K).items():
			M=S.get(H)
			if not M or e in Ba.get(H,set()):continue
			s=d(M,P)
			if not A.path.isdir(s):continue
			A0=f"{H}|{e}{A.sep}";a=u((B for(A,B)in Z.items()if A.startswith(A0)),E)
			if a:L(f"Dossier {P} : contient des fichiers du pack « {a} » — fusion au lieu du remplacement.");continue
			b=A.path.join(h,Aj,H,P);A.makedirs(A.path.dirname(b),exist_ok=B);I.move(s,b);Y[AG].append([H,P]);L(f"Dossier existant mis de côté ({n[H]}) : {P} — remplacé proprement.")
		for(k,(A1,H,U))in A9(K):
			M=S[H];g=d(M,U);l=H+'|'+U.lower()
			if l in Z:L(f"Attention : {U} appartient déjà au pack « {Z[l]} » — écrasé.")
			A.makedirs(A.path.dirname(g),exist_ok=B)
			if A.path.exists(g)and l not in Z:
				b=A.path.join(h,H,U);A.makedirs(A.path.dirname(b),exist_ok=B);I.copy2(g,b);Y[y][AW(H,U)]=B;i+=1
				if q:L(f"Sauvegarde de l'original ({n[H]}) : {U}")
			I.copy2(A1,g);Y[j].append([H,U])
			if q:L(f"Copie ({n[H]}) : {U}")
			elif(k+1)%z==0:L(f"{k+1}/{C(K)} fichiers copiés ({i} originaux sauvegardés)...")
			progress(k+1,C(K))
	except G as m:L(f"Erreur pendant l'installation : {m}",F);BZ(S,h,Y,L);raise Q(f"Installation échouée ({m}) — tout a été annulé.")from m
	c[W][X]=Y;Aw(c);t=sum(1 for A in Y[j]if r(A)[0]==R);A2=f" (dont {t} dans GTA V)"if t else D;L(f"« {X} » chargé : {C(K)} fichiers copiés{A2}, {i} originaux sauvegardés.",N)
def Bc(pack_name,bases,state,log,progress):
	a=bases;U=state;M=pack_name;G=log;O=U[W].get(M)
	if not O:raise V("Ce pack n'est pas chargé.")
	if AQ():raise Q('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	P=A.path.join(Au,M);J=O[j];b=set();G(f"Désinstallation de « {M} » — {C(J)} fichiers...");S=0;X=C(J)<=60;g=max(1,C(J)//10)
	for(Y,c)in A9(J):
		D,H=r(c);K=a.get(D)
		if not K:G(f"Cible {n.get(D,D)} introuvable — {H} laissé en place.",F);continue
		try:E=d(K,H)
		except V as h:G(f"Entrée ignorée : {h}",F);continue
		if A.path.exists(E):
			A.remove(E)
			if X:G(f"Suppression ({n[D]}) : {H}")
		e,i=A.path.join(P,D,H),A.path.join(P,H);k=O[y].get(AW(D,H))or p(c,f)and O[y].get(H)
		if k:
			R=e if A.path.exists(e)else i
			if A.path.exists(R):
				A.makedirs(A.path.dirname(E),exist_ok=B);I.move(R,E);S+=1
				if X:G(f"Original restauré : {H}")
		if not X and(Y+1)%g==0:G(f"{Y+1}/{C(J)} fichiers retirés ({S} originaux restaurés)...")
		L=A.path.dirname(E)
		while C(L)>C(K):b.add(L);L=A.path.dirname(L)
		progress(Y+1,C(J))
	for L in Ac(b,key=C,reverse=B):
		try:A.rmdir(L)
		except T:pass
	for(D,Z)in O.get(AG,[]):
		K=a.get(D)
		if not K:continue
		try:E=d(K,Z)
		except V:continue
		R=A.path.join(P,Aj,D,Z)
		if A.path.exists(R):
			if A.path.isdir(E):I.rmtree(E,ignore_errors=B)
			I.move(R,E);S+=1;G(f"Dossier original restauré ({n[D]}) : {Z}")
	if A.path.isdir(P):I.rmtree(P,ignore_errors=B)
	del U[W][M];Aw(U);G(f"« {M} » déchargé : {C(J)} fichiers retirés, {S} originaux restaurés.",N)
class AX(G):0
A6=E
def Bd(fn):global A6;A6=fn
def A7():
	if A6 is not E and A6():raise AX('Téléchargement annulé.')
def AY(url,key):
	A=url
	if not key:return A
	B='&'if z in A else z;return f"{A}{B}key={urllib.parse.quote(key)}"
def B1(url,key):A=urllib.request.Request(AY(url,key),headers={k:m});return urllib.request.urlopen(A,timeout=30)
def Be(cfg):
	C=cfg.get(l)
	if not C:return[]
	D=cfg.get(A0)
	with B1(C,D)as G:B=L.loads(G.read().decode(U))
	E=C.rsplit(Z,1)[0]+Z;F=B.get(Ae,B)if p(B,A8)else B
	for A in F:
		if not A.get(e):A[e]=AY(urllib.parse.urljoin(E,A[Ak]),D)
		if A.get(S)and not A[S].startswith((A1,A2,'data:')):A[S]=AY(urllib.parse.urljoin(E,A[S]),D)
	return F
def B2(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return BH,A
	if D in B and'/folders/'in B:
		C=H.search('/folders/([\\w-]+)',A)
		if C:return AH,C.group(1)
	if D in B:
		C=H.search('/file/d/([\\w-]+)',A)or H.search('[?&]id=([\\w-]+)',A)
		if C:return Al,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if z in A else z)+'confirm=t'
	return Al,A
Bf='Mozilla/5.0'
Bg=H.compile('data-id="([\\w-]{20,})"')
Bh=H.compile('<title>([^<]*)</title>')
def AZ(url,rng=E):
	A={k:Bf}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def B3(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def B4(fid):
	with AZ(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(U,Ag)
def Bi(html,fallback):
	B=fallback;C=Bh.search(html)
	if not C:return B
	A=C.group(1).replace('\xa0',' ');A=H.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',D,A).strip();return A or B
def Bj(html,self_id):
	B,C=[],{self_id}
	for A in Bg.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def Bk(fid):
	for J in range(2):
		try:
			with AZ(B3(fid),'bytes=0-0')as A:C=A.headers.get('Content-Disposition',D);K=A.headers.get_content_type();F=A.headers.get('Content-Range',D)
			if'attachment'in C and not K.startswith('text/html'):I=H.search('filename="([^"]+)"',C)or H.search("filename\\*=UTF-8''(.+)",C);L=urllib.parse.unquote(I.group(1))if I else E;N=Y(F.split(Z)[-1])if Z in F else 0;return B,L,N
			return M,E,0
		except urllib.error.HTTPError as O:
			if O.code in(403,429)and J==0:continue
			return E,E,0
		except G:return E,E,0
	return E,E,0
def Bl(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def Aa(seg):A=seg;A=H.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def Bm(folder_id,log):
	B=folder_id;C=[]
	def E(cid,fname,size,prefix):E=prefix;D=fname;B=cid;F=A.path.join(E,Aa(D or B))if E else Aa(D or B);C.append((F,B,size))
	def I(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in Bj(html,fid):
			L,D,F=Bk(B)
			if L:E(B,D,F,C);continue
			try:H=B4(B)
			except G:E(B,D,F,C);continue
			if not Bl(H):E(B,D,F,C);continue
			K=Aa(Bi(H,B));I(B,H,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');I(B,B4(B),D,0);return C
def Bn(folder_id,dest,log,progress):
	G=log;F=dest;D=Bm(folder_id,G)
	if not D:raise Q('Dossier Drive vide ou illisible (accès restreint ?).')
	E=sum(A for(B,C,A)in D);G(f"{C(D)} fichiers dans le dossier"+(f" ({E/1048576:.0f} Mo)."if E else q))
	if E:A5(F,E,Am)
	A.makedirs(F,exist_ok=B);J=0;L=max(1,C(D)//20)
	for(H,(M,N,S))in A9(D):
		A7();K=d(F,M);A.makedirs(A.path.dirname(K),exist_ok=B)
		with AZ(B3(N))as O,P(K,AI)as R:
			while B:
				A7();I=O.read(262144)
				if not I:break
				R.write(I);J+=C(I)
				if E:progress(J,E)
		if(H+1)%L==0 or H+1==C(D):G(f"{H+1}/{C(D)} fichiers téléchargés...")
def Bo(url,log):
	M='status';J='data';O=url.rstrip(Z).split(Z)[-1].split(z)[0]
	def B(u,data=E,headers=E):
		A=data;B={k:m,'Accept':AJ};B.update(headers or{})
		if A is not E:B[An]=AJ;A=L.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return L.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[J]['token']
	try:P=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={k:m}),timeout=30).read().decode();R=H.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',P).group(1)
	except G as D:raise Q(f"Gofile : jeton du site introuvable ({D}).")from D
	A=B(f"https://api.gofile.io/contents/{O}?wt={R}",headers={'Authorization':f"Bearer {C}"})
	if A.get(M)!=N:raise Q(f"Gofile a refusé le lien ({A.get(M)}).")
	S=A[J];T=S.get('children')or{};F=[A for A in T.values()if A.get('type')==Ak]
	if not F:raise Q('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	I=max(F,key=lambda c:c.get(AK,0));return I['link'],{'Cookie':f"accountToken={C}"},I.get(K)
def B5(s):s=s.replace('-','+').replace('_',Z);return Aq.b64decode(s+'='*(-C(s)%4))
def Bp(url,out_path,log,progress):
	N='g';M=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as R,algorithms as S,modes as T
	except BA as b:raise Q('Support Mega indisponible (module cryptography manquant).')from b
	I=H.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or H.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not I:raise Q('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	c,d=I.group(1),I.group(2);A=AL.unpack('>8I',B5(d));U=AL.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);e=AL.pack('>2I',A[4],A[5])+M*8;f=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=L.dumps([{'a':N,N:1,'p':c}]).encode(),headers={An:AJ,k:m});E=L.loads(urllib.request.urlopen(f,timeout=30).read().decode())
	if p(E,Y)or p(E,AA)and p(E[0],Y):raise Q('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	E=E[0];g,F=E[N],Y(E.get('s',0));J='mega_pack'
	try:
		V=R(S.AES(U),T.CBC(M*16)).decryptor();W=V.update(B5(E['at']))+V.finalize()
		if W.startswith(b'MEGA'):J=L.loads(W[4:].split(M)[0].decode())['n']
	except G:pass
	if F:A5(O,Y(F*2.3),Am)
	log(f"Fichier Mega : {J}"+(f" ({F/1048576:.0f} Mo)"if F else D));X=R(S.AES(U),T.CTR(e)).decryptor();Z=0
	with urllib.request.urlopen(urllib.request.Request(g,headers={k:m}),timeout=60)as h,P(out_path,AI)as a:
		while B:
			A7();K=h.read(262144)
			if not K:break
			a.write(X.update(K));Z+=C(K)
			if F:progress(Z,F)
		a.write(X.finalize())
	return J
def B6(pack,cfg,log,progress):
	b=progress;J=log;H=pack;F=A.path.join(O,H[K]);A.makedirs(O,exist_ok=B);p,V=BJ.mkstemp(suffix='.pack',dir=O);A.close(p);M=E
	try:
		J(f"Téléchargement de « {H[K]} »...")
		if AQ():J("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		M,W=B2(H[e]);L=H.get(Ak)
		if M==AH:
			if A.path.isdir(F):I.rmtree(F)
			Bn(W,F,J,b);B9(F,J)
		elif M=='mega':L=Bp(W,V,J,b)or L
		else:
			if M==BH:J('Résolution du lien Gofile...');c,i,q=Bo(W,J);L=L or q
			else:c,i=W,{}
			j={k:m};j.update(i)
			with urllib.request.urlopen(urllib.request.Request(c,headers=j),timeout=60)as R:
				L=R.headers.get_filename()or L or A.path.basename(urllib.parse.urlparse(c).path)
				if R.headers.get_content_type().startswith('text/'):raise Q('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				T=Y(R.headers.get(Ao,0))
				if T:A5(O,Y(T*2.3),Am)
				if L:J(f"Fichier : {L}"+(f" ({T/1048576:.0f} Mo)"if T else D))
				l=0
				with P(V,AI)as r:
					while B:
						A7();d=R.read(262144)
						if not d:break
						r.write(d);l+=C(d)
						if T:b(l,T)
		if M!=AH:
			J(f"Extraction dans le cache local ({H[K]})...")
			if A.path.isdir(F):I.rmtree(F)
			B8(V,F,J);Z=A.listdir(F)
			if C(Z)==1 and A.path.isdir(A.path.join(F,Z[0]))and Z[0].lower()not in(AC,w,AD):
				g=A.path.join(F,Z[0])
				for n in A.listdir(g):I.move(A.path.join(g,n),A.path.join(F,n))
				A.rmdir(g)
			if not Bs(F):B9(F,J)
		if H.get(a):
			with P(A.path.join(F,BG),'w',encoding=U)as h:h.write(f(H[a]))
		if H.get(S)and not Ax(H[K]):
			try:
				with B1(H[S],E)as R:
					o=A.path.splitext(urllib.parse.urlparse(H[S]).path)[1]or AB
					if o.lower()in AO:
						with P(A.path.join(F,X+o.lower()),AI)as h:h.write(R.read())
			except G:pass
		J(f"« {H[K]} » téléchargé et extrait.",N)
	except AX:
		if M==AH and A.path.isdir(F):I.rmtree(F,ignore_errors=B)
		raise
	finally:
		if A.path.exists(V):A.remove(V)
B7=134217728
Bq={'.zip','.rar','.7z'}
o=H.compile('\\.part(\\d+)\\.rar$',H.I)
s=H.compile('\\.r\\d{2}$',H.I)
i=H.compile('\\.(\\d{3})$')
def Br():J='-o{d}';I='7-Zip';H='-inul';G='-ibck';F='WinRAR';E='UnRAR';D='{d}\\';C='-y';B='x';K=[(E,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,g,D]),(E,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,g,D]),(F,['C:\\Program Files\\WinRAR\\WinRAR.exe',B,G,H,C,g,D]),(F,['C:\\Program Files (x86)\\WinRAR\\WinRAR.exe',B,G,H,C,g,D]),(I,['C:\\Program Files\\7-Zip\\7z.exe',B,C,J,g]),(I,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,J,g]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',g,'-C','{d}'])];return[(C,B)for(C,B)in K if A.path.exists(B[0])]
def B8(archive,dest,log):
	D=archive;C=dest;A.makedirs(C,exist_ok=B)
	if As.is_zipfile(D):
		try:
			with As.ZipFile(D)as H:
				for I in H.namelist():
					M=A.path.realpath(A.path.join(C,I))
					if not M.startswith(A.path.realpath(C)+A.sep):raise V(f"Chemin suspect dans l'archive : {I}")
				H.extractall(C)
			return
		except V:raise
		except G as N:log(f"Zip non lisible en natif ({N}) — essai d'un extracteur externe...")
	J=Br()
	if not J:raise Q('Aucun extracteur trouvé — installe WinRAR ou 7-Zip.')
	K=[]
	for(L,E)in J:
		log(f"Extraction avec {L}...");E=[A.replace(g,D).replace('{d}',C)for A in E];F=Ar.run(E,capture_output=B,text=B,creationflags=B7)
		if F.returncode==0:return
		K.append(f"{L} : {(F.stderr or F.stdout).strip()[:200]}")
	raise Q('Échec extraction — '+' | '.join(K))
def B9(dest,log):
	L=log;M=set()
	for S in range(3):
		C=[]
		for(P,T,Q)in A.walk(dest):C+=[A.path.join(P,B)for B in Q if A.path.splitext(B)[1].lower()in Bq or i.search(B)or s.search(B)]
		C=[A for A in C if A not in M]
		if not C:return
		H=[]
		for B in C:
			E=A.path.basename(B)
			if s.search(E):continue
			J=i.search(E)
			if J and J.group(1)!='001':continue
			K=o.search(E)
			if K and Y(K.group(1))>1:continue
			if K:N=o.sub(D,E)
			elif J:O=i.sub(D,E);N=A.path.splitext(O)[0]or O
			else:N=A.path.splitext(E)[0]
			L(f"Archive dans le pack : {E} — extraction...")
			try:B8(B,A.path.join(A.path.dirname(B),N),L)
			except G as R:L(f"Extraction de {E} impossible : {R}",F);M.add(B);continue
			H.append(B)
			if K:I=o.sub(D,B).lower();H+=[A for A in C if A!=B and o.search(A)and o.sub(D,A).lower()==I]
			elif J:I=i.sub(D,B).lower();H+=[A for A in C if A!=B and i.search(A)and i.sub(D,A).lower()==I]
			elif E.lower().endswith('.rar'):I=B[:-4].lower();H+=[A for A in C if s.search(A)and s.sub(D,A).lower()==I]
		for B in C:
			if B in H:
				if A.path.exists(B):A.remove(B)
			elif o.search(B)or s.search(B)or i.search(B):M.add(B)
def Bs(dest):
	C=AR|Az|AU|AV|AS
	for(F,D,E)in A.walk(dest):
		if any(A.lower()in C for A in D):return B
		if any(A.lower().endswith((AF,AE))for A in E):return B
	return M
def Bt():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except G:pass
class Bu:
	def __init__(A):A.state=BS();A.cfg=A4();A.fivem=BQ();A.gta=BR(A.fivem);A.remote_packs=[];A.custom_packs=AA(A.cfg.get('custom_packs',[]));A.background=A.cfg.get(Ap);A.busy=M;A._cancel=h.Event();Bd(A._cancel.is_set);A._lock=h.Lock();A._buf_lock=h.Lock();A._logs=[];A._prog=0,0;A._dirty=M
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=B
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,M
		return{'logs':B,'prog':AA(A._prog),'busy':A.busy,'dirty':C}
	def _all_remote(C):
		D={A[K]:A8(A)for A in C.remote_packs}
		for E in C.custom_packs:A=A8(E);A[A3]=B;D[A[K]]=A
		return AA(D.values())
	def background_url(D):
		B=D.background
		if not B:return
		if B.startswith((A1,A2)):return B
		C=A.path.join(b,B);return f"/bg?{Y(A.path.getmtime(C))}"if A.path.exists(C)else E
	def get_state(A):
		Q='remote';P='image_link';O='nfiles';I=[];L={A[K]:A for A in A._all_remote()}
		for H in AP():F=L.pop(H,E);N=Ay(H);I.append({K:H,AK:BT(H),a:N,W:H in A.state[W],O:C(A.state[W].get(H,{}).get(j,[])),S:Ax(H)or(F or{}).get(S),P:(F or{}).get(S),e:(F or{}).get(e),X:(F or{}).get(X),Q:M,A3:t(F and F.get(A3)),x:t(F and F.get(a)and f(F[a])!=(N or D))})
		for G in L.values():I.append({K:G[K],AK:G.get(AK,D),a:G.get(a),W:M,O:0,S:G.get(S),P:G.get(S),e:G.get(e),X:G.get(X),Q:B,A3:t(G.get(A3)),x:M})
		return{J:A.fivem,R:A.gta,Ae:I,Ap:A.background_url(),l:A.cfg.get(l,D),A0:A.cfg.get(A0,D),'background_setting':A.background or D,'busy':A.busy}
	def open_site(B):A.startfile('https://uxqt.site')
	def add_custom_pack(C,name,url,image,preview=D,old_name=D):
		M=image;L=url;J=preview;H=name;E=old_name;H,L,M=H.strip(),L.strip(),M.strip();J,E=J.strip(),E.strip()
		if not H or not L:C._log('Nom et lien requis pour ajouter un pack.',F);return
		try:B2(L)
		except G as Q:C._log(f"Lien refusé : {Q}",F);return
		if J and not J.startswith((A1,A2)):C._log('Lien preview refusé (il faut un lien http).',F);return
		R={H,E}-{D};C.custom_packs=[A for A in C.custom_packs if A[K]not in R];P={K:H,e:L}
		if M:P[S]=M
		if J:P[X]=J
		C.custom_packs.append(P);c(custom_packs=C.custom_packs)
		if E and E!=H and E in AP():I.rmtree(A.path.join(O,E),ignore_errors=B)
		C._log(f"Pack « {H} » {"modifié"if E else"ajouté"}.",N);C._refresh_ui()
	def preview(C,name):
		D=u((A for A in C._all_remote()if A[K]==name),E);B=(D or{}).get(X)
		if B and B.startswith((A1,A2)):A.startfile(B)
		else:C._log('Pas de preview pour ce pack.',F)
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if C in B.state[W]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[K]!=C];c(custom_packs=B.custom_packs)
		try:D=d(O,C)
		except V:D=E
		if D and A.path.isdir(D):
			try:I.rmtree(D);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",N)
			except T as G:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {G}",F)
		else:B._log(f"Pack « {C} » retiré.",N)
		B._refresh_ui()
	def choose_background(A):return Bt()or D
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=E;c(background=E);C._log('Image de fond retirée.',N)
		elif B.startswith((A1,A2)):C.background=B;c(background=B);C._log('Image de fond (lien) enregistrée.',N)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(b,H))
				except T:pass
			D=A.path.splitext(B)[1].lower();D=D if D in AO else AB;G=Ap+D;I.copy2(B,A.path.join(b,G));C.background=G;c(background=G);C._log('Image de fond enregistrée.',N)
		else:C._log(f"Image introuvable : {B}",F)
	def save_settings(B,url,key,fivem,gta,bg):
		E=fivem;C=gta;B.cfg[l]=url.strip();B.cfg[A0]=key.strip();c(packs_url=B.cfg[l],packs_key=B.cfg[A0]);E=E.strip()
		if E:
			if A.path.isdir(E):B.fivem=E;c(fivem_path=E);B._log(f"Dossier FiveM : {E}",N)
			else:B._log(f"Dossier introuvable : {E}",F)
		C=C.strip()
		if C:
			if A.path.isdir(C)and A.path.exists(A.path.join(C,BF)):B.gta=C;c(gta_path=C);B._log(f"Dossier GTA V : {C}",N)
			else:B._log(f"Dossier GTA V invalide (GTA5.exe absent) : {C}",F)
		if(bg or D).strip()!=(B.background or D):B._set_background(bg or D)
		B._log('Paramètres enregistrés.',N)
		if B.cfg[l]:B.fetch_remote()
		else:B.remote_packs=[];B._refresh_ui()
	def fetch_remote(A):
		if not A.cfg.get(l):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def D():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=Be(A.cfg);A._log(f"{C(A.remote_packs)} pack(s) disponibles en ligne.",N)
			except G as B:A.remote_packs=[];A._log(f"Serveur inaccessible : {B}",F)
			A._refresh_ui()
		h.Thread(target=D,daemon=B).start()
	def _run(A,fn):
		def C():
			with A._lock:
				A._cancel.clear();A.busy=B;A._refresh_ui()
				try:fn()
				except AX as C:A._log(f"{C} Rien n'a été installé.",F)
				except G as C:A._log(f"Erreur : {C}",F)
				finally:A._cancel.clear();A.busy=M;A._prog=0,0;A._refresh_ui()
		h.Thread(target=C,daemon=B).start()
	def cancel(A):
		if not A.busy:return{N:M}
		if not A._cancel.is_set():A._cancel.set();A._log('Annulation demandée, arrêt en cours...')
		return{N:B}
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return M
		return B
	def load(A,name):
		C=name
		if not A._need_fivem():return
		def B():
			B=u((A for A in A._all_remote()if A[K]==C),E);F=C in AP();G=B and B.get(a)and f(B[a])!=(Ay(C)or D)
			if B and(not F or G):B6(B,A.cfg,A._log,A._progress)
			elif not F:raise V('Pack introuvable (ni local, ni sur le serveur).')
			Bb(C,{J:A.fivem,R:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:Bc(name,{J:A.fivem,R:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=u((A for A in A._all_remote()if A[K]==name),E)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:B6(B,A.cfg,A._log,A._progress))
Bv='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que uxqt.site (palette igloo dark) :\n     noir pur, verre translucide, lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  /* le bouton annuler prend le margin auto, "vider" se colle à sa droite */\n  #console-head #btn-cancel + button { margin-left: 14px; }\n  #console-head #btn-cancel { color: var(--err); }\n  #console-head #btn-cancel:hover { color: var(--err); text-decoration: underline; }\n  #console-head #btn-cancel:disabled { color: var(--muted); cursor: default;\n                                       text-decoration: none; }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>FiveM Pack Manager</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">uxqt.site &#8599;</button>\n  </header>\n\n  <main><div class="grid" id="grid"></div><div class="empty" id="empty" style="display:none">\n    Aucun pack disponible.<br>\n    Vérifie la connexion au serveur (bouton Actualiser)<br>\n    ou l\'URL configurée dans Options.\n  </div></main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button id="btn-cancel" style="display:none"\n              onclick="cancelDownload()">annuler le téléchargement</button>\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  async function cancelDownload() {\n    const b = document.getElementById(\'btn-cancel\');\n    b.disabled = true;\n    b.textContent = \'annulation...\';\n    try { await api(\'cancel\'); } catch (e) { appendLog(\'Annulation : \' + e, \'err\'); }\n  }\n\n  // visible seulement pendant une action ; l\'arrêt n\'est effectif que si on est\n  // encore en phase de téléchargement (l\'installation, elle, va au bout)\n  function setBusyUI(busy) {\n    const b = document.getElementById(\'btn-cancel\');\n    if (!busy) {\n      b.style.display = \'none\';\n      b.disabled = false;\n      b.textContent = \'annuler le téléchargement\';\n    } else if (b.style.display === \'none\') {\n      b.style.display = \'\';\n    }\n  }\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = st.packs.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = st.packs.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) renderCustomList();\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      setBusyUI(r.busy);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    appendLog(\'FiveM Pack Manager démarré.\', \'ok\');\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
Bw={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',X,'cancel'}
def Bx(api):
	H='text/plain';D=secrets.token_urlsafe(16);I=Bv.replace('__TOKEN__',D).encode(U)
	class J(BK):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(An,ctype);A.send_header(Ao,f(C(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def do_GET(B):
			if B.path in(Z,'/index.html'):B._send(200,I,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				D=api.background;C=A.path.join(b,D)if D and not D.startswith(Al)else E
				if C and A.path.exists(C):
					F=A.path.splitext(C)[1].lower()
					with P(C,'rb')as G:B._send(200,G.read(),Av.get(F,'application/octet-stream'))
				else:B._send(404,b'no background',H)
			else:B._send(404,b'not found',H)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if B not in Bw or A.headers.get(BI)!=D:A._send(403,b'forbidden',H);return
			try:C=Y(A.headers.get(Ao,0));E=L.loads(A.rfile.read(C)or b'[]');F=Ab(api,B)(*E);A._send(200,L.dumps(F,ensure_ascii=M).encode(U),'application/json; charset=utf-8')
			except G as I:A._send(500,L.dumps({'error':f(I)}).encode(U),AJ)
	F=BL(('127.0.0.1',0),J);h.Thread(target=F.serve_forever,daemon=B).start();return F,f"http://127.0.0.1:{F.server_address[1]}/",D
def By():
	H=Bu();I,E,J=Bx(H);K=[J];D=At.create_window(BM,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def C(*A):C=' '.join(f(A)for A in A);print(C.encode('ascii',Ag).decode(),flush=B)
		def L():
			F.sleep(4)
			try:import urllib.request as B;H=B.Request(E+'api/poll',data=b'[]',method='POST');H.add_header(BI,K[0]);I=B.urlopen(H,timeout=5).read()[:80];C('SELFTEST urllib POST:',I)
			except G as A:C('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except G as A:C('SELFTEST inject KO:',A)
			F.sleep(4)
			try:C('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));C('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));C('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except G as A:C('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		h.Thread(target=L,daemon=B).start()
	try:At.start(gui='edgechromium')
	finally:I.shutdown()
if __name__=='__main__':By()