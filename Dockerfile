FROM ubuntu:22.04
ADD MyApp /MyApp

ADD  install.sh  /root/
RUN chmod a+x /root/install.sh /MyApp/run.sh

RUN /root/install.sh
CMD /MyApp/run.sh
