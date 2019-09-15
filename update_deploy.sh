DOSE=docker-compose

echo "current dir:"
pwd

git pull

$DOSE down
$DOSE pull app
$DOSE up -d

echo success
echo $?
