<<<<<<< HEAD
from django.test import TestCase
from datetime import datetime

strDate='24/10/2021'
date = datetime.strptime(strDate, '%d/%m/%Y')
=======
from django.test import TestCase
from datetime import datetime

strDate='24/10/2021'
date = datetime.strptime(strDate, '%d/%m/%Y')
>>>>>>> ff6a3c90b9141ef6edc7254235d24cf57f2487b3
print (date, strDate)