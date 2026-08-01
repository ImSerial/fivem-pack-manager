(() => {
  const doux = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── sons synthétisés : aucun fichier, tout est généré à la volée ──
     Le contexte audio ne peut naître qu'après un geste de l'utilisateur,
     règle des navigateurs contre les sites qui font du bruit tout seuls. */
  const Son = (() => {
    let ctx = null, master = null, dernier = 0;

    const demarrer = () => {
      if (ctx) return;
      const AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return;
      ctx = new AC();
      master = ctx.createGain();
      master.gain.value = .5;
      const filtre = ctx.createBiquadFilter();      // adoucit les aigus
      filtre.type = 'lowpass'; filtre.frequency.value = 5200;
      master.connect(filtre); filtre.connect(ctx.destination);
    };

    const note = (f0, f1, duree, vol, forme = 'sine') => {
      if (!ctx) return;
      const t = ctx.currentTime;
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.type = forme;
      o.frequency.setValueAtTime(f0, t);
      if (f1 !== f0) o.frequency.exponentialRampToValueAtTime(f1, t + duree);
      // attaque très courte mais non nulle : à zéro on entend un clic parasite
      g.gain.setValueAtTime(.0001, t);
      g.gain.exponentialRampToValueAtTime(vol, t + .006);
      g.gain.exponentialRampToValueAtTime(.0001, t + duree);
      o.connect(g); g.connect(master);
      o.start(t); o.stop(t + duree + .02);
    };

    return {
      eveiller: demarrer,
      survol() {
        if (!ctx) return;
        const t = performance.now();
        if (t - dernier < 55) return;        // évite la mitraillette
        dernier = t;
        const d = 1 + (Math.random() - .5) * .06;   // micro-variation de hauteur
        note(1240 * d, 1180 * d, .045, .022, 'triangle');
      },
      bouton() {
        if (!ctx) return;
        const t = performance.now();
        if (t - dernier < 55) return;
        dernier = t;
        note(700, 940, .07, .03, 'sine');
      },
      clic() {
        if (!ctx) return;
        note(540, 300, .085, .045, 'sine');
        note(1120, 880, .07, .022, 'triangle');
      },
      ouvre() { if (ctx) note(520, 880, .1, .03, 'sine'); },
      ferme() { if (ctx) note(760, 420, .09, .026, 'sine'); }
    };
  })();

  // le contexte audio n'a le droit de démarrer qu'après une interaction
  ['pointerdown', 'keydown'].forEach(e =>
    addEventListener(e, () => Son.eveiller(), { once: true }));

  document.querySelectorAll('.bulle, .carte, .spec, .etape, nav a')
    .forEach(el => el.addEventListener('pointerenter', () => Son.survol()));
  document.querySelectorAll('.btn, summary')
    .forEach(el => el.addEventListener('pointerenter', () => Son.bouton()));
  document.querySelectorAll('.btn').forEach(el =>
    el.addEventListener('click', () => Son.clic()));
  document.querySelectorAll('details').forEach(d =>
    d.addEventListener('toggle', () => d.open ? Son.ouvre() : Son.ferme()));

  /* ── navigation sans dièse dans l'adresse ──
     On fait défiler nous-mêmes et on ne touche jamais à location.hash. */
  document.querySelectorAll('[data-vers]').forEach(a => {
    a.addEventListener('click', e => {
      const cible = document.getElementById(a.dataset.vers);
      if (!cible) return;
      e.preventDefault();
      Son.clic();
      const y = cible.getBoundingClientRect().top + scrollY - 84;
      scrollTo({ top: y, behavior: doux ? 'auto' : 'smooth' });
    });
  });

  /* ── halo qui suit la souris + reflet dans les cartes ── */
  const torche = document.querySelector('.torche');
  let sx = innerWidth / 2, sy = innerHeight / 3, cx = sx, cy = sy, bouge = false;
  addEventListener('pointermove', e => {
    sx = e.clientX; sy = e.clientY;
    if (!bouge) { bouge = true; document.body.classList.add('pointeur'); }
  }, { passive: true });

  const zonesReflet = document.querySelectorAll('.carte, .btn');
  addEventListener('pointermove', e => {
    for (const el of zonesReflet) {
      const r = el.getBoundingClientRect();
      if (e.clientX < r.left - 40 || e.clientX > r.right + 40 ||
          e.clientY < r.top - 40 || e.clientY > r.bottom + 40) continue;
      el.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      el.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }
  }, { passive: true });

  /* ── inclinaison de la capture ── */
  const cadre = document.getElementById('cadre');
  if (!doux) cadre.addEventListener('pointermove', e => {
    const r = cadre.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width - .5;
    const py = (e.clientY - r.top) / r.height - .5;
    cadre.style.setProperty('--ry', (px * 5).toFixed(2) + 'deg');
    cadre.style.setProperty('--rx', (-py * 4).toFixed(2) + 'deg');
  }, { passive: true });
  cadre.addEventListener('pointerleave', () => {
    cadre.style.setProperty('--rx', '0deg');
    cadre.style.setProperty('--ry', '0deg');
  });

  /* ── champ de particules ──
     Un seul canvas, redessine dans la boucle d'animation existante. Les
     points derivent lentement, se relient quand ils sont proches, et
     s'ecartent du curseur. Densite calculee sur l'aire : un ecran large ne
     doit pas se retrouver avec un nuage plus dense qu'un portable. */
  const champ = document.getElementById('champ');
  const ctx2d = champ.getContext('2d', { alpha: true });
  let points = [], dpr = 1, L = 0, H = 0;

  const semer = () => {
    dpr = Math.min(devicePixelRatio || 1, 2);
    L = innerWidth; H = innerHeight;
    champ.width = L * dpr; champ.height = H * dpr;
    champ.style.width = L + 'px'; champ.style.height = H + 'px';
    ctx2d.setTransform(dpr, 0, 0, dpr, 0, 0);
    const n = Math.min(90, Math.round(L * H / 20000));
    points = Array.from({ length: n }, () => ({
      x: Math.random() * L, y: Math.random() * H,
      vx: (Math.random() - .5) * .16, vy: (Math.random() - .5) * .16,
      r: Math.random() * 1.5 + .5,
      rouge: Math.random() < .22          // une minorite de points rouges
    }));
  };
  semer();
  let redim;
  addEventListener('resize', () => { clearTimeout(redim); redim = setTimeout(semer, 200); });

  const dessiner = () => {
    ctx2d.clearRect(0, 0, L, H);
    for (const p of points) {
      p.x += p.vx; p.y += p.vy;
      // le curseur repousse doucement ce qui passe a proximite
      const dx = p.x - cx, dy = p.y - cy, d2 = dx * dx + dy * dy;
      if (d2 < 26000 && d2 > 1) {
        const f = (1 - d2 / 26000) * .5, d = Math.sqrt(d2);
        p.x += dx / d * f; p.y += dy / d * f;
      }
      if (p.x < -12) p.x = L + 12; else if (p.x > L + 12) p.x = -12;
      if (p.y < -12) p.y = H + 12; else if (p.y > H + 12) p.y = -12;
      ctx2d.beginPath();
      ctx2d.arc(p.x, p.y, p.r, 0, 6.2832);
      ctx2d.fillStyle = p.rouge ? 'rgba(216,26,26,.55)' : 'rgba(255,255,255,.28)';
      ctx2d.fill();
    }
    // liaisons : boucle sur les paires, l'opacite decroit avec la distance
    for (let i = 0; i < points.length; i++) {
      for (let j = i + 1; j < points.length; j++) {
        const a = points[i], b = points[j];
        const dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy;
        if (d2 > 15000) continue;
        const o = (1 - d2 / 15000) * .16;
        ctx2d.strokeStyle = (a.rouge || b.rouge)
          ? 'rgba(216,26,26,' + o.toFixed(3) + ')'
          : 'rgba(255,255,255,' + (o * .7).toFixed(3) + ')';
        ctx2d.lineWidth = 1;
        ctx2d.beginPath();
        ctx2d.moveTo(a.x, a.y); ctx2d.lineTo(b.x, b.y); ctx2d.stroke();
      }
    }
  };

  /* ── boucle d'animation unique : halo, parallaxe, particules ── */
  const grille = document.querySelector('.grille');
  const entete = document.getElementById('haut');
  const boucle = () => {
    cx += (sx - cx) * .09; cy += (sy - cy) * .09;      // lissage
    const y = scrollY;
    if (!doux) {                       // halo et parallaxe : seulement si voulu
      torche.style.setProperty('--tx', cx.toFixed(1) + 'px');
      torche.style.setProperty('--ty', cy.toFixed(1) + 'px');
      grille.style.setProperty('--par', (-y * .06).toFixed(1) + 'px');
    }
    entete.classList.toggle('colle', y > 12);
    if (!document.hidden) dessiner();   // rien a calculer si l'onglet est cache
    requestAnimationFrame(boucle);
  };
  requestAnimationFrame(boucle);

  /* ── apparition au défilement ── */
  const io = new IntersectionObserver(es => {
    es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('vu'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -70px 0px' });
  document.querySelectorAll('.monte').forEach(el => io.observe(el));

  /* ── lien de navigation actif selon la section visible ── */
  const liens = [...document.querySelectorAll('nav a[data-vers]')];
  const ioNav = new IntersectionObserver(es => {
    es.forEach(e => {
      if (!e.isIntersecting) return;
      liens.forEach(a => a.classList.toggle('actif', a.dataset.vers === e.target.id));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  liens.forEach(a => {
    const s = document.getElementById(a.dataset.vers);
    if (s) ioNav.observe(s);
  });
})();
