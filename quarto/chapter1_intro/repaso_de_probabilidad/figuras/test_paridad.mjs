// Paridad JS vs scipy. Uso: node figuras/test_paridad.mjs <referencia.json>
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const { distributions } = await import(pathToFileURL(resolve('figuras/distribuciones.js')).href);
const ref = JSON.parse(readFileSync(process.argv[2], 'utf8'));

const TOL_PDF = 1e-10, TOL_CDF = 1e-11;   // pdf: tolerancia relativa a max(1,|ref|); cdf: absoluta
const byDist = {};
for (const c of ref.cases) {
  const D = distributions[c.dist];
  const args = D.params.length === 1 ? [c.p1] : [c.p1, c.p2];
  const ep = Math.abs(D.pdf(c.x, ...args) - c.pdf) / Math.max(1, Math.abs(c.pdf));
  const ec = Math.abs(D.cdf(c.x, ...args) - c.cdf);
  const r = (byDist[c.dist] ??= { n: 0, maxErrPdf: 0, maxErrCdf: 0, worst: null });
  r.n++;
  if (ep > r.maxErrPdf) r.maxErrPdf = ep;
  if (ec > r.maxErrCdf) { r.maxErrCdf = ec; r.worst = c; }
}
let pass = true;
for (const [name, r] of Object.entries(byDist)) {
  r.pass = r.maxErrPdf < TOL_PDF && r.maxErrCdf < TOL_CDF;
  pass &&= r.pass;
  console.log(name.padEnd(12), `n=${String(r.n).padStart(5)}`, `maxErrPdf=${r.maxErrPdf.toExponential(2)}`, `maxErrCdf=${r.maxErrCdf.toExponential(2)}`, r.pass ? 'PASS' : 'FAIL', r.pass ? '' : JSON.stringify(r.worst));
}
console.log(pass ? 'ALL PASS' : 'FAILURES');
process.exit(pass ? 0 : 1);
