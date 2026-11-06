/* DriFox Docs — 动效脚本：进度条 / 滚动淡入 / 光斑视差 */
(function () {
  'use strict';

  document.body.classList.add('fx-ready');

  /* 阅读进度条 */
  var bar = document.createElement('div');
  bar.id = 'fx-progress';
  document.body.appendChild(bar);
  var ticking = false;
  function updateBar() {
    var doc = document.documentElement;
    var max = doc.scrollHeight - doc.clientHeight;
    bar.style.width = (max > 0 ? (doc.scrollTop / max) * 100 : 0) + '%';
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(updateBar); }
  }, { passive: true });
  updateBar();

  /* 滚动淡入：正文二级内容 + 卡片 */
  var targets = Array.prototype.slice.call(
    document.querySelectorAll('.document h2, .document .admonition, .document table.docutils, .fx-card')
  );
  targets.forEach(function (el) { el.classList.add('fx-reveal'); });

  function revealAll() { targets.forEach(function (el) { el.classList.add('fx-in'); }); }

  var revealed = 0;
  var ioOK = false;
  if ('IntersectionObserver' in window) {
    try {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add('fx-in');
            revealed++;
            io.unobserve(e.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      targets.forEach(function (el) { io.observe(el); });
      ioOK = true;
    } catch (err) { ioOK = false; }
  }

  /* IO 兜底：800ms 内一个都没触发说明环境不支持，全部显示 */
  if (ioOK) {
    setTimeout(function () {
      if (revealed === 0 && targets.length > 0) revealAll();
    }, 800);
  } else {
    revealAll();
  }

  /* Hero 光斑轻视差 */
  var hero = document.querySelector('.drifox-hero');
  if (hero && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    hero.addEventListener('mousemove', function (ev) {
      var r = hero.getBoundingClientRect();
      var dx = (ev.clientX - r.left) / r.width - 0.5;
      var dy = (ev.clientY - r.top) / r.height - 0.5;
      hero.querySelectorAll('.fx-orb').forEach(function (orb, i) {
        var k = (i + 1) * 10;
        orb.style.transform = 'translate(' + dx * k + 'px,' + dy * k + 'px)';
      });
    });
    hero.addEventListener('mouseleave', function () {
      hero.querySelectorAll('.fx-orb').forEach(function (orb) { orb.style.transform = ''; });
    });
  }
})();
