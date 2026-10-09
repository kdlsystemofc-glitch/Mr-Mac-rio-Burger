/**
 * motion-sections.js — Animações por Seção do Mr. Macário Burger
 * Regras Globais:
 * - Apenas transform e opacity nas camadas-folha.
 * - Elementos decorativos contínuos (bordas rasgadas, divisórias SVG, paper-noise) NUNCA se movem.
 * - 3 modos: 'full', 'reduced', 'paused'.
 * - 2 qualidades: 'high', 'low' (reduz loops e parallax em low).
 * - Nada acima da dobra depende de JS para aparecer.
 */

(function (window, document) {
  'use strict';

  var MrMacarioSections = {
    initHero: function () {
      var M = window.MrMacarioMotion;
      if (!M || !window.gsap) return;

      var heroSec = document.getElementById('hero');
      if (!heroSec) return;

      // Se for modo reduzido, garante estado estático limpo
      if (M.mode === 'reduced') {
        return;
      }

      var isHighQuality = M.quality === 'high';
      var isDesktop = window.innerWidth >= 1024;

      // 1. Elementos Selecionados (camadas-folha)
      var burgerImg = heroSec.querySelector('.hero-burger-img');
      var burgerShadow = heroSec.querySelector('.hero-burger-shadow');
      var stampMint = heroSec.querySelector('.stamp-mint');
      var bgText = heroSec.querySelector('.hero-bg-text');
      var brandTop = heroSec.querySelector('.hero-top-brand');

      var flyingFries = heroSec.querySelector('.fries-fly-wrapper img');
      var dice = heroSec.querySelector('.dice-wrapper img');
      var neon = heroSec.querySelector('.neon-doodle-wrapper img');
      var cheeseDrip = heroSec.querySelector('.cheese-drip-top-left');

      var stamps = heroSec.querySelectorAll('.stamp-blue, .stamp-coral, .badge-fresh-meat');
      var pills = heroSec.querySelectorAll('.pill-saude, .pill-hours');
      var receipts = heroSec.querySelectorAll('.receipt');

      // 2. Timeline de Entrada Cinematográfica (Awwwards Hero Intro)
      var tl = window.gsap.timeline({
        defaults: { ease: 'power3.out' }
      });

      // Letreiro de fundo e marca topo (expansão sutil de palco)
      if (bgText) {
        tl.fromTo(
          bgText,
          { opacity: 0.4, scale: 0.97 },
          { opacity: 1, scale: 1, duration: 0.85, ease: 'power2.out' },
          0
        );
      }
      if (brandTop) {
        tl.fromTo(
          brandTop,
          { opacity: 0.6, y: -10 },
          { opacity: 1, y: 0, duration: 0.7 },
          0.1
        );
      }

      // Pouso heróico do Burger e assentamento de sombra
      if (burgerImg && burgerShadow) {
        if (isDesktop && isHighQuality) {
          tl.fromTo(
            burgerImg,
            { y: -28, scale: 1.04 },
            { y: 0, scale: 1, duration: 0.85, ease: 'elastic.out(1, 0.75)' },
            0.1
          );
          tl.fromTo(
            burgerShadow,
            { opacity: 0.2, scale: 0.85 },
            { opacity: 0.75, scale: 1, duration: 0.85, ease: 'power2.out' },
            0.1
          );
        } else {
          // Em mobile/low quality, preserva a pintura instantânea do elemento LCP sem adiar para o final da animação
          tl.fromTo(
            burgerShadow,
            { opacity: 0.4 },
            { opacity: 0.75, duration: 0.5, ease: 'power2.out' },
            0.1
          );
        }
      }

      // Selo do Pão (adesivado com impacto leve)
      if (stampMint) {
        tl.fromTo(
          stampMint,
          { scale: 1.3, opacity: 0.7 },
          { scale: 1, opacity: 1, duration: 0.6, ease: 'back.out(2)' },
          0.4
        );
      }

      // Satélites dinâmicos (Batatas voadoras, dados, neon, gota de queijo)
      if (flyingFries) {
        tl.fromTo(
          flyingFries,
          { y: 24, rotation: -6, opacity: 0.5 },
          { y: 0, rotation: 0, opacity: 1, duration: 0.8, ease: 'back.out(1.5)' },
          0.25
        );
      }
      if (dice) {
        tl.fromTo(
          dice,
          { y: -18, rotation: 8, opacity: 0.5 },
          { y: 0, rotation: 0, opacity: 1, duration: 0.75, ease: 'back.out(1.4)' },
          0.3
        );
      }
      if (neon) {
        tl.fromTo(
          neon,
          { opacity: 0.3, scale: 0.9 },
          { opacity: 1, scale: 1, duration: 0.6, ease: 'power2.out' },
          0.35
        );
      }
      if (cheeseDrip) {
        tl.fromTo(
          cheeseDrip,
          { y: -15, opacity: 0.6 },
          { y: 0, opacity: 1, duration: 0.7, ease: 'power2.out' },
          0.2
        );
      }

      // Selos, pílulas e comandas com carimbo sequencial
      if (stamps.length) {
        tl.fromTo(
          stamps,
          { scale: 1.2, opacity: 0.6 },
          { scale: 1, opacity: 1, duration: 0.55, stagger: 0.08, ease: 'back.out(1.8)' },
          0.35
        );
      }
      if (pills.length) {
        tl.fromTo(
          pills,
          { y: 12, opacity: 0.6 },
          { y: 0, opacity: 1, duration: 0.6, stagger: 0.06, ease: 'power2.out' },
          0.4
        );
      }
      if (receipts.length) {
        tl.fromTo(
          receipts,
          { y: 15, opacity: 0.6 },
          { y: 0, opacity: 1, duration: 0.65, stagger: 0.08, ease: 'power3.out' },
          0.45
        );
      }

      // 3. Loops Contínuos Sutis (apenas em High Quality e na Viewport)
      if (isHighQuality) {
        if (flyingFries) {
          var friesLoop = window.gsap.to(flyingFries, {
            y: -5,
            rotation: 1.5,
            duration: 3.6,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1
          });
          M.registerLoop(flyingFries, friesLoop);
        }

        if (dice) {
          var diceLoop = window.gsap.to(dice, {
            y: -4,
            rotation: -2,
            duration: 4.2,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1
          });
          M.registerLoop(dice, diceLoop);
        }

        if (neon) {
          var neonLoop = window.gsap.to(neon, {
            opacity: 0.82,
            duration: 2.6,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1
          });
          M.registerLoop(neon, neonLoop);
        }
      }

      // 4. Parallax de Cursor Interativo (Mouse Follow Awwwards — apenas Desktop High Quality)
      if (isDesktop && isHighQuality) {
        var quickBurgerX = window.gsap.quickTo(burgerImg, 'x', { duration: 0.6, ease: 'power2.out' });
        var quickBurgerY = window.gsap.quickTo(burgerImg, 'y', { duration: 0.6, ease: 'power2.out' });
        var quickFriesX = flyingFries ? window.gsap.quickTo(flyingFries, 'x', { duration: 0.5, ease: 'power2.out' }) : null;
        var quickFriesY = flyingFries ? window.gsap.quickTo(flyingFries, 'y', { duration: 0.5, ease: 'power2.out' }) : null;
        var quickDiceX = dice ? window.gsap.quickTo(dice, 'x', { duration: 0.5, ease: 'power2.out' }) : null;
        var quickDiceY = dice ? window.gsap.quickTo(dice, 'y', { duration: 0.5, ease: 'power2.out' }) : null;

        var onMouseMove = function (e) {
          if (M.mode === 'paused' || M.isPausedByUser) return;
          var rect = heroSec.getBoundingClientRect();
          if (rect.bottom < 0 || rect.top > window.innerHeight) return;

          var relX = (e.clientX - rect.left) / rect.width - 0.5;
          var relY = (e.clientY - rect.top) / rect.height - 0.5;

          quickBurgerX(relX * 12);
          quickBurgerY(relY * 8);

          if (quickFriesX && quickFriesY) {
            quickFriesX(relX * 22);
            quickFriesY(relY * 16);
          }
          if (quickDiceX && quickDiceY) {
            quickDiceX(relX * -18);
            quickDiceY(relY * -14);
          }
        };

        var onMouseLeave = function () {
          quickBurgerX(0);
          quickBurgerY(0);
          if (quickFriesX && quickFriesY) {
            quickFriesX(0);
            quickFriesY(0);
          }
          if (quickDiceX && quickDiceY) {
            quickDiceX(0);
            quickDiceY(0);
          }
        };

        heroSec.addEventListener('mousemove', onMouseMove, { passive: true });
        heroSec.addEventListener('mouseleave', onMouseLeave, { passive: true });
      }

      // 5. ScrollTrigger Parallax Suave para Saída do Hero
      if (window.ScrollTrigger) {
        window.ScrollTrigger.create({
          trigger: heroSec,
          start: 'top top',
          end: 'bottom top',
          scrub: 0.6,
          onUpdate: function (self) {
            if (M.mode === 'paused') return;
            var progress = self.progress;
            if (burgerImg) {
              window.gsap.set(burgerImg, { yPercent: -12 * progress });
            }
            if (bgText) {
              window.gsap.set(bgText, { yPercent: 6 * progress });
            }
          }
        });
      }
    },

    initMenu: function () {
      var M = window.MrMacarioMotion;
      if (!M || !window.gsap || !window.ScrollTrigger) return;

      var menuSec = document.getElementById('menu-highlights');
      if (!menuSec) return;

      if (M.mode === 'reduced') return;

      var isHighQuality = M.quality === 'high';

      // 1. Elementos Selecionados (camadas-folha)
      var menuTitle = menuSec.querySelector('.menu-title');
      var items = menuSec.querySelectorAll('.menu-display-item');
      var burguinhoTag = menuSec.querySelector('.pill-burguinho-tag');
      var precoJustoStamp = menuSec.querySelector('.stamp-preco-justo');
      var menuDice = menuSec.querySelector('.menu-dice-float img');
      var menuNeon = menuSec.querySelector('.menu-neon-float img');

      // 2. Timeline de Entrada Disparada a ~35% de Visibilidade
      var tl = window.gsap.timeline({
        scrollTrigger: {
          trigger: menuSec,
          start: 'top 65%', // Disparo quando ~35% da seção está no viewport
          once: true
        },
        defaults: { ease: 'power3.out' }
      });

      // Título da Seção
      if (menuTitle) {
        tl.fromTo(
          menuTitle,
          { y: 24, opacity: 0 },
          { y: 0, opacity: 1, duration: 0.65 },
          0
        );
      }

      // Os 3 Pratos com Leve Pouso Defasado (Stagger)
      if (items.length) {
        var visuals = [];
        var shadows = [];
        items.forEach(function (it) {
          var vis = it.querySelector('.menu-food-visual');
          var shd = it.querySelector('.menu-ground-shadow');
          if (vis) visuals.push(vis);
          if (shd) shadows.push(shd);
        });

        tl.fromTo(
          visuals,
          { y: 35, opacity: 0 },
          { y: 0, opacity: 1, duration: 0.75, stagger: 0.15 },
          0.15
        );

        if (shadows.length) {
          tl.fromTo(
            shadows,
            { scale: 0.8, opacity: 0.1 },
            { scale: 1, opacity: 0.7, duration: 0.75, stagger: 0.15 },
            0.15
          );
        }
      }

      // Selos e Tags nos Lanches (Carimbo Elástico)
      if (burguinhoTag) {
        tl.fromTo(
          burguinhoTag,
          { scale: 1.25, opacity: 0 },
          { scale: 1, opacity: 1, duration: 0.55, ease: 'back.out(1.8)' },
          0.45
        );
      }
      if (precoJustoStamp) {
        tl.fromTo(
          precoJustoStamp,
          { scale: 1.2, rotation: -12, opacity: 0 },
          { scale: 1, rotation: -5, opacity: 1, duration: 0.6, ease: 'back.out(1.6)' },
          0.55
        );
      }

      // Elementos Satélites do Smash (Dados e Neon)
      if (menuDice) {
        tl.fromTo(
          menuDice,
          { y: -16, opacity: 0 },
          { y: 0, opacity: 1, duration: 0.65, ease: 'back.out(1.4)' },
          0.35
        );
      }
      if (menuNeon) {
        tl.fromTo(
          menuNeon,
          { opacity: 0, scale: 0.9 },
          { opacity: 1, scale: 1, duration: 0.6 },
          0.4
        );
      }

      // 3. Flutuação Contínua Sutil (apenas em High Quality e na Viewport)
      if (isHighQuality) {
        if (menuDice) {
          var diceLoop = window.gsap.to(menuDice, {
            y: -4,
            rotation: 2,
            duration: 3.4,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1
          });
          M.registerLoop(menuDice, diceLoop);
        }

        if (menuNeon) {
          var neonLoop = window.gsap.to(menuNeon, {
            opacity: 0.8,
            duration: 2.5,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1
          });
          M.registerLoop(menuNeon, neonLoop);
        }

        // 4. Parallax Leve nos Pratos (0.06, máx ~18px, sem cobrir texto)
        var burguinhoVisual = menuSec.querySelector('.item-burguinho .menu-food-visual');
        if (burguinhoVisual) {
          window.ScrollTrigger.create({
            trigger: menuSec,
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.8,
            onUpdate: function (self) {
              if (M.mode === 'paused') return;
              var offset = (self.progress - 0.5) * -20;
              window.gsap.set(burguinhoVisual, { y: offset });
            }
          });
        }
      }
    },

    initGriddle: function () {
      var M = window.MrMacarioMotion;
      if (!M || !window.gsap || !window.ScrollTrigger) return;

      var griddleSec = document.getElementById('griddle-craft');
      if (!griddleSec) return;

      if (M.mode === 'reduced') return;

      var isHighQuality = M.quality === 'high';

      // 1. Elementos Selecionados (camadas-folha internas apenas)
      var griddleTitle = griddleSec.querySelector('.griddle-title');
      var maillardStamp = griddleSec.querySelector('.stamp-maillard');
      var chalkArrow = griddleSec.querySelector('.chalk-arrow');
      var griddleImg = griddleSec.querySelector('.griddle-bg-img');

      // 2. Timeline de Entrada Disparada a ~35% de Visibilidade
      var tl = window.gsap.timeline({
        scrollTrigger: {
          trigger: griddleSec,
          start: 'top 65%',
          once: true
        },
        defaults: { ease: 'power3.out' }
      });

      if (griddleTitle) {
        tl.fromTo(
          griddleTitle,
          { y: 28, opacity: 0 },
          { y: 0, opacity: 1, duration: 0.75 },
          0
        );
      }

      if (maillardStamp) {
        tl.fromTo(
          maillardStamp,
          { scale: 1.25, opacity: 0 },
          { scale: 1, opacity: 1, duration: 0.65, ease: 'back.out(1.8)' },
          0.2
        );
      }

      if (chalkArrow) {
        tl.fromTo(
          chalkArrow,
          { opacity: 0, x: 12, y: -10 },
          { opacity: 1, x: 0, y: 0, duration: 0.65, ease: 'power2.out' },
          0.4
        );
      }

      // 3. Efeitos em High Quality (Parallax sutil na imagem da chapa e pulso no selo)
      if (isHighQuality) {
        if (maillardStamp) {
          var stampPulse = window.gsap.to(maillardStamp, {
            scale: 1.04,
            duration: 3.0,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1
          });
          M.registerLoop(maillardStamp, stampPulse);
        }

        // Parallax leve na chapa (0.05, max 16px, contido sob a moldura de papel)
        if (griddleImg) {
          window.ScrollTrigger.create({
            trigger: griddleSec,
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.6,
            onUpdate: function (self) {
              if (M.mode === 'paused') return;
              var offset = (self.progress - 0.5) * -18;
              window.gsap.set(griddleImg, { y: offset });
            }
          });
        }
      }
    }
  };

  window.MrMacarioSections = MrMacarioSections;
})(window, document);
