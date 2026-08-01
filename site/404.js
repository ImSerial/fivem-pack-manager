  // affiche l'adresse demandée, échappée : elle vient de la barre d'adresse
  // et ne doit jamais être injectée telle quelle dans le document
  const p = document.createElement('b');
  p.textContent = location.pathname.slice(0, 120) || '/';
  const boite = document.getElementById('chemin');
  boite.append('modium.xyz', p);
