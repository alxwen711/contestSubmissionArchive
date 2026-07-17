.PHONY: build archive

# Flags
PATH="archive/unsorted"

build:
	@echo "Constructing new base folder..."
	python LIVE/build.py -n $(PATH)

archive:
	@echo "Moving contest folder..."
	python LIVE/archive.py -p $(PATH)