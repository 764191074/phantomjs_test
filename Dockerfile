FROM opensuse:tumbleweed
RUN zypper mr -da
RUN zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/tumbleweed/repo/oss/ USTC:42.2:OSS
RUN zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/tumbleweed/repo/non-oss/ USTC:42.2:NON-:OSS
RUN zypper in phantomjs -y
RUN zypper in python3 -y
RUN zypper in python3-pip -y
RUN pip3 install selenium

COPY ./test/ /test
WORKDIR /test
CMD python3 test.py