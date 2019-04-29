DOSE=docker-compose

echo "current dir:"
pwd

git pull

$DOSE down
$DOSE pull
$DOSE up -d

$DOSE exec app bash -c 'python manage.py shell < add_dummy_data.py'
