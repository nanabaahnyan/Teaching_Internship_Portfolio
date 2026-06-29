/* ============================================================
   TEACHING PORTFOLIO — main.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    /* ── Image Carousel ── */
    initCarousel();

    /* ── Gallery Lightbox ── */
    initLightbox();

    /* ── Scroll-in animations ── */
    initScrollReveal();

    /* ── Active nav highlight (fallback) ── */
    highlightNav();
});


/* ── Carousel ────────────────────────────────────────── */
function initCarousel() {
    const wrappers = document.querySelectorAll('[data-carousel]');
    wrappers.forEach(wrapper => {
        const track  = wrapper.querySelector('.carousel-track');
        const slides = wrapper.querySelectorAll('.carousel-slide');
        const dots   = wrapper.querySelectorAll('.carousel-dot');
        const prev   = wrapper.querySelector('.carousel-btn.prev');
        const next   = wrapper.querySelector('.carousel-btn.next');
        if (!track || slides.length === 0) return;

        let current  = 0;
        let timer    = null;

        function goTo(idx) {
            current = (idx + slides.length) % slides.length;
            track.style.transform = `translateX(-${current * 100}%)`;
            dots.forEach((d, i) => d.classList.toggle('active', i === current));
        }

        function startAuto() { timer = setInterval(() => goTo(current + 1), 4500); }
        function stopAuto()  { clearInterval(timer); }

        prev  && prev.addEventListener('click',  () => { stopAuto(); goTo(current - 1); startAuto(); });
        next  && next.addEventListener('click',  () => { stopAuto(); goTo(current + 1); startAuto(); });
        dots.forEach((d, i) => d.addEventListener('click', () => { stopAuto(); goTo(i); startAuto(); }));

        /* Touch / swipe */
        let touchStartX = 0;
        wrapper.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
        wrapper.addEventListener('touchend',   e => {
            const diff = touchStartX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 40) { stopAuto(); goTo(diff > 0 ? current + 1 : current - 1); startAuto(); }
        });

        goTo(0);
        startAuto();
    });
}


/* ── Lightbox ────────────────────────────────────────── */
function initLightbox() {
    const lightbox = document.getElementById('lightbox');
    if (!lightbox) return;

    const lbImg     = lightbox.querySelector('#lightboxImg');
    const lbCaption = lightbox.querySelector('#lightboxCaption');
    const lbClose   = lightbox.querySelector('.lightbox-close');

    document.querySelectorAll('[data-lightbox]').forEach(item => {
        item.addEventListener('click', () => {
            const src     = item.dataset.src     || item.querySelector('img')?.src || '';
            const caption = item.dataset.caption  || item.querySelector('.gallery-caption')?.textContent || '';
            lbImg.src         = src;
            lbCaption.textContent = caption;
            lightbox.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

    function closeLightbox() {
        lightbox.classList.remove('open');
        document.body.style.overflow = '';
        lbImg.src = '';
    }

    lbClose && lbClose.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });
}


/* ── Scroll Reveal ───────────────────────────────────── */
function initScrollReveal() {
    const els = document.querySelectorAll('.reveal');
    if (!els.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });

    els.forEach(el => observer.observe(el));
}


/* ── Active Nav ──────────────────────────────────────── */
function highlightNav() {
    const path  = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === path) link.classList.add('active');
    });
}
