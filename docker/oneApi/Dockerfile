FROM python:3.10.6-slim-bullseye as base

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir torch==1.13.1+cu116 torchvision==0.14.1+cu116 -i https://download.pytorch.org/whl/cu116
RUN pip install --no-cache-dir thop==0.1.1.post2209072238

COPY ./requirements_oneapi.txt /requirements_oneapi.txt
RUN pip install --no-cache-dir -r requirements_oneapi.txt
RUN pip install --no-cache-dir boto3


FROM python:3.10.6-slim-bullseye as build

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

RUN mkdir -p /ml_app
COPY . /ml_app
WORKDIR /ml_app/

CMD ["python", "app.py"]
ENV PYTHONBUFFERED 1