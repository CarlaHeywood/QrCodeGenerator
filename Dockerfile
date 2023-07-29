FROM python:3

WORKDIR /var/www/BulkEmailer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD [ "python", "run.py" ]