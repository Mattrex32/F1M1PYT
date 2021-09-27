Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 3*10
30
>>> 100 -10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10//3
3
>>> 
>>> print(Adnan)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(Adnan)
NameError: name 'Adnan' is not defined
>>> naam = "Adnan"
>>> print(naam)
Adnan
>>> print(naam.upper())
ADNAN
>>> 
>>> print(naam[::-1])
nandA
>>> print(naam[0:2])
Ad
>>> 
>>> leeftijd = 18
>>> print('Hallo' + naam + 'jij ben al' + leeftijd)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('Hallo' + naam + 'jij ben al' + leeftijd)
TypeError: can only concatenate str (not "int") to str
>>> print('Hallo' + naam + 'jij ben al' + str(leeftijd))
HalloAdnanjij ben al18
>>> print('Hallo ' + naam +' jij ben al ' + str(leeftijd))
Hallo Adnan jij ben al 18
>>> leeftijd = leeftijd+1
>>> leeftijd
19
>>> leeftijd-=1
>>> leeftijd
18
>>> 
>>> if leeftijd <18:
	hoelang_tot18jaar = 18 - leeftijd
	print ('over' +str(hoelang_tot18jaar) + 'jaar wordt je 18')
    elif leeftijd > 18:
	    hoelang_al18jaar = leeftijd - 18
	    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd -)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    
SyntaxError: unindent does not match any outer indentation level
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')

Je bent precies 18 jaar
>>> from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

SyntaxError: multiple statements found while compiling a single statement
>>> from random import randint
>>> randit(0,1000)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    randit(0,1000)
NameError: name 'randit' is not defined
>>> from random import randint
>>> randint(0,1000)
262
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
362
>>> print("willekeurig getal tussen 0 en 1000: " + str(willekeurig_getal))
willekeurig getal tussen 0 en 1000: 362
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-09-27 12:27:36.586328
>>> 2021-09-27 12:27:36.586328
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> datum.strftime("%A %d %B %Y")
'Monday 27 September 2021'
>>> 
>>> import locale
>>> locale.setlocale(locale.LC_TIME, "nl_Nl")
'nl_Nl'
>>> datum
datetime.datetime(2021, 9, 27, 12, 27, 36, 586328)
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'maandag 27 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime("%A %d %B %Y")
'lunedì 27 settembre 2021'
>>> datum.now()
datetime.datetime(2021, 9, 27, 12, 34, 32, 139005)
>>> locale.setlocale(locale.LC_TIME, 'SYR_syr')
'Syriac_Syria.utf8'
>>> datum.strftime("%A %d %B %Y")
'Ü¬ÜªÜ\x9dÜ¢Â\xa0Ü’Ü«Ü’Ü\x90 27 Ü\x90Ü\x9dÜ\xa0Ü˜Ü\xa0 2021'
>>> 