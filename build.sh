#!/bin/bash

LOC=buildfiles
OUTDIR=output
INPUT=guide.tex

function Help() {
   echo "Build LaTeX file into a pdf or count words"
   echo
   echo "Syntax: build.sh [-h] [count]"
   echo
   echo "options:"
   echo "count    Counts the words in guide"
   echo
   echo "Passing no arguments will build the project into a pdf"
}

function build() {
   run "pdflatex -output-directory /$OUTDIR $INPUT"
}

function count() {
   run "texcount $INPUT"
}

function run() {
   docker run \
      -v $PWD/src/:/$LOC \
      -v $PWD/$OUTDIR:/$OUTDIR \
      -u $USERID:$GROUPID \
      -w /$LOC \
      texlive/texlive \
      $1
}

while getopts ":h" option; do
   case $option in
      h)
         Help
         exit;;
   esac
done

# Create output directory
if [[ ! -d ./$OUTDIR ]]; then
   echo "Creating output directory"
   mkdir -p ./$OUTDIR
fi

USERID=$(stat -c '%u' $OUTDIR)
GROUPID=$(stat -c '%g' $OUTDIR)

if [[ "$#" -eq 0 ]]; then
   build
else
   if [[ $1 -eq "count" ]]; then
      count
   fi
fi
