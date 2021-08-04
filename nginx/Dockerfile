FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY 9D6ECA0F18B629F3BD040E62636E247A.txt /etc/nginx/9D6ECA0F18B629F3BD040E62636E247A.txt

COPY certificate /app/certificate