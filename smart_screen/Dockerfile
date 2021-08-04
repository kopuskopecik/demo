FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /smart_screen
WORKDIR /smart_screen
COPY . /smart_screen

RUN pip install -r /smart_screen/requirements.txt
# RUN pip install -r /smart_screen/requirements-dev.txt

RUN chmod +x /smart_screen/docker-entrypoint.sh
CMD ["/bin/bash", "/smart_screen/docker-entrypoint.sh"]