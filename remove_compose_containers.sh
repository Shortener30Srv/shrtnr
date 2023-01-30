#fedora sync RAM
sudo sync -f
sudo docker compose -f "docker-compose.shortener.yml" down -v
sudo docker compose -f "docker-compose.shortener.yml" rm
sleep 1;
sudo docker compose -f "docker-compose.db.yml" down -v
sudo docker compose -f "docker-compose.db.yml" rm
sleep 1;
sudo docker compose -f "docker-compose.nginx.yml" down -v
sudo docker compose -f "docker-compose.nginx.yml" rm
sleep 1;
sudo docker ps -a
