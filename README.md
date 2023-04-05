# DVC .git folder growing

The issue occurs when passing nested data as stage dependency.

In my case, a `foreach` preprocessing stage recreates directories structure from `data/raw` in `data/interim` . The latter is added as a dependency of `train` stage. Running an experiment leads to `.git` catalog growing approximately the size of `data/interim` (with object packs from this folder), and if the data is large - quite a long wait for `Updating lock file 'dvc.lock'` at the end.

## Input data:
```
data
└───raw
    ├───dirA
    │       file0.txt
    │       file1.txt
    │
    └───dirB
            file0.txt
            file1.txt
```

## Stages:
```
                +--------------+
                | data\raw.dvc |
                +--------------+
                **            **
              **                **
            **                    **
+-----------------+         +-----------------+
| preprocess@dirA |         | preprocess@dirB |
+-----------------+         +-----------------+
                **            **
                  **        **
                    **    **
                   +-------+
                   | train |
                   +-------+
```

## To reproduce:
1. Create data : `python create_data.py` (~20 MB)
2. Check .git folder size (small)
3. (optional) Run just the preprocessing stage: `dvc exp run -fs preprocess`.
Check .git folder size (small)
4. Run an experiment `dvc exp run -f`
Check .git folder size (~15 MB)

Tested with dvc 2.52.0 (Windows).

## To clean .git folder:
run `./clean.bat`
