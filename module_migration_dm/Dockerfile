FROM python:3.11

WORKDIR /module_migration_dm
COPY . /module_migration_dm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "alembic", "upgrade", "head" ]
CMD [ "python", "-m", "src.seed_tickets" ]
