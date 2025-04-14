# Base image with python
FROM python:3.11-slim

# Set working directory

WORKDIR / app

# Run requirments

RUN pip install --uppgrade pip & pip install - r requirments.txt

# copy all file to dockerimge

COPY . .


# Expose Steamlot Port 
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "calculator.py", "--server.port=8501", "--server.address=0.0.0.0"]