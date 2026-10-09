/**
 * motion-core.js — Núcleo Global de Motion Mr. Macário Burger
 * Regras Estritas:
 * - Camadas-folha apenas (transform e opacity).
 * - Elementos decorativos contínuos nunca se movem e não possuem ancestrais animados.
 * - 3 modos: 'full', 'reduced', 'paused'.
 * - 2 níveis de qualidade: 'high', 'low'.
 * - Nada acima da dobra depende de JS para aparecer.
 * - Scripts clássicos auto-hospedados (sem CDN, compatível com file://).
 */

(function (window, document) {
  'use strict';

  var MrMacarioMotion = {
    mode: 'full', // 'full' | 'reduced' | 'paused'
    quality: 'high', // 'high' | 'low'
    lenis: null,
    isPausedByUser: false,
    sectionModules: {},
    activeLoops: [],
    loopObservers: [],

    detectQuality: function () {
      var isLowMemory = navigator.deviceMemory && navigator.deviceMemory <= 4;
      var isLowCpu = navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4;
      var isDataSaver = navigator.connection && (
        navigator.connection.saveData === true ||
        /2g|3g/.test(navigator.connection.effectiveType || '')
      );
      var isNarrow = window.innerWidth < 640;

      if (isLowMemory || isLowCpu || isDataSaver || isNarrow) {
        return 'low';
      }
      return 'high';
    },

    detectReducedMotion: function () {
      return !!(
        window.matchMedia &&
        window.matchMedia('(prefers-reduced-motion: reduce)').matches
      );
    },

    init: function () {
      var self = this;

      // 1. Detectar preferências do usuário e recursos de hardware
      self.quality = self.detectQuality();
      if (self.detectReducedMotion()) {
        self.mode = 'reduced';
      } else {
        self.mode = 'full';
      }

      document.documentElement.setAttribute('data-motion-mode', self.mode);
      document.documentElement.setAttribute('data-motion-quality', self.quality);

      // Ouvinte para prefers-reduced-motion em tempo real
      if (window.matchMedia) {
        var mq = window.matchMedia('(prefers-reduced-motion: reduce)');
        if (mq.addEventListener) {
          mq.addEventListener('change', function (e) {
            self.setMode(e.matches ? 'reduced' : 'full');
          });
        }
      }

      // 2. Registrar GSAP Plugins se disponíveis
      if (window.gsap && window.ScrollTrigger) {
        window.gsap.registerPlugin(window.ScrollTrigger);
        window.ScrollTrigger.config({ limitCallbacks: true });
      }

      // 3. Inicializar Lenis Smooth Scroll (Apenas em desktop e modo full)
      self.initLenis();

      // 4. Configurar Botão de Pausa Acessível
      self.setupPauseButton();

      // 5. Configurar Pausa em Aba Oculta
      document.addEventListener('visibilitychange', function () {
        if (document.hidden) {
          self.pauseAll();
        } else if (!self.isPausedByUser && self.mode !== 'paused') {
          self.resumeAll();
        }
      });

      // 6. Configurar Observadores de Loops Fora da Tela
      self.setupLoopVisibilityObserver();

      // Log informativo de inicialização
      console.log(
        '[MrMacarioMotion] Núcleo ativo | Modo:',
        self.mode,
        '| Qualidade:',
        self.quality,
        '| Lenis:',
        !!self.lenis
      );
    },

    initLenis: function () {
      var self = this;
      // Lenis só é ativado em Full Motion e telas desktop/laptop (>= 1024px)
      if (self.mode === 'reduced' || window.innerWidth < 1024 || !window.Lenis) {
        if (self.lenis) {
          self.lenis.destroy();
          self.lenis = null;
        }
        return;
      }

      try {
        self.lenis = new window.Lenis({
          duration: 1.15,
          easing: function (t) {
            return Math.min(1, 1.001 - Math.pow(2, -10 * t));
          },
          smoothWheel: true,
          touchMultiplier: 1.5,
          infinite: false
        });

        if (window.gsap && window.ScrollTrigger) {
          self.lenis.on('scroll', window.ScrollTrigger.update);
          window.gsap.ticker.add(function (time) {
            if (self.lenis) self.lenis.raf(time * 1000);
          });
          window.gsap.ticker.lagSmoothing(0);
        } else {
          var raf = function (time) {
            if (self.lenis) {
              self.lenis.raf(time);
              requestAnimationFrame(raf);
            }
          };
          requestAnimationFrame(raf);
        }
      } catch (err) {
        console.warn('[MrMacarioMotion] Falha ao iniciar Lenis:', err);
      }
    },

    setMode: function (newMode) {
      var self = this;
      self.mode = newMode;
      document.documentElement.setAttribute('data-motion-mode', newMode);

      if (newMode === 'reduced') {
        if (self.lenis) {
          self.lenis.destroy();
          self.lenis = null;
        }
        if (window.gsap) {
          window.gsap.globalTimeline.timeScale(1);
        }
        self.activeLoops.forEach(function (l) {
          if (l.tween) l.tween.pause(0);
        });
      } else if (newMode === 'paused') {
        self.pauseAll();
      } else if (newMode === 'full') {
        self.isPausedByUser = false;
        self.initLenis();
        self.resumeAll();
      }
    },

    pauseAll: function () {
      var self = this;
      if (window.gsap) {
        window.gsap.globalTimeline.pause();
      }
      if (self.lenis) {
        self.lenis.stop();
      }
      self.activeLoops.forEach(function (l) {
        if (l.tween) l.tween.pause();
      });
    },

    resumeAll: function () {
      var self = this;
      if (self.mode === 'paused' || self.isPausedByUser) return;

      if (window.gsap) {
        window.gsap.globalTimeline.play();
      }
      if (self.lenis) {
        self.lenis.start();
      }
      self.activeLoops.forEach(function (l) {
        if (l.tween && l.isVisible) l.tween.play();
      });
    },

    togglePause: function () {
      var self = this;
      if (self.isPausedByUser || self.mode === 'paused') {
        self.isPausedByUser = false;
        self.setMode(self.detectReducedMotion() ? 'reduced' : 'full');
        self.updatePauseButtonUI(false);
      } else {
        self.isPausedByUser = true;
        self.setMode('paused');
        self.updatePauseButtonUI(true);
      }
    },

    setupPauseButton: function () {
      var self = this;
      var btn = document.getElementById('motion-pause-toggle');
      if (!btn) return;

      btn.addEventListener('click', function () {
        self.togglePause();
      });
    },

    updatePauseButtonUI: function (isPaused) {
      var btn = document.getElementById('motion-pause-toggle');
      if (!btn) return;

      btn.setAttribute('aria-pressed', isPaused ? 'true' : 'false');
      btn.setAttribute(
        'aria-label',
        isPaused ? 'Retomar animações' : 'Pausar animações'
      );
      btn.classList.toggle('is-paused', isPaused);
      var textSpan = btn.querySelector('.motion-toggle-label');
      if (textSpan) {
        textSpan.textContent = isPaused ? 'RETOMAR' : 'PAUSAR';
      }
    },

    registerLoop: function (element, tween) {
      var self = this;
      if (!element || !tween) return;

      var loopObj = {
        element: element,
        tween: tween,
        isVisible: true
      };
      self.activeLoops.push(loopObj);

      // Se qualidade for low, pausamos loops contínuos não essenciais
      if (self.quality === 'low' || self.mode === 'reduced') {
        tween.pause(0);
        loopObj.isVisible = false;
      }
    },

    setupLoopVisibilityObserver: function () {
      var self = this;
      if (!window.IntersectionObserver) return;

      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            for (var i = 0; i < self.activeLoops.length; i++) {
              var l = self.activeLoops[i];
              if (l.element === entry.target) {
                l.isVisible = entry.isIntersecting;
                if (!self.isPausedByUser && self.mode === 'full' && self.quality === 'high') {
                  if (entry.isIntersecting) {
                    l.tween.play();
                  } else {
                    l.tween.pause();
                  }
                }
                break;
              }
            }
          });
        },
        { threshold: 0.05 }
      );

      self.loopObserver = observer;
    },

    registerSection: function (sectionId, initCallback) {
      this.sectionModules[sectionId] = initCallback;
    }
  };

  window.MrMacarioMotion = MrMacarioMotion;
})(window, document);
