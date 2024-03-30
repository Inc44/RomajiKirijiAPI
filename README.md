### Romaji Kiriji API
#### Install
```
conda create --name RomajiKirijiAPI python=3.10.13
conda deactivate
conda activate RomajiKirijiAPI
pip install fastapi gunicorn pykakasi uvicorn
git clone https://github.com/Inc44/RomajiKirijiAPI.git
```
#### Develop
```
cd RomajiKirijiAPI
conda deactivate
conda activate RomajiKirijiAPI
uvicorn api:api --reload
```
#### Run
```
cd RomajiKirijiAPI
conda deactivate
conda activate RomajiKirijiAPI
gunicorn api:api -w 13 -k uvicorn.workers.UvicornWorker --log-level critical
```
#### Test
```
curl -X 'POST' 'http://127.0.0.1:8000/translate/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"japanese_text": "我は官軍我（わが）敵は天地容れざる朝敵ぞ敵の大將たる者は古今無雙（双）の英雄で"}'
```
#### Benchmark
```
cd RomajiKirijiAPI
wrk -t13 -c1000 -d10s -s post.lua http://127.0.0.1:8000/translate/
```
