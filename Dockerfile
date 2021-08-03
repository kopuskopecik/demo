FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir mydemo
WORKDIR /mydemo
COPY . /mydemo

RUN pip install -r ./requirements.txt
# RUN pip install -r /smart_screen/requirements-dev.txt

RUN chmod +x ./docker-entrypoint.sh
CMD ["/bin/bash", "./docker-entrypoint.sh"]