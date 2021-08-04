server {
    listen 80;
    server_name erdogansahin.net www.erdogansahin.net;
    return 301 https://$host$request_uri;

    location / {
        proxy_pass http://backend;
    }

}