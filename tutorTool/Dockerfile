# Use the official Python image as the base image
FROM python:3.12-slim

LABEL authors="shola"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Collect static files
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    echo 'alias ll="ls -l"' >> ~/.bashrc

RUN mkdir -p /var/log/gunicorn && chown -R www-data:www-data /var/log/gunicorn

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "/var/log/gunicorn/access.log", "--error-logfile", "/var/log/gunicorn/error.log", "tutorproject.wsgi:application"]
