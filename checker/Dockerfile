FROM python:3.6
RUN mkdir /checker
RUN mkdir /checker/database
COPY ./checker /checker
COPY ./database /checker/database
WORKDIR /checker
RUN pip3 install --no-cache-dir -r requirements.txt