DOSE=docker-compose

echo "current dir:"
pwd

git pull

$DOSE pull app
$DOSE stop app
$DOSE rm -f app
$DOSE up -d app

echo success
echo $?
