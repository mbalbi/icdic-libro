// Distribuciones de probabilidad en JS puro. Verificadas contra scipy.stats por figuras/test_paridad.mjs
const SQRT_2PI = Math.sqrt(2 * Math.PI);

// ---------- Normal ----------
export const phi = (x, mu = 0, sigma = 1) => {
  const z = (x - mu) / sigma;
  return Math.exp(-0.5 * z * z) / (sigma * SQRT_2PI);
};

// Phi(z) = 1/2 + phi(z) * sum_{n>=0} z^(2n+1) / (1*3*5*...*(2n+1)); exacta para |z| <= 8,
// y expansion asintotica de la cola mas alla (error < 1e-15).
export const Phi = (x, mu = 0, sigma = 1) => {
  const z = (x - mu) / sigma;
  if (Math.abs(z) > 8) {
    const z2 = z * z;
    const tail = (Math.exp(-0.5 * z2) / (Math.abs(z) * SQRT_2PI)) * (1 - 1 / z2 + 3 / (z2 * z2) - 15 / (z2 * z2 * z2));
    return z > 0 ? 1 - tail : tail;
  }
  let term = z, sum = z;
  for (let n = 1; n < 500; n++) {
    term *= (z * z) / (2 * n + 1);
    sum += term;
    if (Math.abs(term) < 1e-17 * Math.abs(sum)) break;
  }
  return 0.5 + Math.exp(-0.5 * z * z) / SQRT_2PI * sum;
};

// ---------- Funciones especiales (para Beta) ----------
const LANCZOS = [0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313,
  -176.61502916214059, 12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];

export function lgamma(z) {
  if (z < 0.5) return Math.log(Math.PI / Math.abs(Math.sin(Math.PI * z))) - lgamma(1 - z);
  z -= 1;
  let a = LANCZOS[0];
  const t = z + 7.5;
  for (let i = 1; i < 9; i++) a += LANCZOS[i] / (z + i);
  return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(a);
}

// Fraccion continua de Lentz para la beta incompleta regularizada
function betacf(x, a, b) {
  const FPMIN = 1e-300, EPS = 1e-16;
  const qab = a + b, qap = a + 1, qam = a - 1;
  let c = 1, d = 1 - qab * x / qap;
  if (Math.abs(d) < FPMIN) d = FPMIN;
  d = 1 / d;
  let h = d;
  for (let m = 1; m <= 1000; m++) {
    const m2 = 2 * m;
    let aa = m * (b - m) * x / ((qam + m2) * (a + m2));
    d = 1 + aa * d; if (Math.abs(d) < FPMIN) d = FPMIN;
    c = 1 + aa / c; if (Math.abs(c) < FPMIN) c = FPMIN;
    d = 1 / d; h *= d * c;
    aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2));
    d = 1 + aa * d; if (Math.abs(d) < FPMIN) d = FPMIN;
    c = 1 + aa / c; if (Math.abs(c) < FPMIN) c = FPMIN;
    d = 1 / d;
    const del = d * c;
    h *= del;
    if (Math.abs(del - 1) < EPS) break;
  }
  return h;
}

export function betainc(x, a, b) {
  if (x <= 0) return 0;
  if (x >= 1) return 1;
  const bt = Math.exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * Math.log(x) + b * Math.log(1 - x));
  return x < (a + 1) / (a + b + 2) ? bt * betacf(x, a, b) / a : 1 - bt * betacf(1 - x, b, a) / b;
}

// ---------- Catalogo (parametrizacion del libro) ----------
export const distributions = {
  Normal: {
    params: [{ label: "Mu", value: 0 }, { label: "Sigma", value: 1 }],
    valid: (m, s) => s > 0,
    pdf: (x, m, s) => phi(x, m, s),
    cdf: (x, m, s) => Phi(x, m, s),
    range: (m, s) => [m - 4 * s, m + 4 * s],
  },
  LogNormal: {  // lambda = media de ln X, xi = desvio de ln X
    params: [{ label: "LogMu", value: 0 }, { label: "LogSigma", value: 0.5 }],
    valid: (l, xi) => xi > 0,
    pdf: (x, l, xi) => x <= 0 ? 0 : Math.exp(-0.5 * ((Math.log(x) - l) / xi) ** 2) / (x * xi * SQRT_2PI),
    cdf: (x, l, xi) => x <= 0 ? 0 : Phi(Math.log(x), l, xi),
    range: (l, xi) => [Math.max(0.01, Math.exp(l - 4 * xi)), Math.exp(l + 4 * xi)],
  },
  Exponential: {
    params: [{ label: "Rate (λ)", value: 1 }],
    valid: (r) => r > 0,
    pdf: (x, r) => x < 0 ? 0 : r * Math.exp(-r * x),
    cdf: (x, r) => x < 0 ? 0 : 1 - Math.exp(-r * x),
    range: (r) => [0, 5 / r],
  },
  Beta: {
    params: [{ label: "Alpha", value: 2 }, { label: "Beta", value: 5 }],
    valid: (a, b) => a > 0 && b > 0,
    pdf: (x, a, b) => {
      if (x < 0 || x > 1) return 0;
      if (x === 0) return a > 1 ? 0 : a === 1 ? b : Infinity;
      if (x === 1) return b > 1 ? 0 : b === 1 ? a : Infinity;
      return Math.exp((a - 1) * Math.log(x) + (b - 1) * Math.log(1 - x) - (lgamma(a) + lgamma(b) - lgamma(a + b)));
    },
    cdf: (x, a, b) => betainc(x, a, b),
    range: () => [0, 1],
  },
  Gumbel: {
    params: [{ label: "Location", value: 0 }, { label: "Scale", value: 1 }],
    valid: (m, s) => s > 0,
    pdf: (x, m, s) => { const z = (x - m) / s; return Math.exp(-(z + Math.exp(-z))) / s; },
    cdf: (x, m, s) => Math.exp(-Math.exp(-(x - m) / s)),
    range: (m, s) => [m - 4 * s, m + 6 * s],
  },
};
