all:
	pdflatex template

clean:
	rm -f *.log *.out *.snm *.nav *~ *.aux *.toc *.idx snippets/*~ *.vrb, *.fls *.fdb_latexmk *.synctex.gz *.vrb

cleanall: clean
	rm -f *.pdf

copypdf:
	cp *.pdf ../pdf
