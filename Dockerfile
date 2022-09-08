from python:3.9
COPY . /app
WORKDIR /app
RUN pip install flash
ENV PYTHONUNBUFFERED 1
EXPOSE 8001
CMD python3 ./main.py