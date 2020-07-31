FROM python:3.8.2-slim-buster
RUN apt -y update && apt -y install wget
RUN pip install --upgrade pip && pip install -U discord.py==1.3.4
RUN pip install requests
COPY bot.py /bot.py
WORKDIR /
ENTRYPOINT ["python3"] 
CMD ["bot.py"]
