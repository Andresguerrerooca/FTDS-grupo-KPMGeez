PYTHON ?= python
SEED ?= 2026
DATA_OUTPUT ?= data/raw
DIST_OUTPUT ?= dist

.PHONY: install demo-data medium-data full-data docker-up docker-down load-staging sql-pipeline streamlit test validate release

install:
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -e ".[dev]"

demo-data:
	$(PYTHON) scripts/generate_data.py --profile demo --seed $(SEED) --output $(DATA_OUTPUT)

medium-data:
	$(PYTHON) scripts/generate_data.py --profile medium --seed $(SEED) --output $(DATA_OUTPUT)

full-data:
	$(PYTHON) scripts/generate_data.py --profile full --seed $(SEED) --output $(DATA_OUTPUT)

docker-up:
	docker compose up -d

docker-down:
	docker compose down

load-staging:
	$(PYTHON) scripts/load_raw_data.py --input $(DATA_OUTPUT)

sql-pipeline:
	$(PYTHON) scripts/run_sql_pipeline.py

streamlit:
	$(PYTHON) -m streamlit run app/Home.py

test:
	$(PYTHON) -m pytest

validate:
	$(PYTHON) scripts/validate_project.py

release:
	$(PYTHON) scripts/build_student_release.py --output $(DIST_OUTPUT)
