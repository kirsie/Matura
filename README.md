# Matura
Program for analyzing matura's results.  
All tasks have been completed (bonuses also)  
## Get started
- Python 3.6 or 3.7  

- Internet connection for remote data. (u can use --lokalne argument to create data base on your local machine, then u can   use program without internet connection: more info below about --lokalne)  

- Copy repository on your local machine. You can use the following git command:  
*git clone https://github.com/kirsie/Matura.git*

- To get started with program, run the following in a virtual environment:  
*pip install requests*

## Usage
### General using:
To run program you need to open virtual environment and run command:  
*python matura.py + Choosen command line arguments*

### Available arguments:
- -w --wojewodztwo {state}  
- -p --plec {m} or {k}  
- -s --srednia {year}  
- -z --zdawalnosc  
- -n --najlepsze {year}  
- -r --regresja  
- -x {state}  
- -y {state}  
- -l --lokalne  

### Counting average number of students:
for example:  
Average in years 2010-2015 in Pomorskie for all:    
*python matura.py --srednia 2015 --wojewodztwo Pomorskie*  

Average in years 2010-2015 in Pomorskie for women:    
*python matura.py -s 2015 -w Pomorskie -p k*

### Counting pass rate of a given state:
for example:  
Pass rate for Pomorskie for all:    
*python matura.py --zdawalnosc -wojewodztwo Pomorskie*  

Pass rate for Pomorskie for men:    
*python matura.py -z -w Pomorskie -p m*  

### Counting best state in given year
Best state in 2010 for all:    
*python matura.py -n 2010*   

Best state in 2010 for men:*    
*python matura.py --najlepsze 2010 --plec m*  

### Compare two states:
*python matura.py -x Pomorskie -y Opolskie*  

*python matura.py -x Pomorskie -y Opolskie -p m*  

### Show regression:
python matura.py -r*  

python matura.py -r -p m*  

### Additional argument --lokalne
When you add --lokalne or -l to your command line arguments, program will use data from your local disk if **matura.db** file exist, if not program will create local data base from remote data, store it in **matura.db** file and then use it. 
 

