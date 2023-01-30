#fedora sync RAM
sudo sync -f
sudo docker compose -f "docker-compose.db.yml" down -v
sudo docker compose -f "docker-compose.db.yml" rm
sleep 1;

sudo docker compose -f "docker-compose.shortener.yml" down -v
sudo docker compose -f "docker-compose.shortener.yml" rm
sleep 1;
sudo docker compose -f "docker-compose.nginx.yml" down -v
sudo docker compose -f "docker-compose.nginx.yml" rm
sleep 1;
sudo docker compose -f "docker-compose.db.yml" up --build --force-recreate --renew-anon-volumes -d
sleep 20;
sudo docker compose -f "docker-compose.shortener.yml" up --build --force-recreate --renew-anon-volumes -d
sleep 20;
sudo docker compose -f "docker-compose.nginx.yml" up --build --force-recreate --renew-anon-volumes -d
sudo bash links_show.sh
