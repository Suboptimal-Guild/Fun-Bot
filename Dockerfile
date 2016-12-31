FROM jfloff/alpine-python:latest-slim

# Copy harambot files in
COPY /run.py /run.py
COPY /fun /fun

# Copy requirements file for package installation.
COPY /requirements.txt /requirements.txt

# Copy the credentials files
COPY .credentials /root/.credentials

# Add all of the python packages we need.
RUN pip install -r requirements.txt
