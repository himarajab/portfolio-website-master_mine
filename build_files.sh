# build_files.sh
source env/bin/activate
pip install -r requirements.txt
python manage.py collectstatic