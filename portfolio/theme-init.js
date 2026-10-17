/* Apply the saved appearance before styles paint. Dark is the site default. */
(() => {
  let theme = 'dark';
  try {
    const saved = localStorage.getItem('site-theme');
    if (saved === 'light' || saved === 'dark') theme = saved;
  } catch (_) {}
  document.documentElement.dataset.theme = theme;
  document.querySelector('meta[name="theme-color"]').content = theme === 'dark' ? '#111614' : '#f6f4ef';
})();
