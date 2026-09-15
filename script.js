document.getElementById('year').textContent = new Date().getFullYear();

// scroll progress bar
const scrollBar = document.getElementById('scrollProgress');
if (scrollBar) {
  const updateProgress = () => {
    const h = document.documentElement;
    const scrolled = h.scrollTop;
    const height = h.scrollHeight - h.clientHeight;
    scrollBar.style.width = (height > 0 ? (scrolled / height) * 100 : 0) + '%';
  };
  document.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
}

// mobile menu toggle
const menuBtn = document.getElementById('menuBtn');
const navLinks = document.getElementById('navLinks');
if (menuBtn && navLinks) {
  menuBtn.addEventListener('click', () => navLinks.classList.toggle('open'));
  navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));
}

// scroll reveal
const revealEls = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && revealEls.length) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
  revealEls.forEach(el => io.observe(el));
} else {
  revealEls.forEach(el => el.classList.add('in'));
}

// nav scrollspy (top-level sections)
const spySections = ['projects', 'about', 'skills', 'contact']
  .map(id => document.getElementById(id))
  .filter(Boolean);
const navAnchors = document.querySelectorAll('.nav-links a');
if ('IntersectionObserver' in window && spySections.length) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navAnchors.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + id));
      }
    });
  }, { threshold: 0.5 });
  spySections.forEach(s => spy.observe(s));
}
