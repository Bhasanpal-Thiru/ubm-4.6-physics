# UBM 4.6: Theory and Numerical Verification

This repository contains the numerical proofs and simulation scripts for the 
**Unified Buffer Model 4.6** as submitted to Physical Review D (Letters).

## Code-to-Figure Mapping
- **Figure 1 (SO(10) Unification):** See `notebooks/01_RGE_Unification.ipynb`. 
  Uses $\xi = -1.21 \times 10^{-12}$ to match PDG 2024 $\alpha_s(M_Z)$.
- **Figure 2 (Kinetic Stability):** See `notebooks/02_DHOST_Stability.ipynb`. 
  Symbolic proof that $Q(X) > 0$ across all scales $X \in [0, M_P^4]$.
- **Figure 3 (CP Phase):** See `notebooks/03_Flavor_Topology.ipynb`. 
  Derivation of $\delta_{CP} \approx 1.32\pi$ from topological boundaries.
- **JUICE Forecast (Sec. V):** See `scripts/juice_forecast.py`. 
  Monte Carlo prediction of $+1.84 \times 10^{-8}$ Hz Doppler shift for Sept 29, 2026.

## Requirements
- Python 3.11+
- SymPy (Symbolic Math)
- NumPy / Matplotlib (Plotting)

## Citation
Please cite the corresponding PRD Letter (arXiv:2603.XXXXX) when using this code.
[![DOI](https://zenodo.org/badge/1171734140.svg)](https://doi.org/10.5281/zenodo.18850770)
