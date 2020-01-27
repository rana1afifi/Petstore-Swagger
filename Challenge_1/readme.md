## Bids Api

### To Setup and Start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt 
python app.py
```
## Swagger UI
Hosted Locally
http://127.0.0.1:5000/swagger/

### Get All 
```bash
curl -X GET http://127.0.0.1:5000/request
``

### Post Request
```bash
curl -X POST http://127.0.0.1:5000/request -H 'Content-Type: application/json' -d '{'petID': 1 , 'userID': 3 , 'money': 55}'
```


### Testing with Nose 
```bash
$ nosetests -v tests/app_test.py
Test getting all requests ... ok
Test adding posting request ... ok
Test adding bad post request ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.009s

```






