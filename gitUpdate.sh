#!/bin/bash
date > updated.txt

# ensure to get origin's data and discard any local change
git fetch
git reset origin/main --hard

git pull
