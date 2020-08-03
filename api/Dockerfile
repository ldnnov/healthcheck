FROM python:3.6
RUN mkdir /api
RUN mkdir /api/database
COPY ./api /api
COPY ./database /api/database
WORKDIR /api
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080