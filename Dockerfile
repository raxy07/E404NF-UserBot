# Using Python Slim-Buster
FROM vckyouuu/vckyouu:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/vckyou/E404NF-UserBot /home/vckyouuu/ \
    && chmod 777 /home/vckyouuu \
    && mkdir /home/vckyouuu/bin/

WORKDIR /home/vckyouuu/

# Finalization
CMD ["python3","-m","userbot"]
