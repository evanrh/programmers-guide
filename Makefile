CC = pdflatex

ODIR = output
SDIR = src
TEXINPUTS = TEXINPUTS="src:"

_SRCS = guide.tex
SRCS = $(patsubst %, $(SDIR)/%, $(_SRCS))
MAIN = guide

all: $(SRCS)
	$(TEXINPUTS) $(CC) -output-directory $(ODIR) $(SDIR)/$(MAIN).tex
	BIBINPUTS="src:" TEXMFOUTPUT="$(ODIR)" bibtex $(ODIR)/$(MAIN)
	$(TEXINPUTS) $(CC) -output-directory $(ODIR) $(MAIN).tex
	$(TEXINPUTS) $(CC) -output-directory $(ODIR) $(MAIN).tex
