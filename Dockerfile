FROM opensuse:tumbleweed
RUN zypper mr -da
RUN zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/tumbleweed/repo/oss/ USTC:42.2:OSS
RUN zypper ar -fc https://mirrors.ustc.edu.cn/opensuse/tumbleweed/repo/non-oss/ USTC:42.2:NON-:OSS
RUN zypper in phantomjs
RUN zypper in python3
RUN zypper se python3-pip
RUN pip3 install selenium
