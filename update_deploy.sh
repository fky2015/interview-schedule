DOSE=docker-compose

echo "current dir:"
pwd

git pull

$DOSE down
$DOSE pull
$DOSE up -d
