"""Plot illustrative three-well Theis drawdown without external data."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # Save the figure on machines without a display.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import exp1


def theis_drawdown(
    distance_m: float, time_days: np.ndarray, pumping_m3_day: float,
    transmissivity_m2_day: float, storativity: float,
) -> np.ndarray:
    """Return confined-aquifer Theis drawdown in metres for positive inputs."""
    times = np.asarray(time_days, dtype=float)
    if (distance_m <= 0 or np.any(times <= 0) or pumping_m3_day < 0
            or transmissivity_m2_day <= 0 or not 0 < storativity <= 1):
        raise ValueError("Use r > 0, t > 0, Q >= 0, T > 0 and 0 < S <= 1")
    u = distance_m**2 * storativity / (4 * transmissivity_m2_day * times)
    return pumping_m3_day * exp1(u) / (4 * np.pi * transmissivity_m2_day)


def main() -> None:
    wells = [(0.0, -500.0), (0.0, 0.0), (0.0, 500.0)]  # x, y in m
    observation = (250.0, 260.0)
    time_days = np.geomspace(1, 5 * 365, 250)
    contributions = []

    fig, ax = plt.subplots(figsize=(8, 5))
    for number, (x, y) in enumerate(wells, start=1):
        distance = np.hypot(observation[0] - x, observation[1] - y)
        drawdown = theis_drawdown(distance, time_days, 2400, 1323, 0.2)
        contributions.append(drawdown)
        ax.plot(time_days, drawdown, label=f"Well {number}")

    ax.plot(time_days, np.sum(contributions, axis=0), color="black",
            linewidth=2.5, label="Combined drawdown")
    ax.set(xlabel="Time since pumping began (days)", ylabel="Drawdown (m)",
           title="Three-well Theis example · observation at (250, 260) m")
    ax.set_xscale("log")
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    output = Path("outputs/transient_flow_demo.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=180)
    plt.close(fig)
    print(f"Saved {output}")


if __name__ == "__main__":
    main()
