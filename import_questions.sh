#! /bin/bash

echo "Running python script insert_questions.py..."
python insert_questions.py
#sudo rm /var/cache/hhvm/hhvm.hhbc &> /dev/null
#sudo hhvm-repo-mode enable /var/www/fbctf &> /dev/null
#sudo chown www-data:www-data /var/cache/hhvm/hhvm.hhbc &> /dev/null
#echo "Starting hhvm.."
#sudo service hhvm start &> /dev/null
#echo "Restarting nginx..."
#sudo service nginx restart &> /dev/null
echo 'flush_all' | nc localhost 11211
echo "Finished"
