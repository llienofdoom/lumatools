#!/usr/bin/env bash

cd src

pdflatex -quiet -aux-directory=./tmp -output-directory=.. -job-name=lumatools _main.tex
