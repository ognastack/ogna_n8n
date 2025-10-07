# ogna_n8n

# setting up certificates

```
    mkdir -p /certs
```

1. Generate certificates (this will create them in /etc/letsencrypt by default)

```

    sudo certbot certonly --standalone -d <YOUR DOAIM> -d <www.YOUR DOAIM>
```

2. copy the certificates

```
    sudo cp -L /etc/letsencrypt/live/<YOURDOMAIN>/privkey.pem /certs/
    sudo cp -L /etc/letsencrypt/live/YOURDOMAIN>/fullchain.pem /certs/
```

3. Chnage permissions

```
    sudo chmod 640 /certs/privkey.pem
    sudo chmod 644 /certs/privkey.pem
```
