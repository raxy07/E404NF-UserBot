# We're using Ubuntu 20.10
FROM vckyouuu/bismillah:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b E404NF https://github.com/vckyou/E404NF-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/vckyou/E404NF-UserBot/master/requirements.txt

CMD ["python3","-m","userbot"]
