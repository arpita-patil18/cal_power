FROM python:3.14.0
WORKDIR /dockerfile
COPY . .
CMD ["python", "power.py"]