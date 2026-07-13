B3='X-Token'
B2='gofile'
B1='plugins'
B0='.version'
A_='GTA5.exe'
Az='CitizenFX.ini'
Ay='FiveM.app'
Ax='image/jpeg'
Aw=reversed
Av=ImportError
Ab='background'
Aa='Content-Length'
AZ='Content-Type'
AY='le téléchargement'
AX='http'
AW='gdrive_folder'
AV='file'
AU='_dirs'
AT='x64'
AS='.rpf'
AR='replace'
AQ='FiveM'
AP='packs'
AO='LOCALAPPDATA'
AN=sorted
AM=getattr
AA='size'
A9='application/json'
A8='wb'
A7='purged'
A6='citizen'
A5='.png'
A4=next
A3=enumerate
A2=dict
z='custom'
y='https://'
x='http://'
w='packs_key'
v='?'
u='backups'
t='update'
s='.'
r='r'
q=list
o='{a}'
n='mods'
m=isinstance
i='packs_url'
h='User-Agent'
g='files'
e='url'
f=str
a='version'
Z='/'
Y=int
X=ValueError
W='preview'
V='loaded'
U=OSError
S='gta'
R='utf-8'
Q='image'
P='ok'
O='fivem'
N=False
M=RuntimeError
L=open
J=Exception
H='name'
F='err'
E=''
D=None
C=True
B=len
import base64 as Ac,json as I,os as A,re as T,secrets,shutil as G,struct as AB,subprocess as Ad,sys,tempfile as B4,threading as j,urllib.parse,urllib.request,zipfile as Ae
from http.server import BaseHTTPRequestHandler as B5,ThreadingHTTPServer as B6
import webview as Af
B7='FiveM Pack Manager'
k='FiveMPackManager/2.0'
def B8():
	if AM(sys,'frozen',N):B=A.path.join(A.environ.get(AO,A.path.dirname(sys.executable)),'FiveMPackManager');A.makedirs(B,exist_ok=C);return B
	return A.path.dirname(A.path.abspath(__file__))
b=B8()
K=A.path.join(b,AP)
Ag=A.path.join(b,'_backups')
AC=A.path.join(b,'state.json')
AD=A.path.join(b,'config.json')
def B9():
	B=[A.path.dirname(A.path.abspath(__file__))]
	if AM(sys,'_MEIPASS',D):B.insert(0,sys._MEIPASS)
	for E in B:
		C=A.path.join(E,'embedded_config.json')
		if A.path.exists(C):
			try:
				with L(C,r,encoding=R)as F:return I.load(F)
			except(U,I.JSONDecodeError):pass
	return{}
BA=B9()
AE=A5,'.jpg','.jpeg','.webp','.gif'
Ah={A5:'image/png','.jpg':Ax,'.jpeg':Ax,'.webp':'image/webp','.gif':'image/gif'}
def A0():
	B=A2(BA)
	if A.path.exists(AD):
		try:
			with L(AD,r,encoding=R)as C:B.update(I.load(C))
		except(U,I.JSONDecodeError):pass
	return B
def c(**B):
	A=A0();A.update(B)
	with L(AD,'w',encoding=R)as C:I.dump(A,C,indent=2)
def BB():
	F='fivem_path';C=[];D=A0()
	if D.get(F):C.append(D[F])
	G=A.environ.get(AO,E);C.append(A.path.join(G,AQ,Ay))
	for B in C:
		if B and A.path.isdir(B)and(A.path.exists(A.path.join(B,Az))or A.path.isdir(A.path.join(B,A6))):return B
