FROM python:3.9-slim

# Set the working directory
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . /app/
EXPOSE 5000
CMD ["python", "app.py"]
