# dead-reckoning-rnn

**Place cells from path integration.** Does an RNN that tracks its own position from movement alone develop place-cell or grid-cell-like units?

Part of the **Latent Space Project**: 18 small PyTorch repos that test one idea, that neural networks encode concepts and strategy in their latent space, and that we can read and edit those representations. Everything trains on a single consumer GPU or a laptop.

| Roadmap | Phase | Depends on | Status |
| --- | --- | --- | --- |
| 9 of 18 | 4. Strategy and navigation | Nothing | Not started (scaffolded) |

## Question

Does an RNN that tracks its own position from movement alone develop place-cell or grid-cell-like units?

## Plan

- **Architecture:** an RNN (vanilla or LSTM, 256–1024 units). Input is velocity (speed, plus heading as sine and cosine). Output is a population code over simulated place cells in the arena, which works better than predicting raw (x, y).
- **Data:** simulated smooth random walks in a square arena that turn away from walls.

## Experiments

- A rate map (activation by position) for every hidden unit.
- Spatial autocorrelation and gridness scores.
- How activation constraints and output encoding change the result.

## Done when

The definition of done every Latent Space Project repo shares:

Apply this checklist with the project-specific requirements and exceptions in
[CLAUDE.md](CLAUDE.md#project-specific-scope).

- `just quick` runs end to end on CPU in under 5 minutes, as a smoke test.
- The full run fits on one consumer GPU (8–12 GB VRAM) and auto-detects cuda, mps or cpu.
- Each run saves weights, `metrics.json` and its plots to `runs/<run-name>/`.
- This README shows the headline result with plots, compares against baselines, and states negative results plainly.
- Tests cover data generators, tensor shapes and one tiny overfit check.

## Notes

- **Caution:** grid patterns are known to depend heavily on these choices (Schaeffer et al. 2022). Report clearly what does and does not emerge.

## Quickstart

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Everything else, Python 3.12 included, comes from uv.

```sh
just setup              # uv sync, then install the pre-commit hooks
just quick              # CPU smoke test, under 5 minutes
just train              # full run; flags pass through, e.g. --run-name wd1.0-seed0
just analyze <run>      # baselines, probes, interventions and plots
just test               # pytest
just check              # ruff and basedpyright, as in CI
```

Copy `.env.example` to `.env` (gitignored) for `HF_TOKEN` and `HF_USER`.

## Layout

```
dead-reckoning-rnn/
├── README.md                goal, plan, results with plots
├── CLAUDE.md                instructions for coding agents; AGENTS.md points here
├── .agents/                 instructions/ (Python formatting, commits) and plans/
├── pyproject.toml           metadata, dependencies, tool settings
├── uv.lock                  committed lockfile
├── .python-version          pinned by uv
├── justfile                 every routine command
├── .pre-commit-config.yaml
├── .github/workflows/ci.yml
├── src/dead_reckoning_rnn/
│   └── model.py, data.py, analysis.py, utils.py
├── train.py                 CLI; --quick runs the CPU smoke test
├── predict.py               load weights and run inference
├── analyze.py               baselines, probes, interventions, plots
├── notebooks/               marimo notebooks for exploration
├── tests/
└── runs/                    outputs, gitignored
```

## Results

_No results yet._ The headline result with plots, the comparison against baselines, and any negative results go here.

## Sources

- Cueva and Wei 2018, Grid-like representations in RNNs
- Schaeffer et al. 2022, No free lunch from deep learning in neuroscience

## License

MIT
