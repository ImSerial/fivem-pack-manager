BQ='X-Token'
BP='gofile'
BO='Content-Range'
BN='.version'
BM='GTA5.exe'
BL='CitizenFX.ini'
BK='FiveM.app'
BJ='image/jpeg'
BI=reversed
BH=ImportError
Aq='background'
Ap='Content-Type'
Ao='http'
An='gdrive_folder'
Am='file'
Al='Content-Length'
Ak='status'
Aj='_dirs'
Ai='x64'
Ah='.ini'
Ag='replace'
Af='FiveM'
Ae='packs'
Ad='LOCALAPPDATA'
Ac=sorted
AJ='size'
AI='application/json'
AH='le téléchargement'
AG='purged'
AF='.rpf'
AE='.asi'
AD='plugins'
AC='citizen'
AB='.png'
AA=enumerate
A9=getattr
A4='custom'
A3='backups'
A2='update'
A1='mods'
A0=next
v='https://'
u='http://'
t='packs_key'
s=list
r=bool
p='User-Agent'
o='files'
k='{a}'
j='url'
i='.'
h='packs_url'
g=str
f=dict
c='version'
b=isinstance
a='preview'
Z='loaded'
Y=int
X=open
V='/'
U='utf-8'
S='image'
R='gta'
Q=ValueError
P=RuntimeError
O='ok'
N=OSError
L='name'
K='fivem'
H=Exception
G=False
F='err'
E=len
D=''
C=None
B=True
import base64 as Ar,json as M,os as A,re as I,secrets as As,shutil as J,struct as A5,subprocess as AK,sys,tempfile as BR,threading as l,time,urllib.error,urllib.parse,urllib.request,zipfile as At
from http.server import BaseHTTPRequestHandler as BS,ThreadingHTTPServer as BT
import webview as Au
BU='FiveM Pack Manager'
w='FiveMPackManager/2.0'
def BV():
	if A9(sys,'frozen',G):C=A.path.join(A.environ.get(Ad,A.path.dirname(sys.executable)),'FiveMPackManager');A.makedirs(C,exist_ok=B);return C
	return A.path.dirname(A.path.abspath(__file__))
d=BV()
T=A.path.join(d,Ae)
Av=A.path.join(d,'_backups')
AL=A.path.join(d,'state.json')
AM=A.path.join(d,'config.json')
BW={h:'https://uxqt.site/packs-096759e8/packs.json',t:'glt7ExuP7EBzBc56fUzoAmHy618FWBhT'}
def BX():
	B=f(BW);D=[A.path.dirname(A.path.abspath(__file__))]
	if A9(sys,'_MEIPASS',C):D.insert(0,sys._MEIPASS)
	for F in D:
		E=A.path.join(F,'embedded_config.json')
		if A.path.exists(E):
			try:
				with X(E,'r',encoding=U)as G:B.update(M.load(G))
				break
			except(N,M.JSONDecodeError):pass
	return B
BY=BX()
AN=AB,'.jpg','.jpeg','.webp','.gif'
Aw={AB:'image/png','.jpg':BJ,'.jpeg':BJ,'.webp':'image/webp','.gif':'image/gif'}
def Ax(path,data):
	C=path+'.tmp'
	with X(C,'w',encoding=U)as B:M.dump(data,B,indent=2,ensure_ascii=G);B.flush();A.fsync(B.fileno())
	A.replace(C,path)
def A6():
	B=f(BY)
	if A.path.exists(AM):
		try:
			with X(AM,'r',encoding=U)as C:B.update(M.load(C))
		except(N,M.JSONDecodeError):pass
	return B
def e(**B):A=A6();A.update(B);Ax(AM,A)
def BZ():
	F='fivem_path';C=[];E=A6()
	if E.get(F):C.append(E[F])
	G=A.environ.get(Ad,D);C.append(A.path.join(G,Af,BK))
	for B in C:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,BL))or A.path.isdir(A.path.join(B,AC))):return B
def Ba(fivem=C):
	I=fivem;M=A6();E=[M.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(Ad,D),Af,BK))
	for K in J:
		G=A.path.join(K,BL)if K else C
		if G and A.path.exists(G):
			try:
				with X(G,'r',encoding=U,errors=Ag)as O:
					for L in O:
						if L.strip().lower().startswith('ivpath='):E.append(L.split('=',1)[1].strip())
			except N:pass
	try:
		import winreg as H
		for P in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,P)as Q:E.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except N:pass
	except BH:pass
	for B in('C:','D:','E:','F:'):E+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in E:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,BM)):return F
def Bb():
	if A.path.exists(AL):
		try:
			with X(AL,'r',encoding=U)as B:return M.load(B)
		except(N,M.JSONDecodeError):pass
	return{Z:{}}
