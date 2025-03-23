```shell
Microsoft Windows [Version 10.0.26100.2894]
(c) Microsoft Corporation. All rights reserved.

C:\Users\alame\OneDrive\Desktop\project2024>where python3.10
INFO: Could not find files for the given pattern(s).

C:\Users\alame\OneDrive\Desktop\project2024>py -3.9 -c "import sys; print(sys.executable)"
No suitable Python runtime found
Pass --list (-0) to see all detected environments on your machine
or set environment variable PYLAUNCHER_ALLOW_INSTALL to use winget
or open the Microsoft Store to the requested version.

C:\Users\alame\OneDrive\Desktop\project2024>py -3.10 -c "import sys; print(sys.executable)"
C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe

C:\Users\alame\OneDrive\Desktop\project2024>"C:\Users\alame\AppData\Local\Programs\Python\Python310\Scripts\pip.exe" --version
pip 21.2.3 from C:\Users\alame\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

C:\Users\alame\OneDrive\Desktop\project2024>doskey /history > history.txt

C:\Users\alame\OneDrive\Desktop\project2024>dir /b
history.txt
mysqlclient-2.2.4-pp310-pypy310_pp73-win_amd64.whl
turffinal
venv

C:\Users\alame\OneDrive\Desktop\project2024>more history.txt
where python3.10
py -3.9 -c "import sys; print(sys.executable)"
py -3.10 -c "import sys; print(sys.executable)"
"C:\Users\alame\AppData\Local\Programs\Python\Python310\Scripts\pip.exe" --version
doskey /history > history.txt

C:\Users\alame\OneDrive\Desktop\project2024>"C:\Users\alame\AppData\Local\Programs\Python\Python310\Scripts\pip.exe" install virtualenvwrapper
Collecting virtualenvwrapper
  Downloading virtualenvwrapper-6.1.1-py3-none-any.whl (22 kB)
Collecting stevedore
  Downloading stevedore-5.4.0-py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB 2.9 MB/s
Collecting virtualenv
  Downloading virtualenv-20.29.2-py3-none-any.whl (4.3 MB)
     |████████████████████████████████| 4.3 MB 1.6 MB/s
Collecting virtualenv-clone
  Downloading virtualenv_clone-0.5.7-py3-none-any.whl (6.6 kB)
Collecting pbr>=2.0.0
  Downloading pbr-6.1.1-py2.py3-none-any.whl (108 kB)
     |████████████████████████████████| 108 kB 3.2 MB/s
Requirement already satisfied: setuptools in c:\users\alame\appdata\local\programs\python\python310\lib\site-packages (from pbr>=2.0.0->stevedore->virtualenvwrapper) (57.4.0)
Collecting filelock<4,>=3.12.2
  Downloading filelock-3.17.0-py3-none-any.whl (16 kB)
Collecting distlib<1,>=0.3.7
  Downloading distlib-0.3.9-py2.py3-none-any.whl (468 kB)
     |████████████████████████████████| 468 kB 6.4 MB/s
Collecting platformdirs<5,>=3.9.1
  Downloading platformdirs-4.3.6-py3-none-any.whl (18 kB)
Installing collected packages: platformdirs, pbr, filelock, distlib, virtualenv-clone, virtualenv, stevedore, virtualenvwrapper
Successfully installed distlib-0.3.9 filelock-3.17.0 pbr-6.1.1 platformdirs-4.3.6 stevedore-5.4.0 virtualenv-20.29.2 virtualenv-clone-0.5.7 virtualenvwrapper-6.1.1
WARNING: You are using pip version 21.2.3; however, version 25.0.1 is available.
You should consider upgrading via the 'C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip' command.

C:\Users\alame\OneDrive\Desktop\project2024>where python3.10
INFO: Could not find files for the given pattern(s).

C:\Users\alame\OneDrive\Desktop\project2024>color 3

C:\Users\alame\OneDrive\Desktop\project2024>color 4

C:\Users\alame\OneDrive\Desktop\project2024>color 2

C:\Users\alame\OneDrive\Desktop\project2024>"C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe" -m virtualenv env2
created virtual environment CPython3.10.0.final.0-64 in 932ms
  creator CPython3Windows(dest=C:\Users\alame\OneDrive\Desktop\project2024\env2, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\alame\AppData\Local\pypa\virtualenv)
    added seed packages: pip==25.0.1, setuptools==75.8.0, wheel==0.45.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

C:\Users\alame\OneDrive\Desktop\project2024>cd env2

C:\Users\alame\OneDrive\Desktop\project2024\env2>cd Scripts

C:\Users\alame\OneDrive\Desktop\project2024\env2\Scripts>activate

(env2) C:\Users\alame\OneDrive\Desktop\project2024\env2\Scripts>cd..\..

(env2) C:\Users\alame\OneDrive\Desktop\project2024>"C:\Users\alame\AppData\Local\Programs\Python\Python310\Scripts\pip.exe" install mysqlclient==2.2.4
Collecting mysqlclient==2.2.4
  Downloading mysqlclient-2.2.4-cp310-cp310-win_amd64.whl (203 kB)
     |████████████████████████████████| 203 kB 819 kB/s
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.2.4
WARNING: You are using pip version 21.2.3; however, version 25.0.1 is available.
You should consider upgrading via the 'C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip' command.

(env2) C:\Users\alame\OneDrive\Desktop\project2024>pip install mysqlclient==2.2.4
Collecting mysqlclient==2.2.4
  Downloading mysqlclient-2.2.4-cp310-cp310-win_amd64.whl.metadata (4.6 kB)
Downloading mysqlclient-2.2.4-cp310-cp310-win_amd64.whl (203 kB)
Installing collected packages: mysqlclient
Successfully installed mysqlclient-2.2.4

(env2) C:\Users\alame\OneDrive\Desktop\project2024>pip install django==4.1
Collecting django==4.1
  Using cached Django-4.1-py3-none-any.whl.metadata (4.0 kB)
Collecting asgiref<4,>=3.5.2 (from django==4.1)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.2.2 (from django==4.1)
  Using cached sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from django==4.1)
  Using cached tzdata-2025.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting typing-extensions>=4 (from asgiref<4,>=3.5.2->django==4.1)
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Using cached Django-4.1-py3-none-any.whl (8.1 MB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
Using cached tzdata-2025.1-py2.py3-none-any.whl (346 kB)
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Installing collected packages: tzdata, typing-extensions, sqlparse, asgiref, django
Successfully installed asgiref-3.8.1 django-4.1 sqlparse-0.5.3 typing-extensions-4.12.2 tzdata-2025.1

(env2) C:\Users\alame\OneDrive\Desktop\project2024>cd turffinal

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>"C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe" manage.py runserver
Traceback (most recent call last):
  File "C:\Users\alame\OneDrive\Desktop\project2024\turffinal\manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\alame\OneDrive\Desktop\project2024\turffinal\manage.py", line 22, in <module>
    main()
  File "C:\Users\alame\OneDrive\Desktop\project2024\turffinal\manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>"C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe" -m manage.py runserver
C:\Users\alame\AppData\Local\Programs\Python\Python310\python.exe: Error while finding module specification for 'manage.py' (ModuleNotFoundError: __path__ attribute not found on 'manage' while trying to find 'manage.py'). Try using 'manage' instead of 'manage.py' as the module name.

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>pip list
Package           Version
----------------- -------
asgiref           3.8.1
Django            4.1
mysqlclient       2.2.4
pip               25.0.1
setuptools        75.8.0
sqlparse          0.5.3
typing_extensions 4.12.2
tzdata            2025.1
wheel             0.45.1

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>python manage.py runserver
C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\models\base.py:364: RuntimeWarning: Model 'tapp.turf' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\models\base.py:364: RuntimeWarning: Model 'tapp.turf' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
Watching for file changes with StatReloader
Performing system checks...

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
System check identified no issues (0 silenced).
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\mysql\base.py", line 247, in get_new_connection
    connection = Database.connect(**conn_params)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\MySQLdb\__init__.py", line 121, in Connect
    return Connection(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\MySQLdb\connections.py", line 195, in __init__
    super().__init__(*args, **kwargs2)
MySQLdb.OperationalError: (1049, "Unknown database 'gamevillage'")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\alame\AppData\Local\Programs\Python\Python310\lib\threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "C:\Users\alame\AppData\Local\Programs\Python\Python310\lib\threading.py", line 946, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\core\management\commands\runserver.py", line 137, in inner_run
    self.check_migrations()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\core\management\base.py", line 564, in check_migrations
    executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\migrations\executor.py", line 18, in __init__
    self.loader = MigrationLoader(self.connection)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\migrations\loader.py", line 58, in __init__
    self.build_graph()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\migrations\loader.py", line 235, in build_graph
    self.applied_migrations = recorder.applied_migrations()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\migrations\recorder.py", line 81, in applied_migrations
    if self.has_table():
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\migrations\recorder.py", line 57, in has_table
    with self.connection.cursor() as cursor:
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 323, in cursor
    return self._cursor()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 299, in _cursor
    self.ensure_connection()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 281, in ensure_connection
    with self.wrap_database_errors:
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\backends\mysql\base.py", line 247, in get_new_connection
    connection = Database.connect(**conn_params)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\MySQLdb\__init__.py", line 121, in Connect
    return Connection(*args, **kwargs)
  File "C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\MySQLdb\connections.py", line 195, in __init__
    super().__init__(*args, **kwargs2)
django.db.utils.OperationalError: (1049, "Unknown database 'gamevillage'")

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>python manage.py makemigrations
C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\models\base.py:364: RuntimeWarning: Model 'tapp.turf' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
No changes detected

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>python manage.py migrate
C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\models\base.py:364: RuntimeWarning: Model 'tapp.turf' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tapp
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying tapp.0001_initial... OK
  Applying tapp.0002_club_district_locations_package_payments_saleitem_and_more... OK

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>python manage.py runserver
C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\models\base.py:364: RuntimeWarning: Model 'tapp.turf' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
C:\Users\alame\OneDrive\Desktop\project2024\env2\lib\site-packages\django\db\models\base.py:364: RuntimeWarning: Model 'tapp.turf' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
Watching for file changes with StatReloader
Performing system checks...

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
System check identified no issues (0 silenced).
February 13, 2025 - 21:23:14
Django version 4.1, using settings 'turf.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[13/Feb/2025 21:23:20] "GET / HTTP/1.1" 200 33706
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/aos/aos.css HTTP/1.1" 200 26053
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/remixicon/remixicon.css HTTP/1.1" 200 110438
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/swiper/swiper-bundle.min.css HTTP/1.1" 200 15563
[13/Feb/2025 21:23:20] "GET /static/assets/css/style.css HTTP/1.1" 200 38921
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/aos/aos.js HTTP/1.1" 200 14690
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js HTTP/1.1" 200 78129
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/glightbox/js/glightbox.min.js HTTP/1.1" 200 56222
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/isotope-layout/isotope.pkgd.min.js HTTP/1.1" 200 35445
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/bootstrap-icons/bootstrap-icons.css HTTP/1.1" 200 73271
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/animate.css/animate.min.css HTTP/1.1" 200 71750
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/php-email-form/validate.js HTTP/1.1" 200 2731
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/waypoints/noframework.waypoints.js HTTP/1.1" 200 21112
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/glightbox/css/glightbox.min.css HTTP/1.1" 200 13785
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/swiper/swiper-bundle.min.js HTTP/1.1" 200 135617
[13/Feb/2025 21:23:20] "GET /static/assets/js/main.js HTTP/1.1" 200 4325
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/boxicons/css/boxicons.min.css HTTP/1.1" 200 63781
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/bootstrap/css/bootstrap.min.css HTTP/1.1" 200 163873
[13/Feb/2025 21:23:20] "GET /static/images/nextturf.jpg HTTP/1.1" 200 346967
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/bootstrap-icons/fonts/bootstrap-icons.woff2?a74547b2f0863226942ff8ded57db345 HTTP/1.1" 200 92004
[13/Feb/2025 21:23:20] "GET /static/assets/vendor/boxicons/fonts/boxicons.woff2 HTTP/1.1" 200 102988
[13/Feb/2025 21:23:20] "GET /static/assets/img/favicon.png HTTP/1.1" 200 491
[13/Feb/2025 21:23:25] "GET /static/images/players.jpg HTTP/1.1" 200 747679
[13/Feb/2025 21:23:30] "GET /static/images/turf1.jpg HTTP/1.1" 200 1066679

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>doskey /history > history.txt

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>. explorer
'.' is not recognized as an internal or external command,
operable program or batch file.

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>. explorer.exe
'.' is not recognized as an internal or external command,
operable program or batch file.

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>explorer .

(env2) C:\Users\alame\OneDrive\Desktop\project2024\turffinal>
```