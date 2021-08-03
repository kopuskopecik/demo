server {
    listen 80;
    server_name erdogansahin.net;
    return 301 https://$host$request_uri;

    location / {
        proxy_pass http://backend;
    }

}

server {
    listen 443 ssl;
    server_name erdogansahin.net;

    # proxy_connect_timeout 900;
    # proxy_send_timeout 900;
    # proxy_read_timeout 900;
    # send_timeout 900;

    ssl_certificate     /etc/letsencrypt/live/erdogansahin.net/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/erdogansahin.net/privkey.pem;

    client_max_body_size 100M;

    location / {
        proxy_read_timeout 300;
        proxy_connect_timeout 300;
        proxy_send_timeout 300;
        send_timeout 300;
        proxy_set_header Host $host;
        proxy_pass http://backend;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
    }
   
}