// minify.cjs — minificação usada pelo scripts/build.py
//   node scripts/minify.cjs css <entrada> <saida>
//   node scripts/minify.cjs js  <entrada> <saida>
//
// CSS: clean-css nível 1 apenas. O nível 2 funde/sobrescreve propriedades e removeria
// fallbacks intencionais (ex.: min-height:100vh antes de 100svh, background-image PNG antes de
// image-set(), prefixos -webkit-). O nível 1 só remove espaços/comentários e encurta valores.
// JS: terser (compress + mangle de escopo local; globais como window.MrMacarioMotion intactos).
const fs = require('fs');
const [, , kind, input, output] = process.argv;
const src = fs.readFileSync(input, 'utf8');

if (kind === 'css') {
  const CleanCSS = require('clean-css');
  const out = new CleanCSS({ level: 1, compatibility: '*', rebase: false }).minify(src);
  if (out.errors.length) { console.error(out.errors.join('\n')); process.exit(1); }
  if (out.warnings.length) console.warn(out.warnings.join('\n'));
  fs.writeFileSync(output, out.styles);
} else if (kind === 'js') {
  require('terser')
    .minify(src, { ecma: 5, compress: { passes: 2 }, mangle: true, format: { comments: false } })
    .then((r) => fs.writeFileSync(output, r.code))
    .catch((e) => { console.error(e); process.exit(1); });
} else {
  console.error('uso: minify.cjs css|js <entrada> <saida>');
  process.exit(1);
}
