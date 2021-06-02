#!/bin/bash

# Run docker command to open up container

LOC=src
OUTDIR=output
INPUT=guide

USERID=$(stat -c '%u' $OUTDIR)
GROUPID=$(stat -c '%g' $OUTDIR)

docker run -it \
   -v $PWD/src/:/$LOC \
   -v $PWD/$OUTDIR:/$OUTDIR \
   -v $PWD/Makefile:/Makefile \
   -v $PWD/styles/:/styles \
   -u $USERID:$GROUPID\
   texlive/texlive \
