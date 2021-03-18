# WebServerFlask
Simple HTTP Web Server made in Python Flask

## How to run the project:

If you dont't have python installed already, check [here](https://www.python.org/downloads/).

First, you need to pip install the `requirements.txt` (this will install Flask library and dependencies):

```
python -m pip install -r requirements.txt
```

Also, you'll need to set the `FLASK_APP`environment variable to the path of the project file like this:
- On Windows: `SET FLASK_APP=path/to/webserver.py`
- On Linux: `EXPORT FLASK_APP=path/to/webserver.py`

Finally, you will be able to run the server by writing on shell/cmd: 
```
flask run
```
Flask runs by default on `port 5000`. You can specify the port by adding `--port={PORT}` to the run command.
