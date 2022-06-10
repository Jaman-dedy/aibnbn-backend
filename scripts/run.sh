 #!/bin/bash
 
 python3 manage.py runserver 0.0.0.0:${port:-8000} --nothreading