Bb='X-Token'
Ba='categories'
BZ='gofile'
BY='Accept'
BX='Content-Range'
BW='.version'
BV='GTA5.exe'
BU='CitizenFX.ini'
BT='FiveM.app'
BS='image/jpeg'
BR='Modium'
BQ=reversed
BP=ImportError
Aw='background'
Av='Content-Type'
Au='http'
At='gdrive_folder'
As='setup'
Ar='file'
Aq='Content-Length'
Ap='status'
Ao='_dirs'
An='x64'
Am='.ini'
Al='replace'
Ak='FiveM'
Aj='packs'
Ai='LOCALAPPDATA'
AP='size'
AO='application/json'
AN='le téléchargement'
AM='purged'
AL='.rpf'
AK='.asi'
AJ='plugins'
AI='citizen'
AH='.png'
AG=enumerate
AF=sorted
AE=getattr
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
j='categorie'
i=str
h=isinstance
g=dict
d='url'
c='preview'
a='/'
Z='loaded'
Y=int
X=open
V='version'
U='utf-8'
S='image'
R='gta'
Q=ValueError
P='fivem'
O=RuntimeError
N=OSError
L='name'
J='ok'
H=False
G=Exception
F='err'
E=len
D=None
C=True
B=''
import base64 as Ax,json as M,os as A,re as I,secrets as Ay,shutil as K,struct as A7,subprocess as A8,sys as r,tempfile as Bc,threading as e,time,urllib.error,urllib.parse,urllib.request,zipfile as Az
from http.server import BaseHTTPRequestHandler as Bd,ThreadingHTTPServer as Be
import webview as A_
Bf=BR
A9='3.1.1'
s=f"Modium/{A9}"
AQ='ImSerial/modium'
Bg='FiveMPackManager'
def Bh():
	if not AE(r,'frozen',H):return A.path.dirname(A.path.abspath(__file__))
	E=A.environ.get(Ai)or A.path.dirname(r.executable);B=A.path.join(E,BR);D=A.path.join(E,Bg)
	if A.path.isdir(D)and not A.path.isdir(B):
		try:A.rename(D,B)
		except N:return D
	A.makedirs(B,exist_ok=C);return B
f=Bh()
T=A.path.join(f,Aj)
B0=A.path.join(f,'_backups')
AR=A.path.join(f,'state.json')
AS=A.path.join(f,'config.json')
Bi={k:'https://modium.xyz/packs-096759e8/packs.json',w:'glt7ExuP7EBzBc56fUzoAmHy618FWBhT'}
def Bj():
	B=g(Bi);C=[A.path.dirname(A.path.abspath(__file__))]
	if AE(r,'_MEIPASS',D):C.insert(0,r._MEIPASS)
	for F in C:
		E=A.path.join(F,'embedded_config.json')
		if A.path.exists(E):
			try:
				with X(E,'r',encoding=U)as G:B.update(M.load(G))
				break
			except(N,M.JSONDecodeError):pass
	return B
Bk=Bj()
AT=AH,'.jpg','.jpeg','.webp','.gif'
B1={AH:'image/png','.jpg':BS,'.jpeg':BS,'.webp':'image/webp','.gif':'image/gif'}
def B2(path,data):
	C=path+'.tmp'
	with X(C,'w',encoding=U)as B:M.dump(data,B,indent=2,ensure_ascii=H);B.flush();A.fsync(B.fileno())
	A.replace(C,path)
def AA():
	B=g(Bk)
	if A.path.exists(AS):
		try:
			with X(AS,'r',encoding=U)as C:B.update(M.load(C))
		except(N,M.JSONDecodeError):pass
	return B
def W(**B):A=AA();A.update(B);B2(AS,A)
def Bl():
	F='fivem_path';D=[];E=AA()
	if E.get(F):D.append(E[F])
	G=A.environ.get(Ai,B);D.append(A.path.join(G,Ak,BT))
	for C in D:
		if C and A.path.isdir(C)and(A.path.exists(A.path.join(C,BU))or A.path.isdir(A.path.join(C,AI))):return C
def Bm(fivem=D):
	I=fivem;M=AA();E=[M.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(Ai,B),Ak,BT))
	for K in J:
		G=A.path.join(K,BU)if K else D
		if G and A.path.exists(G):
			try:
				with X(G,'r',encoding=U,errors=Al)as O:
					for L in O:
						if L.strip().lower().startswith('ivpath='):E.append(L.split('=',1)[1].strip())
			except N:pass
	try:
		import winreg as H
		for P in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,P)as Q:E.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except N:pass
	except BP:pass
	for C in('C:','D:','E:','F:'):E+=[C+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',C+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',C+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',C+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',C+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',C+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',C+'\\Program Files\\Epic Games\\GTAV']
	for F in E:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,BV)):return F
def B3():
	if A.path.exists(AR):
		try:
			with X(AR,'r',encoding=U)as B:return M.load(B)
		except(N,M.JSONDecodeError):pass
	return{Z:{}}
