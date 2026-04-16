# U.S. Code snippets for Paper/Redefining_Racism.tex (nickvido/us-code)
USC_TAG ?= annual/2025

.PHONY: usc-snippets usc-diffs usc-all

usc-snippets:
	python3 tools/usc_extract.py --tag $(USC_TAG)

usc-diffs:
	bash tools/usc_diff.sh

usc-all: usc-snippets usc-diffs
