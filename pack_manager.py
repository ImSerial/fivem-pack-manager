Ay='X-Token'
Ax='gofile'
Aw='plugins'
Av='.version'
Au='GTA5.exe'
At='CitizenFX.ini'
As='FiveM.app'
Ar='image/jpeg'
Aq=ImportError
AW='background'
AV='Content-Length'
AU='Content-Type'
AT='le téléchargement'
AS='http'
AR='gdrive_folder'
AQ='https://'
AP='http://'
AO='file'
AN='replace'
AM='citizen'
AL='FiveM'
AK='packs'
AJ='LOCALAPPDATA'
AI=enumerate
AH=sorted
AG=getattr
A5='size'
A4='application/json'
A3='wb'
A2='url'
A1='mods'
A0='preview'
z='.png'
y=max
x=dict
s='custom'
r='packs_key'
q='?'
p='backups'
o='.'
n='r'
m=list
j='{a}'
i=isinstance
f='packs_url'
e='User-Agent'
d='files'
c='/'
b=str
Y='version'
X=int
W=ValueError
V='gta'
U='loaded'
T='image'
S=OSError
P='fivem'
O='utf-8'
M='ok'
L=False
K=RuntimeError
J=open
I=Exception
H='name'
F='err'
E=''
D=None
C=True
B=len
import base64 as AX,json as G,os as A,re as Q,secrets,shutil as R,struct as A6,subprocess as AY,sys as t,tempfile as Az,threading as g,urllib.parse,urllib.request,zipfile as AZ
from http.server import BaseHTTPRequestHandler as A_,ThreadingHTTPServer as B0
import webview as Aa
B1='FiveM Pack Manager'
h='FiveMPackManager/2.0'
def B2():
	if AG(t,'frozen',L):B=A.path.join(A.environ.get(AJ,A.path.dirname(t.executable)),'FiveMPackManager');A.makedirs(B,exist_ok=C);return B
	return A.path.dirname(A.path.abspath(__file__))
Z=B2()
N=A.path.join(Z,AK)
Ab=A.path.join(Z,'_backups')
A7=A.path.join(Z,'state.json')
A8=A.path.join(Z,'config.json')
def B3():
	B=[A.path.dirname(A.path.abspath(__file__))]
	if AG(t,'_MEIPASS',D):B.insert(0,t._MEIPASS)
	for E in B:
		C=A.path.join(E,'embedded_config.json')
		if A.path.exists(C):
			try:
				with J(C,n,encoding=O)as F:return G.load(F)
			except(S,G.JSONDecodeError):pass
	return{}
B4=B3()
A9=z,'.jpg','.jpeg','.webp','.gif'
Ac={z:'image/png','.jpg':Ar,'.jpeg':Ar,'.webp':'image/webp','.gif':'image/gif'}
def u():
	B=x(B4)
	if A.path.exists(A8):
		try:
			with J(A8,n,encoding=O)as C:B.update(G.load(C))
		except(S,G.JSONDecodeError):pass
	return B
def a(**B):
	A=u();A.update(B)
	with J(A8,'w',encoding=O)as C:G.dump(A,C,indent=2)
def B5():
	F='fivem_path';C=[];D=u()
	if D.get(F):C.append(D[F])
	G=A.environ.get(AJ,E);C.append(A.path.join(G,AL,As))
	for B in C:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,At))or A.path.isdir(A.path.join(B,AM))):return B
def B6(fivem=D):
	I=fivem;N=u();C=[N.get('gta_path')];K=[I]if I else[];K.append(A.path.join(A.environ.get(AJ,E),AL,As))
	for L in K:
		G=A.path.join(L,At)if L else D
		if G and A.path.exists(G):
			try:
				with J(G,n,encoding=O,errors=AN)as P:
					for M in P:
						if M.strip().lower().startswith('ivpath='):C.append(M.split('=',1)[1].strip())
			except S:pass
	try:
		import winreg as H
		for Q in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,Q)as R:C.append(H.QueryValueEx(R,'InstallFolder')[0])
			except S:pass
	except Aq:pass
	for B in('C:','D:','E:','F:'):C+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in C:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,Au)):return F
