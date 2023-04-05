dvc queue remove --all
dvc exp remove -A
dvc gc -wf
git reflog expire --expire=now --all
git gc --aggressive --prune=now
