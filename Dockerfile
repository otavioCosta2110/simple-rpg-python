FROM python

COPY . /home

CMD [ "python",  "-u", "/home/main.py" ]