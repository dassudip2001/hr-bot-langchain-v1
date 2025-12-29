# Use a Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache \
    uv sync --locked --no-dev --no-install-project

COPY . .

# Install your project (if it's a package) or any remaining dev dependencies
# RUN uv pip install --upgrade . # If your app is a package
# RUN uv pip install --upgrade -r requirements-dev.txt # If you have dev dependencies

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"] 