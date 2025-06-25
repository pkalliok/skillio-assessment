FROM docker.io/library/python
RUN pip3 install psycopg2-binary flask gunicorn
COPY web_service.py .
#CMD ["flask", "--app", "web_service", "run", "--host", "0.0.0.0"]
CMD ["gunicorn", "web_service:app", "-b", "0.0.0.0:5000"]
