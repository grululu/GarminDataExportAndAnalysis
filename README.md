# Garmin data export
**About this project:** The main idea of this project is to not only extract all activities data from Garmin Connect for those who use its system, but also to organize both GPX and CSV data on a **PostGIS** database. 

:warning: **Obviously, this project has no relation to Garmin and its use should be tke care of its rigth**.

## Setup:

#### PostgreSQL
```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO felipe2;
```

```

from sqlalchemy_views import CreateView, DropView
from sqlalchemy.sql import text
from sqlalchemy import Table

con, meta = connect(databaseUser, databasePW, databaseName, databaseServer, port = 5432)

view = Table('garmin_ids', meta)
definition = text("SELECT distinct(\"idGarmin\") FROM summary")

create_view = CreateView(view, definition, or_replace=True)
print(create_view)

```
## Python 3 module used in this project
:heavy_check_mark: [Selenium](https://selenium-python.readthedocs.io/)  
:heavy_check_mark: [osgeo](http://gdal.org/python/)  
:heavy_check_mark: [SQLAlchemy](http://www.sqlalchemy.org/)  
:heavy_check_mark: [psycopg2](http://initd.org/psycopg/docs/)  
:heavy_check_mark: [pyvirtualdisplay](http://pyvirtualdisplay.readthedocs.io/en/latest/)  
  
#### Important consideration about installation  
* [Installing and config Chrome for Selenium](https://christopher.su/2015/selenium-chromedriver-ubuntu/)  
* [**Consider Chrome Driver latest version**](https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip)  

* **sqlalchemy_views**  

### About codes:
* [infos.py](): Set of important parameters and informations that will be necessary:
    * GCuser = "GarminUserName"
    * GCpass="GarminPassWord"
    * databaseServer = "localhost"
    * databaseName = "DBName"
    * databaseUser = "DBUser"
    * databasePW = "DBPassWord"
* [s]()

## Useful links:
* https://www.guru99.com/selenium-python.html  
* http://www.thetaranights.com/login-to-a-website-using-selenium-python-python-selenium-example/  
* https://selenium-python.readthedocs.io/  
* http://www.sqlalchemy.org/library.html#tutorials
* https://suhas.org/sqlalchemy-tutorial/
* http://docs.sqlalchemy.org/en/rel_1_0/core/tutorial.html  
* http://docs.sqlalchemy.org/en/rel_1_0/index.html  
* http://initd.org/psycopg/docs/
* https://wiki.postgresql.org/wiki/Psycopg2_Tutorial  
* http://gdal.org/functions_c.html#index_c

## Data base creation:
```
postgres=# CREATE DATABASE tennis;
CREATE DATABASE
postgres=# CREATE USER federer WITH PASSWORD 'grandestslam';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE tennis TO federer;
GRANT
```

### *Garmin Connect* links

[url_gc_login](https://sso.garmin.com/sso/login?service=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&webhost=olaxpw-connect04&source=https%3A%2F%2Fconnect.garmin.com%2Fen-US%2Fsignin&redirectAfterAccountLoginUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&redirectAfterAccountCreationUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_US&id=gauth-widget&cssUrl=https%3A%2F%2Fstatic.garmincdn.com%2Fcom.garmin.connect%2Fui%2Fcss%2Fgauth-custom-v1.1-min.css&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&usernameShown=false&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false&generateExtraServiceTicket=false)  
[url_gc_post_auth](https://connect.garmin.com/post-auth/login?)  
[url_gc_search](http://connect.garmin.com/proxy/activity-search-service-1.0/json/activities?)  
[url_gc_gpx_activity](http://connect.garmin.com/proxy/activity-service-1.1/gpx/activity/)  
[url_gc_tcx_activity](http://connect.garmin.com/proxy/activity-service-1.1/tcx/activity/)  
[url_gc_original_activity](http://connect.garmin.com/proxy/download-service/files/activity/)  

#### New endpoints
[url_gc_tcx_activity](https://connect.garmin.com/modern/proxy/download-service/export/tcx/activity/)  
[url_gc_gpx_activity](https://connect.garmin.com/modern/proxy/download-service/export/gpx/activity/)  
[por JSON](https://connect.garmin.com/proxy/activity-search-service-1.0/json/activities?)