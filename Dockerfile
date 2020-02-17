FROM python
RUN apt-get update -y
WORKDIR appp
COPY app /appp
COPY . /appp
RUN pip install -r requirements.txt
EXPOSE 4500
CMD ["python", "main.py"]




