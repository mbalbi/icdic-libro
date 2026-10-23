"""Genera valores de referencia de scipy para el test de paridad con JS (todas las distribuciones del catalogo)."""
import json, sys
import numpy as np
from scipy import stats

def scipy_dist(name, p1, p2):
    if name == "Normal":      return stats.norm(loc=p1, scale=p2)
    if name == "LogNormal":   return stats.lognorm(s=p2, scale=np.exp(p1))
    if name == "Exponential": return stats.expon(scale=1 / p1)
    if name == "Beta":        return stats.beta(p1, p2)
    if name == "Gumbel":      return stats.gumbel_r(loc=p1, scale=p2)

def grid(name, p1, p2):
    d = scipy_dist(name, p1, p2)
    lo, hi = d.ppf(1e-9), d.ppf(1 - 1e-9)          # cubre casi todo el soporte, incluidas las colas
    if name == "Beta": lo, hi = 0.0, 1.0
    if name in ("Exponential", "LogNormal"): lo = max(lo, 0.0)
    return np.concatenate([np.linspace(lo, hi, 400), [d.ppf(q) for q in (0.001, 0.01, 0.5, 0.99, 0.999)]])

PARAMS = {
    "Normal":      [(0, 1), (1, 2), (-3, 0.5)],
    "LogNormal":   [(0, 0.5), (-1, 1), (1, 0.2)],
    "Exponential": [(1, None), (0.5, None), (0.2, None), (5, None)],
    "Beta":        [(2, 5), (5, 2), (1, 1), (0.5, 0.5), (0.5, 3), (10, 10), (30, 2)],
    "Gumbel":      [(0, 1), (2, 1), (0, 2)],
}

cases = []
for name, plist in PARAMS.items():
    for p1, p2 in plist:
        d = scipy_dist(name, p1, p2)
        for x in grid(name, p1, p2):
            pdf, cdf = float(d.pdf(x)), float(d.cdf(x))
            if not np.isfinite(pdf):          # p. ej. Beta(0.5, 0.5) en los extremos
                continue
            cases.append({"dist": name, "p1": p1, "p2": p2, "x": float(x), "pdf": pdf, "cdf": cdf})
json.dump({"cases": cases}, open(sys.argv[1], "w"))
print(len(cases), "casos escritos")