def BC(fivem=D):
	I=fivem;N=A0();C=[N.get('gta_path')];J=[I]if I else[];J.append(A.path.join(A.environ.get(AO,E),AQ,Ay))
	for K in J:
		G=A.path.join(K,Az)if K else D
		if G and A.path.exists(G):
			try:
				with L(G,r,encoding=R,errors=AR)as O:
					for M in O:
						if M.strip().lower().startswith('ivpath='):C.append(M.split('=',1)[1].strip())
			except U:pass
	try:
		import winreg as H
		for P in('SOFTWARE\\WOW6432Node\\Rockstar Games\\Grand Theft Auto V','SOFTWARE\\WOW6432Node\\Rockstar Games\\GTAV'):
			try:
				with H.OpenKey(H.HKEY_LOCAL_MACHINE,P)as Q:C.append(H.QueryValueEx(Q,'InstallFolder')[0])
			except U:pass
	except Av:pass
	for B in('C:','D:','E:','F:'):C+=[B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy',B+'\\Program Files\\Rockstar Games\\Grand Theft Auto V',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\Program Files (x86)\\Steam\\steamapps\\common\\Grand Theft Auto V',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V Legacy',B+'\\SteamLibrary\\steamapps\\common\\Grand Theft Auto V',B+'\\Program Files\\Epic Games\\GTAV']
	for F in C:
		if F and A.path.isdir(F)and A.path.exists(A.path.join(F,A_)):return F
def BD():
	if A.path.exists(AC):
		try:
			with L(AC,r,encoding=R)as B:return I.load(B)
		except(U,I.JSONDecodeError):pass
	return{V:{}}
def Ai(state):
	with L(AC,'w',encoding=R)as A:I.dump(state,A,indent=2,ensure_ascii=N)
def AF():A.makedirs(K,exist_ok=C);return AN(B for B in A.listdir(K)if A.path.isdir(A.path.join(K,B))and not B.startswith(s))
def Bi(pack_path):
	B=pack_path
	for(C,H,F)in A.walk(B):
		G=A.path.normpath(C)==A.path.normpath(B)
		for D in F:
			E=D.lower()
			if E.startswith(s)or G and A.path.splitext(E)[0]==W:continue
			yield A.path.relpath(A.path.join(C,D),B)
def BE(pack_name):
	B=0
	for(C,G,D)in A.walk(A.path.join(K,pack_name)):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except U:pass
	for F in('o','Ko','Mo','Go'):
		if B<1024:return f"{B:.0f} {F}"
		B/=1024
	return f"{B:.1f} To"
def Aj(pack_name):
	D=A.path.join(K,pack_name)
	for B in AE:
		C=A.path.join(D,W+B)
		if A.path.exists(C):
			try:
				with L(C,'rb')as E:F=Ac.b64encode(E.read()).decode('ascii')
				return f"data:{Ah[B]};base64,{F}"
			except U:return
def Ak(name):
	B=A.path.join(K,name,B0)
	if A.path.exists(B):
		try:
			with L(B,r,encoding=R)as C:return C.read().strip()
		except U:pass
def d(base,rel):
	B=A.path.realpath(A.path.join(base,rel))
	if not B.startswith(A.path.realpath(base)+A.sep):raise X(f"Chemin refusé (sort du dossier cible) : {rel}")
	return B
def AG():
	try:
		D=Ad.run(['tasklist','/FO','CSV'],capture_output=C,text=C,creationflags=Au,timeout=10).stdout.lower()
		for A in D.splitlines():
			if not A.startswith('"'):continue
			B=A.split('","',1)[0].strip('"')
			if B.startswith('fivempackmanager'):continue
			if B.startswith((O,'gta5')):return C
		return N
	except J:return N
def A1(path,need_bytes,what):
	B=need_bytes;C=G.disk_usage(A.path.splitdrive(A.path.realpath(path))[0]+A.sep).free
	if C<B+1024**3:raise M(f"Espace disque insuffisant pour {what} : {B/1e9:.1f} Go nécessaires, {C/1e9:.1f} Go libres.")
def Bj(path):
	B=0
	for(C,F,D)in A.walk(path):
		for E in D:
			try:B+=A.path.getsize(A.path.join(C,E))
			except U:pass
	return B
Al={A6,n,B1}
BF={'gtav','gta5','gta v','gta 5','grand theft auto v','grand theft auto v legacy',S}
BG={'.dll','.asi','.ini','.fx','.cfg','.json','.yml'}
def BH(gta_base):
	B=gta_base;C={}
	if not B or not A.path.isdir(B):return C
	for(F,E,G)in A.walk(B):
		E[:]=[A for A in E if A.lower()!=n]
		for D in G:
			if D.lower().endswith(AS):H=A.path.relpath(A.path.join(F,D),B);C.setdefault(D.lower(),[]).append(H)
	return C
def Am(src,pack_path,rpf_index,log):
	C=A.path.basename(src);D=A.path.relpath(src,pack_path).split(A.sep);H=[A.lower()for A in D]
	for(F,G)in A3(H[:-1]):
		if G in(t,AT):return A.path.join(*D[F:])
		if G=='dlcpacks':return A.path.join(t,AT,*D[F:])
	E=rpf_index.get(C.lower(),[])
	if B(E)==1:return E[0]
	if B(E)>1:log(f"{C} : plusieurs rpf du même nom dans le jeu — posé à la racine de mods.")
	return C
def AH(plan,src_dir,target,dst_prefix):
	C=dst_prefix;B=src_dir
	for(G,I,H)in A.walk(B):
		for D in H:
			if D.startswith(s):continue
			E=A.path.join(G,D);F=A.path.relpath(E,B);plan.append((E,target,A.path.join(C,F)if C else F))
def BI(pack_path,log,gta_base=D):
	d='racine FiveM';P='rpf vers mods';M=log;H=pack_path;C=[];V=BH(gta_base);Q=[]
	for(J,K,k)in A.walk(H):
		if any(A.lower()in Al for A in K):Q.append(J)
	if not Q:M("Structure standard non détectée — copie de l'archive telle quelle.");AH(C,H,O,E);return[(C,D,B)for(C,D,B)in C if not(A.path.dirname(B)==E and A.path.splitext(B)[0].lower()==W)]
	R=min(Q,key=lambda p:B(A.path.relpath(p,H).split(A.sep)));D={}
	for T in AN(A.listdir(R)):
		N=A.path.join(R,T);G=T.lower()
		if A.path.isdir(N):
			if G in Al:U=B(C);AH(C,N,O,G);D[f"{G} vers FiveM"]=B(C)-U
			elif G in('reshade-shaders','reshade-presets'):U=B(C);AH(C,N,O,G);D[f"{G} vers FiveM"]=B(C)-U
		elif A.path.splitext(G)[1]in BG:C.append((N,O,T));D[d]=D.get(d,0)+1
	e=A.path.realpath(R)
	for(J,K,f)in A.walk(H):
		if A.path.realpath(J)==e:K[:]=[];continue
		for L in q(K):
			if L.lower()in BF:
				X=A.path.join(J,L)
				for(g,l,h)in A.walk(X):
					for I in h:
						if I.startswith(s):continue
						F=A.path.join(g,I)
						if I.lower().endswith(AS):C.append((F,O,A.path.join(n,Am(F,H,V,M))));D[P]=D.get(P,0)+1
						else:i=A.path.relpath(F,X);C.append((F,S,i));D[f"{An(L)} vers GTA V"]=D.get(f"{An(L)} vers GTA V",0)+1
				K.remove(L)
		for I in f:
			if I.lower().endswith(AS):F=A.path.join(J,I);C.append((F,O,A.path.join(n,Am(F,H,V,M))));D[P]=D.get(P,0)+1
	Y,Z=set(),[]
	for(F,a,b)in C:
		c=a,b.lower()
		if c not in Y:Y.add(c);Z.append((F,a,b))
	j=', '.join(f"{A} : {B}"for(A,B)in D.items())or'rien à installer';M(f"Structure détectée — {j}.");return Z
def An(name):A=name;return A if B(A)<=20 else A[:17]+'...'
def p(e):return(O,e)if m(e,f)else(e[0],e[1])
def AI(target,rel):return f"{target}|{rel}"
def BJ(bases,backup_root,manifest,log):
	M=bases;K=manifest;I=backup_root
	for O in Aw(K[g]):
		D,L=p(O);E=M.get(D)
		if not E:continue
		try:
			B=d(E,L)
			if A.path.exists(B):A.remove(B)
			if K[u].get(AI(D,L)):
				H=A.path.join(I,D,L)
				if A.path.exists(H):G.move(H,B)
		except J:pass
	for(D,N)in Aw(K.get(A7,[])):
		E=M.get(D)
		if not E:continue
		try:
			B=d(E,N);H=A.path.join(I,AU,D,N)
			if A.path.exists(H):
				if A.path.isdir(B):G.rmtree(B,ignore_errors=C)
				G.move(H,B)
		except J:pass
	G.rmtree(I,ignore_errors=C);log("Installation annulée — jeu restauré dans son état d'origine.",F)
l={O:AQ,S:'GTA V'}
BK={O:{A6},S:{t,AT,'redistributables','installers','dlc','_commonredist',n}}
def BL(plan):
	D={}
	for(G,E,F)in plan:
		C=F.replace(Z,A.sep).split(A.sep)
		if B(C)>1:D.setdefault((E,C[0].lower()),C[0])
	return D
def BM(pack_name,bases,state,log,progress):
	a=state;R=bases;Q=pack_name;L=log
	if Q in a[V]:raise X('Ce pack est déjà chargé.')
	if AG():raise M('FiveM ou GTA V est ouvert — ferme-les avant de charger un pack.')
	s=A.path.join(K,Q);H=BI(s,L,R.get(S))
	if not H:raise X('Pack vide — aucun fichier à installer.')
	k=[1 for(B,A,C)in H if A==S and not R.get(S)]
	if k:L(f"Dossier GTA V introuvable — {B(k)} fichiers ENB/jeu non installés (indique le dossier dans Options).",F);H=[(B,A,C)for(B,A,C)in H if not(A==S and not R.get(S))]
	if not H:raise X('Rien à installer (dossier GTA V non configuré).')
	t=sum(A.path.getsize(B)for(B,C,D)in H if A.path.exists(B));A1(R[O],t,"l'installation");T={g:[],u:{},A7:[]};U={}
	for(W,v)in a[V].items():
		if W!=Q:
			for m in v[g]:U[p(m)[0]+'|'+p(m)[1].lower()]=W
	L(f"Installation de « {Q} » — {B(H)} fichiers...");e=A.path.join(Ag,Q);f=0;n=B(H)<=60;w=max(1,B(H)//10)
	try:
		for((I,o),Y)in BL(H).items():
			b=R.get(I)
			if not b or o in BK.get(I,set()):continue
			q=d(b,Y)
			if not A.path.isdir(q):continue
			x=f"{I}|{o}{A.sep}";W=A4((B for(A,B)in U.items()if A.startswith(x)),D)
			if W:L(f"Dossier {Y} : contient des fichiers du pack « {W} » — fusion au lieu du remplacement.");continue
			Z=A.path.join(e,AU,I,Y);A.makedirs(A.path.dirname(Z),exist_ok=C);G.move(q,Z);T[A7].append([I,Y]);L(f"Dossier existant mis de côté ({l[I]}) : {Y} — remplacé proprement.")
		for(h,(y,I,N))in A3(H):
			b=R[I];c=d(b,N);i=I+'|'+N.lower()
			if i in U:L(f"Attention : {N} appartient déjà au pack « {U[i]} » — écrasé.")
			A.makedirs(A.path.dirname(c),exist_ok=C)
			if A.path.exists(c)and i not in U:
				Z=A.path.join(e,I,N);A.makedirs(A.path.dirname(Z),exist_ok=C);G.copy2(c,Z);T[u][AI(I,N)]=C;f+=1
				if n:L(f"Sauvegarde de l'original ({l[I]}) : {N}")
			G.copy2(y,c);T[g].append([I,N])
			if n:L(f"Copie ({l[I]}) : {N}")
			elif(h+1)%w==0:L(f"{h+1}/{B(H)} fichiers copiés ({f} originaux sauvegardés)...")
			progress(h+1,B(H))
	except J as j:L(f"Erreur pendant l'installation : {j}",F);BJ(R,e,T,L);raise M(f"Installation échouée ({j}) — tout a été annulé.")from j
	a[V][Q]=T;Ai(a);r=sum(1 for A in T[g]if p(A)[0]==S);z=f" (dont {r} dans GTA V)"if r else E;L(f"« {Q} » chargé : {B(H)} fichiers copiés{z}, {f} originaux sauvegardés.",P)
def BN(pack_name,bases,state,log,progress):
	a=bases;T=state;N=pack_name;H=log;O=T[V].get(N)
	if not O:raise X("Ce pack n'est pas chargé.")
	if AG():raise M('FiveM ou GTA V est ouvert — ferme-les avant de décharger.')
	Q=A.path.join(Ag,N);J=O[g];b=set();H(f"Désinstallation de « {N} » — {B(J)} fichiers...");S=0;W=B(J)<=60;h=max(1,B(J)//10)
	for(Y,c)in A3(J):
		D,I=p(c);K=a.get(D)
		if not K:H(f"Cible {l.get(D,D)} introuvable — {I} laissé en place.",F);continue
		try:E=d(K,I)
		except X as i:H(f"Entrée ignorée : {i}",F);continue
		if A.path.exists(E):
			A.remove(E)
			if W:H(f"Suppression ({l[D]}) : {I}")
		e,j=A.path.join(Q,D,I),A.path.join(Q,I);k=O[u].get(AI(D,I))or m(c,f)and O[u].get(I)
		if k:
			R=e if A.path.exists(e)else j
			if A.path.exists(R):
				A.makedirs(A.path.dirname(E),exist_ok=C);G.move(R,E);S+=1
				if W:H(f"Original restauré : {I}")
		if not W and(Y+1)%h==0:H(f"{Y+1}/{B(J)} fichiers retirés ({S} originaux restaurés)...")
		L=A.path.dirname(E)
		while B(L)>B(K):b.add(L);L=A.path.dirname(L)
		progress(Y+1,B(J))
	for L in AN(b,key=B,reverse=C):
		try:A.rmdir(L)
		except U:pass
	for(D,Z)in O.get(A7,[]):
		K=a.get(D)
		if not K:continue
		try:E=d(K,Z)
		except X:continue
		R=A.path.join(Q,AU,D,Z)
		if A.path.exists(R):
			if A.path.isdir(E):G.rmtree(E,ignore_errors=C)
			G.move(R,E);S+=1;H(f"Dossier original restauré ({l[D]}) : {Z}")
	if A.path.isdir(Q):G.rmtree(Q,ignore_errors=C)
	del T[V][N];Ai(T);H(f"« {N} » déchargé : {B(J)} fichiers retirés, {S} originaux restaurés.",P)
def AJ(url,key):
	A=url
	if not key:return A
	B='&'if v in A else v;return f"{A}{B}key={urllib.parse.quote(key)}"
def Ao(url,key):A=urllib.request.Request(AJ(url,key),headers={h:k});return urllib.request.urlopen(A,timeout=30)
def BO(cfg):
	C=cfg.get(i)
	if not C:return[]
	D=cfg.get(w)
	with Ao(C,D)as G:B=I.loads(G.read().decode(R))
	E=C.rsplit(Z,1)[0]+Z;F=B.get(AP,B)if m(B,A2)else B
	for A in F:
		if not A.get(e):A[e]=AJ(urllib.parse.urljoin(E,A[AV]),D)
		if A.get(Q)and not A[Q].startswith((x,y,'data:')):A[Q]=AJ(urllib.parse.urljoin(E,A[Q]),D)
	return F
def Ap(url):
	D='drive.google.com';A=url.strip();B=A.lower()
	if'mega.nz'in B or'mega.co.nz'in B:return'mega',A
	if'gofile.io'in B:return B2,A
	if D in B and'/folders/'in B:
		C=T.search('/folders/([\\w-]+)',A)
		if C:return AW,C.group(1)
	if D in B:
		C=T.search('/file/d/([\\w-]+)',A)or T.search('[?&]id=([\\w-]+)',A)
		if C:return AX,f"https://drive.usercontent.google.com/download?id={C.group(1)}&export=download&confirm=t"
	if'drive.usercontent.google.com'in B and'confirm='not in B:A+=('&'if v in A else v)+'confirm=t'
	return AX,A
BP='Mozilla/5.0'
BQ=T.compile('data-id="([\\w-]{20,})"')
BR=T.compile('<title>([^<]*)</title>')
def AK(url,rng=D):
	A={h:BP}
	if rng:A['Range']=rng
	return urllib.request.urlopen(urllib.request.Request(url,headers=A),timeout=30)
def Aq(fid):return f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
def Ar(fid):
	with AK(f"https://drive.google.com/drive/folders/{fid}")as A:return A.read().decode(R,AR)
def BS(html,fallback):
	B=fallback;C=BR.search(html)
	if not C:return B
	A=C.group(1).replace('\xa0',' ');A=T.sub('\\s*[–—-]\\s*Google\\s+Drive\\s*$',E,A).strip();return A or B
def BT(html,self_id):
	B,C=[],{self_id}
	for A in BQ.finditer(html):
		if A.group(1)not in C:C.add(A.group(1));B.append(A.group(1))
	return B
def BU(fid):
	for H in range(2):
		try:
			with AK(Aq(fid),'bytes=0-0')as A:B=A.headers.get('Content-Disposition',E);I=A.headers.get_content_type();F=A.headers.get('Content-Range',E)
			if'attachment'in B and not I.startswith('text/html'):G=T.search('filename="([^"]+)"',B)or T.search("filename\\*=UTF-8''(.+)",B);K=urllib.parse.unquote(G.group(1))if G else D;L=Y(F.split(Z)[-1])if Z in F else 0;return C,K,L
			return N,D,0
		except urllib.error.HTTPError as M:
			if M.code in(403,429)and H==0:continue
			return D,D,0
		except J:return D,D,0
	return D,D,0
def BV(html):return'application/vnd.google-apps.folder'in html or'data-id="'in html
def AL(seg):A=seg;A=T.sub('[<>:"/\\\\|?*]','_',A).strip(' .');return A or'_'
def BW(folder_id,log):
	B=folder_id;C=[]
	def D(cid,fname,size,prefix):E=prefix;D=fname;B=cid;F=A.path.join(E,AL(D or B))if E else AL(D or B);C.append((F,B,size))
	def H(fid,html,prefix,depth):
		I=depth;C=prefix
		if I>8:return
		for B in BT(html,fid):
			L,E,F=BU(B)
			if L:D(B,E,F,C);continue
			try:G=Ar(B)
			except J:D(B,E,F,C);continue
			if not BV(G):D(B,E,F,C);continue
			K=AL(BS(G,B));H(B,G,A.path.join(C,K)if C else K,I+1)
	log('Lecture du dossier Google Drive...');H(B,Ar(B),E,0);return C
def BX(folder_id,dest,log,progress):
	G=log;F=dest;D=BW(folder_id,G)
	if not D:raise M('Dossier Drive vide ou illisible (accès restreint ?).')
	E=sum(A for(B,C,A)in D);G(f"{B(D)} fichiers dans le dossier"+(f" ({E/1048576:.0f} Mo)."if E else s))
	if E:A1(F,E,AY)
	A.makedirs(F,exist_ok=C);J=0;N=max(1,B(D)//20)
	for(H,(O,P,S))in A3(D):
		K=d(F,O);A.makedirs(A.path.dirname(K),exist_ok=C)
		with AK(Aq(P))as Q,L(K,A8)as R:
			while C:
				I=Q.read(262144)
				if not I:break
				R.write(I);J+=B(I)
				if E:progress(J,E)
		if(H+1)%N==0 or H+1==B(D):G(f"{H+1}/{B(D)} fichiers téléchargés...")
def BY(url,log):
	L='status';K='data';N=url.rstrip(Z).split(Z)[-1].split(v)[0]
	def B(u,data=D,headers=D):
		A=data;B={h:k,'Accept':A9};B.update(headers or{})
		if A is not D:B[AZ]=A9;A=I.dumps(A).encode()
		C=urllib.request.Request(u,data=A,headers=B);return I.loads(urllib.request.urlopen(C,timeout=30).read().decode())
	C=B('https://api.gofile.io/accounts',data={})[K]['token']
	try:O=urllib.request.urlopen(urllib.request.Request('https://gofile.io/dist/js/global.js',headers={h:k}),timeout=30).read().decode();Q=T.search('wt\\s*[:=]\\s*["\\\']([\\w-]+)["\\\']',O).group(1)
	except J as E:raise M(f"Gofile : jeton du site introuvable ({E}).")from E
	A=B(f"https://api.gofile.io/contents/{N}?wt={Q}",headers={'Authorization':f"Bearer {C}"})
	if A.get(L)!=P:raise M(f"Gofile a refusé le lien ({A.get(L)}).")
	R=A[K];S=R.get('children')or{};F=[A for A in S.values()if A.get('type')==AV]
	if not F:raise M('Gofile : aucun fichier dans ce lien (dossier vide ?).')
	G=max(F,key=lambda c:c.get(AA,0));return G['link'],{'Cookie':f"accountToken={C}"},G.get(H)
def As(s):s=s.replace('-','+').replace('_',Z);return Ac.b64decode(s+'='*(-B(s)%4))
def BZ(url,out_path,log,progress):
	P='g';O=b'\x00'
	try:from cryptography.hazmat.primitives.ciphers import Cipher as Q,algorithms as R,modes as S
	except Av as b:raise M('Support Mega indisponible (module cryptography manquant).')from b
	G=T.search('mega\\.(?:nz|co\\.nz)/file/([\\w-]+)#([\\w-]+)',url)or T.search('mega\\.(?:nz|co\\.nz)/#!([\\w-]+)!([\\w-]+)',url)
	if not G:raise M('Lien Mega non reconnu (attendu : mega.nz/file/ID#CLÉ).')
	c,d=G.group(1),G.group(2);A=AB.unpack('>8I',As(d));U=AB.pack('>4I',A[0]^A[4],A[1]^A[5],A[2]^A[6],A[3]^A[7]);e=AB.pack('>2I',A[4],A[5])+O*8;f=urllib.request.Request('https://g.api.mega.co.nz/cs?id=0',data=I.dumps([{'a':P,P:1,'p':c}]).encode(),headers={AZ:A9,h:k});D=I.loads(urllib.request.urlopen(f,timeout=30).read().decode())
	if m(D,Y)or m(D,q)and m(D[0],Y):raise M('Mega a refusé le lien (fichier supprimé ou clé invalide).')
	D=D[0];g,F=D[P],Y(D.get('s',0));H='mega_pack'
	try:
		V=Q(R.AES(U),S.CBC(O*16)).decryptor();W=V.update(As(D['at']))+V.finalize()
		if W.startswith(b'MEGA'):H=I.loads(W[4:].split(O)[0].decode())['n']
	except J:pass
	if F:A1(K,Y(F*2.3),AY)
	log(f"Fichier Mega : {H}"+(f" ({F/1048576:.0f} Mo)"if F else E));X=Q(R.AES(U),S.CTR(e)).decryptor();Z=0
	with urllib.request.urlopen(urllib.request.Request(g,headers={h:k}),timeout=60)as i,L(out_path,A8)as a:
		while C:
			N=i.read(262144)
			if not N:break
			a.write(X.update(N));Z+=B(N)
			if F:progress(Z,F)
		a.write(X.finalize())
	return H
def At(pack,cfg,log,progress):
	b=progress;N=log;F=pack;I=A.path.join(K,F[H]);A.makedirs(K,exist_ok=C);q,U=B4.mkstemp(suffix='.pack',dir=K);A.close(q)
	try:
		N(f"Téléchargement de « {F[H]} »...")
		if AG():N("Note : FiveM est ouvert — le téléchargement passe, mais ferme-le avant l'installation.")
		V,X=Ap(F[e]);O=F.get(AV)
		if V==AW:
			if A.path.isdir(I):G.rmtree(I)
			BX(X,I,N,b)
		elif V=='mega':O=BZ(X,U,N,b)or O
		else:
			if V==B2:N('Résolution du lien Gofile...');c,j,r=BY(X,N);O=O or r
			else:c,j=X,{}
			l={h:k};l.update(j)
			with urllib.request.urlopen(urllib.request.Request(c,headers=l),timeout=60)as S:
				O=S.headers.get_filename()or O or A.path.basename(urllib.parse.urlparse(c).path)
				if S.headers.get_content_type().startswith('text/'):raise M('Le lien renvoie une page web, pas un fichier (lien mort, quota dépassé, ou accès restreint).')
				T=Y(S.headers.get(Aa,0))
				if T:A1(K,Y(T*2.3),AY)
				if O:N(f"Fichier : {O}"+(f" ({T/1048576:.0f} Mo)"if T else E))
				m=0
				with L(U,A8)as s:
					while C:
						d=S.read(262144)
						if not d:break
						s.write(d);m+=B(d)
						if T:b(m,T)
		if V!=AW:
			N(f"Extraction dans le cache local ({F[H]})...")
			if A.path.isdir(I):G.rmtree(I)
			Bb(U,I,N);Z=A.listdir(I)
			if B(Z)==1 and A.path.isdir(A.path.join(I,Z[0]))and Z[0].lower()not in(A6,n,B1):
				g=A.path.join(I,Z[0])
				for o in A.listdir(g):G.move(A.path.join(g,o),A.path.join(I,o))
				A.rmdir(g)
		if F.get(a):
			with L(A.path.join(I,B0),'w',encoding=R)as i:i.write(f(F[a]))
		if F.get(Q)and not Aj(F[H]):
			try:
				with Ao(F[Q],D)as S:
					p=A.path.splitext(urllib.parse.urlparse(F[Q]).path)[1]or A5
					if p.lower()in AE:
						with L(A.path.join(I,W+p.lower()),A8)as i:i.write(S.read())
			except J:pass
		N(f"« {F[H]} » téléchargé et extrait.",P)
	finally:
		if A.path.exists(U):A.remove(U)
Au=134217728
def Ba():
	H='-o{d}';G='7-Zip';F='{d}\\';E='WinRAR';C='-y';B='x';I=[(E,['C:\\Program Files\\WinRAR\\UnRAR.exe',B,C,o,F]),(E,['C:\\Program Files (x86)\\WinRAR\\UnRAR.exe',B,C,o,F]),(G,['C:\\Program Files\\7-Zip\\7z.exe',B,C,H,o]),(G,['C:\\Program Files (x86)\\7-Zip\\7z.exe',B,C,H,o]),('tar',[A.path.join(A.environ.get('SystemRoot','C:\\Windows'),'System32','tar.exe'),'-xf',o,'-C','{d}'])]
	for(J,D)in I:
		if A.path.exists(D[0]):return J,D
def Bb(archive,dest,log):
	D=archive;B=dest;A.makedirs(B,exist_ok=C)
	if Ae.is_zipfile(D):
		with Ae.ZipFile(D)as G:
			for H in G.namelist():
				K=A.path.realpath(A.path.join(B,H))
				if not K.startswith(A.path.realpath(B)+A.sep):raise X(f"Chemin suspect dans l'archive : {H}")
			G.extractall(B)
		return
	I=Ba()
	if not I:raise M('Aucun extracteur RAR trouvé — installe WinRAR ou 7-Zip.')
	J,E=I;log(f"Extraction avec {J}...");E=[A.replace(o,D).replace('{d}',B)for A in E];F=Ad.run(E,capture_output=C,text=C,creationflags=Au)
	if F.returncode!=0:raise M(f"Échec extraction ({J}) : {(F.stderr or F.stdout).strip()[:300]}")
def Bc():
	try:
		import ctypes as C;from ctypes import wintypes as A
		class E(C.Structure):_fields_=[('lStructSize',A.DWORD),('hwndOwner',A.HWND),('hInstance',A.HINSTANCE),('lpstrFilter',A.LPCWSTR),('lpstrCustomFilter',A.LPWSTR),('nMaxCustFilter',A.DWORD),('nFilterIndex',A.DWORD),('lpstrFile',A.LPWSTR),('nMaxFile',A.DWORD),('lpstrFileTitle',A.LPWSTR),('nMaxFileTitle',A.DWORD),('lpstrInitialDir',A.LPCWSTR),('lpstrTitle',A.LPCWSTR),('Flags',A.DWORD),('nFileOffset',A.WORD),('nFileExtension',A.WORD),('lpstrDefExt',A.LPCWSTR),('lCustData',A.LPARAM),('lpfnHook',A.LPVOID),('lpTemplateName',A.LPCWSTR),('pvReserved',A.LPVOID),('dwReserved',A.DWORD),('FlagsEx',A.DWORD)]
		D=C.create_unicode_buffer(1024);B=E();B.lStructSize=C.sizeof(B);B.lpstrFilter='Images\x00*.png;*.jpg;*.jpeg;*.webp;*.gif\x00Tous\x00*.*\x00\x00';B.lpstrFile=C.cast(D,A.LPWSTR);B.nMaxFile=1024;B.lpstrTitle='Choisir une image de fond';B.Flags=530432
		if C.windll.comdlg32.GetOpenFileNameW(C.byref(B)):return D.value
	except J:pass
class Bd:
	def __init__(A):A.state=BD();A.cfg=A0();A.fivem=BB();A.gta=BC(A.fivem);A.remote_packs=[];A.custom_packs=q(A.cfg.get('custom_packs',[]));A.background=A.cfg.get(Ab);A.busy=N;A._lock=j.Lock();A._buf_lock=j.Lock();A._logs=[];A._prog=0,0;A._dirty=N
	def _log(A,msg,kind='info'):
		with A._buf_lock:A._logs.append((msg,kind))
	def _progress(A,cur,total):A._prog=cur,total
	def _refresh_ui(A):A._dirty=C
	def poll(A):
		with A._buf_lock:B,A._logs=A._logs,[];C,A._dirty=A._dirty,N
		return{'logs':B,'prog':q(A._prog),'busy':A.busy,'dirty':C}
	def _all_remote(B):
		D={A[H]:A2(A)for A in B.remote_packs}
		for E in B.custom_packs:A=A2(E);A[z]=C;D[A[H]]=A
		return q(D.values())
	def background_url(E):
		B=E.background
		if not B:return
		if B.startswith((x,y)):return B
		C=A.path.join(b,B);return f"/bg?{Y(A.path.getmtime(C))}"if A.path.exists(C)else D
	def get_state(A):
		R='remote';P='image_link';M='nfiles';J=[];K={A[H]:A for A in A._all_remote()}
		for I in AF():F=K.pop(I,D);L=Ak(I);J.append({H:I,AA:BE(I),a:L,V:I in A.state[V],M:B(A.state[V].get(I,{}).get(g,[])),Q:Aj(I)or(F or{}).get(Q),P:(F or{}).get(Q),e:(F or{}).get(e),W:(F or{}).get(W),R:N,z:bool(F and F.get(z)),t:bool(F and F.get(a)and f(F[a])!=(L or E))})
		for G in K.values():J.append({H:G[H],AA:G.get(AA,E),a:G.get(a),V:N,M:0,Q:G.get(Q),P:G.get(Q),e:G.get(e),W:G.get(W),R:C,z:bool(G.get(z)),t:N})
		return{O:A.fivem,S:A.gta,AP:J,Ab:A.background_url(),i:A.cfg.get(i,E),w:A.cfg.get(w,E),'background_setting':A.background or E,'busy':A.busy}
	def open_site(B):A.startfile('https://uxqt.site')
	def add_custom_pack(B,name,url,image,preview=E,old_name=E):
		N=image;M=url;L=preview;I=name;D=old_name;I,M,N=I.strip(),M.strip(),N.strip();L,D=L.strip(),D.strip()
		if not I or not M:B._log('Nom et lien requis pour ajouter un pack.',F);return
		try:Ap(M)
		except J as R:B._log(f"Lien refusé : {R}",F);return
		if L and not L.startswith((x,y)):B._log('Lien preview refusé (il faut un lien http).',F);return
		S={I,D}-{E};B.custom_packs=[A for A in B.custom_packs if A[H]not in S];O={H:I,e:M}
		if N:O[Q]=N
		if L:O[W]=L
		B.custom_packs.append(O);c(custom_packs=B.custom_packs)
		if D and D!=I and D in AF():G.rmtree(A.path.join(K,D),ignore_errors=C)
		B._log(f"Pack « {I} » {"modifié"if D else"ajouté"}.",P);B._refresh_ui()
	def preview(C,name):
		E=A4((A for A in C._all_remote()if A[H]==name),D);B=(E or{}).get(W)
		if B and B.startswith((x,y)):A.startfile(B)
		else:C._log('Pas de preview pour ce pack.',F)
	def remove_custom_pack(B,name):
		C=name
		if B.busy:B._log("Attends la fin de l'opération en cours.",F);return
		if C in B.state[V]:B._log(f"« {C} » est chargé — décharge-le avant de le supprimer.",F);return
		B.custom_packs=[A for A in B.custom_packs if A[H]!=C];c(custom_packs=B.custom_packs)
		try:E=d(K,C)
		except X:E=D
		if E and A.path.isdir(E):
			try:G.rmtree(E);B._log(f"Pack « {C} » retiré (fichiers téléchargés supprimés).",P)
			except U as I:B._log(f"Pack « {C} » retiré, mais cache non supprimé : {I}",F)
		else:B._log(f"Pack « {C} » retiré.",P)
		B._refresh_ui()
	def choose_background(A):return Bc()or E
	def _set_background(C,bg):
		B=bg;B=B.strip()
		if not B:C.background=D;c(background=D);C._log('Image de fond retirée.',P)
		elif B.startswith((x,y)):C.background=B;c(background=B);C._log('Image de fond (lien) enregistrée.',P)
		elif A.path.isfile(B):
			for I in('background.png','background.jpg','background.jpeg','background.webp'):
				try:A.remove(A.path.join(b,I))
				except U:pass
			E=A.path.splitext(B)[1].lower();E=E if E in AE else A5;H=Ab+E;G.copy2(B,A.path.join(b,H));C.background=H;c(background=H);C._log('Image de fond enregistrée.',P)
		else:C._log(f"Image introuvable : {B}",F)
	def save_settings(B,url,key,fivem,gta,bg):
		D=fivem;C=gta;B.cfg[i]=url.strip();B.cfg[w]=key.strip();c(packs_url=B.cfg[i],packs_key=B.cfg[w]);D=D.strip()
		if D:
			if A.path.isdir(D):B.fivem=D;c(fivem_path=D);B._log(f"Dossier FiveM : {D}",P)
			else:B._log(f"Dossier introuvable : {D}",F)
		C=C.strip()
		if C:
			if A.path.isdir(C)and A.path.exists(A.path.join(C,A_)):B.gta=C;c(gta_path=C);B._log(f"Dossier GTA V : {C}",P)
			else:B._log(f"Dossier GTA V invalide (GTA5.exe absent) : {C}",F)
		if(bg or E).strip()!=(B.background or E):B._set_background(bg or E)
		B._log('Paramètres enregistrés.',P)
		if B.cfg[i]:B.fetch_remote()
		else:B.remote_packs=[];B._refresh_ui()
	def fetch_remote(A):
		if not A.cfg.get(i):A._log("Pas d'URL de serveur configurée (voir Options).",F);return
		def D():
			try:A._log('Connexion au serveur de packs...');A.remote_packs=BO(A.cfg);A._log(f"{B(A.remote_packs)} pack(s) disponibles en ligne.",P)
			except J as C:A.remote_packs=[];A._log(f"Serveur inaccessible : {C}",F)
			A._refresh_ui()
		j.Thread(target=D,daemon=C).start()
	def _run(A,fn):
		def B():
			with A._lock:
				A.busy=C;A._refresh_ui()
				try:fn()
				except J as B:A._log(f"Erreur : {B}",F)
				finally:A.busy=N;A._prog=0,0;A._refresh_ui()
		j.Thread(target=B,daemon=C).start()
	def _need_fivem(A):
		if not A.fivem:A._log('Dossier FiveM introuvable — indique-le dans Options.',F);return N
		return C
	def load(A,name):
		C=name
		if not A._need_fivem():return
		def B():
			B=A4((A for A in A._all_remote()if A[H]==C),D);F=C in AF();G=B and B.get(a)and f(B[a])!=(Ak(C)or E)
			if B and(not F or G):At(B,A.cfg,A._log,A._progress)
			elif not F:raise X('Pack introuvable (ni local, ni sur le serveur).')
			BM(C,{O:A.fivem,S:A.gta},A.state,A._log,A._progress)
		A._run(B)
	def unload(A,name):
		if not A._need_fivem():return
		A._run(lambda:BN(name,{O:A.fivem,S:A.gta},A.state,A._log,A._progress))
	def download(A,name):
		B=A4((A for A in A._all_remote()if A[H]==name),D)
		if not B:A._log(f"Pack « {name} » introuvable sur le serveur.",F);return
		A._run(lambda:At(B,A.cfg,A._log,A._progress))
Be='<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<style>\n  /* Même langage visuel que uxqt.site (palette igloo dark) :\n     noir pur, verre translucide, lignes fines, mono majuscules espacées. */\n  :root {\n    --bg: #000000;\n    --text: #f5f5f5;\n    --muted: #8a8a8e;\n    --accent: #ffffff;\n    --line: rgba(255, 255, 255, 0.14);\n    --glass: rgba(255, 255, 255, 0.04);\n    --glass-hover: rgba(255, 255, 255, 0.08);\n    --err: #ff7a70;\n  }\n  * { margin: 0; padding: 0; box-sizing: border-box; }\n  body {\n    background: var(--bg); color: var(--text);\n    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n    display: flex; flex-direction: column; height: 100vh; overflow: hidden;\n    user-select: none; -webkit-font-smoothing: antialiased;\n  }\n  ::selection { background: var(--accent); color: var(--bg); }\n  .mono {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;\n    color: var(--muted);\n  }\n\n  /* ---- barre du haut ---- */\n  header {\n    display: flex; align-items: center; gap: 8px;\n    padding: 14px 22px; border-bottom: 1px solid var(--line); flex-shrink: 0;\n  }\n  header h1 {\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 12px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; color: var(--text);\n  }\n  header .path {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.04em; color: var(--muted);\n    margin-left: 10px; white-space: nowrap; overflow: hidden;\n    text-overflow: ellipsis; flex: 1;\n  }\n  header .path.err { color: var(--err); cursor: pointer; text-decoration: underline; }\n  .btn-top {\n    border: 1px solid var(--line); background: var(--glass);\n    backdrop-filter: blur(8px); color: var(--text);\n    height: 30px; padding: 0 16px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s;\n  }\n  .btn-top:hover { border-color: var(--accent); transform: translateY(-1px); }\n  .btn-site {\n    border: 1px solid var(--accent); background: var(--accent); color: #000;\n    height: 30px; padding: 0 20px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; font-weight: 700; letter-spacing: 0.22em;\n    text-transform: uppercase; margin-left: 6px;\n    animation: sitePulse 2.6s ease-in-out infinite;\n    transition: transform 0.25s;\n  }\n  .btn-site:hover { transform: translateY(-1px) scale(1.04); animation: none;\n                    box-shadow: 0 0 22px rgba(255, 255, 255, 0.55); }\n  @keyframes sitePulse {\n    0%, 100% { box-shadow: 0 0 6px rgba(255, 255, 255, 0.25); }\n    50% { box-shadow: 0 0 20px rgba(255, 255, 255, 0.6); }\n  }\n\n  /* ---- grille de packs ---- */\n  main { flex: 1; overflow-y: auto; padding: 20px 22px; }\n  .grid {\n    display: grid; gap: 14px;\n    grid-template-columns: repeat(auto-fill, minmax(225px, 1fr));\n  }\n  .card {\n    background: var(--glass); border: 1px solid var(--line);\n    border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;\n    backdrop-filter: blur(8px);\n    transition: border-color 0.25s, transform 0.25s, background 0.25s;\n  }\n  .card:hover { border-color: var(--accent); transform: translateY(-1px);\n                background: var(--glass-hover); }\n  .card.on { border-color: rgba(255, 255, 255, 0.45); }\n  .thumb {\n    height: 116px; background: rgba(255, 255, 255, 0.02);\n    display: flex; align-items: center; justify-content: center;\n    position: relative; border-bottom: 1px solid var(--line);\n  }\n  .thumb .initials {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 22px; letter-spacing: 0.35em; color: rgba(255, 255, 255, 0.18);\n  }\n  .thumb img { width: 100%; height: 100%; object-fit: cover; }\n  .badge {\n    position: absolute; top: 10px; right: 10px;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.22em; text-transform: uppercase;\n    padding: 3px 10px; border-radius: 999px;\n    background: rgba(0, 0, 0, 0.65); border: 1px solid var(--line);\n    backdrop-filter: blur(6px);\n  }\n  .badge.on { color: var(--text); border-color: rgba(255, 255, 255, 0.4); }\n  .badge.off { color: var(--muted); }\n  .badge.cloud { color: var(--muted); }\n  .body { padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 9px; }\n  .name { font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; }\n  .meta {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.06em; color: var(--muted); min-height: 13px;\n  }\n  .meta .upd { color: var(--text); }\n  .actions { display: flex; gap: 7px; }\n  .btn {\n    flex: 1; height: 30px; border-radius: 999px; cursor: pointer;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;\n    transition: border-color 0.25s, transform 0.25s, opacity 0.25s;\n  }\n  .btn:disabled { opacity: .25; cursor: default; transform: none; }\n  .btn.load { border: 1px solid var(--accent); background: var(--accent); color: #000; }\n  .btn.load:hover:not(:disabled) { transform: translateY(-1px); }\n  .btn.unload { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.unload:hover:not(:disabled) { border-color: var(--err); color: var(--err);\n                                     transform: translateY(-1px); }\n  .btn.dl { border: 1px solid var(--line); background: var(--glass); color: var(--text); }\n  .btn.dl:hover:not(:disabled) { border-color: var(--accent); transform: translateY(-1px); }\n  .empty {\n    color: var(--muted); font-size: 13px; text-align: center; margin-top: 70px;\n    line-height: 2;\n  }\n\n  /* ---- console ---- */\n  #console-wrap { flex-shrink: 0; border-top: 1px solid var(--line);\n                  background: rgba(255, 255, 255, 0.02); }\n  #progress { height: 2px; background: transparent; }\n  #progress div { height: 100%; width: 0%; background: var(--accent);\n                  transition: width .1s; }\n  #console-head {\n    display: flex; align-items: center; padding: 8px 18px 0;\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; color: var(--muted); letter-spacing: 0.28em;\n    text-transform: uppercase;\n  }\n  #console-head button {\n    margin-left: auto; background: none; border: none; color: var(--muted);\n    font-family: ui-monospace, Consolas, monospace; font-size: 9px;\n    letter-spacing: 0.18em; text-transform: uppercase; cursor: pointer;\n  }\n  #console-head button:hover { color: var(--text); }\n  #console {\n    height: 148px; overflow-y: auto; padding: 7px 18px 12px;\n    font-family: ui-monospace, "Cascadia Mono", Consolas, monospace;\n    font-size: 11px; line-height: 1.7; user-select: text;\n  }\n  #console .t { color: rgba(255, 255, 255, 0.25); margin-right: 10px; }\n  #console .info { color: var(--muted); }\n  #console .ok { color: var(--text); }\n  #console .err { color: var(--err); }\n  ::-webkit-scrollbar { width: 8px; }\n  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14);\n                              border-radius: 999px; }\n  ::-webkit-scrollbar-track { background: transparent; }\n\n  /* ---- modal paramètres ---- */\n  #modal { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7);\n           backdrop-filter: blur(4px);\n           display: none; align-items: center; justify-content: center; }\n  #modal.show { display: flex; }\n  #modal .box {\n    background: rgba(20, 20, 22, 0.95); border: 1px solid var(--line);\n    border-radius: 12px; padding: 24px; width: 460px;\n  }\n  #modal h2 {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 11px; font-weight: 600; letter-spacing: 0.28em;\n    text-transform: uppercase; margin-bottom: 14px;\n  }\n  #modal label {\n    font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase;\n    color: var(--muted); display: block; margin: 12px 0 5px;\n  }\n  #modal input {\n    width: 100%; background: rgba(0, 0, 0, 0.6); border: 1px solid var(--line);\n    border-radius: 8px; color: var(--text); padding: 8px 11px;\n    font-size: 12px; font-family: ui-monospace, Consolas, monospace;\n  }\n  #modal input:focus { outline: none; border-color: var(--accent); }\n  #modal .row { display: flex; gap: 8px; margin-top: 20px; }\n  .tab-head { display: flex; gap: 6px; margin-bottom: 16px;\n              border-bottom: 1px solid var(--line); padding-bottom: 2px; }\n  .tab-btn {\n    background: none; border: none; color: var(--muted); cursor: pointer;\n    padding: 6px 12px 8px; font-family: ui-monospace, Consolas, monospace;\n    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;\n    border-bottom: 2px solid transparent; margin-bottom: -3px;\n  }\n  .tab-btn.active { color: var(--text); border-bottom-color: var(--accent); }\n  .cp-list { margin-top: 16px; display: flex; flex-direction: column; gap: 6px;\n             max-height: 180px; overflow-y: auto; }\n  .cp-row {\n    display: flex; align-items: center; gap: 10px;\n    border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px;\n    background: rgba(255, 255, 255, 0.02);\n  }\n  .cp-row .cp-n { flex: 1; font-size: 12px; overflow: hidden;\n                  text-overflow: ellipsis; white-space: nowrap; }\n  .cp-row .cp-u { font-family: ui-monospace, Consolas, monospace;\n                  font-size: 9px; color: var(--muted); }\n  .cp-row button {\n    background: none; border: 1px solid var(--line); color: var(--muted);\n    border-radius: 999px; width: 22px; height: 22px; cursor: pointer;\n    font-size: 13px; line-height: 1; flex-shrink: 0;\n  }\n  .cp-row button:hover { border-color: var(--err); color: var(--err); }\n  .cp-row button.edit {\n    width: auto; padding: 0 10px; font-size: 9px; letter-spacing: .12em;\n    text-transform: uppercase;\n  }\n  .cp-row button.edit:hover { border-color: #f5f5f5; color: #f5f5f5; }\n  .cp-empty { color: var(--muted); font-size: 11px; padding: 8px 2px; }\n</style>\n</head>\n<body>\n  <header>\n    <h1>FiveM Pack Manager</h1>\n    <div class="path" id="fivem-path"></div>\n    <button class="btn-top" onclick="api(\'fetch_remote\')">Actualiser</button>\n    <button class="btn-top" onclick="openSettings()">Options</button>\n    <button class="btn-site" onclick="api(\'open_site\')">uxqt.site &#8599;</button>\n  </header>\n\n  <main><div class="grid" id="grid"></div><div class="empty" id="empty" style="display:none">\n    Aucun pack disponible.<br>\n    Vérifie la connexion au serveur (bouton Actualiser)<br>\n    ou l\'URL configurée dans Options.\n  </div></main>\n\n  <div id="console-wrap">\n    <div id="progress"><div id="progress-bar"></div></div>\n    <div id="console-head">Console\n      <button onclick="document.getElementById(\'console\').innerHTML=\'\'">vider</button>\n    </div>\n    <div id="console"></div>\n  </div>\n\n  <div id="modal">\n    <div class="box">\n      <h2>Options</h2>\n\n      <div class="tab-head">\n        <button class="tab-btn active" data-tab="packs">Mes packs</button>\n        <button class="tab-btn" data-tab="apparence">Apparence</button>\n        <button class="tab-btn" data-tab="avance">Avancé</button>\n      </div>\n\n      <div class="tab" data-tab="packs">\n        <label>Ajouter un pack (Google Drive, Gofile, Mega.nz ou lien direct)</label>\n        <input id="cp-name" placeholder="Nom du pack">\n        <input id="cp-url" style="margin-top:6px" placeholder="https://drive.google.com/... ou mega.nz/file/... ou gofile.io/d/...">\n        <input id="cp-img" style="margin-top:6px" placeholder="Lien image (optionnel)">\n        <input id="cp-prev" style="margin-top:6px" placeholder="Lien YouTube preview (optionnel)">\n        <div class="row" style="margin-top:12px">\n          <button class="btn dl" id="cp-submit" onclick="addPack()">Ajouter</button>\n          <button class="btn unload" id="cp-cancel" style="display:none"\n                  onclick="cancelEdit()">Annuler</button>\n        </div>\n        <div id="cp-list" class="cp-list"></div>\n      </div>\n\n      <div class="tab" data-tab="apparence" style="display:none">\n        <label>Image de fond (fichier local ou lien http)</label>\n        <input id="set-bg" placeholder="vide = aucun fond">\n        <div class="row" style="margin-top:10px">\n          <button class="btn dl" onclick="browseBg()">Parcourir...</button>\n          <button class="btn unload" onclick="document.getElementById(\'set-bg\').value=\'\'">Retirer le fond</button>\n        </div>\n      </div>\n\n      <div class="tab" data-tab="avance" style="display:none">\n        <label>URL du packs.json (serveur)</label>\n        <input id="set-url" placeholder="https://tonsite.fr/packs-x7k2/packs.json">\n        <label>Clé d\'accès (optionnel)</label>\n        <input id="set-key" placeholder="laisser vide si aucune">\n        <label>Dossier FiveM.app (vide = détection auto)</label>\n        <input id="set-fivem" placeholder="C:\\Users\\toi\\AppData\\Local\\FiveM\\FiveM.app">\n        <label>Dossier GTA V (vide = détection auto)</label>\n        <input id="set-gta" placeholder="C:\\Program Files\\Rockstar Games\\Grand Theft Auto V Legacy">\n      </div>\n\n      <div class="row">\n        <button class="btn dl" onclick="saveSettings()">Enregistrer</button>\n        <button class="btn unload" onclick="closeSettings()">Fermer</button>\n      </div>\n    </div>\n  </div>\n\n<script>\n  window.__errs = [];\n  window.onerror = (m, s, l) => { if (window.__errs.length < 50) window.__errs.push(m + \' @\' + l); };\n  let st = null;\n  const TOKEN = "__TOKEN__";\n\n  // toute la communication passe par HTTP local : fiable, pas de pont pywebview\n  async function api(fn, ...args) {\n    const r = await fetch(\'/api/\' + fn, {\n      method: \'POST\',\n      headers: {\'X-Token\': TOKEN},\n      body: JSON.stringify(args),\n    });\n    if (!r.ok) throw new Error(fn + \' -> HTTP \' + r.status);\n    return await r.json();\n  }\n\n  function esc(s) { const d = document.createElement(\'div\'); d.textContent = s ?? \'\'; return d.innerHTML; }\n\n  function appendLog(msg, kind) {\n    const c = document.getElementById(\'console\');\n    const now = new Date().toLocaleTimeString(\'fr-FR\');\n    const line = document.createElement(\'div\');\n    line.innerHTML = `<span class="t">[${now}]</span><span class="${kind||\'info\'}">${esc(msg)}</span>`;\n    c.appendChild(line);\n    while (c.childElementCount > 400) c.removeChild(c.firstChild);\n    c.scrollTop = c.scrollHeight;\n  }\n\n  function setProgress(cur, total) {\n    const bar = document.getElementById(\'progress-bar\');\n    bar.style.width = total > 0 ? (100 * cur / total) + \'%\' : \'0%\';\n  }\n\n  function card(p) {\n    const badge = p.remote ? \'<span class="badge cloud">EN LIGNE</span>\'\n                : p.loaded ? \'<span class="badge on">INSTALLE</span>\'\n                           : \'<span class="badge off">PRET</span>\';\n    const initials = esc(p.name.split(/\\s+/).map(w => w[0]).join(\'\').slice(0, 3).toUpperCase());\n    const img = p.image ? `<img src="${p.image}" alt="">`\n                        : `<span class="initials">${initials}</span>`;\n    let meta = [];\n    if (p.version) meta.push(\'v\' + esc(p.version));\n    if (p.size) meta.push(esc(p.size));\n    if (p.loaded) meta.push(p.nfiles + \' fichiers installés\');\n    if (p.update) meta.push(\'<span class="upd">mise à jour disponible</span>\');\n    const dis = st.busy ? \'disabled\' : \'\';\n    // "Charger" télécharge + extrait + installe tout seul si besoin\n    // data-* + délégation : pas d\'injection possible via le nom du pack\n    const actions = `\n      <button class="btn load" data-fn="load" ${dis} ${p.loaded ? \'disabled\' : \'\'}\n              >Charger</button>\n      <button class="btn unload" data-fn="unload" ${dis} ${p.loaded ? \'\' : \'disabled\'}\n              >Décharger</button>\n      ${p.preview ? \'<button class="btn dl" data-fn="preview">Preview</button>\' : \'\'}`;\n    return `<div class="card ${p.loaded ? \'on\' : \'\'}" data-name="${esc(p.name)}">\n      <div class="thumb">${img}${badge}</div>\n      <div class="body">\n        <div class="name">${esc(p.name)}</div>\n        <div class="meta">${meta.join(\' · \')}</div>\n        <div class="actions">${actions}</div>\n      </div></div>`;\n  }\n\n  function applyBackground(url) {\n    if (url) {\n      document.body.style.backgroundImage =\n        `linear-gradient(rgba(0,0,0,.74), rgba(0,0,0,.84)), url("${url}")`;\n      document.body.style.backgroundSize = \'cover\';\n      document.body.style.backgroundPosition = \'center\';\n      document.body.style.backgroundAttachment = \'fixed\';\n    } else {\n      document.body.style.backgroundImage = \'\';\n    }\n  }\n\n  document.addEventListener(\'click\', e => {\n    const btn = e.target.closest(\'button[data-fn]\');\n    if (!btn || btn.disabled) return;\n    const name = btn.closest(\'.card\')?.dataset.name;\n    if (name) api(btn.dataset.fn, name);\n  });\n\n  async function refresh() {\n    st = await api(\'get_state\');\n    applyBackground(st.background);\n    const path = document.getElementById(\'fivem-path\');\n    if (st.fivem) {\n      path.textContent = \'FiveM : \' + st.fivem\n        + \'    GTA V : \' + (st.gta || \'introuvable (Options)\');\n      path.className = \'path\'; path.onclick = null;\n    } else {\n      path.textContent = \'FiveM introuvable — cliquer pour indiquer le dossier\';\n      path.className = \'path err\';\n      path.onclick = () => openSettings();\n    }\n    const grid = document.getElementById(\'grid\');\n    grid.innerHTML = st.packs.map(card).join(\'\');\n    document.getElementById(\'empty\').style.display = st.packs.length ? \'none\' : \'block\';\n    if (document.getElementById(\'modal\').classList.contains(\'show\')) renderCustomList();\n  }\n\n  function renderCustomList() {\n    const box = document.getElementById(\'cp-list\');\n    const mine = (st?.packs || []).filter(p => p.custom);\n    if (!mine.length) { box.innerHTML = \'<div class="cp-empty">Aucun pack ajouté.</div>\'; return; }\n    box.innerHTML = mine.map(p => `<div class="cp-row">\n      <div class="cp-n">${esc(p.name)}</div>\n      <button class="edit" data-ed="${esc(p.name)}" title="Modifier ce pack">Modifier</button>\n      <button data-rm="${esc(p.name)}" title="Supprimer (retire le pack et ses fichiers téléchargés)">&times;</button>\n    </div>`).join(\'\');\n    box.querySelectorAll(\'button[data-rm]\').forEach(b =>\n      b.onclick = () => {\n        if (confirm(\'Supprimer « \' + b.dataset.rm + \' » et ses fichiers téléchargés ?\'))\n          api(\'remove_custom_pack\', b.dataset.rm);\n      });\n    box.querySelectorAll(\'button[data-ed]\').forEach(b =>\n      b.onclick = () => startEdit(b.dataset.ed));\n  }\n\n  let editingOld = \'\';  // nom d\'origine du pack en cours de modification\n\n  function startEdit(name) {\n    const p = (st?.packs || []).find(x => x.name === name);\n    if (!p) return;\n    editingOld = name;\n    document.getElementById(\'cp-name\').value = p.name;\n    document.getElementById(\'cp-url\').value = p.url || \'\';\n    document.getElementById(\'cp-img\').value = p.image_link || \'\';\n    document.getElementById(\'cp-prev\').value = p.preview || \'\';\n    document.getElementById(\'cp-submit\').textContent = \'Enregistrer\';\n    document.getElementById(\'cp-cancel\').style.display = \'\';\n  }\n\n  function cancelEdit() {\n    editingOld = \'\';\n    [\'cp-name\', \'cp-url\', \'cp-img\', \'cp-prev\'].forEach(id =>\n      document.getElementById(id).value = \'\');\n    document.getElementById(\'cp-submit\').textContent = \'Ajouter\';\n    document.getElementById(\'cp-cancel\').style.display = \'none\';\n  }\n\n  function addPack() {\n    const n = document.getElementById(\'cp-name\');\n    const u = document.getElementById(\'cp-url\');\n    const i = document.getElementById(\'cp-img\');\n    const v = document.getElementById(\'cp-prev\');\n    if (!n.value.trim() || !u.value.trim()) return;\n    api(\'add_custom_pack\', n.value, u.value, i.value, v.value, editingOld);\n    cancelEdit();\n  }\n\n  async function browseBg() {\n    const p = await api(\'choose_background\');\n    if (p) document.getElementById(\'set-bg\').value = p;\n  }\n\n  document.querySelectorAll(\'.tab-btn\').forEach(b => b.onclick = () => {\n    document.querySelectorAll(\'.tab-btn\').forEach(x => x.classList.toggle(\'active\', x === b));\n    document.querySelectorAll(\'.tab[data-tab]\').forEach(t =>\n      t.style.display = t.dataset.tab === b.dataset.tab ? \'\' : \'none\');\n  });\n\n  function openSettings() {\n    document.getElementById(\'set-url\').value = st?.packs_url || \'\';\n    document.getElementById(\'set-key\').value = st?.packs_key || \'\';\n    document.getElementById(\'set-fivem\').value = st?.fivem || \'\';\n    document.getElementById(\'set-gta\').value = st?.gta || \'\';\n    document.getElementById(\'set-bg\').value = st?.background_setting || \'\';\n    renderCustomList();\n    document.getElementById(\'modal\').classList.add(\'show\');\n  }\n  function closeSettings() { document.getElementById(\'modal\').classList.remove(\'show\'); }\n  function saveSettings() {\n    api(\'save_settings\',\n      document.getElementById(\'set-url\').value,\n      document.getElementById(\'set-key\').value,\n      document.getElementById(\'set-fivem\').value,\n      document.getElementById(\'set-gta\').value,\n      document.getElementById(\'set-bg\').value);\n    closeSettings();\n  }\n\n  // boucle de récupération : logs, progression, rafraîchissements\n  let polling = false;\n  async function poll() {\n    if (polling) return;\n    polling = true;\n    try {\n      const r = await api(\'poll\');\n      for (const [msg, kind] of r.logs) appendLog(msg, kind);\n      setProgress(r.prog[0], r.prog[1]);\n      if (r.dirty) await refresh();\n    } catch (e) { /* app en cours de fermeture */ }\n    polling = false;\n  }\n\n  document.addEventListener(\'DOMContentLoaded\', async () => {\n    appendLog(\'FiveM Pack Manager démarré.\', \'ok\');\n    try { await refresh(); } catch (e) { appendLog(\'Erreur init : \' + e, \'err\'); }\n    api(\'fetch_remote\');   // les packs du site arrivent tout seuls\n    setInterval(poll, 250);\n  });\n</script>\n</body>\n</html>'
Bf={'get_state','poll','fetch_remote','load','unload','download','open_site','save_settings','add_custom_pack','remove_custom_pack','choose_background',W}
def Bg(api):
	G='text/plain';E=secrets.token_urlsafe(16);H=Be.replace('__TOKEN__',E).encode(R)
	class K(B5):
		def log_message(A,*B):0
		def _send(A,code,body,ctype):A.send_response(code);A.send_header(AZ,ctype);A.send_header(Aa,f(B(body)));A.send_header('Cache-Control','no-store');A.end_headers();A.wfile.write(body)
		def do_GET(B):
			if B.path in(Z,'/index.html'):B._send(200,H,'text/html; charset=utf-8')
			elif B.path.startswith('/bg'):
				E=api.background;C=A.path.join(b,E)if E and not E.startswith(AX)else D
				if C and A.path.exists(C):
					F=A.path.splitext(C)[1].lower()
					with L(C,'rb')as I:B._send(200,I.read(),Ah.get(F,'application/octet-stream'))
				else:B._send(404,b'no background',G)
			else:B._send(404,b'not found',G)
		def do_POST(A):
			B=A.path.removeprefix('/api/')
			if B not in Bf or A.headers.get(B3)!=E:A._send(403,b'forbidden',G);return
			try:C=Y(A.headers.get(Aa,0));D=I.loads(A.rfile.read(C)or b'[]');F=AM(api,B)(*D);A._send(200,I.dumps(F,ensure_ascii=N).encode(R),'application/json; charset=utf-8')
			except J as H:A._send(500,I.dumps({'error':f(H)}).encode(R),A9)
	F=B6(('127.0.0.1',0),K);j.Thread(target=F.serve_forever,daemon=C).start();return F,f"http://127.0.0.1:{F.server_address[1]}/",E
def Bh():
	G=Bd();H,E,I=Bg(G);K=[I];D=Af.create_window(B7,url=E,width=980,height=720,min_size=(700,520),background_color='#12121a')
	if A.environ.get('PM_SELFTEST'):
		import time as F
		def B(*A):B=' '.join(f(A)for A in A);print(B.encode('ascii',AR).decode(),flush=C)
		def L():
			F.sleep(4)
			try:import urllib.request as C;G=C.Request(E+'api/poll',data=b'[]',method='POST');G.add_header(B3,K[0]);H=C.urlopen(G,timeout=5).read()[:80];B('SELFTEST urllib POST:',H)
			except J as A:B('SELFTEST urllib POST KO:',A)
			try:D.evaluate_js("fetch('/api/poll', {method:'POST', headers:{'X-Token': TOKEN}, body:'[]'}).then(r => window.__errs.push('fetch OK ' + r.status)).catch(e => window.__errs.push('fetch KO ' + e))")
			except J as A:B('SELFTEST inject KO:',A)
			F.sleep(4)
			try:B('SELFTEST cards:',D.evaluate_js("document.querySelectorAll('.card').length"));B('SELFTEST console:',D.evaluate_js("document.getElementById('console').innerText"));B('SELFTEST jserrors:',D.evaluate_js("window.__errs.join(' | ') || 'none'"))
			except J as A:B('SELFTEST evaluate_js KO (pont pywebview):',A)
			D.destroy()
		j.Thread(target=L,daemon=C).start()
	try:Af.start(gui='edgechromium')
	finally:H.shutdown()
if __name__=='__main__':Bh()
