FROM python:3.7

MAINTAINER linyangxin "104317359@qq.com"

COPY /requirements.txt /requirements.txt

WORKDIR /

ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

ENV LANG C.UTF-8

EXPOSE 80

RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /

CMD python /run.py
