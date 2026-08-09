/**
 * Animaciones de la portada (hero + scroll-reveal) con GSAP + ScrollTrigger.
 * Se degrada a estado visible estático si el usuario prefiere menos movimiento
 * o si GSAP no llegó a cargar (p. ej. fallo de CDN).
 */
(function () {
  /* ---------- Carrusel horizontal de negocios destacados ----------
   * Scroll nativo (no depende de GSAP ni de ninguna librería): las flechas
   * solo desplazan el contenedor. Si el contenido cabe sin hacer scroll,
   * las ocultamos para no mostrar controles que no hacen nada. */
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-carousel]").forEach(function (track) {
      var key = track.dataset.carousel;
      var controls = document.querySelector(
        '[data-carousel-controls="' + key + '"]'
      );

      function updateControlsVisibility() {
        if (!controls) return;
        var canScroll = track.scrollWidth > track.clientWidth + 4;
        controls.classList.toggle("sm:hidden", !canScroll);
        controls.classList.toggle("sm:flex", canScroll);
      }

      function scrollByCard(direction) {
        var card = track.querySelector(":scope > *");
        var gap = 16; /* debe coincidir con la clase gap-4 del contenedor */
        var amount = card ? card.getBoundingClientRect().width + gap : 250;
        track.scrollBy({ left: direction * amount, behavior: "smooth" });
      }

      var prevBtn = document.querySelector('[data-carousel-prev="' + key + '"]');
      var nextBtn = document.querySelector('[data-carousel-next="' + key + '"]');
      if (prevBtn) prevBtn.addEventListener("click", function () { scrollByCard(-1); });
      if (nextBtn) nextBtn.addEventListener("click", function () { scrollByCard(1); });

      updateControlsVisibility();
      window.addEventListener("resize", updateControlsVisibility);
    });
  });

  /* ---------- Botón de "Me gusta" (guardar negocio en favoritos) ----------
   * Envía el formulario por AJAX para que el corazón cambie al instante, sin
   * recargar la página. Si algo falla (red caída, etc.) se manda el formulario
   * de verdad como respaldo. */
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-favorito-form]").forEach(function (form) {
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        var btn = form.querySelector("[data-favorito-btn]");
        var icon = btn ? btn.querySelector("i") : null;
        var csrfInput = form.querySelector('[name="csrfmiddlewaretoken"]');

        fetch(form.action, {
          method: "POST",
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfInput ? csrfInput.value : "",
          },
          body: new FormData(form),
        })
          .then(function (response) {
            if (!response.ok) throw new Error("network");
            return response.json();
          })
          .then(function (data) {
            if (!icon) return;
            icon.classList.toggle("bi-heart-fill", data.liked);
            icon.classList.toggle("bi-heart", !data.liked);
            if (btn) {
              btn.setAttribute(
                "aria-label",
                data.liked ? "Quitar de mis favoritos" : "Guardar en mis favoritos"
              );
            }
          })
          .catch(function () {
            form.submit();
          });
      });
    });
  });

  /* ---------- Estrellas de valoración (1 a 5) ----------
   * Cada tarjeta trae 5 botones invisibles superpuestos a las estrellas.
   * Al pulsar uno se envía la puntuación por AJAX y se rellenan en dorado
   * las estrellas correspondientes (redondeo a la mitad superior). */
  function pintarEstrellas(widget, valor) {
    var val = Number(valor) || 0;
    widget.querySelectorAll("[data-rating-star]").forEach(function (ic, i) {
      var starNum = i + 1;
      var isFill = val >= starNum;
      var isHalf = !isFill && val >= (starNum - 0.5);

      ic.classList.toggle("bi-star-fill", isFill);
      ic.classList.toggle("bi-star-half", isHalf);
      ic.classList.toggle("bi-star", !isFill && !isHalf);

      ic.classList.toggle("text-nica-gold", isFill || isHalf);
      ic.classList.toggle("text-slate-400", !isFill && !isHalf);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-rating-widget]").forEach(function (widget) {
      var url = widget.dataset.rateUrl;
      var label = widget.querySelector("[data-rating-label]");
      var csrfInput = widget.querySelector('[name="csrfmiddlewaretoken"]');
      if (!url) return;

      widget.querySelectorAll("[data-rate]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var puntuacion = btn.dataset.rate;

          fetch(url, {
            method: "POST",
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": csrfInput ? csrfInput.value : "",
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: "puntuacion=" + encodeURIComponent(puntuacion),
          })
            .then(function (response) {
              if (!response.ok) throw new Error("network");
              return response.json();
            })
            .then(function (data) {
              pintarEstrellas(widget, data.rating_avg);
              if (label) {
                var nota = Number(data.rating_avg);
                label.textContent = Number.isFinite(nota) ? nota.toFixed(1).replace(".", ",") : "-";
              }
            })
            .catch(function () {
              /* Sin conexión: no forzamos recarga para no perder el scroll del carrusel */
            });
        });
      });
    });
  });

  var prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  if (typeof gsap === "undefined" || prefersReducedMotion) {
    document
      .querySelectorAll("[data-reveal], [data-hero-el]")
      .forEach(function (el) {
        el.style.opacity = 1;
        el.style.transform = "none";
      });
    return;
  }

  if (typeof ScrollTrigger !== "undefined") {
    gsap.registerPlugin(ScrollTrigger);
  }

  document.addEventListener("DOMContentLoaded", function () {
    /* ---------- Entrada del hero ---------- */
    var heroEls = gsap.utils.toArray("[data-hero-el]");
    if (heroEls.length) {
      gsap.set(heroEls, { autoAlpha: 0, y: 26 });
      gsap
        .timeline({ defaults: { ease: "power3.out", duration: 0.9 } })
        .to(heroEls, { autoAlpha: 1, y: 0, stagger: 0.14 });
    }

    /* ---------- Parallax suave de la imagen del hero ---------- */
    var heroBg = document.querySelector("[data-hero-bg]");
    if (heroBg && typeof ScrollTrigger !== "undefined") {
      gsap.to(heroBg, {
        yPercent: 14,
        ease: "none",
        scrollTrigger: {
          trigger: heroBg.closest("[data-hero-section]") || heroBg,
          start: "top top",
          end: "bottom top",
          scrub: true,
        },
      });
    }

    /* ---------- Revelado al hacer scroll para el resto de secciones ---------- */
    if (typeof ScrollTrigger !== "undefined") {
      gsap.utils.toArray("[data-reveal]").forEach(function (el, i) {
        gsap.fromTo(
          el,
          { autoAlpha: 0, y: 28 },
          {
            autoAlpha: 1,
            y: 0,
            duration: 0.7,
            ease: "power2.out",
            delay: (i % 3) * 0.08,
            scrollTrigger: {
              trigger: el,
              start: "top 88%",
              toggleActions: "play none none none",
            },
          }
        );
      });

      /* Contadores animados de la banda de estadísticas */
      gsap.utils.toArray("[data-counter]").forEach(function (el) {
        var target = parseFloat(el.dataset.counter);
        if (isNaN(target)) return;
        var suffix = el.dataset.counterSuffix || "";
        var counter = { val: 0 };
        gsap.to(counter, {
          val: target,
          duration: 1.6,
          ease: "power1.out",
          scrollTrigger: {
            trigger: el,
            start: "top 90%",
            toggleActions: "play none none none",
          },
          onUpdate: function () {
            el.textContent = Math.round(counter.val) + suffix;
          },
        });
      });
    } else {
      gsap.set("[data-reveal]", { autoAlpha: 1, y: 0 });
    }
  });
})();
