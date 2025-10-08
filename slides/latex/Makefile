# All top-level TeX sources minus pygments
TEX_SRCS := $(filter-out pygments.tex,$(wildcard *.tex))
PDFS := $(TEX_SRCS:.tex=.pdf)

all:
	@for f in $(PDFS); do \
	    echo "Compiling $$f"; \
	    pdflatex "$${f%.pdf}.tex"; \
	    pdflatex "$${f%.pdf}.tex"; \
	done

# Rule: build PDF from TeX
%.pdf: %.tex
	pdflatex $<

clean:
	rm -f *.log *.out *.snm *.nav *~ *.aux *.toc *.idx snippets/*~ *.vrb, *.fls *.fdb_latexmk *.synctex.gz *.vrb

cleanall: clean
	rm -f *.pdf

copypdf:
	cp *.pdf ../pdf || true
	
.PHONY: all clean cleanall copypdf
