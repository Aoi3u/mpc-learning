IMAGE ?= mpspdz:mascot-party
PLAYERS ?= 2
PROTOCOL ?= mascot
PROGRAM ?= tutorial_ja

MPSPDZ_DIR := MP-SPDZ
USER_PROGRAMS := /usr/src/MP-SPDZ/Programs/Source/user_programs
PLAYER_DATA := /usr/src/MP-SPDZ/Player-Data

.PHONY: get-mpspdz build tutorial pwd run

get-mpspdz:
	test -d $(MPSPDZ_DIR) || git clone https://github.com/data61/MP-SPDZ.git $(MPSPDZ_DIR)

build:
	docker build --tag $(IMAGE) --build-arg machine=mascot-party.x $(MPSPDZ_DIR)

tutorial:
	docker run --rm -it -e PLAYERS=$(PLAYERS) $(IMAGE) ./Scripts/compile-run.py $(PROTOCOL) tutorial

pwd:
	docker run --rm -it $(IMAGE) pwd

run:
	mkdir -p Player-Data
	docker run --rm -it \
		-e PLAYERS=$(PLAYERS) \
		-v "$(PWD)/programs:$(USER_PROGRAMS):ro" \
		-v "$(PWD)/Player-Data:$(PLAYER_DATA)" \
		$(IMAGE) \
		./Scripts/compile-run.py $(PROTOCOL) user_programs/$(PROGRAM)
