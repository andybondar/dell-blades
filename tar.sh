#!/bin/bash

directory=`date +%s`

mkdir -p ../$directory/dell-blades
cp requirements.txt serveraction.py ../$directory/dell-blades/
cd ../$directory/dell-blades/
virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt
deactivate

wd=`pwd`
arr=($(grep $wd/.env $wd/.env/bin/* | awk -F":" '{print $1}'))

for i in ${arr[@]};
 do sed -i s,$wd,/home/virtualenv/dell-blades,g $i
done

echo '#!/bin/bash' > venv.sh
echo 'wd=`pwd`' >> venv.sh
echo 'arr=($(grep $wd/.env $wd/.env/bin/* | awk -F":" '\''{print $1}'\''))' >> venv.sh
echo 'for i in ${arr[@]};' >> venv.sh
echo ' do sed -i s,/home/virtualenv/dell-blades,$wd,g $i' >> venv.sh
echo 'done' >> venv.sh
echo 'source .env/bin/activate' >> venv.sh

chmod 755 venv.sh

cd ..
tar cvfz dell-blades.tar.gz dell-blades/
rm -rf dell-blades/