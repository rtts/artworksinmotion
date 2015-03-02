server {
  server_name artworksinmotion.com;
  rewrite ^(.*) http://www.artworksinmotion.com$1 permanent;
}

server {
  server_name www.artworksinmotion.com;
  root /home/www/artworksinmotion;
}
