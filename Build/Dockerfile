FROM ubuntu:20.04

RUN mkdir -p /media/Activities
RUN mkdir -p /Credentials

ADD credentials.json token.pickle /Credentials/

ADD  installSelenium.sh run.sh  /root/

RUN chmod a+x /root/installSelenium.sh /root/run.sh
RUN /root/installSelenium.sh
CMD /root/run.sh
