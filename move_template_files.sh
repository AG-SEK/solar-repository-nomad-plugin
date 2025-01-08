#!/bin/sh

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh solar-repo-perolab/ .
  rm -rfv solar-repo-perolab
fi
