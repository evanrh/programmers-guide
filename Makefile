CC = pdflatex

ODIR = output
SDIR = src
TEXINPUTS = TEXINPUTS="src:"

_SRCS = guide.tex
SRCS = $(patsubst %, $(SDIR)/%, $(_SRCS))
MAIN = guide

all: $(SRCS)
	$(TEXINPUTS) $(CC) -output-directory $(ODIR) $(SDIR)/$(MAIN).tex
	cd $(ODIR) && BIBINPUTS="../src:" TEXMFOUTPUT="$(ODIR)" biber $(MAIN) && cd ..
	$(TEXINPUTS) $(CC) -output-directory $(ODIR) $(MAIN).tex
	$(TEXINPUTS) $(CC) -output-directory $(ODIR) $(MAIN).tex
