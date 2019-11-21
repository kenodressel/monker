FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r PRDREQ
# could potentially add ; python app.py for flask server
CMD sh -c "python monker.py $ASSET $QUOTE"
