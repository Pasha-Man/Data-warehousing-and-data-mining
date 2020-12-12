import pyodbc

server = 'IBRAHIM\SQLEXPRESS01'
database = 'Assignment2'
username = 'pasha'
password = 'pasha'
cnxn = pyodbc.connect('Trusted_Connection=Yes;DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print("connected to database" + database)




def rollUpForYearAndQuat():
    print ('Reading data from table')
    tsql = "SELECT year,quater,SUM(dollars_sold) as TotalSales FROM dbo.TimeDimension, dbo.SalesFact group by rollup(year,quater);"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        print("year\tQuater\tTotal Sales\n")
        while row:
           
            print  ( str (row[0]) +"\t" + str (row[1]) + "\t"+ str (row[2]))
         
            row = cursor.fetchone()

def rollUpByCountCityState():
    print ('Reading data from table')
    tsql = "SELECT city,country,province_or_street,SUM(dollars_sold) as TotalSales FROM dbo.LocationDimension, dbo.SalesFact group by rollup(country,city,province_or_street);"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        print("Country\tCity\tProvince or street\ttotal sold")
        while row:
            print  ( str (row[0]) +"\t" + str (row[1]) + "\t"+ str (row[2]) + "\t" + str(row[3]) )
         
            row = cursor.fetchone()

def rollUPByBrandType():
    print('Reading data from Table')
    tsql = "SELECT brand,type,SUM(dollars_sold) as TotalSales FROM dbo.ItemDimension, dbo.SalesFact group by rollup(brand,type);"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        print("Brand\t Type\t Total sum")
        while row:
             print  ( str (row[0]) +"\t" + str (row[1]) + "\t"+ str (row[2]))
             row = cursor.fetchone()

def drillDownByDayMonth(): 
    print("Reading data from Table")
    tsql = "SELECT day,month,SUM(dollars_sold) as TotalSales FROM dbo.TimeDimension, dbo.SalesFact group by day,month;"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        print('Day\t Month\t Sum')
        while row:
             print  ( str (row[0]) +"\t" + str (row[1]) + "\t"+ str (row[2])) #there is a small issue where the month number are not sorted. the ones with 1 in them are written first and the rest follow.
             row = cursor.fetchone()

def drillDownByItemName():
    print('Reading data from Table')
    tsql = "SELECT item_name,SUM(dollars_sold) as TotalSales FROM dbo.ItemDimension, dbo.SalesFact WHERE dbo.ItemDimension.item_key=dbo.SalesFact.item_key group by item_name;"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        print('Item name\t Total sold')
        while row:
            print  ( str (row[0]) +"\t" + str (row[1]) )
            row = cursor.fetchone()

def drillDownByStreetOrProvince():
    print('reading data from table')
    tsql = "SELECT province_or_street,SUM(dollars_sold) as TotalSales FROM dbo.LocationDimension, dbo.SalesFact WHERE dbo.LocationDimension.location_key=dbo.SalesFact.location_key group by province_or_street;"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        print('province/street\tSum')
        while row:
                print  ( str (row[0]) +"\t\t" + str (row[1]))
        
                row = cursor.fetchone()
print('press 1 to request roll-up for total sales by year and by quater')
print('press 2 to request roll-up for total sales by Country, by City and by state')
print('press 3 to request roll-up for total sales by Brand and by Type')
print('press 4 to request drill down on total sales by Month and by Day')
print('press 5 to request drill down on total sales by Item name')
print('press 6 to request drill down on total sales by street address')
print('press 7 to quit')
print('Enter Choice:') 

userInput = str(input())
if( userInput == '1'):
    rollUpForYearAndQuat()
elif (userInput == '2'):
    rollUpByCountCityState()
elif (userInput == '3'):
    drillDownByDayMonth()
elif (userInput == '4'):
    drillDownByDayMonth()
elif (userInput == '5'):
    drillDownByItemName()
elif (userInput == '6'):
    drillDownByStreetOrProvince()
elif (userInput == '7'):
    print('Exiting')

