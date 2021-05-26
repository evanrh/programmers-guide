#!/bin/bash
LOC=buildfiles
OUTDIR=output

# Create output directory
if [[ ! -d ./$OUTDIR ]]
then
   echo "Creating output directory"
   mkdir -p ./$OUTDIR
fi

USERID=$(stat -c '%u' $OUTDIR)
GROUPID=$(stat -c '%g' $OUTDIR)

docker run \
   -v $PWD/src/:/$LOC \
   -v $PWD/$OUTDIR:/$OUTDIR \
   -u $USERID:$GROUPID \
   texlive/texlive \
   pdflatex -output-directory /$OUTDIR $LOC/guide.tex 
