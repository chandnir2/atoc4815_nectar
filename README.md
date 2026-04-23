# Nectar

A lightweight python package that analyzes weather station temperature data from Colorado Climate Center (https://climate.colostate.edu/data_access_new.html) and data from Project Feederwatch (https://feederwatch.org/) to compare estimated flowering day of year and estimated hummingbird arrival day of year for four species of migratory hummingbirds in Colorado.  

> **Data source:**   
> Colorado Climate Center Station Data provided by Colorado State Univeristy
> Project Feederwatch Data provided by Cornell Lab of Ornithology

# Usage

Nectar is intended to be used for scientists and wildlife officials to determine temporal mismatch between hummingbird arrivalals and flowering bloom time. This package outputs a dataframe with an average estimated hummingbird arrival day of year (DOY), an estimated flowering DOY for all of the existing data years provided, the number of days of temporal mismatch, and the mean temporal mismatch over all of the years analyzed. Additionally, the plotting functionality provides a visual representation of how migration and estimated bloom evolve over time. This analysis can be used to help better understand trends over time. 

## Installation

```bash
pip install -e .
```

Or from source:

```bash
git clone [(https://github.com/chandnir2/atoc4815_nectar.git)]
cd nectar
pip install -e .
```

## Quick Start -- Need to figure this out...

```python
from lorenz_project import Lorenz63

model = Lorenz63(sigma=10, rho=28, beta=8/3)
trajectory = model.run([1, 1, 1], dt=0.01, n_steps=5000)
```

## Command Line

```bash
run-nectar    # generates data/flowering_vs_arrival.png and data/mismatch.png
```

## Files

- `lorenz63.py` — Lorenz63 model class
- `integrators.py` — Forward Euler integrator
- `plotting.py` — Ensemble visualization
- `run_lorenz_ensemble.py` — Driver script

## License

MIT
