# Hydro-geo-logy

Groundwater flow and solute transport examples in Python. This repository collects two research notebooks and a small, reproducible transient-flow example. It is intended as an educational starting point; site-specific inputs and model assumptions need to be checked before applying the examples to another aquifer or experiment.

| Example | What it covers | Current status |
| --- | --- | --- |
| [Transient groundwater flow](Transient%20Groundwater%20Flow%20Example.ipynb) | Pumping-test interpretation, Theis drawdown, superposition, image wells and river influx | Analysis notebook; its original pumping-test spreadsheet is not included. Saved plots and embedded diagrams are retained as illustrations of the original analysis. |
| [Sand tank Monte Carlo](SandTank_Flopy_MonteCarlo.ipynb) | FloPy setup for MODFLOW-2005 and MT3DMS, parameter sampling and breakthrough-curve comparison | Annotated research template; observation data, parameter bounds, executable paths and several model inputs must be supplied. It cannot be run end to end as provided. |
| [Three-well demo](examples/transient_flow_demo.py) | A self-contained Theis calculation for three pumping wells | Runnable without external data or groundwater solver executables. |

## Quick start

Python 3.10 or newer is recommended. From the repository root:

```bash
python -m venv .venv
# On Windows: .venv\Scripts\activate
# On macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python examples/transient_flow_demo.py
```

The demo writes `outputs/transient_flow_demo.png`. It uses illustrative aquifer properties (`T = 1323 m²/day`, `S = 0.2`) and three wells pumping `2400 m³/day` each. It plots unconstrained Theis drawdown at a specified observation point; the valley boundaries in the notebook are **not** included in this demo.

To browse the notebooks, run `jupyter lab` after installing `requirements-notebooks.txt` alongside the base requirements:

```bash
python -m pip install -r requirements-notebooks.txt
jupyter lab
```

### Running the transient-flow notebook

The notebook expects a local Excel workbook with a `days` column and drawdown columns for the observation wells. The workbook used in the original analysis was not committed. Change `file` in the first data-loading cell to your workbook path and verify the pumping rate, observation-well distances, aquifer geometry and units against your data. The original code uses two different lists of observation-well distances, so confirm which one applies before rerunning. The saved plots and embedded diagrams illustrate the original analysis; they are not fresh results from data supplied here.

### Adapting the sand-tank template

Install the optional FloPy dependency with `python -m pip install -r requirements-modflow.txt`, and obtain compatible **MODFLOW-2005** and **MT3DMS** executables separately. FloPy does not bundle those executables. Work through the annotated placeholders in the notebook: provide experimental breakthrough curves and times, set parameter bounds and random seed, configure well locations and stress periods, then assign the solver paths and an isolated model workspace. Check mass balance and solver success for every realization before scoring the results. Some longer model fragments are displayed as code listings because they contain incomplete placeholders and require adaptation; they are not executable cells.

## Scope and reproducibility

- Coordinates, pumping rates and aquifer properties in the notebooks come from their original teaching/research examples and are not universal defaults.
- The repository does not contain the transient pumping-test workbook, the sand-tank observations or the external solver binaries. As a result, the original notebook results cannot be regenerated from this checkout alone.
- Outputs created by the demo are ignored by Git. The notebook illustrations remain embedded in the notebooks so the examples can be read without external image files.
- No license is currently specified. Contact the repository owner before reusing or redistributing the material beyond what applicable law permits.

## Contact

Open a GitHub issue for corrections or questions about the examples.
