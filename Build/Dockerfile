FROM ubuntu:20.04

RUN mkdir -p /media/Activities
RUN mkdir -p /Credentials

#ADD credentials.json token.pickle /Credentials/

ADD ../MyApp /MyApp

#ADD  install.sh run.sh  /root/
#RUN chmod a+x /root/install.sh /root/run.sh

ADD  install.sh  /root/
RUN chmod a+x /root/install.sh

RUN /root/install.sh
CMD /root/run.sh
