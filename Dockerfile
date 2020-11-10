FROM python:3.9-slim

WORKDIR /

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./
ENTRYPOINT [ "python", "/app/app.py" ] 