def B4(state):B2(AR,state)
def AU():A.makedirs(T,exist_ok=C);return AF(B for B in A.listdir(T)if A.path.isdir(A.path.join(T,B))and not B.startswith(l))
def CQ(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(l)or G and A.path.splitext(E)[0]==c:continue
			yield A.path.relpath(A.path.join(C,D),B)
def Bn(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(T,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except N:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
B5={}
def Bo(pack_name):
	G=A.path.join(T,pack_name)
	for E in AT:
		B=A.path.join(G,c+E)
		try:C=A.stat(B)
		except N:continue
		D=B5.get(B)
		if D and D[0]==C.st_mtime and D[1]==C.st_size:return D[2]
		try:
			with X(B,'rb')as H:I=Ax.b64encode(H.read()).decode('ascii')
		except N:return
		F=f"data:{B1[E]};base64,{I}";B5[B]=C.st_mtime,C.st_size,F;return F
def B6(name):
	B=A.path.join(T,name,BW)
	if A.path.exists(B):
		try:
			with X(B,'r',encoding=U)as C:return C.read().strip()
		except N:pass
def b(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise Q(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
Bp=I.compile('[<>:"/\\\\|?*\\x00-\\x1f]')
def AB(name):
	D=name;C=(D or B).strip().strip('. ')
	if not C or Bp.search(C)or C in(l,'..')or A.path.isabs(D or B):raise Q(f"Nom de pack invalide : {D!r}")
	return C
def B7(path):
	try:return u(A.lstat(path).st_file_attributes&1024)
	except(N,AttributeError):return A.path.islink(path)
def AV():
	try:
		D=A8.run(['tasklist','/FO','CSV'],capture_output=C,text=C,creationflags=Ah,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			B=A.split('","',1)[0].strip('"')
			if B.startswith(('modium','fivempackmanager')):continue
			if B.startswith((P,'gta5')):return C
		return H
	except G:return H
def z(path,need_bytes,what):
	B=need_bytes;C=K.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise O(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def CR(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except N:pass
	return B
AW={AI,A3,AJ}
B8={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto 5','grand theft auto v legacy','gta v legacy','gtav legacy','gta 5 legacy','gta5 legacy','singleplayer','single player',R}
AX={'enbseries','enbcache'}
Bq=I.compile('^(enb[\\w .()-]*\\.(ini|dll|asi|fx|fxh|dds|bmp|cfg)|d3d(9|10|11|12)\\.dll|d3dcompiler[\\w.]*\\.dll|dxgi\\.dll)$',I.I)
Br={'.dll',AK,Am,'.fx','.fxh','.cfg','.json','.yml','.xml'}
def Bs(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=A3]
		for D in G:
			if D.lower().endswith(AL):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def Bt(src,pack_path,rpf_index,log):
	B=A.path.basename(src);C=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in C]
	for(F,G)in AG(H[:-1]):
		if G in(A4,An):return A.path.join(*C[F:])
		if G=='dlcpacks':return A.path.join(A4,An,*C[F:])
	D=rpf_index.get(B.lower(),[])
	if E(D)==1:return D[0]
	if E(D)>1:log(f"{B} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return B
def AY(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(l):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
AZ={P,'five m','five-m','fivem.app','fivem app','fivem files','five m files','fivem folder'}
Aa={'reshade-shaders','reshade-presets'}
def Bu(pack_path,log,gta_base=D):
	D=pack_path;I=log;C=[];T=Bs(gta_base);F={}
	def G(key,n=1):F[key]=F.get(key,0)+n
	def N(src):C.append((src,P,A.path.join(A3,Bt(src,D,T,I))));G('rpf vers mods')
	def O(gta_dir,label,prefix=B):
		F=prefix;E=gta_dir
		for(I,K,J)in A.walk(E):
			for B in J:
				if B.startswith(l):continue
				D=A.path.join(I,B)
				if B.lower().endswith(AL):N(D)
				else:H=A.path.relpath(D,E);C.append((D,R,A.path.join(F,H)if F else H));G(f"{label} vers GTA V")
	def Q(dirpath,in_fivem=H,depth=0):
		V='asi vers plugins';S=depth;J=in_fivem;H=dirpath
		if S>12:I(f"Profondeur maximale atteinte, dossier ignoré : {H}");return
		K=AF(A.listdir(H));T={B.lower()for B in K if A.path.isdir(A.path.join(H,B))};U=A.path.basename(H).lower();J=J or U in AZ;W=U in AZ or u(T&(AW|Aa));X=not J and(u(T&AX)or any(A.lower().startswith('enb')and A.lower().endswith(Am)for A in K));Y={A.path.splitext(B)[0].lower()for B in K if B.lower().endswith(AK)}
		for F in K:
			B=A.path.join(H,F);D=F.lower()
			if B7(B):I(f"Lien/jonction ignoré dans le pack : {F}");continue
			if A.path.isdir(B):
				if D in AW or D in Aa:M=E(C);AY(C,B,P,D);G(f"{D} vers FiveM",E(C)-M)
				elif D in B8:O(B,B9(F))
				elif D in AX:
					if J:M=E(C);AY(C,B,P,D);G(f"{D} vers FiveM",E(C)-M)
					else:O(B,B9(F),prefix=D)
				else:Q(B,J,S+1)
			elif not D.startswith(l):
				L=A.path.splitext(D)[1]
				if L==AL:N(B)
				elif X and Bq.match(F):C.append((B,R,F));G('ENB vers GTA V')
				elif L==AK:C.append((B,P,A.path.join(AJ,F)));G(V)
				elif L==Am and A.path.splitext(D)[0]in Y:C.append((B,P,A.path.join(AJ,F)));G(V)
				elif W and L in Br:C.append((B,P,F));G('racine FiveM')
	Q(D)
	if not C:I("Structure standard non détectée — copie de l'archive telle quelle.");AY(C,D,P,B)
	C=[(E,D,C)for(E,D,C)in C if not(D==P and A.path.dirname(C)==B and A.path.splitext(C)[0].lower()==c)];J,K=set(),[]
	for(U,L,M)in C:
		S=L,M.lower()
		if S not in J:J.add(S);K.append((U,L,M))
	V=', '.join(f"{A} : {B}"for(A,B)in F.items())or'rien à installer';I(f"Structure détectée — {V}.");return K
def B9(name):A=name;return A if E(A)<=20 else A[:17]+'...'
def A0(e):return(P,e)if h(e,i)else(e[0],e[1])
def Ab(target,rel):return f"{target}|{rel}"
def Bv(bases,backup_root,manifest,log):
	M=bases;J=manifest;I=backup_root
	for O in BQ(J[q]):
		D,L=A0(O);E=M.get(D)
		if not E:continue
		try:
			B=b(E,L)
			if A.path.exists(B):A.remove(B)
			if J[A5].get(Ab(D,L)):
				H=A.path.join(I,D,L)
				if A.path.exists(H):K.move(H,B)
		except G:pass
	for(D,N)in BQ(J.get(AM,[])):
		E=M.get(D)
		if not E:continue
		try:
			B=b(E,N);H=A.path.join(I,Ao,D,N)
			if A.path.exists(H):
				if A.path.isdir(B):K.rmtree(B,ignore_errors=C)
				K.move(H,B)
		except G:pass
	K.rmtree(I,ignore_errors=C);log("Installation annulée — jeu restauré dans son état d'origine.",F)
o={P:Ak,R:'GTA V'}
Bw={P:{AI},R:{A4,An,'redistributables','installers','dlc','_commonredist',A3}}
def BA(plan):
	C={}
	for(G,D,F)in plan:
		B=F.replace(a,A.sep).split(A.sep)
		if E(B)>1:C.setdefault((D,B[0].lower()),B[0])
	return C
def Bx(pack_name,bases,state,log,progress):
	e=state;W=pack_name;S=bases;L=log
	if W in e[Z]:raise Q('Ce pack est déjà chargé.')
	if AV():raise O('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	v=b(T,AB(W));I=Bu(v,L,S.get(R))
	if not I:raise Q('Pack vide — aucun fichier à installer.')
	p=[1 for(B,A,C)in I if A==R and not S.get(R)]
	if p:L(f"Dossier GTA V introuvable — {E(p)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);I=[(B,A,C)for(B,A,C)in I if not(A==R and not S.get(R))]
	if not I:raise Q('Rien à installer (dossier GTA V non configuré).')
	i={}
	for(w,X,A7)in I:
		try:i[X]=i.get(X,0)+A.path.getsize(w)
		except N:pass
	for(X,x)in i.items():
		if S.get(X):z(S[X],x,f"l'installation ({o[X]})")
	Y={q:[],A5:{},AM:[]};a={}
	for(c,y)in e[Z].items():
		if c!=W:
			for r in y[q]:a[A0(r)[0]+'|'+A0(r)[1].lower()]=c
	L(f"Installation de « {W} » — {E(I)} fichiers...");j=A.path.join(B0,W);k=0;s=E(I)<=60;A1=max(1,E(I)//10)
	try:
		for((H,f),U)in BA(I).items():
			M=S.get(H)
			if H!=P or not M or not A.path.isdir(M):continue
			g=A2((A for A in A.listdir(M)if A.lower()==f),D)
			if g and g!=U:
				try:A.rename(A.path.join(M,g),A.path.join(M,U));L(f"Dossier {g} renommé en {U}.")
				except N:pass
		for((H,f),U)in BA(I).items():
			M=S.get(H)
			if not M or f in Bw.get(H,set()):continue
			t=b(M,U)
			if not A.path.isdir(t):continue
			A3=f"{H}|{f}{A.sep}";c=A2((B for(A,B)in a.items()if A.startswith(A3)),D)
			if c:L(f"Dossier {U} : contient des fichiers du pack « {c} » — fusion au lieu du remplacement.");continue
			d=A.path.join(j,Ao,H,U);A.makedirs(A.path.dirname(d),exist_ok=C);K.move(t,d);Y[AM].append([H,U]);L(f"Dossier existant mis de côté ({o[H]}) : {U} — remplacé proprement. Ton contenu précédent est sauvegardé et sera remis au déchargement du pack.")
		for(l,(A4,H,V))in AG(I):
			M=S[H];h=b(M,V);m=H+'|'+V.lower()
			if m in a:L(f"Attention : {V} appartient déjà au pack « {a[m]} » — écrasé.")
			A.makedirs(A.path.dirname(h),exist_ok=C)
			if A.path.exists(h)and m not in a:
				d=A.path.join(j,H,V);A.makedirs(A.path.dirname(d),exist_ok=C);K.copy2(h,d);Y[A5][Ab(H,V)]=C;k+=1
				if s:L(f"Sauvegarde de l'original ({o[H]}) : {V}")
			K.copy2(A4,h);Y[q].append([H,V])
			if s:L(f"Copie ({o[H]}) : {V}")
			elif(l+1)%A1==0:L(f"{l+1}/{E(I)} fichiers copiés ({k} originaux sauvegardés)...")
			progress(l+1,E(I))
	except G as n:L(f"Erreur pendant l'installation : {n}",F);Bv(S,j,Y,L);raise O(f"Installation échouée ({n}) — tout a été annulé.")from n
	e[Z][W]=Y;B4(e);u=sum(1 for A in Y[q]if A0(A)[0]==R);A6=f" (dont {u} dans GTA V)"if u else B;L(f"« {W} » chargé : {E(I)} fichiers copiés{A6}, {k} originaux sauvegardés.",J)
def By(pack_name,bases,state,log,progress):
	c=bases;V=state;P=pack_name;G=log;R=V[Z].get(P)
	if not R:raise Q("Ce pack n'est pas chargé.")
	if AV():raise O('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	S=A.path.join(B0,P);I=R[q];d=set();G(f"Désinstallation de « {P} » — {E(I)} fichiers...");U=0;W=E(I)<=60;g=max(1,E(I)//10)
	for(X,e)in AG(I):
		B,H=A0(e);M=c.get(B)
		if not M:G(f"Cible {o.get(B,B)} introuvable — {H} laissé en place.",F);continue
		try:D=b(M,H)
		except Q as j:G(f"Entrée ignorée : {j}",F);continue
		if A.path.exists(D):
			A.remove(D)
			if W:G(f"Suppression ({o[B]}) : {H}")
		f,k=A.path.join(S,B,H),A.path.join(S,H);l=R[A5].get(Ab(B,H))or h(e,i)and R[A5].get(H)
		if l:
			T=f if A.path.exists(f)else k
			if A.path.exists(T):
				A.makedirs(A.path.dirname(D),exist_ok=C);K.move(T,D);U+=1
				if W:G(f"Original restauré : {H}")
		if not W and(X+1)%g==0:G(f"{X+1}/{E(I)} fichiers retirés ({U} originaux restaurés)...")
		Y=A.path.realpath(M);L=A.path.dirname(D)
		while A.path.commonpath([Y,L])==Y and L!=Y:d.add(L);L=A.path.dirname(L)
		progress(X+1,E(I))
	for L in AF(d,key=E,reverse=C):
		try:A.rmdir(L)
		except N:pass
	for(B,a)in R.get(AM,[]):
		M=c.get(B)
		if not M:continue
		try:D=b(M,a)
		except Q:continue
		T=A.path.join(S,Ao,B,a)
		if A.path.exists(T):
			if A.path.isdir(D):K.rmtree(D,ignore_errors=C)
			K.move(T,D);U+=1;G(f"Dossier original restauré ({o[B]}) : {a}")
	if A.path.isdir(S):K.rmtree(S,ignore_errors=C)
	del V[Z][P];B4(V);G(f"« {P} » déchargé : {E(I)} fichiers retirés, {U} originaux restaurés.",J)
class Ac(G):0
AC=D
def Bz(fn):global AC;AC=fn
def Ad():
	if AC is not D and AC():raise Ac('Téléchargement annulé.')
B_=262144
Ae=4
C0=3
class BB(O):0
def C1(exc):
	A=exc
	if h(A,BB):return H
	if h(A,urllib.error.HTTPError):return A.code in(408,429)or A.code>=500
	return C
def C2(url,headers,offset):
	A=offset;B=g(headers)
	if A:B['Range']=f"bytes={A}-"
	return urllib.request.urlopen(urllib.request.Request(url,headers=B),timeout=60)
def AD(url,out_path,log,progress,headers=D,make_transform=D,align=1,check_space=C,quiet=H):
	W=check_space;V=make_transform;U=out_path;P=log;K=headers;K=g(K or{});K.setdefault(m,s);Z=A.path.dirname(U)or l;H,I,Q,L=0,0,D,0
	while C:
		Ad()
		try:
			with C2(url,K,H)as J:
				if H and AE(J,Ap,200)!=206:P('Le serveur ne gère pas la reprise — reprise depuis le début.');H=0
				if Q is D:Q=J.headers.get_filename()
				if H==0 and J.headers.get_content_type().startswith('text/'):raise BB('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				if not I:
					R=J.headers.get(BX,B)
					if a in R and R.rsplit(a,1)[1].isdigit():I=Y(R.rsplit(a,1)[1])
					else:S=J.headers.get(Aq);I=Y(S)+H if S and S.isdigit()else 0
					if I and W and H==0:z(Z,Y(I*2.3),AN)
				b=V(H)if V else D
				with X(U,'r+b'if H else'wb')as T:
					T.seek(H);T.truncate(H);c=H
					while C:
						Ad();M=J.read(B_)
						if not M:break
						T.write(b(M)if b else M);H+=E(M)
						if I:progress(H,I)
						elif H-c>=256*1024**2:
							c=H
							if W:z(Z,512*1024**2,AN)
							if not quiet:P(f"{H/1048576:.0f} Mo téléchargés...")
			return Q,I or H
		except Ac:raise
		except G as N:
			if not C1(N):raise
			L+=1
			if L>Ae:raise O(f"Téléchargement échoué après {Ae} reprises ({N})")from N
			H-=H%align;d=C0*L;P(f"Coupure réseau ({N}) — reprise dans {d}s à {H/1048576:.0f} Mo (essai {L}/{Ae}).",F);time.sleep(d)
def Af(url,key):
	A=url
	if not key:return A
	B='&'if'?'in A else'?';return f"{A}{B}key={urllib.parse.quote(key)}"
def BC(url,key):A=urllib.request.Request(Af(url,key),headers={m:s});return urllib.request.urlopen(A,timeout=30)
def C3(cfg):
	C=cfg.get(k)
	if not C:return[]
	D=cfg.get(w)
	with BC(C,D)as G:B=M.loads(G.read().decode(U))
	E=C.rsplit(a,1)[0]+a;H=B.get(Aj,B)if h(B,g)else B;F=[]
	for A in H:
		if not h(A,g)or not A.get(L):continue
		try:
			AB(A[L])
			if not A.get(d):A[d]=Af(urllib.parse.urljoin(E,A[Ar]),D)
			if A.get(S)and not A[S].startswith((x,y,'data:')):A[S]=Af(urllib.parse.urljoin(E,A[S]),D)
		except(KeyError,Q,TypeError):continue
		F.append(A)
	return F
def BD(v):return tuple(Y(A)for A in I.findall('\\d+',v or B))or(0,)
def C4():
	G=urllib.request.Request(f"https://api.github.com/repos/{AQ}/releases/latest",headers={m:s,BY:'application/vnd.github+json'})
	with urllib.request.urlopen(G,timeout=15)as H:A=M.loads(H.read().decode(U))
	C=(A.get('tag_name')or B).strip()
	if not C:return
	D=B
	for E in A.get('assets',[]):
		F=(E.get(L)or B).lower()
		if F.endswith('.exe')and As in F:D=E.get('browser_download_url')or B;break
	I=A.get('html_url')or f"https://github.com/{AQ}/releases";return C,I,D
def BE(url):A=f"https://github.com/{AQ}/releases/download/";return url.startswith(A)and'..'not in url
def BF(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return BZ,A
	if D in B and'/folders/'in B:
		C=I.search('/folders/([\\w-]+)',A)
		if C:return At,C.group(1)
	if D in B:
		C=I.search('/file/d/([\\w-]+)',A)or I.search('[?&]id=([\\w-]+)',A)
		if C:return Au,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if'?'in A else'?')+'confirm=t'
	return Au,A
BG='Mozilla/5.0'
C5=I.compile('data-id="([\\w-]{20,})"')
C6=I.compile('<title>([^<]*)</title>')
def BH(url,rng=D):
	A={m:BG}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def BI(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def BJ(fid):
	with BH(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(U,Al)
def C7(html,fallback):
	C=fallback;D=C6.search(html)
	if not D:return C
	A=D.group(1).replace('\xa0',' ');A=I.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',B,A).strip();return A or C
def C8(html,self_id):
	B,C=[],{self_id}
	for A in C5.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def C9(fid):
	for K in range(2):
		try:
			with BH(BI(fid),'bytes=0-0')as A:E=A.headers.get('Content-Disposition',B);L=A.headers.get_content_type();F=A.headers.get(BX,B)
			if'attachment'in E and not L.startswith('text/html'):J=I.search('filename="([^"]+)"',E)or I.search("filename\\*=UTF-8''(.+)",E);M=urllib.parse.unquote(J.group(1))if J else D;N=Y(F.split(a)[-1])if a in F else 0;return C,M,N
			return H,D,0
		except urllib.error.HTTPError as O:
			if O.code in(403,429)and K==0:continue
			return D,D,0
		except G:return D,D,0
	return D,D,0
def CA(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def Ag(seg):A=seg;A=I.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def CB(folder_id,log):
	C=folder_id;E=[]
	def D(cid,fname,size,prefix):D=prefix;C=fname;B=cid;F=A.path.join(D,Ag(C or B))if D else Ag(C or B);E.append((F,B,size))
	def I(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in C8(html,fid):
			L,E,F=C9(B)
			if L:D(B,E,F,C);continue
			try:H=BJ(B)
			except G:D(B,E,F,C);continue
			if not CA(H):D(B,E,F,C);continue
			K=Ag(C7(H,B));I(B,H,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');I(C,BJ(C),B,0);return E
def CC(folder_id,dest,log,progress):
	I=dest;G=log;B=CB(folder_id,G)
	if not B:raise O('Dossier Drive vide ou illisible (accès restreint ?).')
	F=sum(A for(B,C,A)in B);G(f"{E(B)} fichiers dans le dossier"+(f" ({F/1048576:.0f} Mo)."if F else l))
	if F:z(I,F,AN)
	A.makedirs(I,exist_ok=C);K=0;N=max(1,E(B)//20)
	for(J,(P,Q,S))in AG(B):
		Ad();L=b(I,P);A.makedirs(A.path.dirname(L),exist_ok=C);M=K;T,R=AD(BI(Q),L,G,lambda cur,tot,_b=M:progress(_b+cur,F)if F else D,headers={m:BG},check_space=H,quiet=C);K=M+R
		if(J+1)%N==0 or J+1==E(B):G(f"{J+1}/{E(B)} fichiers téléchargés...")
def CD(url,log):
	K='data';N=url.rstrip(a).split(a)[-1].split('?')[0]
	def B(u,data=D,headers=D):
		A=data;B={m:s,BY:AO};B.update(headers or{})
		if A is not D:B[Av]=AO;A=M.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return M.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[K]['token']
	try:P=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={m:s}),timeout=30).read().decode();Q=I.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',P).group(1)
	except G as E:raise O(f"Gofile ne fonctionne plus avec ce type de lien ({E}). Ré-héberge le pack sur Google Drive ou Mega.")from E
	A=B(f"https://api.gofile.io/contents/{N}?wt={Q}",headers={'Authorization':f"Bearer {C}"})
	if A.get(Ap)!=J:raise O(f"Gofile a refusé le lien ({A.get(Ap)}).")
	R=A[K];S=R.get('children')or{};F=[A for A in S.values()if A.get('type')==Ar]
	if not F:raise O('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	H=max(F,key=lambda c:c.get(AP,0));return H['link'],{'Cookie':f"accountToken={C}"},H.get(L)
def BK(s):s=s.replace('-','+').replace('_',a);return Ax.b64decode(s+'='*(-E(s)%4))
def CE(url,out_path,log,progress):
	K='g';J=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as L,algorithms as N,modes as P
	except BP as U:raise O('Support Mega indisponible (module cryptography manquant).')from U
	E=I.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or I.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not E:raise O('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	V,W=E.group(1),E.group(2);A=A7.unpack('>8I',BK(W));Q=A7.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);X=A7.pack('>2I',A[4],A[5])+J*8;Z=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=M.dumps([{'a':K,K:1,'p':V}]).encode(),headers={Av:AO,m:s});C=M.loads(urllib.request.urlopen(Z,timeout=30).read().decode())
	if h(C,Y)or h(C,v)and h(C[0],Y):raise O('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	C=C[0];a,D=C[K],Y(C.get('s',0));F='mega_pack'
	try:
		R=L(N.AES(Q),P.CBC(J*16)).decryptor();S=R.update(BK(C['at']))+R.finalize()
		if S.startswith(b'MEGA'):F=M.loads(S[4:].split(J)[0].decode())['n']
	except G:pass
	if D:z(T,Y(D*2.3),AN)
	log(f"Fichier Mega : {F}"+(f" ({D/1048576:.0f} Mo)"if D else B))
	def b(offset):A=X[:8]+A7.pack('>Q',offset//16);return L(N.AES(Q),P.CTR(A)).decryptor().update
	AD(a,out_path,log,progress,make_transform=b,align=16,check_space=H);return F
def BL(pack,cfg,log,progress):
	W=progress;I=pack;H=log;Y=AB(I[L]);P=b(T,Y);F=P+'.part';A.makedirs(T,exist_ok=C);k,N=Bc.mkstemp(suffix='.pack',dir=T);A.close(k);O=D
	try:
		H(f"Téléchargement de « {I[L]} »...")
		if AV():H("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		O,Q=BF(I[d]);M=I.get(Ar)
		if A.path.isdir(F):K.rmtree(F,ignore_errors=C)
		if O==At:CC(Q,F,H,W);BO(F,H)
		elif O=='mega':M=CE(Q,N,H,W)or M
		else:
			if O==BZ:H('Résolution du lien Gofile...');Z,f,l=CD(Q,H);M=M or l
			else:Z,f=Q,{}
			m,g=AD(Z,N,H,W,headers=f);M=m or M or A.path.basename(urllib.parse.urlparse(Z).path)
			if M:H(f"Fichier : {M}"+(f" ({g/1048576:.0f} Mo)"if g else B))
		if O!=At:
			H(f"Extraction dans le cache local ({Y})...");BN(N,F,H);R=A.listdir(F)
			if E(R)==1 and A.path.isdir(A.path.join(F,R[0]))and R[0].lower()not in(AI,A3,AJ):
				a=A.path.join(F,R[0])
				for h in A.listdir(a):K.move(A.path.join(a,h),A.path.join(F,h))
				A.rmdir(a)
			if not CI(F):BO(F,H)
		if I.get(V):
			with X(A.path.join(F,BW),'w',encoding=U)as e:e.write(i(I[V]))
		if I.get(S):
			try:
				with BC(I[S],D)as n:
					j=A.path.splitext(urllib.parse.urlparse(I[S]).path)[1]or AH
					if j.lower()in AT:
						with X(A.path.join(F,c+j.lower()),'wb')as e:e.write(n.read())
			except G:pass
		if A.path.isdir(P):K.rmtree(P)
		A.replace(F,P);H(f"« {Y} » téléchargé et extrait.",J)
	except BaseException:K.rmtree(F,ignore_errors=C);raise
	finally:
		if A.path.exists(N):A.remove(N)
Ah=134217728
BM=3600
CF={'.zip','.rar','.7z'}
t=I.compile('\\.part(\\d+)\\.rar$',I.I)
A1=I.compile('\\.r\\d{2}$',I.I)
p=I.compile('\\.(\\d{3})$')
def CG():K='-o{d}';J='7-Zip';I='-inul';H='-ibck';G='WinRAR';F='UnRAR';E='{d}\\';D='-p-';C='-y';B='x';L=[(F,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,D,n,E]),(F,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,D,n,E]),(G,['C:\\Program Files\\WinRAR\\WinRAR.exe',B,H,I,C,D,n,E]),(G,['C:\\Program Files (x86)\\WinRAR\\WinRAR.exe',B,H,I,C,D,n,E]),(J,['C:\\Program Files\\7-Zip\\7z.exe',B,C,'-p',K,n]),(J,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,'-p',K,n]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',n,'-C','{d}'])];return[(C,B)for(C,B)in L if A.path.exists(B[0])]
def BN(archive,dest,log):
	H=log;E=archive;B=dest;A.makedirs(B,exist_ok=C)
	if Az.is_zipfile(E):
		try:
			with Az.ZipFile(E)as L:
				for M in L.namelist():
					P=A.path.realpath(A.path.join(B,M))
					if not P.startswith(A.path.realpath(B)+A.sep):raise Q(f"Chemin suspect dans l'archive : {M}")
				L.extractall(B)
			return
		except Q:raise
		except G as R:H(f"Zip non lisible en natif ({R}) — essai d'un extracteur externe...")
	N=CG()
	if not N:raise O('Aucun extracteur trouvé — installe WinRAR ou 7-Zip.')
	I=[]
	for(D,J)in N:
		H(f"Extraction avec {D}...");J=[A.replace(n,E).replace('{d}',B)for A in J]
		try:K=A8.run(J,capture_output=C,text=C,creationflags=Ah,timeout=BM)
		except A8.TimeoutExpired:I.append(f"{D} : abandon après {BM//60} min (archive protégée par mot de passe ?)");H(f"{D} ne répond plus — abandon.",F);continue
		if K.returncode==0:CH(B);return
		I.append(f"{D} : {(K.stderr or K.stdout).strip()[:200]}")
	raise O('Échec extraction — '+' | '.join(I))
def CH(dest):
	for(E,B,F)in A.walk(dest):
		for C in v(B)+v(F):
			D=A.path.join(E,C)
			if B7(D):
				if C in B:B.remove(C);A.rmdir(D)
				else:A.remove(D)
def BO(dest,log):
	L=log;M=set()
	for S in range(3):
		D=[]
		for(P,T,Q)in A.walk(dest):D+=[A.path.join(P,B)for B in Q if A.path.splitext(B)[1].lower()in CF or p.search(B)or A1.search(B)]
		D=[A for A in D if A not in M]
		if not D:return
		H=[]
		for C in D:
			E=A.path.basename(C)
			if A1.search(E):continue
			J=p.search(E)
			if J and J.group(1)!='001':continue
			K=t.search(E)
			if K and Y(K.group(1))>1:continue
			if K:N=t.sub(B,E)
			elif J:O=p.sub(B,E);N=A.path.splitext(O)[0]or O
			else:N=A.path.splitext(E)[0]
			L(f"Archive dans le pack : {E} — extraction...")
			try:BN(C,A.path.join(A.path.dirname(C),N),L)
			except G as R:L(f"Extraction de {E} impossible : {R}",F);M.add(C);continue
			H.append(C)
			if K:I=t.sub(B,C).lower();H+=[A for A in D if A!=C and t.search(A)and t.sub(B,A).lower()==I]
			elif J:I=p.sub(B,C).lower();H+=[A for A in D if A!=C and p.search(A)and p.sub(B,A).lower()==I]
			elif E.lower().endswith('.rar'):I=C[:-4].lower();H+=[A for A in D if A1.search(A)and A1.sub(B,A).lower()==I]
		for C in D:
			if C in H:
				if A.path.exists(C):A.remove(C)
			elif t.search(C)or A1.search(C)or p.search(C):M.add(C)
def CI(dest):
	B=AW|B8|AZ|Aa|AX
	for(F,D,E)in A.walk(dest):
		if any(A.lower()in B for A in D):return C
		if any(A.lower().endswith((AL,AK))for A in E):return C
	return H
def CJ():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except G:pass
class CK:
	def __init__(A):A.state=B3();A.cfg=AA();A.fivem=Bl();A.gta=Bm(A.fivem);A.remote_packs=[];A.custom_packs=v(A.cfg.get('custom_packs',[]));A.categories=[i(A)for A in A.cfg.get(Ba,[])];A.background=A.cfg.get(Aw);A.busy=H;A._maj=D;A._cancel=e.Event();Bz(A._cancel.is_set);A._lock=e.Lock();A._buf_lock=e.Lock();A._logs=[];A._prog=0,0;A._dirty=H
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=C
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,H
		return{'logs':B,'prog':v(A._prog),'busy':A.busy,'dirty':C,'maj':A._maj}
	def _all_remote(B):
		D={A[L]:g(A)for A in B.remote_packs}
		for E in B.custom_packs:A=g(E);A[A6]=C;D[A[L]]=A
		return v(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((x,y)):return B
		C=A.path.join(f,B);return f"/bg?{Y(A.path.getmtime(C))}"if A.path.exists(C)else D
	def get_state(A):
		Q='remote';O='image_link';N='nfiles';J=[];K={A[L]:A for A in A._all_remote()}
		for I in AU():F=K.pop(I,D);M=B6(I);J.append({L:I,AP:Bn(I),V:M,Z:I in A.state[Z],N:E(A.state[Z].get(I,{}).get(q,[])),S:(F or{}).get(S)or Bo(I),O:(F or{}).get(S),d:(F or{}).get(d),c:(F or{}).get(c),Q:H,A6:u(F and F.get(A6)),j:(F or{}).get(j,B),A4:u(F and F.get(V)and i(F[V])!=(M or B))})
		for G in K.values():J.append({L:G[L],AP:G.get(AP,B),V:G.get(V),Z:H,N:0,S:G.get(S),O:G.get(S),d:G.get(d),c:G.get(c),Q:C,A6:u(G.get(A6)),j:G.get(j,B),A4:H})
		return{P:A.fivem,R:A.gta,Aj:J,Aw:A.background_url(),k:A.cfg.get(k,B),w:A.cfg.get(w,B),'background_setting':A.background or B,'busy':A.busy,V:A9,Ba:A.categories}
	def open_site(B):A.startfile('https://modium.xyz')
	def ouvrir_maj(C):
		B=(C._maj or{}).get(d)
		if B and B.startswith('https://github.com/'):A.startfile(B)
	def installer_maj(D):
		E=g(D._maj or{});G=E.get(As)or B
		if not BE(G):D._log('Installeur indisponible — ouverture de la page.',F);D.ouvrir_maj();return
		if D.busy:D._log('Une opération est en cours — réessaie après.',F);return
		def H():
			F=A.path.join(f,'_maj');A.makedirs(F,exist_ok=C);B=A.path.join(F,'Modium-Setup.exe');D._log(f"Téléchargement de la version {E.get(V)}...");AD(G,B,D._log,D._progress);H=A.path.getsize(B)
			if H<1000000:A.remove(B);raise O('fichier reçu trop petit, téléchargement invalide')
			with X(B,'rb')as I:
				if I.read(2)!=b'MZ':A.remove(B);raise O("le fichier reçu n'est pas un exécutable")
			D._log(f"Installation de {E.get(V)} — Modium va se fermer et redémarrer.",J);time.sleep(1.2);A8.Popen([B,'/SILENT','/NORESTART','/CLOSEAPPLICATIONS','/RESTARTAPPLICATIONS'],creationflags=Ah|8);e.Timer(.8,lambda:A._exit(0)).start()
		D._run(H)
	def ignorer_maj(A):A._maj=D
	def add_custom_pack(A,name,url,image,preview=B,old_name=B,categorie=B):
		N=image;M=categorie;I=preview;H=url;E=old_name;D=name;D,H,N=D.strip(),H.strip(),N.strip();I,E=I.strip(),E.strip();M=M.strip()
		if not D or not H:A._log('Nom et lien requis pour ajouter un pack.',F);return
		try:D=AB(D);BF(H)
		except G as P:A._log(f"Refusé : {P}",F);return
		if not H.lower().startswith((x,y)):A._log('Lien refusé : il faut une URL http(s).',F);return
		if I and not I.startswith((x,y)):A._log('Lien preview refusé (il faut un lien http).',F);return
		R={D,E}-{B};A.custom_packs=[A for A in A.custom_packs if A[L]not in R];O={L:D,d:H}
		if N:O[S]=N
		if I:O[c]=I
		if M:
			O[j]=M
			if M not in A.categories:A.categories.append(M);W(categories=A.categories)
		A.custom_packs.append(O);W(custom_packs=A.custom_packs)
		if E and E!=D and E in AU():
			try:K.rmtree(b(T,E),ignore_errors=C)
			except Q:pass
		A._log(f"Pack « {D} » {"modifié"if E else"ajouté"}.",J);A._refresh_ui()
	def add_categorie(B,nom):
		A=nom;A=' '.join(A.split())[:40]
		if not A:return
		if A in B.categories:B._log(f"La catégorie « {A} » existe déjà.",F);return
		B.categories.append(A);W(categories=B.categories);B._log(f"Catégorie « {A} » créée.",J);B._refresh_ui()
	def remove_categorie(A,nom):
		C=nom
		if C not in A.categories:return
		A.categories=[A for A in A.categories if A!=C];E=0
		for F in A.custom_packs:
			if F.get(j)==C:F.pop(j,D);E+=1
		W(categories=A.categories,custom_packs=A.custom_packs);G=f" — {E} pack(s) sans catégorie"if E else B;A._log(f"Catégorie « {C} » supprimée{G}.",J);A._refresh_ui()
	def rename_categorie(A,ancien,nouveau):
		C=ancien;B=nouveau;B=' '.join(B.split())[:40]
		if not B or C not in A.categories or B==C:return
		if B in A.categories:A._log(f"La catégorie « {B} » existe déjà.",F);return
		A.categories=[B if A==C else A for A in A.categories]
		for D in A.custom_packs:
			if D.get(j)==C:D[j]=B
		W(categories=A.categories,custom_packs=A.custom_packs);A._log(f"Catégorie renommée en « {B} ».",J);A._refresh_ui()
	def preview(C,name):
		E=A2((A for A in C._all_remote()if A[L]==name),D);B=(E or{}).get(c)
		if B and B.startswith((x,y)):A.startfile(B)
		else:C._log('Pas de preview pour ce pack.',F)
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if C in B.state[Z]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[L]!=C];W(custom_packs=B.custom_packs)
		try:E=b(T,C)
		except Q:E=D
		if E and A.path.isdir(E):
			try:K.rmtree(E);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",J)
			except N as G:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {G}",F)
		else:B._log(f"Pack « {C} » retiré.",J)
		B._refresh_ui()
	def choose_background(A):return CJ()or B
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=D;W(background=D);C._log('Image de fond retirée.',J)
		elif B.startswith((x,y)):C.background=B;W(background=B);C._log('Image de fond (lien) enregistrée.',J)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(f,H))
				except N:pass
			E=A.path.splitext(B)[1].lower();E=E if E in AT else AH;G=Aw+E;K.copy2(B,A.path.join(f,G));C.background=G;W(background=G);C._log('Image de fond enregistrée.',J)
		else:C._log(f"Image introuvable : {B}",F)
	def save_settings(C,url,key,fivem,gta,bg):
		E=fivem;D=gta;C.cfg[k]=url.strip();C.cfg[w]=key.strip();W(packs_url=C.cfg[k],packs_key=C.cfg[w]);E=E.strip()
		if E:
			if A.path.isdir(E):C.fivem=E;W(fivem_path=E);C._log(f"Dossier FiveM : {E}",J)
			else:C._log(f"Dossier introuvable : {E}",F)
		D=D.strip()
		if D:
			if A.path.isdir(D)and A.path.exists(A.path.join(D,BV)):C.gta=D;W(gta_path=D);C._log(f"Dossier GTA V : {D}",J)
			else:C._log(f"Dossier GTA V invalide (GTA5.exe absent) : {D}",F)
		if(bg or B).strip()!=(C.background or B):C._set_background(bg or B)
		C._log('Paramètres enregistrés.',J)
		if C.cfg[k]:C.fetch_remote()
		else:C.remote_packs=[];C._refresh_ui()
	def check_update(D):
		def A():
			try:
				A=C4()
				if A and BD(A[0])>BD(A9):D._maj={V:A[0],d:A[1],As:A[2]if BE(A[2])else B,'actuelle':A9};D._refresh_ui()
			except G:pass
		e.Thread(target=A,daemon=C).start()
	def fetch_remote(A):
		if not A.cfg.get(k):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def B():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=C3(A.cfg);A._log(f"{E(A.remote_packs)} pack(s) disponibles en ligne.",J)
			except G as B:A.remote_packs=[];A._log(f"Serveur inaccessible : {B}",F)
			A._refresh_ui()
		e.Thread(target=B,daemon=C).start()
	def _run(A,fn):
		def B():
			if not A._lock.acquire(blocking=H):A._log('Une opération est déjà en cours.',F);return
			try:
				A._cancel.clear();A.busy=C;A._refresh_ui()
				try:fn()
				except Ac as B:A._log(f"{B} Rien n'a été installé.",F)
				except G as B:A._log(f"Erreur : {B}",F)
				finally:A._cancel.clear();A.busy=H;A._prog=0,0;A._refresh_ui()
			finally:A._lock.release()
		e.Thread(target=B,daemon=C).start()
	def cancel(A):
		if not A.busy:return{J:H}
		if not A._cancel.is_set():A._cancel.set();A._log('Annulation demandée, arrêt en cours...')
		return{J:C}
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return H
		return C
	def load(A,name):
		E=name
		if not A._need_fivem():return
		def C():
			C=A2((A for A in A._all_remote()if A[L]==E),D);F=E in AU();G=C and C.get(V)and i(C[V])!=(B6(E)or B)
			if C and(not F or G):BL(C,A.cfg,A._log,A._progress)
			elif not F:raise Q('Pack introuvable (ni local, ni sur le serveur).')
			Bx(E,{P:A.fivem,R:A.gta},A.state,A._log,A._progress)
		A._run(C)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:By(name,{P:A.fivem,R:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=A2((A for A in A._all_remote()if A[L]==name),D)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:BL(B,A.cfg,A._log,A._progress))
CL='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que le site : noir pur, verre translucide,\n     lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow: hidden; }\n  /* ---- colonne des catégories ---- */\n  main { display: flex; gap: 0; }\n  #cotes {\n    width: 176px; flex-shrink: 0; padding: 20px 12px 20px 22px;\n    border-right: 1px solid var(--line); overflow-y: auto;\n  }\n  .cote-t {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted); padding: 0 10px 10px;\n  }\n  .cote {\n    display: flex; align-items: center; gap: 8px; width: 100%;\n    background: none; border: 1px solid transparent; border-radius: 8px;\n    color: var(--muted); cursor: pointer; text-align: left;\n    padding: 8px 10px; margin-bottom: 3px; font-size: 12px;\n    transition: background 0.2s, color 0.2s, border-color 0.2s, transform 0.2s;\n  }\n  .cote:hover { background: var(--glass); color: var(--text); transform: translateX(2px); }\n  .cote.on { background: var(--glass); color: var(--text); border-color: var(--line); }\n  .cote .n {\n    margin-left: auto; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted);\n  }\n  .zone { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  main > .zone { min-width: 0; }\n  #cotes:empty { display: none; }\n\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  /* le bouton annuler prend le margin auto, "vider" se colle à sa droite */\n  #console-head #btn-cancel + button { margin-left: 14px; }\n  #console-head #btn-cancel { color: var(--err); }\n  #console-head #btn-cancel:hover { color: var(--err); text-decoration: underline; }\n  #console-head #btn-cancel:disabled { color: var(--muted); cursor: default;\n                                       text-decoration: none; }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n\n  /* ---- fenêtre de mise à jour ---- */\n  /* Reprend la carte de pack telle quelle : même bordure, même rayon, même\n     vignette. Seule la vignette change de contenu — le numéro de version en\n     néon à la place de l\'image. */\n  #maj {\n    position: fixed; inset: 0; z-index: 200; display: none;\n    align-items: center; justify-content: center;\n    background: rgba(0, 0, 0, 0.86); backdrop-filter: blur(7px);\n  }\n  #maj.show { display: flex; animation: majFond .45s ease-out; }\n  @keyframes majFond { from { opacity: 0 } to { opacity: 1 } }\n  #maj-fond { position: absolute; inset: 0; width: 100%; height: 100%; }\n  .maj-carte {\n    position: relative; width: 290px; cursor: default;\n    box-shadow: 0 30px 80px -18px rgba(0, 0, 0, 0.95),\n                0 0 60px -14px rgba(216, 26, 26, 0.5);\n    animation: majCarte .55s cubic-bezier(.2, .8, .25, 1);\n  }\n  .maj-carte:hover { transform: none; }\n  @keyframes majCarte {\n    from { opacity: 0; transform: translateY(24px) scale(.92) }\n    to { opacity: 1; transform: none }\n  }\n  .maj-carte .thumb { height: 132px; }\n  /* La bannière vient du site : la fenêtre ne s\'ouvre que si la vérification\n     de version a abouti, donc la connexion est forcément là. En cas d\'échec\n     l\'image se masque et le numéro reprend toute la place. */\n  .maj-carte .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .maj-carte .thumb::after {\n    content: \'\'; position: absolute; inset: 0;\n    background: linear-gradient(180deg, rgba(0,0,0,.15), rgba(0,0,0,.78));\n  }\n  .maj-carte .maj-v, .maj-carte .badge { position: absolute; z-index: 1; }\n  .maj-carte .maj-v { bottom: 12px; left: 16px; }\n  .maj-carte .badge.cloud {\n    color: #ff6a6a; border-color: rgba(216, 26, 26, 0.5);\n    background: rgba(216, 26, 26, 0.12);\n    animation: majPouls 2.2s ease-in-out infinite;\n  }\n  @keyframes majPouls {\n    0%, 100% { box-shadow: 0 0 10px rgba(216, 26, 26, .25) }\n    50% { box-shadow: 0 0 26px rgba(216, 26, 26, .6) }\n  }\n  .maj-v {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 30px; font-weight: 700; letter-spacing: -0.02em;\n    background-image: linear-gradient(100deg, #fff 20%, #9a9aa4 55%, #fff 85%);\n    background-size: 220% 100%;\n    -webkit-background-clip: text; background-clip: text; color: transparent;\n    animation: majBrille 6s linear infinite;\n    filter: drop-shadow(0 0 16px rgba(255, 255, 255, .32))\n            drop-shadow(0 0 40px rgba(216, 26, 26, .5));\n  }\n  @keyframes majBrille { to { background-position: -220% 0 } }\n  .maj-carte .name { font-size: 15px; }\n  .maj-carte .actions { margin-top: 2px; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal select {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n    cursor: pointer; appearance: none;\n    /* chevron dessiné en fond : la flèche native est grise et hors charte */\n    background-image: url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'10\' height=\'6\'%3E%3Cpath d=\'M1 1l4 4 4-4\' fill=\'none\' stroke=\'%238a8a8e\' stroke-width=\'1.5\' stroke-linecap=\'round\'/%3E%3C/svg%3E");\n    background-repeat: no-repeat; background-position: right 12px center;\n    padding-right: 30px;\n  }\n  #modal select:focus { outline: none; border-color: var(--accent); }\n  #modal select option { background: #101012; color: var(--text); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>Modium</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">modium.xyz &#8599;</button>\n  </header>\n\n  <main>\n    <aside id="cotes">\n      <div class="cote-t">Catégories</div>\n      <div id="cote-liste"></div>\n    </aside>\n    <div class="zone">\n      <div class="grid" id="grid"></div>\n      <div class="empty" id="empty" style="display:none">\n        Aucun pack disponible.<br>\n        Vérifie la connexion au serveur (bouton Actualiser)<br>\n        ou l\'URL configurée dans Options.\n      </div>\n    </div>\n  </main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button id="btn-cancel" style="display:none"\n              onclick="cancelDownload()">annuler le téléchargement</button>\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n\n  <div id="maj">\n    <canvas id="maj-fond"></canvas>\n    <div class="card maj-carte">\n      <div class="thumb">\n        <img id="maj-img" src="https://modium.xyz/assets/banner.png" alt=""\n             onerror="this.style.display=\'none\'">\n        <span class="maj-v" id="maj-num">—</span>\n        <span class="badge cloud">NOUVELLE VERSION</span>\n      </div>\n      <div class="body">\n        <div class="name">Modium <span id="maj-num2">—</span></div>\n        <div class="meta">tu utilises la v<span id="maj-old">—</span></div>\n        <div class="actions">\n          <button class="btn load" id="maj-go" onclick="lancerMaj()">Mettre à jour</button>\n          <button class="btn unload" onclick="fermerMaj()">Plus tard</button>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="cats">Catégories</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <select id="cp-cat" style="margin-top:6px"></select>\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="cats" style="display:none">\n        <label>Nouvelle catégorie</label>\n        <div class="row" style="margin-top:0">\n          <input id="cat-nom" placeholder="Ex : ENB, Thèmes, Réalistes...">\n          <button class="btn dl" style="flex:0 0 120px" onclick="addCat()">Créer</button>\n        </div>\n        <div id="cat-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n\n  // ---- sons ----------------------------------------------------------\n  // Synthétisés à la volée : aucun fichier à embarquer dans l\'exe. Le\n  // contexte audio ne peut naître qu\'après un geste de l\'utilisateur, règle\n  // des navigateurs — et pywebview embarque un vrai moteur de rendu.\n  const Son = (() => {\n    let ctx = null, master = null, dernier = 0;\n    const demarrer = () => {\n      if (ctx) return;\n      const AC = window.AudioContext || window.webkitAudioContext;\n      if (!AC) return;\n      ctx = new AC();\n      master = ctx.createGain(); master.gain.value = .5;\n      const f = ctx.createBiquadFilter();\n      f.type = \'lowpass\'; f.frequency.value = 5200;\n      master.connect(f); f.connect(ctx.destination);\n    };\n    const note = (f0, f1, duree, vol, forme = \'sine\') => {\n      if (!ctx) return;\n      const t = ctx.currentTime;\n      const o = ctx.createOscillator(), g = ctx.createGain();\n      o.type = forme;\n      o.frequency.setValueAtTime(f0, t);\n      if (f1 !== f0) o.frequency.exponentialRampToValueAtTime(f1, t + duree);\n      // attaque courte mais jamais nulle : à zéro on entend un clic parasite\n      g.gain.setValueAtTime(.0001, t);\n      g.gain.exponentialRampToValueAtTime(vol, t + .006);\n      g.gain.exponentialRampToValueAtTime(.0001, t + duree);\n      o.connect(g); g.connect(master);\n      o.start(t); o.stop(t + duree + .02);\n    };\n    const limite = () => {                 // évite l\'effet mitraillette\n      const t = performance.now();\n      if (t - dernier < 55) return false;\n      dernier = t; return true;\n    };\n    return {\n      eveiller: demarrer,\n      survol() { if (ctx && limite()) { const d = 1 + (Math.random() - .5) * .06;\n                 note(1240 * d, 1180 * d, .045, .022, \'triangle\'); } },\n      bouton() { if (ctx && limite()) note(700, 940, .07, .03, \'sine\'); },\n      clic()   { if (ctx) { note(540, 300, .085, .045, \'sine\');\n                 note(1120, 880, .07, .022, \'triangle\'); } },\n      ok()     { if (ctx) { note(660, 990, .12, .035, \'sine\'); } },\n      err()    { if (ctx) { note(340, 190, .16, .04, \'triangle\'); } }\n    };\n  })();\n  [\'pointerdown\', \'keydown\'].forEach(e =>\n    addEventListener(e, () => Son.eveiller(), { once: true }));\n\n  // délégation : les cartes sont reconstruites à chaque rafraîchissement,\n  // poser les écouteurs une fois pour toutes évite de les reposer à chaque fois\n  document.addEventListener(\'pointerover\', e => {\n    const b = e.target.closest(\'button, .cote, .cp-row, .tab-btn\');\n    if (!b || b.disabled) return;\n    if (e.relatedTarget && b.contains(e.relatedTarget)) return;\n    (b.matches(\'.btn, .btn-top, .btn-site\') ? Son.bouton : Son.survol)();\n  });\n  document.addEventListener(\'pointerdown\', e => {\n    const b = e.target.closest(\'button, .cote\');\n    if (b && !b.disabled) Son.clic();\n  });\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    if (kind === \'ok\') Son.ok(); else if (kind === \'err\') Son.err();\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  async function cancelDownload() {\n    const b = document.getElementById(\'btn-cancel\');\n    b.disabled = true;\n    b.textContent = \'annulation...\';\n    try { await api(\'cancel\'); } catch (e) { appendLog(\'Annulation : \' + e, \'err\'); }\n  }\n\n  // visible seulement pendant une action ; l\'arrêt n\'est effectif que si on est\n  // encore en phase de téléchargement (l\'installation, elle, va au bout)\n  function setBusyUI(busy) {\n    const b = document.getElementById(\'btn-cancel\');\n    if (!busy) {\n      b.style.display = \'none\';\n      b.disabled = false;\n      b.textContent = \'annuler le téléchargement\';\n    } else if (b.style.display === \'none\') {\n      b.style.display = \'\';\n    }\n  }\n\n\n\n  // ---- fenêtre de mise à jour -----------------------------------------\n  let majVue = false, majAnim = 0;\n\n  function ouvrirMaj(m) {\n    if (majVue) return;                       // une seule fois par session\n    majVue = true;\n    const v = String(m.version).replace(/^v/, \'\');\n    document.getElementById(\'maj-num\').textContent = v;\n    document.getElementById(\'maj-num2\').textContent = v;\n    document.getElementById(\'maj-old\').textContent = m.actuelle;\n    document.getElementById(\'maj\').classList.add(\'show\');\n    Son.ok();\n    majFond();\n  }\n\n  async function lancerMaj() {\n    const b = document.getElementById(\'maj-go\');\n    b.disabled = true;\n    b.textContent = \'Téléchargement...\';\n    document.getElementById(\'maj\').classList.remove(\'show\');\n    cancelAnimationFrame(majAnim);\n    // la console reprend la main : la progression y est visible\n    await api(\'installer_maj\');\n  }\n\n  function fermerMaj() {\n    document.getElementById(\'maj\').classList.remove(\'show\');\n    cancelAnimationFrame(majAnim);\n    api(\'ignorer_maj\');\n  }\n\n  // fond animé de la fenêtre : des traits qui filent vers le haut, façon\n  // transfert de données. Dessiné sur canvas, arrêté dès la fermeture.\n  function majFond() {\n    const c = document.getElementById(\'maj-fond\');\n    const g = c.getContext(\'2d\');\n    let L, H, traits;\n    const semer = () => {\n      L = c.width = c.offsetWidth; H = c.height = c.offsetHeight;\n      traits = Array.from({ length: Math.min(70, Math.round(L / 16)) }, () => ({\n        x: Math.random() * L, y: Math.random() * H,\n        v: 0.6 + Math.random() * 2.6, l: 12 + Math.random() * 60,\n        rouge: Math.random() < 0.25\n      }));\n    };\n    semer();\n    const pas = () => {\n      g.clearRect(0, 0, L, H);\n      for (const t of traits) {\n        t.y -= t.v;\n        if (t.y + t.l < 0) { t.y = H + t.l; t.x = Math.random() * L; }\n        const grad = g.createLinearGradient(t.x, t.y, t.x, t.y + t.l);\n        const col = t.rouge ? \'216,26,26\' : \'255,255,255\';\n        grad.addColorStop(0, `rgba(${col},${t.rouge ? .55 : .3})`);\n        grad.addColorStop(1, `rgba(${col},0)`);\n        g.strokeStyle = grad; g.lineWidth = t.rouge ? 1.6 : 1;\n        g.beginPath(); g.moveTo(t.x, t.y); g.lineTo(t.x, t.y + t.l); g.stroke();\n      }\n      majAnim = requestAnimationFrame(pas);\n    };\n    pas();\n  }\n\n  // ---- catégories -----------------------------------------------------\n  let filtre = localStorage.getItem(\'modium-cat\') || \'\';   // \'\' = tout afficher\n\n  function renderCotes() {\n    const cats = st?.categories || [];\n    const packs = st?.packs || [];\n    const compte = c => packs.filter(p => (p.categorie || \'\') === c).length;\n    const sans = packs.filter(p => !p.categorie).length;\n\n    // une catégorie effacée entre-temps ne doit pas laisser une grille vide\n    if (filtre && filtre !== \'__sans\' && !cats.includes(filtre)) filtre = \'\';\n\n    const item = (val, libelle, n) => `\n      <button class="cote${filtre === val ? \' on\' : \'\'}" data-cat="${esc(val)}">\n        <span>${esc(libelle)}</span><span class="n">${n}</span>\n      </button>`;\n\n    let html = item(\'\', \'Tous\', packs.length);\n    for (const c of cats) html += item(c, c, compte(c));\n    if (sans && cats.length) html += item(\'__sans\', \'Sans catégorie\', sans);\n\n    const box = document.getElementById(\'cote-liste\');\n    box.innerHTML = html;\n    box.querySelectorAll(\'.cote\').forEach(b => b.onclick = () => {\n      filtre = b.dataset.cat;\n      localStorage.setItem(\'modium-cat\', filtre);\n      refresh();\n    });\n    // la colonne ne sert à rien tant qu\'aucune catégorie n\'existe\n    document.getElementById(\'cotes\').style.display = cats.length ? \'\' : \'none\';\n  }\n\n  function visibles(packs) {\n    if (!filtre) return packs;\n    if (filtre === \'__sans\') return packs.filter(p => !p.categorie);\n    return packs.filter(p => (p.categorie || \'\') === filtre);\n  }\n\n  function renderCats() {\n    const box = document.getElementById(\'cat-list\');\n    const cats = st?.categories || [];\n    if (!cats.length) {\n      box.innerHTML = \'<div class="cp-empty">Aucune catégorie. Crée-en une ci-dessus.</div>\';\n      return;\n    }\n    const n = c => (st?.packs || []).filter(p => (p.categorie || \'\') === c).length;\n    box.innerHTML = cats.map(c => `<div class="cp-row">\n      <div class="cp-n">${esc(c)}</div>\n      <div class="cp-u">${n(c)} pack${n(c) > 1 ? \'s\' : \'\'}</div>\n      <button class="edit" data-ren="${esc(c)}" title="Renommer">Renommer</button>\n      <button data-rmc="${esc(c)}" title="Supprimer la catégorie">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-ren]\').forEach(b => b.onclick = () => {\n      const v = prompt(\'Nouveau nom de la catégorie :\', b.dataset.ren);\n      if (v && v.trim()) api(\'rename_categorie\', b.dataset.ren, v);\n    });\n    box.querySelectorAll(\'button[data-rmc]\').forEach(b => b.onclick = () => {\n      if (confirm(\'Supprimer la catégorie « \' + b.dataset.rmc + \' » ?\\n\\n\'\n                + \'Les packs qui y sont rangés ne sont pas supprimés, ils se \'\n                + \'retrouvent simplement sans catégorie.\'))\n        api(\'remove_categorie\', b.dataset.rmc);\n    });\n  }\n\n  function addCat() {\n    const i = document.getElementById(\'cat-nom\');\n    if (!i.value.trim()) return;\n    api(\'add_categorie\', i.value);\n    i.value = \'\';\n  }\n\n  function majListeCats(garder) {\n    const sel = document.getElementById(\'cp-cat\');\n    const choix = garder !== undefined ? garder : sel.value;\n    const cats = st?.categories || [];\n    sel.innerHTML = \'<option value="">Sans catégorie</option>\'\n      + cats.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join(\'\')\n      + \'<option value="__new">+ Nouvelle catégorie...</option>\';\n    // une catégorie supprimée entre-temps ne doit pas laisser une valeur morte\n    sel.value = cats.includes(choix) ? choix : \'\';\n  }\n\n  // « + Nouvelle catégorie » : on la crée sans quitter le formulaire\n  document.getElementById(\'cp-cat\').addEventListener(\'change\', async function () {\n    if (this.value !== \'__new\') return;\n    const nom = prompt(\'Nom de la nouvelle catégorie :\');\n    this.value = \'\';\n    if (!nom || !nom.trim()) return;\n    await api(\'add_categorie\', nom);\n    st = await api(\'get_state\');\n    majListeCats(nom.trim().replace(/\\s+/g, \' \').slice(0, 40));\n  });\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    renderCotes();\n    majListeCats();\n    const liste = visibles(st.packs);\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = liste.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = liste.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) {\n      renderCustomList(); renderCats();\n    }\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    majListeCats(p.categorie || \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    majListeCats(\'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    const cat = document.getElementById(\'cp-cat\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld, cat.value);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    renderCats();\n    majListeCats();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      setBusyUI(r.busy);\n      if (r.maj) ouvrirMaj(r.maj);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    appendLog(\'Modium v\' + (st?.version || \'?\') + \' démarré.\', \'ok\');\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    api(\'check_update\');   // signale une nouvelle version, sans rien installer\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
CM={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',c,'cancel','check_update','add_categorie','remove_categorie','rename_categorie','ouvrir_maj','ignorer_maj','installer_maj'}
def CN(api):
	L=b'forbidden';K='127.0.0.1';F='text/plain';I=Ay.token_urlsafe(16);N=CL.replace('__TOKEN__',I).encode(U)
	class O(Bd):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(Av,ctype);A.send_header(Aq,i(E(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def _host_ok(A):C=(A.headers.get('Host')or B).split(']')[-1];return C.split(':')[0]in(K,'localhost')
		def do_GET(B):
			if not B._host_ok():B._send(403,L,F);return
			if B.path in(a,'/index.html'):B._send(200,N,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;C=A.path.join(f,E)if E and not E.startswith(Au)else D
				if C and A.path.exists(C):
					G=A.path.splitext(C)[1].lower()
					with X(C,'rb')as H:B._send(200,H.read(),B1.get(G,'application/octet-stream'))
				else:B._send(404,b'no background',F)
			else:B._send(404,b'not found',F)
		def do_POST(A):
			C=A.path.removeprefix('/api/')
			if not A._host_ok()or C not in CM or not Ay.compare_digest(A.headers.get(Bb)or B,I):A._send(403,L,F);return
			try:
				D=Y(A.headers.get(Aq,0))
				if D>1024**2:A._send(413,b'too large',F);return
				E=M.loads(A.rfile.read(D)or b'[]');J=AE(api,C)(*E);A._send(200,M.dumps(J,ensure_ascii=H).encode(U),'application/json; charset=utf-8')
			except G as K:A._send(500,M.dumps({'error':i(K)}).encode(U),AO)
	J=Be((K,0),O);e.Thread(target=J.serve_forever,daemon=C).start();return J,f"http://127.0.0.1:{J.server_address[1]}/",I
def CO():
	A=AF(B3().get(Z,{}))
	try:print('\n'.join(A))
	except G:pass
	r.exit(1 if A else 0)
def CP():
	if'--check-loaded'in r.argv:CO()
	H=CK();I,E,J=CN(H);K=[J];D=A_.create_window(Bf,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def B(*A):B=' '.join(i(A)for A in A);print(B.encode('ascii',Al).decode(),flush=C)
		def L():
			F.sleep(4)
			try:import urllib.request as C;H=C.Request(E+'api/poll',data=b'[]',method='POST');H.add_header(Bb,K[0]);I=C.urlopen(H,timeout=5).read()[:80];B('SELFTEST urllib POST:',I)
			except G as A:B('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except G as A:B('SELFTEST inject KO:',A)
			F.sleep(4)
			try:B('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));B('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));B('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except G as A:B('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		e.Thread(target=L,daemon=C).start()
	try:A_.start(gui='edgechromium')
	finally:I.shutdown()
if __name__=='__main__':CP()