(function () {
  "use strict";

  /* ─────────────────── helpers ────────────────────────────── */
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fineHover = matchMedia("(hover: hover) and (pointer: fine)").matches;
  function safe(fn, name) { try { fn(); } catch (e) { console.warn("[" + name + "]", e); } }
  function lerp(a, b, t) { return a + (b - a) * t; }

  /* ─────────────────── cursor ────────────────────────────── */
  function initCursor() {
    if (!fineHover) return;
    const cursor = $("#cursor");
    if (!cursor) return;

    const dot  = $(".cursor-dot",  cursor);
    const ring = $(".cursor-ring", cursor);
    let mx = -100, my = -100, rx = -100, ry = -100;
    let firstMove = false;
    let raf;

    window.addEventListener("mousemove", function (e) {
      mx = e.clientX; my = e.clientY;
      if (!firstMove) {
        firstMove = true;
        rx = mx; ry = my;
        ring.style.transform = "translate3d(" + rx + "px," + ry + "px,0)";
        cursor.classList.add("is-ready");
      }
      dot.style.transform = "translate3d(" + mx + "px," + my + "px,0)";
    });

    function movering() {
      rx = lerp(rx, mx, 0.13);
      ry = lerp(ry, my, 0.13);
      ring.style.transform = "translate3d(" + rx + "px," + ry + "px,0)";
      raf = requestAnimationFrame(movering);
    }
    raf = requestAnimationFrame(movering);

    document.addEventListener("mouseover", function (e) {
      const el = e.target.closest("a,button,.service-card,.testi-btn,.cs-card");
      if (el) cursor.classList.add("is-hovering");
    });
    document.addEventListener("mouseout", function (e) {
      const el = e.target.closest("a,button,.service-card,.testi-btn,.cs-card");
      if (el && !el.contains(e.relatedTarget)) cursor.classList.remove("is-hovering");
    });
  }

  /* ─────────────────── nav ────────────────────────────── */
  function initNav() {
    const nav  = $("#nav");
    const ham  = $("#nav-hamburger");
    const mob  = $("#nav-mobile");
    if (!nav) return;

    // Scrolled state
    function checkScroll() {
      nav.classList.toggle("is-scrolled", scrollY > 20);
    }
    checkScroll();
    window.addEventListener("scroll", checkScroll, { passive: true });

    // Hamburger
    if (ham && mob) {
      ham.addEventListener("click", function () {
        const open = ham.getAttribute("aria-expanded") === "true";
        ham.setAttribute("aria-expanded", String(!open));
        ham.classList.toggle("is-open", !open);
        mob.classList.toggle("is-open", !open);
        mob.setAttribute("aria-hidden", String(open));
      });

      // Close on link click
      $$(".nav-mobile-link, .btn-mobile-cta", mob).forEach(function (link) {
        link.addEventListener("click", function () {
          ham.setAttribute("aria-expanded", "false");
          ham.classList.remove("is-open");
          mob.classList.remove("is-open");
          mob.setAttribute("aria-hidden", "true");
        });
      });
    }
  }

  /* ─────────────────── smooth scroll ────────────────────────────── */
  function initSmoothScroll() {
    document.addEventListener("click", function (e) {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute("href");
      if (!id || id === "#") { e.preventDefault(); window.scrollTo({ top: 0, behavior: "smooth" }); return; }
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue("--nav-h")) || 72;
      window.scrollTo({
        top: target.getBoundingClientRect().top + scrollY - offset,
        behavior: reduced ? "auto" : "smooth"
      });
    });
  }

  /* ─────────────────── hero mouse gradient ────────────────────────────── */
  function initHeroMouseGradient() {
    const hero = $(".hero");
    if (!hero) return;
    window.addEventListener("mousemove", function (e) {
      const x = (e.clientX / innerWidth * 100).toFixed(1) + "%";
      const y = (e.clientY / innerHeight * 100).toFixed(1) + "%";
      document.documentElement.style.setProperty("--mx", x);
      document.documentElement.style.setProperty("--my", y);
    }, { passive: true });
  }

  /* ─────────────────── particles ────────────────────────────── */
  function initParticles() {
    if (reduced) return;
    const canvas = $("#hero-particles");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const dpr = Math.min(devicePixelRatio || 1, 2);

    function resize() {
      const hero = $(".hero");
      if (!hero) return;
      const r = hero.getBoundingClientRect();
      canvas.width  = r.width * dpr;
      canvas.height = r.height * dpr;
      canvas.style.width  = r.width + "px";
      canvas.style.height = r.height + "px";
      ctx.scale(dpr, dpr);
    }
    resize();
    window.addEventListener("resize", resize, { passive: true });

    var W = canvas.width / dpr;
    var H = canvas.height / dpr;

    var PARTICLES = 70;
    var CONNECT_DIST = 120;
    var particles = [];

    function rand(min, max) { return min + Math.random() * (max - min); }

    for (var i = 0; i < PARTICLES; i++) {
      particles.push({
        x: rand(0, W), y: rand(0, H),
        vx: rand(-0.18, 0.18), vy: rand(-0.18, 0.18),
        r: rand(0.8, 2.2),
        alpha: rand(0.3, 0.7),
        color: Math.random() > 0.5 ? "99,102,241" : "34,211,238"
      });
    }

    function draw() {
      W = canvas.width / dpr;
      H = canvas.height / dpr;
      ctx.clearRect(0, 0, W, H);

      // Connect nearby particles
      for (var i = 0; i < particles.length; i++) {
        for (var j = i + 1; j < particles.length; j++) {
          var dx = particles[i].x - particles[j].x;
          var dy = particles[i].y - particles[j].y;
          var dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < CONNECT_DIST) {
            ctx.beginPath();
            ctx.strokeStyle = "rgba(99,102,241," + (0.12 * (1 - dist / CONNECT_DIST)) + ")";
            ctx.lineWidth = 0.5;
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.stroke();
          }
        }
      }

      // Draw dots
      particles.forEach(function (p) {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0) p.x = W;
        if (p.x > W) p.x = 0;
        if (p.y < 0) p.y = H;
        if (p.y > H) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(" + p.color + "," + p.alpha + ")";
        ctx.fill();
      });

      requestAnimationFrame(draw);
    }
    draw();
  }

  /* ─────────────────── scroll reveals ────────────────────────────── */
  function initReveals() {
    var els = $$(".reveal");
    if (!els.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.03, rootMargin: "0px 0px -20px 0px" });

    els.forEach(function (el) { io.observe(el); });

    // Safety: force-reveal anything still hidden after 6s
    setTimeout(function () {
      $$(".reveal:not(.is-visible)").forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.top < innerHeight + 200) el.classList.add("is-visible");
      });
    }, 6000);
  }

  /* ─────────────────── counters ────────────────────────────── */
  function initCounters() {
    var els = $$("[data-count]");
    if (!els.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target  = parseInt(el.dataset.count, 10);
        var prefix  = el.dataset.prefix  || "";
        var suffix  = el.dataset.suffix  || "";
        var start   = 0;
        var dur     = 2000;
        var startT  = null;

        function step(ts) {
          if (!startT) startT = ts;
          var prog = Math.min((ts - startT) / dur, 1);
          var ease = 1 - Math.pow(1 - prog, 3);
          var cur  = Math.round(start + (target - start) * ease);
          el.textContent = prefix + cur + suffix;
          if (prog < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        io.unobserve(el);
      });
    }, { threshold: 0.5 });

    els.forEach(function (el) { io.observe(el); });
  }

  /* ─────────────────── service card pointer tracking ────────────────────────────── */
  function initServiceCards() {
    if (!fineHover) return;
    $$(".service-card").forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var rect = card.getBoundingClientRect();
        var x = ((e.clientX - rect.left) / rect.width * 100).toFixed(1) + "%";
        var y = ((e.clientY - rect.top)  / rect.height * 100).toFixed(1) + "%";
        card.style.setProperty("--cx", x);
        card.style.setProperty("--cy", y);
      });
    });
  }

  /* ─────────────────── testimonials slider ────────────────────────────── */
  function initTestimonials() {
    var track  = $("#testi-track");
    var prev   = $("#testi-prev");
    var next   = $("#testi-next");
    var dotsEl = $("#testi-dots");
    if (!track) return;

    var cards = $$(".testi-card", track);
    var dots  = dotsEl ? $$(".testi-dot", dotsEl) : [];
    var total = cards.length;
    var cur   = 0;
    var timer;

    function goTo(index) {
      cur = ((index % total) + total) % total;
      track.style.transform = "translateX(" + (-cur * 100) + "%)";
      dots.forEach(function (d, i) {
        d.classList.toggle("testi-dot--active", i === cur);
        d.setAttribute("aria-selected", String(i === cur));
      });
    }

    function autoPlay() {
      timer = setInterval(function () { goTo(cur + 1); }, 5000);
    }
    function pausePlay() { clearInterval(timer); }

    if (prev) prev.addEventListener("click", function () { pausePlay(); goTo(cur - 1); autoPlay(); });
    if (next) next.addEventListener("click", function () { pausePlay(); goTo(cur + 1); autoPlay(); });

    dots.forEach(function (d) {
      d.addEventListener("click", function () {
        pausePlay();
        goTo(parseInt(d.dataset.i, 10));
        autoPlay();
      });
    });

    // Swipe support
    var touchX = 0;
    track.addEventListener("touchstart", function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    track.addEventListener("touchend", function (e) {
      var dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 40) { pausePlay(); goTo(cur + (dx < 0 ? 1 : -1)); autoPlay(); }
    }, { passive: true });

    autoPlay();
  }

  /* ─────────────────── footer form ────────────────────────────── */
  function initFooterForm() {
    var form = $("#footer-form");
    if (!form) return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = form.querySelector("input[type=email]");
      var btn   = form.querySelector("button");
      if (!input || !input.value) return;
      if (btn) { btn.textContent = "✓ Subscribed"; btn.disabled = true; }
      input.value = "";
    });
  }

  /* ─────────────────── GSAP scroll animations ────────────────────────────── */
  function initScrollAnimations() {
    if (!window.gsap || !window.ScrollTrigger) return;
    gsap.registerPlugin(ScrollTrigger);

    // Hero title word stagger
    var heroSpans = $$(".hero-title span");
    heroSpans.forEach(function (span, i) {
      gsap.fromTo(span,
        { opacity: 0, y: 30 },
        {
          opacity: 1, y: 0, duration: 0.9,
          ease: "power3.out",
          delay: 0.3 + i * 0.12,
          clearProps: "all"
        }
      );
    });

    // Stats count-up via ScrollTrigger trigger
    ScrollTrigger.create({
      trigger: ".stats-section",
      start: "top 75%",
      once: true,
      onEnter: function () {
        $$("[data-count]").forEach(function (el) {
          var ev = new Event("countup");
          el.dispatchEvent(ev);
        });
      }
    });

    // Process steps stagger
    var steps = $$(".process-step");
    if (steps.length) {
      gsap.fromTo(steps,
        { opacity: 0, y: 20 },
        {
          opacity: 1, y: 0,
          duration: 0.7,
          stagger: 0.15,
          ease: "power2.out",
          scrollTrigger: { trigger: ".process-section", start: "top 70%", once: true }
        }
      );
    }

    // Ecosystem SVG lines draw-in
    var ecoLines = $$(".eco-line");
    if (ecoLines.length) {
      ecoLines.forEach(function (line) {
        var len = line.getTotalLength ? line.getTotalLength() : 200;
        gsap.fromTo(line,
          { strokeDasharray: len, strokeDashoffset: len },
          {
            strokeDashoffset: 0,
            duration: 1.8,
            ease: "power2.out",
            stagger: 0.1,
            scrollTrigger: { trigger: ".eco-section", start: "top 65%", once: true }
          }
        );
      });
    }

    // About stats card parallax
    var aboutCard = $(".about-stats-card");
    if (aboutCard) {
      gsap.fromTo(aboutCard,
        { y: 30, opacity: 0 },
        {
          y: 0, opacity: 1,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: { trigger: ".about-section", start: "top 70%", once: true }
        }
      );
    }

    // AI dashboard animate in
    var aiDash = $(".ai-dashboard");
    if (aiDash) {
      gsap.fromTo(aiDash,
        { x: 40, opacity: 0 },
        {
          x: 0, opacity: 1,
          duration: 1,
          ease: "power3.out",
          scrollTrigger: { trigger: ".ai-section", start: "top 65%", once: true }
        }
      );
    }

    // Case study cards stagger
    var csCards = $$(".cs-card");
    if (csCards.length) {
      gsap.fromTo(csCards,
        { opacity: 0, y: 24 },
        {
          opacity: 1, y: 0,
          duration: .8,
          stagger: .15,
          ease: "power2.out",
          scrollTrigger: { trigger: ".cs-section", start: "top 70%", once: true }
        }
      );
    }
  }

  /* ─────────────────── BOOT ────────────────────────────── */
  function boot() {
    safe(initCursor,           "initCursor");
    safe(initNav,              "initNav");
    safe(initSmoothScroll,     "initSmoothScroll");
    safe(initHeroMouseGradient,"initHeroMouseGradient");
    safe(initParticles,        "initParticles");
    safe(initReveals,          "initReveals");
    safe(initCounters,         "initCounters");
    safe(initServiceCards,     "initServiceCards");
    safe(initTestimonials,     "initTestimonials");
    safe(initFooterForm,       "initFooterForm");

    if (window.gsap && window.ScrollTrigger) {
      safe(initScrollAnimations, "initScrollAnimations");
    }

    document.documentElement.classList.add("is-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
