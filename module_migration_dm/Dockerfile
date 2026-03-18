FROM python:3.11

WORKDIR /module_migration_dm
COPY . /module_migration_dm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN echo '#!/bin/sh\nalembic upgrade head\npython -m src.seed_tickets' > /run_migration_and_seed.sh \
    && chmod +x /run_migration_and_seed.sh

CMD ["/run_migration_and_seed.sh"]