def B7():
	if A.path.exists(A7):
		try:
			with J(A7,n,encoding=O)as B:return G.load(B)
		except(S,G.JSONDecodeError):pass
	return{U:{}}
def Ad(state):
	with J(A7,'w',encoding=O)as A:G.dump(state,A,indent=2,ensure_ascii=L)
def Ae():A.makedirs(N,exist_ok=C);return AH(B for B in A.listdir(N)if A.path.isdir(A.path.join(N,B))and not B.startswith(o))
def BZ(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(o)or G and A.path.splitext(E)[0]==A0:continue
			yield A.path.relpath(A.path.join(C,D),B)
def B8(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(N,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except S:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
def Af(pack_name):
	D=A.path.join(N,pack_name)
	for B in A9:
		C=A.path.join(D,A0+B)
		if A.path.exists(C):
			try:
				with J(C,'rb')as E:F=AX.b64encode(E.read()).decode('ascii')
				return f"data:{Ac[B]};base64,{F}"
			except S:return
def Ag(name):
	B=A.path.join(N,name,Av)
	if A.path.exists(B):
		try:
			with J(B,n,encoding=O)as C:return C.read().strip()
		except S:pass
def k(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise W(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
def AA():
	try:
		D=AY.run(['tasklist','/FO','CSV'],capture_output=C,text=C,creationflags=Ap,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			B=A.split('","',1)[0].strip('"')
			if B.startswith('fivempackmanager'):continue
			if B.startswith((P,'gta5')):return C
		return L
	except I:return L
def v(path,need_bytes,what):
	B=need_bytes;C=R.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise K(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def Ba(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except S:pass
	return B
Ah={AM,A1,Aw}
B9={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto v legacy',V}
BA={'.dll','.asi','.ini','.fx','.cfg','.json','.yml'}
def AB(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(o):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
def BB(pack_path,log):
	b='.rpf';a='racine FiveM';N='rpf vers mods';L=pack_path;C=[];O=[]
	for(H,I,i)in A.walk(L):
		if any(A.lower()in Ah for A in I):O.append(H)
	if not O:log("Structure standard non détectée — copie de l'archive telle quelle.");AB(C,L,P,E);return[(C,D,B)for(C,D,B)in C if not(A.path.dirname(B)==E and A.path.splitext(B)[0].lower()==A0)]
	Q=min(O,key=lambda p:B(A.path.relpath(p,L).split(A.sep)));D={}
	for R in AH(A.listdir(Q)):
		M=A.path.join(Q,R);G=R.lower()
		if A.path.isdir(M):
			if G in Ah:S=B(C);AB(C,M,P,G);D[f"{G} vers FiveM"]=B(C)-S
			elif G in('reshade-shaders','reshade-presets'):S=B(C);AB(C,M,P,G);D[f"{G} vers FiveM"]=B(C)-S
		elif A.path.splitext(G)[1]in BA:C.append((M,P,R));D[a]=D.get(a,0)+1
	c=A.path.realpath(Q)
	for(H,I,d)in A.walk(L):
		if A.path.realpath(H)==c:I[:]=[];continue
		for J in m(I):
			if J.lower()in B9:
				T=A.path.join(H,J)
				for(e,j,f)in A.walk(T):
					for F in f:
						if F.startswith(o):continue
						K=A.path.join(e,F)
						if F.lower().endswith(b):C.append((K,P,A.path.join(A1,F)));D[N]=D.get(N,0)+1
						else:g=A.path.relpath(K,T);C.append((K,V,g));D[f"{Ai(J)} vers GTA V"]=D.get(f"{Ai(J)} vers GTA V",0)+1
				I.remove(J)
		for F in d:
			if F.lower().endswith(b):C.append((A.path.join(H,F),P,A.path.join(A1,F)));D[N]=D.get(N,0)+1
	U,W=set(),[]
	for(K,X,Y)in C:
		Z=X,Y.lower()
		if Z not in U:U.add(Z);W.append((K,X,Y))
	h=', '.join(f"{A} : {B}"for(A,B)in D.items())or'rien à installer';log(f"Structure détectée — {h}.");return W
def Ai(name):A=name;return A if B(A)<=20 else A[:17]+'...'
def l(e):return(P,e)if i(e,b)else(e[0],e[1])
def AC(target,rel):return f"{target}|{rel}"
def BC(bases,backup_root,manifest,log):
	H=manifest;G=backup_root
	for L in reversed(H[d]):
		B,D=l(L);J=bases.get(B)
		if not J:continue
		try:
			E=k(J,D)
			if A.path.exists(E):A.remove(E)
			if H[p].get(AC(B,D)):
				K=A.path.join(G,B,D)
				if A.path.exists(K):R.move(K,E)
		except I:pass
	R.rmtree(G,ignore_errors=C);log("Installation annulée — jeu restauré dans son état d'origine.",F)
w={P:AL,V:'GTA V'}
def BD(pack_name,bases,state,log,progress):
	S=state;O=bases;J=pack_name;G=log
	if J in S[U]:raise W('Ce pack est déjà chargé.')
	if AA():raise K('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	m=A.path.join(N,J);D=BB(m,G)
	if not D:raise W('Pack vide — aucun fichier à installer.')
	c=[1 for(B,A,C)in D if A==V and not O.get(V)]
	if c:G(f"Dossier GTA V introuvable — {B(c)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);D=[(B,A,C)for(B,A,C)in D if not(A==V and not O.get(V))]
	if not D:raise W('Rien à installer (dossier GTA V non configuré).')
	n=sum(A.path.getsize(B)for(B,C,D)in D if A.path.exists(B));v(O[P],n,"l'installation");Q={d:[],p:{}};T={}
	for(e,o)in S[U].items():
		if e!=J:
			for f in o[d]:T[l(f)[0]+'|'+l(f)[1].lower()]=e
	G(f"Installation de « {J} » — {B(D)} fichiers...");g=A.path.join(Ab,J);Y=0;h=B(D)<=60;q=y(1,B(D)//10)
	try:
		for(Z,(r,L,H))in AI(D):
			s=O[L];X=k(s,H);a=L+'|'+H.lower()
			if a in T:G(f"Attention : {H} appartient déjà au pack « {T[a]} » — écrasé.")
			A.makedirs(A.path.dirname(X),exist_ok=C)
			if A.path.exists(X)and a not in T:
				i=A.path.join(g,L,H);A.makedirs(A.path.dirname(i),exist_ok=C);R.copy2(X,i);Q[p][AC(L,H)]=C;Y+=1
				if h:G(f"Sauvegarde de l'original ({w[L]}) : {H}")
			R.copy2(r,X);Q[d].append([L,H])
			if h:G(f"Copie ({w[L]}) : {H}")
			elif(Z+1)%q==0:G(f"{Z+1}/{B(D)} fichiers copiés ({Y} originaux sauvegardés)...")
			progress(Z+1,B(D))
	except I as b:G(f"Erreur pendant l'installation : {b}",F);BC(O,g,Q,G);raise K(f"Installation échouée ({b}) — tout a été annulé.")from b
	S[U][J]=Q;Ad(S);j=sum(1 for A in Q[d]if l(A)[0]==V);t=f" (dont {j} dans GTA V)"if j else E;G(f"« {J} » chargé : {B(D)} fichiers copiés{t}, {Y} originaux sauvegardés.",M)
def BE(pack_name,bases,state,log,progress):
	P=state;J=pack_name;E=log;N=P[U].get(J)
	if not N:raise W("Ce pack n'est pas chargé.")
	if AA():raise K('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	O=A.path.join(Ab,J);G=N[d];Y=set();E(f"Désinstallation de « {J} » — {B(G)} fichiers...");Q=0;T=B(G)<=60;e=y(1,B(G)//10)
	for(V,Z)in AI(G):
		H,D=l(Z);X=bases.get(H)
		if not X:E(f"Cible {w.get(H,H)} introuvable — {D} laissé en place.",F);continue
		try:L=k(X,D)
		except W as f:E(f"Entrée ignorée : {f}",F);continue
		if A.path.exists(L):
			A.remove(L)
			if T:E(f"Suppression ({w[H]}) : {D}")
		a,g=A.path.join(O,H,D),A.path.join(O,D);h=N[p].get(AC(H,D))or i(Z,b)and N[p].get(D)
		if h:
			c=a if A.path.exists(a)else g
			if A.path.exists(c):
				A.makedirs(A.path.dirname(L),exist_ok=C);R.move(c,L);Q+=1
				if T:E(f"Original restauré : {D}")
		if not T and(V+1)%e==0:E(f"{V+1}/{B(G)} fichiers retirés ({Q} originaux restaurés)...")
		I=A.path.dirname(L)
		while B(I)>B(X):Y.add(I);I=A.path.dirname(I)
		progress(V+1,B(G))
	for I in AH(Y,key=B,reverse=C):
		try:A.rmdir(I)
		except S:pass
	if A.path.isdir(O):R.rmtree(O,ignore_errors=C)
	del P[U][J];Ad(P);E(f"« {J} » déchargé : {B(G)} fichiers retirés, {Q} originaux restaurés.",M)
def AD(url,key):
	A=url
	if not key:return A
	B='&'if q in A else q;return f"{A}{B}key={urllib.parse.quote(key)}"
def Aj(url,key):A=urllib.request.Request(AD(url,key),headers={e:h});return urllib.request.urlopen(A,timeout=30)
def BF(cfg):
	C=cfg.get(f)
	if not C:return[]
	D=cfg.get(r)
	with Aj(C,D)as H:B=G.loads(H.read().decode(O))
	E=C.rsplit(c,1)[0]+c;F=B.get(AK,B)if i(B,x)else B
	for A in F:
		if not A.get(A2):A[A2]=AD(urllib.parse.urljoin(E,A[AO]),D)
		if A.get(T)and not A[T].startswith((AP,AQ,'data:')):A[T]=AD(urllib.parse.urljoin(E,A[T]),D)
	return F
def Ak(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return Ax,A
	if D in B and'/folders/'in B:
		C=Q.search('/folders/([\\w-]+)',A)
		if C:return AR,C.group(1)
	if D in B:
		C=Q.search('/file/d/([\\w-]+)',A)or Q.search('[?&]id=([\\w-]+)',A)
		if C:return AS,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if q in A else q)+'confirm=t'
	return AS,A
BG='Mozilla/5.0'
BH=Q.compile('data-id="([\\w-]{20,})"')
BI=Q.compile('<title>([^<]*)</title>')
def AE(url,rng=D):
	A={e:BG}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def Al(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def Am(fid):
	with AE(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(O,AN)
def BJ(html,fallback):
	B=fallback;C=BI.search(html)
	if not C:return B
	A=C.group(1).replace('\xa0',' ');A=Q.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',E,A).strip();return A or B
def BK(html,self_id):
	B,C=[],{self_id}
	for A in BH.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def BL(fid):
	for H in range(2):
		try:
			with AE(Al(fid),'bytes=0-0')as A:B=A.headers.get('Content-Disposition',E);J=A.headers.get_content_type();F=A.headers.get('Content-Range',E)
			if'attachment'in B and not J.startswith('text/html'):G=Q.search('filename="([^"]+)"',B)or Q.search("filename\\*=UTF-8''(.+)",B);K=urllib.parse.unquote(G.group(1))if G else D;M=X(F.split(c)[-1])if c in F else 0;return C,K,M
			return L,D,0
		except urllib.error.HTTPError as N:
			if N.code in(403,429)and H==0:continue
			return D,D,0
		except I:return D,D,0
	return D,D,0
def BM(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def AF(seg):A=seg;A=Q.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def BN(folder_id,log):
	B=folder_id;C=[]
	def D(cid,fname,size,prefix):E=prefix;D=fname;B=cid;F=A.path.join(E,AF(D or B))if E else AF(D or B);C.append((F,B,size))
	def H(fid,html,prefix,depth):
		J=depth;C=prefix
		if J>8:return
		for B in BK(html,fid):
			L,E,F=BL(B)
			if L:D(B,E,F,C);continue
			try:G=Am(B)
			except I:D(B,E,F,C);continue
			if not BM(G):D(B,E,F,C);continue
			K=AF(BJ(G,B));H(B,G,A.path.join(C,K)if C else K,J+1)
	log('Lecture du dossier Google Drive...');H(B,Am(B),E,0);return C
def BO(folder_id,dest,log,progress):
	G=log;F=dest;D=BN(folder_id,G)
	if not D:raise K('Dossier Drive vide ou illisible (accès restreint ?).')
	E=sum(A for(B,C,A)in D);G(f"{B(D)} fichiers dans le dossier"+(f" ({E/1048576:.0f} Mo)."if E else o))
	if E:v(F,E,AT)
	A.makedirs(F,exist_ok=C);L=0;N=y(1,B(D)//20)
	for(H,(O,P,S))in AI(D):
		M=k(F,O);A.makedirs(A.path.dirname(M),exist_ok=C)
		with AE(Al(P))as Q,J(M,A3)as R:
			while C:
				I=Q.read(262144)
				if not I:break
				R.write(I);L+=B(I)
				if E:progress(L,E)
		if(H+1)%N==0 or H+1==B(D):G(f"{H+1}/{B(D)} fichiers téléchargés...")
def BP(url,log):
	N='status';L='data';O=url.rstrip(c).split(c)[-1].split(q)[0]
	def B(u,data=D,headers=D):
		A=data;B={e:h,'Accept':A4};B.update(headers or{})
		if A is not D:B[AU]=A4;A=G.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return G.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[L]['token']
	try:P=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={e:h}),timeout=30).read().decode();R=Q.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',P).group(1)
	except I as E:raise K(f"Gofile : jeton du site introuvable ({E}).")from E
	A=B(f"https://api.gofile.io/contents/{O}?wt={R}",headers={'Authorization':f"Bearer {C}"})
	if A.get(N)!=M:raise K(f"Gofile a refusé le lien ({A.get(N)}).")
	S=A[L];T=S.get('children')or{};F=[A for A in T.values()if A.get('type')==AO]
	if not F:raise K('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	J=y(F,key=lambda c:c.get(A5,0));return J['link'],{'Cookie':f"accountToken={C}"},J.get(H)
def An(s):s=s.replace('-','+').replace('_',c);return AX.b64decode(s+'='*(-B(s)%4))
def BQ(url,out_path,log,progress):
	P='g';O=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as R,algorithms as S,modes as T
	except Aq as b:raise K('Support Mega indisponible (module cryptography manquant).')from b
	H=Q.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or Q.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not H:raise K('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	c,d=H.group(1),H.group(2);A=A6.unpack('>8I',An(d));U=A6.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);f=A6.pack('>2I',A[4],A[5])+O*8;g=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=G.dumps([{'a':P,P:1,'p':c}]).encode(),headers={AU:A4,e:h});D=G.loads(urllib.request.urlopen(g,timeout=30).read().decode())
	if i(D,X)or i(D,m)and i(D[0],X):raise K('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	D=D[0];j,F=D[P],X(D.get('s',0));L='mega_pack'
	try:
		V=R(S.AES(U),T.CBC(O*16)).decryptor();W=V.update(An(D['at']))+V.finalize()
		if W.startswith(b'MEGA'):L=G.loads(W[4:].split(O)[0].decode())['n']
	except I:pass
	if F:v(N,X(F*2.3),AT)
	log(f"Fichier Mega : {L}"+(f" ({F/1048576:.0f} Mo)"if F else E));Y=R(S.AES(U),T.CTR(f)).decryptor();Z=0
	with urllib.request.urlopen(urllib.request.Request(j,headers={e:h}),timeout=60)as k,J(out_path,A3)as a:
		while C:
			M=k.read(262144)
			if not M:break
			a.write(Y.update(M));Z+=B(M)
			if F:progress(Z,F)
		a.write(Y.finalize())
	return L
def Ao(pack,cfg,log,progress):
	a=progress;L=log;F=pack;G=A.path.join(N,F[H]);A.makedirs(N,exist_ok=C);n,U=Az.mkstemp(suffix='.pack',dir=N);A.close(n)
	try:
		L(f"Téléchargement de « {F[H]} »...")
		if AA():L("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		V,W=Ak(F[A2]);P=F.get(AO)
		if V==AR:
			if A.path.isdir(G):R.rmtree(G)
			BO(W,G,L,a)
		elif V=='mega':P=BQ(W,U,L,a)or P
		else:
			if V==Ax:L('Résolution du lien Gofile...');c,i,o=BP(W,L);P=P or o
			else:c,i=W,{}
			j={e:h};j.update(i)
			with urllib.request.urlopen(urllib.request.Request(c,headers=j),timeout=60)as Q:
				P=Q.headers.get_filename()or P or A.path.basename(urllib.parse.urlparse(c).path)
				if Q.headers.get_content_type().startswith('text/'):raise K('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				S=X(Q.headers.get(AV,0))
				if S:v(N,X(S*2.3),AT)
				if P:L(f"Fichier : {P}"+(f" ({S/1048576:.0f} Mo)"if S else E))
				k=0
				with J(U,A3)as p:
					while C:
						d=Q.read(262144)
						if not d:break
						p.write(d);k+=B(d)
						if S:a(k,S)
		if V!=AR:
			L(f"Extraction dans le cache local ({F[H]})...")
			if A.path.isdir(G):R.rmtree(G)
			BS(U,G,L);Z=A.listdir(G)
			if B(Z)==1 and A.path.isdir(A.path.join(G,Z[0]))and Z[0].lower()not in(AM,A1,Aw):
				f=A.path.join(G,Z[0])
				for l in A.listdir(f):R.move(A.path.join(f,l),A.path.join(G,l))
				A.rmdir(f)
		if F.get(Y):
			with J(A.path.join(G,Av),'w',encoding=O)as g:g.write(b(F[Y]))
		if F.get(T)and not Af(F[H]):
			try:
				with Aj(F[T],D)as Q:
					m=A.path.splitext(urllib.parse.urlparse(F[T]).path)[1]or z
					if m.lower()in A9:
						with J(A.path.join(G,A0+m.lower()),A3)as g:g.write(Q.read())
			except I:pass
		L(f"« {F[H]} » téléchargé et extrait.",M)
	finally:
		if A.path.exists(U):A.remove(U)
Ap=134217728
def BR():
	H='-o{d}';G='7-Zip';F='{d}\\';E='WinRAR';C='-y';B='x';I=[(E,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,j,F]),(E,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,j,F]),(G,['C:\\Program Files\\7-Zip\\7z.exe',B,C,H,j]),(G,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,H,j]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',j,'-C','{d}'])]
	for(J,D)in I:
		if A.path.exists(D[0]):return J,D
def BS(archive,dest,log):
	D=archive;B=dest;A.makedirs(B,exist_ok=C)
	if AZ.is_zipfile(D):
		with AZ.ZipFile(D)as G:
			for H in G.namelist():
				L=A.path.realpath(A.path.join(B,H))
				if not L.startswith(A.path.realpath(B)+A.sep):raise W(f"Chemin suspect dans l'archive : {H}")
			G.extractall(B)
		return
	I=BR()
	if not I:raise K('Aucun extracteur RAR trouvé — installe WinRAR ou 7-Zip.')
	J,E=I;log(f"Extraction avec {J}...");E=[A.replace(j,D).replace('{d}',B)for A in E];F=AY.run(E,capture_output=C,text=C,creationflags=Ap)
	if F.returncode!=0:raise K(f"Échec extraction ({J}) : {(F.stderr or F.stdout).strip()[:300]}")
def BT():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except I:pass
class BU:
	def __init__(A):A.state=B7();A.cfg=u();A.fivem=B5();A.gta=B6(A.fivem);A.remote_packs=[];A.custom_packs=m(A.cfg.get('custom_packs',[]));A.background=A.cfg.get(AW);A.busy=L;A._lock=g.Lock();A._buf_lock=g.Lock();A._logs=[];A._prog=0,0;A._dirty=L
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=C
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,L
		return{'logs':B,'prog':m(A._prog),'busy':A.busy,'dirty':C}
	def _all_remote(B):
		D={A[H]:x(A)for A in B.remote_packs}
		for E in B.custom_packs:A=x(E);A[s]=C;D[A[H]]=A
		return m(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((AP,AQ)):return B
		C=A.path.join(Z,B);return f"/bg?{X(A.path.getmtime(C))}"if A.path.exists(C)else D
	def get_state(A):
		Q='update';O='remote';N='nfiles';J=[];K={A[H]:A for A in A._all_remote()}
		for F in Ae():G=K.pop(F,D);M=Ag(F);J.append({H:F,A5:B8(F),Y:M,U:F in A.state[U],N:B(A.state[U].get(F,{}).get(d,[])),T:Af(F)or(G or{}).get(T),O:L,s:bool(G and G.get(s)),Q:bool(G and G.get(Y)and b(G[Y])!=(M or E))})
		for I in K.values():J.append({H:I[H],A5:I.get(A5,E),Y:I.get(Y),U:L,N:0,T:I.get(T),O:C,s:bool(I.get(s)),Q:L})
		return{P:A.fivem,V:A.gta,AK:J,AW:A.background_url(),f:A.cfg.get(f,E),r:A.cfg.get(r,E),'background_setting':A.background or E,'busy':A.busy}
	def open_site(B):A.startfile('https://uxqt.site')
	def add_custom_pack(A,name,url,image):
		D=image;C=url;B=name;B,C,D=B.strip(),C.strip(),D.strip()
		if not B or not C:A._log('Nom et lien requis pour ajouter un pack.',F);return
		try:Ak(C)
		except I as G:A._log(f"Lien refusé : {G}",F);return
		A.custom_packs=[A for A in A.custom_packs if A[H]!=B];E={H:B,A2:C}
		if D:E[T]=D
		A.custom_packs.append(E);a(custom_packs=A.custom_packs);A._log(f"Pack « {B} » ajouté.",M);A._refresh_ui()
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if C in B.state[U]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[H]!=C];a(custom_packs=B.custom_packs)
		try:E=k(N,C)
		except W:E=D
		if E and A.path.isdir(E):
			try:R.rmtree(E);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",M)
			except S as G:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {G}",F)
		else:B._log(f"Pack « {C} » retiré.",M)
		B._refresh_ui()
	def choose_background(A):return BT()or E
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=D;a(background=D);C._log('Image de fond retirée.',M)
		elif B.startswith((AP,AQ)):C.background=B;a(background=B);C._log('Image de fond (lien) enregistrée.',M)
		elif A.path.isfile(B):
			for H in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(Z,H))
				except S:pass
			E=A.path.splitext(B)[1].lower();E=E if E in A9 else z;G=AW+E;R.copy2(B,A.path.join(Z,G));C.background=G;a(background=G);C._log('Image de fond enregistrée.',M)
		else:C._log(f"Image introuvable : {B}",F)
	def save_settings(B,url,key,fivem,gta,bg):
		D=fivem;C=gta;B.cfg[f]=url.strip();B.cfg[r]=key.strip();a(packs_url=B.cfg[f],packs_key=B.cfg[r]);D=D.strip()
		if D:
			if A.path.isdir(D):B.fivem=D;a(fivem_path=D);B._log(f"Dossier FiveM : {D}",M)
			else:B._log(f"Dossier introuvable : {D}",F)
		C=C.strip()
		if C:
			if A.path.isdir(C)and A.path.exists(A.path.join(C,Au)):B.gta=C;a(gta_path=C);B._log(f"Dossier GTA V : {C}",M)
			else:B._log(f"Dossier GTA V invalide (GTA5.exe absent) : {C}",F)
		if(bg or E).strip()!=(B.background or E):B._set_background(bg or E)
		B._log('Paramètres enregistrés.',M)
		if B.cfg[f]:B.fetch_remote()
		else:B.remote_packs=[];B._refresh_ui()
	def fetch_remote(A):
		if not A.cfg.get(f):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def D():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=BF(A.cfg);A._log(f"{B(A.remote_packs)} pack(s) disponibles en ligne.",M)
			except I as C:A.remote_packs=[];A._log(f"Serveur inaccessible : {C}",F)
			A._refresh_ui()
		g.Thread(target=D,daemon=C).start()
	def _run(A,fn):
		def B():
			with A._lock:
				A.busy=C;A._refresh_ui()
				try:fn()
				except I as B:A._log(f"Erreur : {B}",F)
				finally:A.busy=L;A._prog=0,0;A._refresh_ui()
		g.Thread(target=B,daemon=C).start()
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return L
		return C
	def load(A,name):
		C=name
		if not A._need_fivem():return
		def B():
			B=next((A for A in A._all_remote()if A[H]==C),D);F=C in Ae();G=B and B.get(Y)and b(B[Y])!=(Ag(C)or E)
			if B and(not F or G):Ao(B,A.cfg,A._log,A._progress)
			elif not F:raise W('Pack introuvable (ni local, ni sur le serveur).')
			BD(C,{P:A.fivem,V:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:BE(name,{P:A.fivem,V:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=next((A for A in A._all_remote()if A[H]==name),D)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:Ao(B,A.cfg,A._log,A._progress))
BV='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que uxqt.site (palette igloo dark) :\n     noir pur, verre translucide, lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>FiveM Pack Manager</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">uxqt.site &#8599;</button>\n  </header>\n\n  <main><div class="grid" id="grid"></div><div class="empty" id="empty" style="display:none">\n    Aucun pack disponible.<br>\n    Vérifie la connexion au serveur (bouton Actualiser)<br>\n    ou l\'URL configurée dans Options.\n  </div></main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" onclick="addPack()">Ajouter</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = st.packs.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = st.packs.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) renderCustomList();\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value);\n    n.value = u.value = i.value = \'\';\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    appendLog(\'FiveM Pack Manager démarré.\', \'ok\');\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
BW={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background'}
def BX(api):
	H='text/plain';E=secrets.token_urlsafe(16);K=BV.replace('__TOKEN__',E).encode(O)
	class M(A_):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(AU,ctype);A.send_header(AV,b(B(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def do_GET(B):
			if B.path in(c,'/index.html'):B._send(200,K,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;C=A.path.join(Z,E)if E and not E.startswith(AS)else D
				if C and A.path.exists(C):
					F=A.path.splitext(C)[1].lower()
					with J(C,'rb')as G:B._send(200,G.read(),Ac.get(F,'application/octet-stream'))
				else:B._send(404,b'no background',H)
			else:B._send(404,b'not found',H)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if B not in BW or A.headers.get(Ay)!=E:A._send(403,b'forbidden',H);return
			try:C=X(A.headers.get(AV,0));D=G.loads(A.rfile.read(C)or b'[]');F=AG(api,B)(*D);A._send(200,G.dumps(F,ensure_ascii=L).encode(O),'application/json; charset=utf-8')
			except I as J:A._send(500,G.dumps({'error':b(J)}).encode(O),A4)
	F=B0(('127.0.0.1',0),M);g.Thread(target=F.serve_forever,daemon=C).start();return F,f"http://127.0.0.1:{F.server_address[1]}/",E
def BY():
	G=BU();H,E,J=BX(G);K=[J];D=Aa.create_window(B1,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def B(*A):B=' '.join(b(A)for A in A);print(B.encode('ascii',AN).decode(),flush=C)
		def L():
			F.sleep(4)
			try:import urllib.request as C;G=C.Request(E+'api/poll',data=b'[]',method='POST');G.add_header(Ay,K[0]);H=C.urlopen(G,timeout=5).read()[:80];B('SELFTEST urllib POST:',H)
			except I as A:B('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except I as A:B('SELFTEST inject KO:',A)
			F.sleep(4)
			try:B('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));B('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));B('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except I as A:B('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		g.Thread(target=L,daemon=C).start()
	try:Aa.start(gui='edgechromium')
	finally:H.shutdown()
if __name__=='__main__':BY()