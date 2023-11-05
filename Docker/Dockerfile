FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./.secrets.toml /code/settings.toml

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./tg_api /code/tg_api

CMD ["uvicorn", "tg_api.presentation.api:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]