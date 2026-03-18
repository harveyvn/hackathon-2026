NETWORK_NAME=harvey-cloud

.PHONY: create-network

create-network:
	@if [ -z "$$(docker network ls --filter name=^$(NETWORK_NAME)$$ --format '{{ .Name }}')" ]; then \
		echo "Creating Docker network: $(NETWORK_NAME)"; \
		docker network create $(NETWORK_NAME); \
	else \
		echo "Docker network '$(NETWORK_NAME)' already exists."; \
	fi

MODULES = module_mysql_db module_metabase
build-all-modules:
	@for module in $(MODULES); do \
		echo "Starting $$module..."; \
		cd $$module && docker compose build --no-cache && docker compose up -d && cd ..; \
		echo "Waiting 5 seconds for $$module to stabilize..."; \
		sleep 5; \
	done

migrate-dm:
	@echo "Starting module_migration_dm..."
	cd module_migration_dm && docker compose up --build

start: create-network build-all-modules migrate-dm
	@echo "All modules started."

# Optional cleanup
clean:
	@for module in $(MODULES) module_airflow module_migration_dm; do \
		echo "Stopping $$module..."; \
		cd $$module && docker compose down && cd ..; \
	done
	@echo "Removing Docker network $(NETWORK_NAME)..."
	docker network rm $(NETWORK_NAME) || true

clean-complete:
	@for module in $(MODULES) module_airflow module_migration_dm; do \
		echo "Stopping and removing $$module..."; \
		cd $$module && docker compose down -v && cd ..; \
	done
	@echo "Removing Docker network $(NETWORK_NAME)..."
	docker network rm $(NETWORK_NAME) || true