# Matura
Program for analyzing matura's results.  

## Get started
Python 3.6 or 3.7

Copy repository on your local machine. You can use the following git command:
git clone https://github.com/kirsie/Matura.git

To get started with program, run the following in a virtual environment:
pip install requests

## Usage
### General using 
To run program you need to open virtual environment and run command:
python matura.py + Choosen command line arguments

### Available arguments:
-w --wojewodztwo {state}
-p --plec {m} or {k}
-s --srednia {year}
-z --zdawalnosc
-n --najlepsze {year}
-r --regresja
-x {state}
-y {state}
-l --lokalne

### Counting average number of student taking exam for a given state from 2010 to specified year:
for example:
Average in years 2010-2015 in Pomorskie for all:
python matura.py --srednia 2015 --wojewodztwo Pomorskie

Average in years 2010-2015 in Pomorskie for women:
python matura.py -s 2015 -w Pomorskie -p k

### Counting average number of student taking exam for a given state from 2010 to specified year:
for example:
Average in years 2010-2015 in Pomorskie for all:
python matura.py --srednia 2015 --wojewodztwo Pomorskie

Average in years 2010-2015 in Pomorskie for women:
python matura.py -s 2015 -w Pomorskie -p k

### Counting pass rate of a given state:
for example:
Pass rate for Pomorskie for all:
python matura.py --zdawalnosc -wojewodztwo Pomorskie

Pass rate for Pomorskie for men:
python matura.py -z -w Pomorskie -p m

### Counting best state in given year
Best state in 2010 for all:
python matura.py -n 2010

Best state in 2010 for men:
python matura.py --najlepsze --plec m

### Compare two states:
for example:
python matura.py -x Pomorskie -y Opolskie

python matura.py -x Pomorskie -y Opolskie -p m

### Show regression:
python matura.py -r 

python matura.py -r -p m

### Additional argument --lokalnie
When you add --lokalnie or -l to your command line argument, program will use data from your local disk (if data base exist), or
it will create local data base from remote data and then use it.

### Summary:
I'd realized all of tasks even bonuses ones.

