FROM python:3.11-slim

ARG COLLECTION
ENV COLLECTION=${COLLECTION}

RUN apt update \
 && apt-get install software-properties-common -y \
 && apt-get update \
 && apt install firefox-esr xvfb -y \
 && apt install wget -y \
 && apt install git -y \
 && git clone https://github.com/rozek/svg_repo_dl \
 && cd svg_repo_dl \
 && sh install.sh
CMD ["sh","-c","Xvfb :10 -ac & DISPLAY=:10 svgrepodl https://www.svgrepo.com/collection/$COLLECTION/ --path /transfer"]