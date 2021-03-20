# Using Python Slim-Buster
FROM vckyouuu/vckyouu:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/vckyou/E404NF-UserBot /home/vckyouu/ \
    && chmod 777 /home/vckyouu \
    && mkdir /home/vckyouu/bin/

WORKDIR /home/vckyouu/

# Finalization
CMD ["python3","-m","userbot"]
