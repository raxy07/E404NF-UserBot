# Using Python Slim-Buster
FROM vckyouuu/vckyouu:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/vckyou/E404NF-UserBot /home/vckyou/ \
    && chmod 777 /home/weebproject \
    && mkdir /home/weebproject/bin/

WORKDIR /home/weebproject/

# Finalization
CMD ["python3","-m","userbot"]
