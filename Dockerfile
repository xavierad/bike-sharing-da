FROM python:3.10.11-slim-bullseye

RUN apt-get update -y && apt install unzip

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt
# RUN kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset
RUN unzip london-bike-sharing-dataset.zip

WORKDIR analytics_project/

CMD ["python", "manage.py", "makemigrations", "dashboard"]
CMD ["python", "manage.py", "migrate", "dashboard"]
CMD ["python", "runscripts", "load_data"]
CMD [ "python", "manage.py", "runserver" ]