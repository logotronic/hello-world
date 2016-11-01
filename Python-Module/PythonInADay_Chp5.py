Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name="Guido"
>>> print name[0]
G
>>> print name.upper()
GUIDO
>>> print name.lower()
guido
>>> print.name.capitalize()
SyntaxError: invalid syntax
>>> print name.capitalize()
Guido
>>> date="11/12/2013"
>>> 
>>> #Go through string and splite
>>> #where there is a '/'
>>> date_manip=date.split('/')
>>> #Shot the outcome
>>> print date_manip
['11', '12', '2013']
>>> print date_manip[0]
11
>>> print date_manip[1]
12
>>> print date_manip[2]
2013
>>> print 'Month: ' + date_manip[0]
Month: 11
>>> print 'Day: ' + date_manip[1]
Day: 12
>>> print 'Year: ' + date_manip[2]
Year: 2013
>>> print ('Month: '+ date_manip[0] +
	       'Day: '+ date_manip[1] +
	       'Year: '+ date_manip[2])
Month: 11Day: 12Year: 2013
>>> print ('Month: '+ date_manip[0] +
	       ' Day: '+ date_manip[1] +
	       ' Year: '+ date_manip[2])
Month: 11 Day: 12 Year: 2013
>>> print ('Month: '+ date_manip[0] +
	       '. Day: '+ date_manip[1] +
	       '. Year: '+ date_manip[2])
Month: 11. Day: 12. Year: 2013
>>> 
