FROM centos:centos7

#ENV PROXY_HOST proxy.hostname.com
#ENV PROXY_PORT 5273
#ENV PROXY_URI http://${PROXY_HOST}:${PROXY_PORT}/

# yum update and install
#RUN echo proxy=${PROXY_URI} >> /etc/yum.conf
RUN yum -y update
RUN yum -y install python

# get get-pip.py
#RUN curl --proxy ${PROXY_URI} -O https://bootstrap.pypa.io/get-pip.py
RUN curl -O https://bootstrap.pypa.io/get-pip.py

# install pip
#   <Install behind a proxy https://pip.pypa.io/en/stable/installing/#get-pip-py-options >
#     python get-pip.py --proxy="[user:passwd@]proxy.server:port"
#RUN python get-pip.py --proxy="${PROXY_HOST}:${PROXY_PORT}"
RUN python get-pip.py

# get package using pip
#   <Run behind a proxy https://pip.pypa.io/en/stable/reference/pip/?highlight=proxy#cmdoption--proxy>
#     pip --proxy [user:passwd@]proxy.server:port install -qr /tmp/requirements.txt
ADD ./webapp/requirements.txt /tmp/requirements.txt
#RUN pip --proxy ${PROXY_HOST}:${PROXY_PORT} install -qr /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt

ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5000

CMD ["python", "sample.py"]