def Ay(state):Ax(AL,state)
def AO():A.makedirs(T,exist_ok=B);return Ac(B for B in A.listdir(T)if A.path.isdir(A.path.join(T,B))and not B.startswith(i))
def CD(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(i)or G and A.path.splitext(E)[0]==a:continue
			yield A.path.relpath(A.path.join(C,D),B)
def Bc(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(T,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except N:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
Az={}
def Bd(pack_name):
	G=A.path.join(T,pack_name)
	for E in AN:
		B=A.path.join(G,a+E)
		try:C=A.stat(B)
		except N:continue
		D=Az.get(B)
		if D and D[0]==C.st_mtime and D[1]==C.st_size:return D[2]
		try:
			with X(B,'rb')as H:I=Ar.b64encode(H.read()).decode('ascii')
		except N:return
		F=f"data:{Aw[E]};base64,{I}";Az[B]=C.st_mtime,C.st_size,F;return F
def A_(name):
	B=A.path.join(T,name,BN)
	if A.path.exists(B):
		try:
			with X(B,'r',encoding=U)as C:return C.read().strip()
		except N:pass
def W(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise Q(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
Be=I.compile('[<>:"/\\\\|?*\\x00-\\x1f]')
def A7(name):
	C=name;B=(C or D).strip().strip('. ')
	if not B or Be.search(B)or B in(i,'..')or A.path.isabs(C or D):raise Q(f"Nom de pack invalide : {C!r}")
	return B
def B0(path):
	try:return r(A.lstat(path).st_file_attributes&1024)
	except(N,AttributeError):return A.path.islink(path)
def AP():
	try:
		D=AK.run(['tasklist','/FO','CSV'],capture_output=B,text=B,creationflags=BD,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			C=A.split('","',1)[0].strip('"')
			if C.startswith('fivempackmanager'):continue
			if C.startswith((K,'gta5')):return B
		return G
	except H:return G
def x(path,need_bytes,what):
	B=need_bytes;C=J.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise P(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def CE(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except N:pass
	return B
AQ={AC,A1,AD}
B1={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto 5','grand theft auto v legacy','gta v legacy','gtav legacy','gta 5 legacy','gta5 legacy','singleplayer','single player',R}
AR={'enbseries','enbcache'}
Bf=I.compile('^(enb[\\w .()-]*\\.(ini|dll|asi|fx|fxh|dds|bmp|cfg)|d3d(9|10|11|12)\\.dll|d3dcompiler[\\w.]*\\.dll|dxgi\\.dll)$',I.I)
Bg={'.dll',AE,Ah,'.fx','.fxh','.cfg','.json','.yml','.xml'}
def Bh(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=A1]
		for D in G:
			if D.lower().endswith(AF):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def Bi(src,pack_path,rpf_index,log):
	B=A.path.basename(src);C=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in C]
	for(F,G)in AA(H[:-1]):
		if G in(A2,Ai):return A.path.join(*C[F:])
		if G=='dlcpacks':return A.path.join(A2,Ai,*C[F:])
	D=rpf_index.get(B.lower(),[])
	if E(D)==1:return D[0]
	if E(D)>1:log(f"{B} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return B
def AS(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(i):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
AT={K,'five m','five-m','fivem.app','fivem app','fivem files','five m files','fivem folder'}
AU={'reshade-shaders','reshade-presets'}
def Bj(pack_path,log,gta_base=C):
	C=pack_path;I=log;B=[];T=Bh(gta_base);F={}
	def H(key,n=1):F[key]=F.get(key,0)+n
	def O(src):B.append((src,K,A.path.join(A1,Bi(src,C,T,I))));H('rpf vers mods')
	def P(gta_dir,label,prefix=D):
		F=prefix;E=gta_dir
		for(I,K,J)in A.walk(E):
			for C in J:
				if C.startswith(i):continue
				D=A.path.join(I,C)
				if C.lower().endswith(AF):O(D)
				else:G=A.path.relpath(D,E);B.append((D,R,A.path.join(F,G)if F else G));H(f"{label} vers GTA V")
	def Q(dirpath,in_fivem=G,depth=0):
		V='asi vers plugins';S=depth;J=in_fivem;G=dirpath
		if S>12:I(f"Profondeur maximale atteinte, dossier ignoré : {G}");return
		L=Ac(A.listdir(G));T={B.lower()for B in L if A.path.isdir(A.path.join(G,B))};U=A.path.basename(G).lower();J=J or U in AT;W=U in AT or r(T&(AQ|AU));X=not J and(r(T&AR)or any(A.lower().startswith('enb')and A.lower().endswith(Ah)for A in L));Y={A.path.splitext(B)[0].lower()for B in L if B.lower().endswith(AE)}
		for F in L:
			C=A.path.join(G,F);D=F.lower()
			if B0(C):I(f"Lien/jonction ignoré dans le pack : {F}");continue
			if A.path.isdir(C):
				if D in AQ or D in AU:N=E(B);AS(B,C,K,D);H(f"{D} vers FiveM",E(B)-N)
				elif D in B1:P(C,B2(F))
				elif D in AR:
					if J:N=E(B);AS(B,C,K,D);H(f"{D} vers FiveM",E(B)-N)
					else:P(C,B2(F),prefix=D)
				else:Q(C,J,S+1)
			elif not D.startswith(i):
				M=A.path.splitext(D)[1]
				if M==AF:O(C)
				elif X and Bf.match(F):B.append((C,R,F));H('ENB vers GTA V')
				elif M==AE:B.append((C,K,A.path.join(AD,F)));H(V)
				elif M==Ah and A.path.splitext(D)[0]in Y:B.append((C,K,A.path.join(AD,F)));H(V)
				elif W and M in Bg:B.append((C,K,F));H('racine FiveM')
	Q(C)
	if not B:I("Structure standard non détectée — copie de l'archive telle quelle.");AS(B,C,K,D)
	B=[(E,C,B)for(E,C,B)in B if not(C==K and A.path.dirname(B)==D and A.path.splitext(B)[0].lower()==a)];J,L=set(),[]
	for(U,M,N)in B:
		S=M,N.lower()
		if S not in J:J.add(S);L.append((U,M,N))
	V=', '.join(f"{A} : {B}"for(A,B)in F.items())or'rien à installer';I(f"Structure détectée — {V}.");return L
def B2(name):A=name;return A if E(A)<=20 else A[:17]+'...'
def y(e):return(K,e)if b(e,g)else(e[0],e[1])
def AV(target,rel):return f"{target}|{rel}"
def Bk(bases,backup_root,manifest,log):
	M=bases;K=manifest;I=backup_root
	for O in BI(K[o]):
		D,L=y(O);E=M.get(D)
		if not E:continue
		try:
			C=W(E,L)
			if A.path.exists(C):A.remove(C)
			if K[A3].get(AV(D,L)):
				G=A.path.join(I,D,L)
				if A.path.exists(G):J.move(G,C)
		except H:pass
	for(D,N)in BI(K.get(AG,[])):
		E=M.get(D)
		if not E:continue
		try:
			C=W(E,N);G=A.path.join(I,Aj,D,N)
			if A.path.exists(G):
				if A.path.isdir(C):J.rmtree(C,ignore_errors=B)
				J.move(G,C)
		except H:pass
	J.rmtree(I,ignore_errors=B);log("Installation annulée — jeu restauré dans son état d'origine.",F)
m={K:Af,R:'GTA V'}
Bl={K:{AC},R:{A2,Ai,'redistributables','installers','dlc','_commonredist',A1}}
def B3(plan):
	C={}
	for(G,D,F)in plan:
		B=F.replace(V,A.sep).split(A.sep)
		if E(B)>1:C.setdefault((D,B[0].lower()),B[0])
	return C
def Bm(pack_name,bases,state,log,progress):
	e=state;X=pack_name;S=bases;L=log
	if X in e[Z]:raise Q('Ce pack est déjà chargé.')
	if AP():raise P('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	v=W(T,A7(X));I=Bj(v,L,S.get(R))
	if not I:raise Q('Pack vide — aucun fichier à installer.')
	q=[1 for(B,A,C)in I if A==R and not S.get(R)]
	if q:L(f"Dossier GTA V introuvable — {E(q)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);I=[(B,A,C)for(B,A,C)in I if not(A==R and not S.get(R))]
	if not I:raise Q('Rien à installer (dossier GTA V non configuré).')
	i={}
	for(w,Y,A8)in I:
		try:i[Y]=i.get(Y,0)+A.path.getsize(w)
		except N:pass
	for(Y,z)in i.items():
		if S.get(Y):x(S[Y],z,f"l'installation ({m[Y]})")
	a={o:[],A3:{},AG:[]};b={}
	for(c,A1)in e[Z].items():
		if c!=X:
			for r in A1[o]:b[y(r)[0]+'|'+y(r)[1].lower()]=c
	L(f"Installation de « {X} » — {E(I)} fichiers...");j=A.path.join(Av,X);k=0;s=E(I)<=60;A2=max(1,E(I)//10)
	try:
		for((G,f),U)in B3(I).items():
			M=S.get(G)
			if G!=K or not M or not A.path.isdir(M):continue
			g=A0((A for A in A.listdir(M)if A.lower()==f),C)
			if g and g!=U:
				try:A.rename(A.path.join(M,g),A.path.join(M,U));L(f"Dossier {g} renommé en {U}.")
				except N:pass
		for((G,f),U)in B3(I).items():
			M=S.get(G)
			if not M or f in Bl.get(G,set()):continue
			t=W(M,U)
			if not A.path.isdir(t):continue
			A4=f"{G}|{f}{A.sep}";c=A0((B for(A,B)in b.items()if A.startswith(A4)),C)
			if c:L(f"Dossier {U} : contient des fichiers du pack « {c} » — fusion au lieu du remplacement.");continue
			d=A.path.join(j,Aj,G,U);A.makedirs(A.path.dirname(d),exist_ok=B);J.move(t,d);a[AG].append([G,U]);L(f"Dossier existant mis de côté ({m[G]}) : {U} — remplacé proprement. Ton contenu précédent est sauvegardé et sera remis au déchargement du pack.")
		for(l,(A5,G,V))in AA(I):
			M=S[G];h=W(M,V);n=G+'|'+V.lower()
			if n in b:L(f"Attention : {V} appartient déjà au pack « {b[n]} » — écrasé.")
			A.makedirs(A.path.dirname(h),exist_ok=B)
			if A.path.exists(h)and n not in b:
				d=A.path.join(j,G,V);A.makedirs(A.path.dirname(d),exist_ok=B);J.copy2(h,d);a[A3][AV(G,V)]=B;k+=1
				if s:L(f"Sauvegarde de l'original ({m[G]}) : {V}")
			J.copy2(A5,h);a[o].append([G,V])
			if s:L(f"Copie ({m[G]}) : {V}")
			elif(l+1)%A2==0:L(f"{l+1}/{E(I)} fichiers copiés ({k} originaux sauvegardés)...")
			progress(l+1,E(I))
	except H as p:L(f"Erreur pendant l'installation : {p}",F);Bk(S,j,a,L);raise P(f"Installation échouée ({p}) — tout a été annulé.")from p
	e[Z][X]=a;Ay(e);u=sum(1 for A in a[o]if y(A)[0]==R);A6=f" (dont {u} dans GTA V)"if u else D;L(f"« {X} » chargé : {E(I)} fichiers copiés{A6}, {k} originaux sauvegardés.",O)
def Bn(pack_name,bases,state,log,progress):
	d=bases;V=state;M=pack_name;G=log;R=V[Z].get(M)
	if not R:raise Q("Ce pack n'est pas chargé.")
	if AP():raise P('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	S=A.path.join(Av,M);I=R[o];e=set();G(f"Désinstallation de « {M} » — {E(I)} fichiers...");U=0;X=E(I)<=60;i=max(1,E(I)//10)
	for(Y,f)in AA(I):
		C,H=y(f);L=d.get(C)
		if not L:G(f"Cible {m.get(C,C)} introuvable — {H} laissé en place.",F);continue
		try:D=W(L,H)
		except Q as j:G(f"Entrée ignorée : {j}",F);continue
		if A.path.exists(D):
			A.remove(D)
			if X:G(f"Suppression ({m[C]}) : {H}")
		h,k=A.path.join(S,C,H),A.path.join(S,H);l=R[A3].get(AV(C,H))or b(f,g)and R[A3].get(H)
		if l:
			T=h if A.path.exists(h)else k
			if A.path.exists(T):
				A.makedirs(A.path.dirname(D),exist_ok=B);J.move(T,D);U+=1
				if X:G(f"Original restauré : {H}")
		if not X and(Y+1)%i==0:G(f"{Y+1}/{E(I)} fichiers retirés ({U} originaux restaurés)...")
		a=A.path.realpath(L);K=A.path.dirname(D)
		while A.path.commonpath([a,K])==a and K!=a:e.add(K);K=A.path.dirname(K)
		progress(Y+1,E(I))
	for K in Ac(e,key=E,reverse=B):
		try:A.rmdir(K)
		except N:pass
	for(C,c)in R.get(AG,[]):
		L=d.get(C)
		if not L:continue
		try:D=W(L,c)
		except Q:continue
		T=A.path.join(S,Aj,C,c)
		if A.path.exists(T):
			if A.path.isdir(D):J.rmtree(D,ignore_errors=B)
			J.move(T,D);U+=1;G(f"Dossier original restauré ({m[C]}) : {c}")
	if A.path.isdir(S):J.rmtree(S,ignore_errors=B)
	del V[Z][M];Ay(V);G(f"« {M} » déchargé : {E(I)} fichiers retirés, {U} originaux restaurés.",O)
class AW(H):0
A8=C
def Bo(fn):global A8;A8=fn
def AX():
	if A8 is not C and A8():raise AW('Téléchargement annulé.')
Bp=262144
AY=4
Bq=3
class B4(P):0
def Br(exc):
	A=exc
	if b(A,B4):return G
	if b(A,urllib.error.HTTPError):return A.code in(408,429)or A.code>=500
	return B
def Bs(url,headers,offset):
	A=offset;B=f(headers)
	if A:B['Range']=f"bytes={A}-"
	return urllib.request.urlopen(urllib.request.Request(url,headers=B),timeout=60)
def AZ(url,out_path,log,progress,headers=C,make_transform=C,align=1,check_space=B,quiet=G):
	Z=check_space;W=make_transform;U=out_path;O=log;K=headers;K=f(K or{});K.setdefault(p,w);a=A.path.dirname(U)or i;G,I,Q,L=0,0,C,0
	while B:
		AX()
		try:
			with Bs(url,K,G)as J:
				if G and A9(J,Ak,200)!=206:O('Le serveur ne gère pas la reprise — reprise depuis le début.');G=0
				if Q is C:Q=J.headers.get_filename()
				if G==0 and J.headers.get_content_type().startswith('text/'):raise B4('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				if not I:
					R=J.headers.get(BO,D)
					if V in R and R.rsplit(V,1)[1].isdigit():I=Y(R.rsplit(V,1)[1])
					else:S=J.headers.get(Al);I=Y(S)+G if S and S.isdigit()else 0
					if I and Z and G==0:x(a,Y(I*2.3),AH)
				b=W(G)if W else C
				with X(U,'r+b'if G else'wb')as T:
					T.seek(G);T.truncate(G);c=G
					while B:
						AX();M=J.read(Bp)
						if not M:break
						T.write(b(M)if b else M);G+=E(M)
						if I:progress(G,I)
						elif G-c>=256*1024**2:
							c=G
							if Z:x(a,512*1024**2,AH)
							if not quiet:O(f"{G/1048576:.0f} Mo téléchargés...")
			return Q,I or G
		except AW:raise
		except H as N:
			if not Br(N):raise
			L+=1
			if L>AY:raise P(f"Téléchargement échoué après {AY} reprises ({N})")from N
			G-=G%align;d=Bq*L;O(f"Coupure réseau ({N}) — reprise dans {d}s à {G/1048576:.0f} Mo (essai {L}/{AY}).",F);time.sleep(d)
def Aa(url,key):
	A=url
	if not key:return A
	B='&'if'?'in A else'?';return f"{A}{B}key={urllib.parse.quote(key)}"
def B5(url,key):A=urllib.request.Request(Aa(url,key),headers={p:w});return urllib.request.urlopen(A,timeout=30)
def Bt(cfg):
	C=cfg.get(h)
	if not C:return[]
	D=cfg.get(t)
	with B5(C,D)as G:B=M.loads(G.read().decode(U))
	E=C.rsplit(V,1)[0]+V;H=B.get(Ae,B)if b(B,f)else B;F=[]
	for A in H:
		if not b(A,f)or not A.get(L):continue
		try:
			A7(A[L])
			if not A.get(j):A[j]=Aa(urllib.parse.urljoin(E,A[Am]),D)
			if A.get(S)and not A[S].startswith((u,v,'data:')):A[S]=Aa(urllib.parse.urljoin(E,A[S]),D)
		except(KeyError,Q,TypeError):continue
		F.append(A)
	return F
def B6(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return BP,A
	if D in B and'/folders/'in B:
		C=I.search('/folders/([\\w-]+)',A)
		if C:return An,C.group(1)
	if D in B:
		C=I.search('/file/d/([\\w-]+)',A)or I.search('[?&]id=([\\w-]+)',A)
		if C:return Ao,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if'?'in A else'?')+'confirm=t'
	return Ao,A
B7='Mozilla/5.0'
Bu=I.compile('data-id="([\\w-]{20,})"')
Bv=I.compile('<title>([^<]*)</title>')
def B8(url,rng=C):
	A={p:B7}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def B9(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def BA(fid):
	with B8(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(U,Ag)
def Bw(html,fallback):
	B=fallback;C=Bv.search(html)
	if not C:return B
	A=C.group(1).replace('\xa0',' ');A=I.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',D,A).strip();return A or B
def Bx(html,self_id):
	B,C=[],{self_id}
	for A in Bu.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def By(fid):
	for K in range(2):
		try:
			with B8(B9(fid),'bytes=0-0')as A:E=A.headers.get('Content-Disposition',D);L=A.headers.get_content_type();F=A.headers.get(BO,D)
			if'attachment'in E and not L.startswith('text/html'):J=I.search('filename="([^"]+)"',E)or I.search("filename\\*=UTF-8''(.+)",E);M=urllib.parse.unquote(J.group(1))if J else C;N=Y(F.split(V)[-1])if V in F else 0;return B,M,N
			return G,C,0
		except urllib.error.HTTPError as O:
			if O.code in(403,429)and K==0:continue
			return C,C,0
		except H:return C,C,0
	return C,C,0
def Bz(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def Ab(seg):A=seg;A=I.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def B_(folder_id,log):
	B=folder_id;C=[]
	def E(cid,fname,size,prefix):E=prefix;D=fname;B=cid;F=A.path.join(E,Ab(D or B))if E else Ab(D or B);C.append((F,B,size))
	def I(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in Bx(html,fid):
			L,D,F=By(B)
			if L:E(B,D,F,C);continue
			try:G=BA(B)
			except H:E(B,D,F,C);continue
			if not Bz(G):E(B,D,F,C);continue
			K=Ab(Bw(G,B));I(B,G,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');I(B,BA(B),D,0);return C
def C0(folder_id,dest,log,progress):
	I=dest;H=log;D=B_(folder_id,H)
	if not D:raise P('Dossier Drive vide ou illisible (accès restreint ?).')
	F=sum(A for(B,C,A)in D);H(f"{E(D)} fichiers dans le dossier"+(f" ({F/1048576:.0f} Mo)."if F else i))
	if F:x(I,F,AH)
	A.makedirs(I,exist_ok=B);K=0;N=max(1,E(D)//20)
	for(J,(O,Q,S))in AA(D):
		AX();L=W(I,O);A.makedirs(A.path.dirname(L),exist_ok=B);M=K;T,R=AZ(B9(Q),L,H,lambda cur,tot,_b=M:progress(_b+cur,F)if F else C,headers={p:B7},check_space=G,quiet=B);K=M+R
		if(J+1)%N==0 or J+1==E(D):H(f"{J+1}/{E(D)} fichiers téléchargés...")
def C1(url,log):
	J='data';K=url.rstrip(V).split(V)[-1].split('?')[0]
	def B(u,data=C,headers=C):
		A=data;B={p:w,'Accept':AI};B.update(headers or{})
		if A is not C:B[Ap]=AI;A=M.dumps(A).encode()
		D=urllib.request.Request(u,data=A,headers=B);return M.loads(urllib.request.urlopen(D,timeout=30).read().decode())
	D=B('https://api.gofile.io/accounts',data={})[J]['token']
	try:N=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={p:w}),timeout=30).read().decode();Q=I.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',N).group(1)
	except H as E:raise P(f"Gofile ne fonctionne plus avec ce type de lien ({E}). Ré-héberge le pack sur Google Drive ou Mega.")from E
	A=B(f"https://api.gofile.io/contents/{K}?wt={Q}",headers={'Authorization':f"Bearer {D}"})
	if A.get(Ak)!=O:raise P(f"Gofile a refusé le lien ({A.get(Ak)}).")
	R=A[J];S=R.get('children')or{};F=[A for A in S.values()if A.get('type')==Am]
	if not F:raise P('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	G=max(F,key=lambda c:c.get(AJ,0));return G['link'],{'Cookie':f"accountToken={D}"},G.get(L)
def BB(s):s=s.replace('-','+').replace('_',V);return Ar.b64decode(s+'='*(-E(s)%4))
def C2(url,out_path,log,progress):
	K='g';J=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as L,algorithms as N,modes as O
	except BH as U:raise P('Support Mega indisponible (module cryptography manquant).')from U
	E=I.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or I.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not E:raise P('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	V,W=E.group(1),E.group(2);A=A5.unpack('>8I',BB(W));Q=A5.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);X=A5.pack('>2I',A[4],A[5])+J*8;Z=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=M.dumps([{'a':K,K:1,'p':V}]).encode(),headers={Ap:AI,p:w});B=M.loads(urllib.request.urlopen(Z,timeout=30).read().decode())
	if b(B,Y)or b(B,s)and b(B[0],Y):raise P('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	B=B[0];a,C=B[K],Y(B.get('s',0));F='mega_pack'
	try:
		R=L(N.AES(Q),O.CBC(J*16)).decryptor();S=R.update(BB(B['at']))+R.finalize()
		if S.startswith(b'MEGA'):F=M.loads(S[4:].split(J)[0].decode())['n']
	except H:pass
	if C:x(T,Y(C*2.3),AH)
	log(f"Fichier Mega : {F}"+(f" ({C/1048576:.0f} Mo)"if C else D))
	def c(offset):A=X[:8]+A5.pack('>Q',offset//16);return L(N.AES(Q),O.CTR(A)).decryptor().update
	AZ(a,out_path,log,progress,make_transform=c,align=16,check_space=G);return F
def BC(pack,cfg,log,progress):
	V=progress;I=pack;G=log;Y=A7(I[L]);P=W(T,Y);F=P+'.part';A.makedirs(T,exist_ok=B);k,M=BR.mkstemp(suffix='.pack',dir=T);A.close(k);N=C
	try:
		G(f"Téléchargement de « {I[L]} »...")
		if AP():G("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		N,Q=B6(I[j]);K=I.get(Am)
		if A.path.isdir(F):J.rmtree(F,ignore_errors=B)
		if N==An:C0(Q,F,G,V);BG(F,G)
		elif N=='mega':K=C2(Q,M,G,V)or K
		else:
			if N==BP:G('Résolution du lien Gofile...');Z,e,l=C1(Q,G);K=K or l
			else:Z,e=Q,{}
			m,f=AZ(Z,M,G,V,headers=e);K=m or K or A.path.basename(urllib.parse.urlparse(Z).path)
			if K:G(f"Fichier : {K}"+(f" ({f/1048576:.0f} Mo)"if f else D))
		if N!=An:
			G(f"Extraction dans le cache local ({Y})...");BF(M,F,G);R=A.listdir(F)
			if E(R)==1 and A.path.isdir(A.path.join(F,R[0]))and R[0].lower()not in(AC,A1,AD):
				b=A.path.join(F,R[0])
				for h in A.listdir(b):J.move(A.path.join(b,h),A.path.join(F,h))
				A.rmdir(b)
			if not C6(F):BG(F,G)
		if I.get(c):
			with X(A.path.join(F,BN),'w',encoding=U)as d:d.write(g(I[c]))
		if I.get(S):
			try:
				with B5(I[S],C)as n:
					i=A.path.splitext(urllib.parse.urlparse(I[S]).path)[1]or AB
					if i.lower()in AN:
						with X(A.path.join(F,a+i.lower()),'wb')as d:d.write(n.read())
			except H:pass
		if A.path.isdir(P):J.rmtree(P)
		A.replace(F,P);G(f"« {Y} » téléchargé et extrait.",O)
	except BaseException:J.rmtree(F,ignore_errors=B);raise
	finally:
		if A.path.exists(M):A.remove(M)
BD=134217728
BE=3600
C3={'.zip','.rar','.7z'}
q=I.compile('\\.part(\\d+)\\.rar$',I.I)
z=I.compile('\\.r\\d{2}$',I.I)
n=I.compile('\\.(\\d{3})$')
def C4():K='-o{d}';J='7-Zip';I='-inul';H='-ibck';G='WinRAR';F='UnRAR';E='{d}\\';D='-p-';C='-y';B='x';L=[(F,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,D,k,E]),(F,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,D,k,E]),(G,['C:\\Program Files\\WinRAR\\WinRAR.exe',B,H,I,C,D,k,E]),(G,['C:\\Program Files (x86)\\WinRAR\\WinRAR.exe',B,H,I,C,D,k,E]),(J,['C:\\Program Files\\7-Zip\\7z.exe',B,C,'-p',K,k]),(J,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,'-p',K,k]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',k,'-C','{d}'])];return[(C,B)for(C,B)in L if A.path.exists(B[0])]
def BF(archive,dest,log):
	G=log;E=archive;C=dest;A.makedirs(C,exist_ok=B)
	if At.is_zipfile(E):
		try:
			with At.ZipFile(E)as L:
				for M in L.namelist():
					O=A.path.realpath(A.path.join(C,M))
					if not O.startswith(A.path.realpath(C)+A.sep):raise Q(f"Chemin suspect dans l'archive : {M}")
				L.extractall(C)
			return
		except Q:raise
		except H as R:G(f"Zip non lisible en natif ({R}) — essai d'un extracteur externe...")
	N=C4()
	if not N:raise P('Aucun extracteur trouvé — installe WinRAR ou 7-Zip.')
	I=[]
	for(D,J)in N:
		G(f"Extraction avec {D}...");J=[A.replace(k,E).replace('{d}',C)for A in J]
		try:K=AK.run(J,capture_output=B,text=B,creationflags=BD,timeout=BE)
		except AK.TimeoutExpired:I.append(f"{D} : abandon après {BE//60} min (archive protégée par mot de passe ?)");G(f"{D} ne répond plus — abandon.",F);continue
		if K.returncode==0:C5(C);return
		I.append(f"{D} : {(K.stderr or K.stdout).strip()[:200]}")
	raise P('Échec extraction — '+' | '.join(I))
def C5(dest):
	for(E,B,F)in A.walk(dest):
		for C in s(B)+s(F):
			D=A.path.join(E,C)
			if B0(D):
				if C in B:B.remove(C);A.rmdir(D)
				else:A.remove(D)
def BG(dest,log):
	L=log;M=set()
	for S in range(3):
		C=[]
		for(P,T,Q)in A.walk(dest):C+=[A.path.join(P,B)for B in Q if A.path.splitext(B)[1].lower()in C3 or n.search(B)or z.search(B)]
		C=[A for A in C if A not in M]
		if not C:return
		G=[]
		for B in C:
			E=A.path.basename(B)
			if z.search(E):continue
			J=n.search(E)
			if J and J.group(1)!='001':continue
			K=q.search(E)
			if K and Y(K.group(1))>1:continue
			if K:N=q.sub(D,E)
			elif J:O=n.sub(D,E);N=A.path.splitext(O)[0]or O
			else:N=A.path.splitext(E)[0]
			L(f"Archive dans le pack : {E} — extraction...")
			try:BF(B,A.path.join(A.path.dirname(B),N),L)
			except H as R:L(f"Extraction de {E} impossible : {R}",F);M.add(B);continue
			G.append(B)
			if K:I=q.sub(D,B).lower();G+=[A for A in C if A!=B and q.search(A)and q.sub(D,A).lower()==I]
			elif J:I=n.sub(D,B).lower();G+=[A for A in C if A!=B and n.search(A)and n.sub(D,A).lower()==I]
			elif E.lower().endswith('.rar'):I=B[:-4].lower();G+=[A for A in C if z.search(A)and z.sub(D,A).lower()==I]
		for B in C:
			if B in G:
				if A.path.exists(B):A.remove(B)
			elif q.search(B)or z.search(B)or n.search(B):M.add(B)
def C6(dest):
	C=AQ|B1|AT|AU|AR
	for(F,D,E)in A.walk(dest):
		if any(A.lower()in C for A in D):return B
		if any(A.lower().endswith((AF,AE))for A in E):return B
	return G
def C7():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except H:pass
class C8:
	def __init__(A):A.state=Bb();A.cfg=A6();A.fivem=BZ();A.gta=Ba(A.fivem);A.remote_packs=[];A.custom_packs=s(A.cfg.get('custom_packs',[]));A.background=A.cfg.get(Aq);A.busy=G;A._cancel=l.Event();Bo(A._cancel.is_set);A._lock=l.Lock();A._buf_lock=l.Lock();A._logs=[];A._prog=0,0;A._dirty=G
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=B
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,G
		return{'logs':B,'prog':s(A._prog),'busy':A.busy,'dirty':C}
	def _all_remote(C):
		D={A[L]:f(A)for A in C.remote_packs}
		for E in C.custom_packs:A=f(E);A[A4]=B;D[A[L]]=A
		return s(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((u,v)):return B
		D=A.path.join(d,B);return f"/bg?{Y(A.path.getmtime(D))}"if A.path.exists(D)else C
	def get_state(A):
		Q='remote';P='image_link';O='nfiles';J=[];M={A[L]:A for A in A._all_remote()}
		for I in AO():F=M.pop(I,C);N=A_(I);J.append({L:I,AJ:Bc(I),c:N,Z:I in A.state[Z],O:E(A.state[Z].get(I,{}).get(o,[])),S:(F or{}).get(S)or Bd(I),P:(F or{}).get(S),j:(F or{}).get(j),a:(F or{}).get(a),Q:G,A4:r(F and F.get(A4)),A2:r(F and F.get(c)and g(F[c])!=(N or D))})
		for H in M.values():J.append({L:H[L],AJ:H.get(AJ,D),c:H.get(c),Z:G,O:0,S:H.get(S),P:H.get(S),j:H.get(j),a:H.get(a),Q:B,A4:r(H.get(A4)),A2:G})
		return{K:A.fivem,R:A.gta,Ae:J,Aq:A.background_url(),h:A.cfg.get(h,D),t:A.cfg.get(t,D),'background_setting':A.background or D,'busy':A.busy}
	def open_site(B):A.startfile('https://uxqt.site')
	def add_custom_pack(A,name,url,image,preview=D,old_name=D):
		K=image;I=preview;G=url;E=old_name;C=name;C,G,K=C.strip(),G.strip(),K.strip();I,E=I.strip(),E.strip()
		if not C or not G:A._log('Nom et lien requis pour ajouter un pack.',F);return
		try:C=A7(C);B6(G)
		except H as N:A._log(f"Refusé : {N}",F);return
		if not G.lower().startswith((u,v)):A._log('Lien refusé : il faut une URL http(s).',F);return
		if I and not I.startswith((u,v)):A._log('Lien preview refusé (il faut un lien http).',F);return
		P={C,E}-{D};A.custom_packs=[A for A in A.custom_packs if A[L]not in P];M={L:C,j:G}
		if K:M[S]=K
		if I:M[a]=I
		A.custom_packs.append(M);e(custom_packs=A.custom_packs)
		if E and E!=C and E in AO():
			try:J.rmtree(W(T,E),ignore_errors=B)
			except Q:pass
		A._log(f"Pack « {C} » {"modifié"if E else"ajouté"}.",O);A._refresh_ui()
	def preview(D,name):
		E=A0((A for A in D._all_remote()if A[L]==name),C);B=(E or{}).get(a)
		if B and B.startswith((u,v)):A.startfile(B)
		else:D._log('Pas de preview pour ce pack.',F)
	def remove_custom_pack(B,name):
		D=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if D in B.state[Z]:B._log(f"« {D} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[L]!=D];e(custom_packs=B.custom_packs)
		try:E=W(T,D)
		except Q:E=C
		if E and A.path.isdir(E):
			try:J.rmtree(E);B._log(f"Pack « {D} » retiré (fichiers téléchargés supprimés).",O)
			except N as G:B._log(f"Pack « {D} » retiré, mais cache non supprimé : {G}",F)
		else:B._log(f"Pack « {D} » retiré.",O)
		B._refresh_ui()
	def choose_background(A):return C7()or D
	def _set_background(D,bg):
		B=bg;B=B.strip()
		if not B:D.background=C;e(background=C);D._log('Image de fond retirée.',O)
		elif B.startswith((u,v)):D.background=B;e(background=B);D._log('Image de fond (lien) enregistrée.',O)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(d,H))
				except N:pass
			E=A.path.splitext(B)[1].lower();E=E if E in AN else AB;G=Aq+E;J.copy2(B,A.path.join(d,G));D.background=G;e(background=G);D._log('Image de fond enregistrée.',O)
		else:D._log(f"Image introuvable : {B}",F)
	def save_settings(B,url,key,fivem,gta,bg):
		E=fivem;C=gta;B.cfg[h]=url.strip();B.cfg[t]=key.strip();e(packs_url=B.cfg[h],packs_key=B.cfg[t]);E=E.strip()
		if E:
			if A.path.isdir(E):B.fivem=E;e(fivem_path=E);B._log(f"Dossier FiveM : {E}",O)
			else:B._log(f"Dossier introuvable : {E}",F)
		C=C.strip()
		if C:
			if A.path.isdir(C)and A.path.exists(A.path.join(C,BM)):B.gta=C;e(gta_path=C);B._log(f"Dossier GTA V : {C}",O)
			else:B._log(f"Dossier GTA V invalide (GTA5.exe absent) : {C}",F)
		if(bg or D).strip()!=(B.background or D):B._set_background(bg or D)
		B._log('Paramètres enregistrés.',O)
		if B.cfg[h]:B.fetch_remote()
		else:B.remote_packs=[];B._refresh_ui()
	def fetch_remote(A):
		if not A.cfg.get(h):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def C():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=Bt(A.cfg);A._log(f"{E(A.remote_packs)} pack(s) disponibles en ligne.",O)
			except H as B:A.remote_packs=[];A._log(f"Serveur inaccessible : {B}",F)
			A._refresh_ui()
		l.Thread(target=C,daemon=B).start()
	def _run(A,fn):
		def C():
			if not A._lock.acquire(blocking=G):A._log('Une opération est déjà en cours.',F);return
			try:
				A._cancel.clear();A.busy=B;A._refresh_ui()
				try:fn()
				except AW as C:A._log(f"{C} Rien n'a été installé.",F)
				except H as C:A._log(f"Erreur : {C}",F)
				finally:A._cancel.clear();A.busy=G;A._prog=0,0;A._refresh_ui()
			finally:A._lock.release()
		l.Thread(target=C,daemon=B).start()
	def cancel(A):
		if not A.busy:return{O:G}
		if not A._cancel.is_set():A._cancel.set();A._log('Annulation demandée, arrêt en cours...')
		return{O:B}
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return G
		return B
	def load(A,name):
		E=name
		if not A._need_fivem():return
		def B():
			B=A0((A for A in A._all_remote()if A[L]==E),C);F=E in AO();G=B and B.get(c)and g(B[c])!=(A_(E)or D)
			if B and(not F or G):BC(B,A.cfg,A._log,A._progress)
			elif not F:raise Q('Pack introuvable (ni local, ni sur le serveur).')
			Bm(E,{K:A.fivem,R:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:Bn(name,{K:A.fivem,R:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=A0((A for A in A._all_remote()if A[L]==name),C)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:BC(B,A.cfg,A._log,A._progress))
C9='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que uxqt.site (palette igloo dark) :\n     noir pur, verre translucide, lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  /* le bouton annuler prend le margin auto, "vider" se colle à sa droite */\n  #console-head #btn-cancel + button { margin-left: 14px; }\n  #console-head #btn-cancel { color: var(--err); }\n  #console-head #btn-cancel:hover { color: var(--err); text-decoration: underline; }\n  #console-head #btn-cancel:disabled { color: var(--muted); cursor: default;\n                                       text-decoration: none; }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>FiveM Pack Manager</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">uxqt.site &#8599;</button>\n  </header>\n\n  <main><div class="grid" id="grid"></div><div class="empty" id="empty" style="display:none">\n    Aucun pack disponible.<br>\n    Vérifie la connexion au serveur (bouton Actualiser)<br>\n    ou l\'URL configurée dans Options.\n  </div></main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button id="btn-cancel" style="display:none"\n              onclick="cancelDownload()">annuler le téléchargement</button>\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  async function cancelDownload() {\n    const b = document.getElementById(\'btn-cancel\');\n    b.disabled = true;\n    b.textContent = \'annulation...\';\n    try { await api(\'cancel\'); } catch (e) { appendLog(\'Annulation : \' + e, \'err\'); }\n  }\n\n  // visible seulement pendant une action ; l\'arrêt n\'est effectif que si on est\n  // encore en phase de téléchargement (l\'installation, elle, va au bout)\n  function setBusyUI(busy) {\n    const b = document.getElementById(\'btn-cancel\');\n    if (!busy) {\n      b.style.display = \'none\';\n      b.disabled = false;\n      b.textContent = \'annuler le téléchargement\';\n    } else if (b.style.display === \'none\') {\n      b.style.display = \'\';\n    }\n  }\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = st.packs.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = st.packs.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) renderCustomList();\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      setBusyUI(r.busy);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    appendLog(\'FiveM Pack Manager démarré.\', \'ok\');\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
CA={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',a,'cancel'}
def CB(api):
	L=b'forbidden';K='127.0.0.1';F='text/plain';I=As.token_urlsafe(16);N=C9.replace('__TOKEN__',I).encode(U)
	class O(BS):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(Ap,ctype);A.send_header(Al,g(E(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def _host_ok(A):B=(A.headers.get('Host')or D).split(']')[-1];return B.split(':')[0]in(K,'localhost')
		def do_GET(B):
			if not B._host_ok():B._send(403,L,F);return
			if B.path in(V,'/index.html'):B._send(200,N,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;D=A.path.join(d,E)if E and not E.startswith(Ao)else C
				if D and A.path.exists(D):
					G=A.path.splitext(D)[1].lower()
					with X(D,'rb')as H:B._send(200,H.read(),Aw.get(G,'application/octet-stream'))
				else:B._send(404,b'no background',F)
			else:B._send(404,b'not found',F)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if not A._host_ok()or B not in CA or not As.compare_digest(A.headers.get(BQ)or D,I):A._send(403,L,F);return
			try:
				C=Y(A.headers.get(Al,0))
				if C>1024**2:A._send(413,b'too large',F);return
				E=M.loads(A.rfile.read(C)or b'[]');J=A9(api,B)(*E);A._send(200,M.dumps(J,ensure_ascii=G).encode(U),'application/json; charset=utf-8')
			except H as K:A._send(500,M.dumps({'error':g(K)}).encode(U),AI)
	J=BT((K,0),O);l.Thread(target=J.serve_forever,daemon=B).start();return J,f"http://127.0.0.1:{J.server_address[1]}/",I
def CC():
	G=C8();I,E,J=CB(G);K=[J];D=Au.create_window(BU,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def C(*A):C=' '.join(g(A)for A in A);print(C.encode('ascii',Ag).decode(),flush=B)
		def L():
			F.sleep(4)
			try:import urllib.request as B;G=B.Request(E+'api/poll',data=b'[]',method='POST');G.add_header(BQ,K[0]);I=B.urlopen(G,timeout=5).read()[:80];C('SELFTEST urllib POST:',I)
			except H as A:C('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except H as A:C('SELFTEST inject KO:',A)
			F.sleep(4)
			try:C('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));C('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));C('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except H as A:C('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		l.Thread(target=L,daemon=B).start()
	try:Au.start(gui='edgechromium')
	finally:I.shutdown()
if __name__=='__main__':CC()