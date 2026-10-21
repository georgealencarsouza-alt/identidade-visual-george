// Escala o canvas de 3480px para a largura da janela e liga os ajustes
// (textura granulada e tratamento da foto).
//
// Parâmetros de URL, usados também pelo script de exportação:
//   ?grain=0          desliga a textura
//   ?photo=original   foto com as cores originais
//   ?export=1         canvas em tamanho real, sem controles
(() => {
  const params = new URLSearchParams(location.search);
  const body = document.body;
  const canvas = document.getElementById('canvas');
  const viewport = canvas.parentElement;
  const grainToggle = document.getElementById('toggle-grain');
  const photoSelect = document.getElementById('photo-tint');

  function setGrain(on) {
    body.classList.toggle('no-grain', !on);
    grainToggle.checked = on;
  }

  function setPhoto(mode) {
    body.classList.toggle('photo-original', mode === 'original');
    photoSelect.value = mode;
  }

  setGrain(params.get('grain') !== '0');
  setPhoto(params.get('photo') === 'original' ? 'original' : 'duotone');

  grainToggle.addEventListener('change', () => setGrain(grainToggle.checked));
  photoSelect.addEventListener('change', () => setPhoto(photoSelect.value));

  if (params.get('export') === '1') {
    body.classList.add('export');
    return;
  }

  function fit() {
    const scale = Math.min(1, document.documentElement.clientWidth / canvas.offsetWidth);
    canvas.style.transform = `scale(${scale})`;
    viewport.style.height = `${canvas.offsetHeight * scale}px`;
  }

  fit();
  window.addEventListener('resize', fit);
  document.fonts?.ready.then(fit);

  // Âncoras da capa: rolar até a seção considerando a escala.
  document.querySelectorAll('.cover__chips a').forEach((link) => {
    link.addEventListener('click', (event) => {
      const target = document.querySelector(link.getAttribute('href'));
      if (!target) return;
      event.preventDefault();
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY, behavior: 'smooth' });
    });
  });
})();
