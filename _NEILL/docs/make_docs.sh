#!/usr/bin/env bash

cd $LA_ROOT/_$LA_BRANCH/docs/src

pdflatex -quiet -aux-directory=./tmp -output-directory=.. -job-name=lumatools _main.tex
