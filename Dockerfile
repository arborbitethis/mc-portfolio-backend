FROM python:3.9

# Install necessary packages for SSM Agent
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install the SSM Agent
RUN curl "https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/amazon-ssm-agent.deb" -o "/tmp/amazon-ssm-agent.deb"
RUN dpkg -i /tmp/amazon-ssm-agent.deb && rm /tmp/amazon-ssm-agent.deb


WORKDIR /code

 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./.env /code/.env
COPY ./src /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

