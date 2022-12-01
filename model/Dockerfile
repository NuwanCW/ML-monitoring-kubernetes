FROM python:3.7
ADD ./ ./ 
RUN pip install -r requirements.txt 
EXPOSE 80
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]
