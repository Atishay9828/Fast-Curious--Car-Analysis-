import pandas as pd

from GraphicalAnalysis.AccelerationvsMPG import get_acc_vs_mpg
from GraphicalAnalysis.CarsvsCompany import get_car_vs_company
from GraphicalAnalysis.CarsvsOrigin import get_car_vs_origin
from GraphicalAnalysis.HorsePowervsMPG import get_hp_vs_mpg
from GraphicalAnalysis.ModelvsHorsePower import get_model_vs_hp
from GraphicalAnalysis.ModelvsMPG import get_model_vs_mpg
from GraphicalAnalysis.WeightvsDisplacement import get_weight_vs_displacement
from GraphicalAnalysis.CylindervsOrigin import get_cylinder_vs_origin

A = pd.read_csv('DataFrames/Cars1.csv',index_col = 0)
A = pd.DataFrame(A)
B = pd.read_csv('DataFrames/Cars2.csv',index_col = 0)
B = pd.DataFrame(B)
C = pd.read_csv('DataFrames/Cars3.csv',index_col = 0)
C = pd.DataFrame(C)
All = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
dict1 = {'family':'Comic Sans MS','color':'c','size':'15','weight':'bold'}
dict2 = {'family':'French Script MT','color':'r','size':'25','weight':'bold'}   



print('Welcome user ! ' )
print('This program will help you run various types of analysis on Cars' )
print('This data mainly tell us about hardware specifications about various cars' )
print('The project has been completed with 3 CSV files' )
print('The data has been taken from https://perso.telecom-paristech.fr' )
print('The First File contains data of : Cars,MPG,Displacement,Model,Origin' )
print('The Second File contains data of : Cars,HorsePower,Acceleration,Weight,Cylinders' )
print('The Third File contains data of : Cars, Model, Origin ' )


print()
print('This Program can carry out following Analysis on this data :' )
print()


print()
print()




while True:


    print('----------------------------------------------------------')
    print( 'MAIN MENU :' )

    print('1) To display The Dataframes' )
    print('2) For Graphical Analysis'    )
    print('3) For Textual Analysis'      )
    print('4) To Exit !'                 )


    print('----------------------------------------------------------')
    print()

    Choice = int(input('Please enter the corresponding Number from the main menu to do the necessary operation on this data : ' ))
    if Choice == 1 :
        while True :

            print('DataFrame Menu: ' )


            print('1) For Performance Specs' )
            print('2) For Hardware Specs'    )
            print('3) For Origin Details'    )
            print('4) To Exit !'             )

            print('----------------------------------------------------------')
            print()


            print('Please enter the corresponding Number form the Dataframe menu to do the necessary operation on this data : ' )
            Choice = int(input())


            print()
            print()
            print()

            if Choice   == 1 :
                print(tb.tabulate(A, headers='keys', tablefmt='psql'))
                print()

            elif Choice == 2 :
                print(tb.tabulate(B, headers='keys', tablefmt='psql'))
                print()

            elif Choice == 3 :
                print(tb.tabulate(C, headers='keys', tablefmt='psql'))
                print()

            elif Choice == 4 :
                break             


            print()
            print('----------------------------------------------------------')

    elif Choice == 2 :
        while True :            
            print('Graphical Analysis Menu:  ')

            print('1) Acceleration vs MPG    ')
            print('2) Cars vs Company        ')
            print('3) Cars vs Origin         ')
            print('4) HorsePower vs MPG      ')
            print('5) Model vs HorsePower    ')
            print('6) Model vs MPG           ')
            print('7) Weight vs Displacement ')
            print('8) Cylinder vs Origin     ')
            print('9) To Exit !              ')


            print('Please enter the corresponding Number from the Graph menu to do the necessary operation on this data : ' )    
            Choice = int(input())

            print()
            print()
            print()

            if Choice == 1 :
                get_acc_vs_mpg()
                
            elif Choice == 2 :
                get_car_vs_company()

            elif Choice == 3 :
                get_car_vs_origin()

            elif Choice == 4 :
                get_hp_vs_mpg()

            elif Choice == 5 :
                get_model_vs_hp()

            elif Choice == 6 :
                get_model_vs_mpg()

            elif Choice == 7 :
                get_weight_vs_displacement()
                
            elif Choice == 8 :
                get_cylinder_vs_origin()

            elif Choice == 9 :
                break

    elif Choice == 3 :
        print('----------------------------------------------------------')

        while True :
            
            print('----------------------------------------------------------')

            print('Textual Analysis Menu:                            ')
            print()
            print('1)Different Company Names                         ')
            print('2)Different regions data is collected form        ')
            print('3)Different Number of cylinders                   ')
            print('4)Year over which analysis is done                ')
            print('5)No.of cars by specific companies                ')
            print('6)Highest & Lowest Acceleration                   ')
            print('7)Region with highest no of car model released    ')
            print('8)Average weight of cars                          ')
            print('9)TOP 5 MPG of different car companies !          ')
            print('10)Total No. of car models released acc to origin ')
            print('11)Average displacement by using mean             ')
            print('12)No. of cars released from 70-76                ')
            print('13)Highest & Lowest HorsePower                    ')
            print('14)No. of cars released from 76-82                ')
            print('15) To Exit !!                                    ')


            print('----------------------------------------------------------')
            print('Please enter the corresponding Number form the Dataframe menu to do the necessary operation on this data : ' )
            Choice = int(input())
            print()

            print()

            print()

            if Choice   == 1 :
                print('The different Company names are as Follows : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                b = []
                d = []
                for x in A['Car']:
                    b.append(x)
                    c = len(b)
                for x in b:
                    c = str(x.split()[0])
                    d.append(c)
                A['Company'] = d
                CName = A['Company'].unique()
                print(CName)

            elif Choice == 2 :
                print('The different regions from which data is being compared are : ')                
                A = pd.read_csv('cars.csv' , sep = ';' , skiprows = [1] )
                Country = A['Origin'].unique()                
                print(Country)
                
            elif Choice == 3 :
                print('The Different Number of cylinders seen in cars are : ')
                C = []
                D = []
                A = pd.read_csv('cars.csv' , sep = ';' , skiprows = [1] )
                Country = A['Origin'].unique()
                Cylinders = A['Cylinders'].unique()
                print(Cylinders)

            elif Choice == 4 :
                print('The Year range over which analysis is done : ')
                B=[]
                D=[]
                for x in A['Car']:
                    C = str(x.split()[0])
                    D.append(C)                      
                A['Company'] = D
                CName = A['Company'].value_counts()
                F = A['Model'].value_counts() 
                Year = A['Model'].unique()
                print(Year)
                
            elif Choice == 5 :
                print('The different number of Car Models made by different Companies are : ')
                D=[]
                for x in A['Car']:
                    C = str(x.split()[0])
                    D.append(C)
                A['Company'] = D
                CName = A['Company'].value_counts()
                print(CName)

            elif Choice == 6 :
                print('The Highest & Lowest Acceleration observed : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                A = A.sort_values(by = ['Acceleration'],ascending = False)
                pd.set_option("display.max_columns", None)
                print(A.head(1))
                print(A.tail(1))

            elif Choice == 7 :
                print('The regions from where most car models were released : ')
                A = pd.read_csv('cars.csv' , sep = ';' , skiprows = [1] )
                C = []
                Country = A['Origin'].unique()
                for x in Country :
                    B = len(A[A['Origin'] == x ])
                    C.append(B)
                print('US', max(C))

            elif Choice == 8 :
                print('The average weight of cars is as follows : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                print(A[['Weight']].mean())

            elif Choice == 9 :
                print('The highest 5 MPG of Cars are : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                A = A.sort_values(by = ['MPG'],ascending = False)
                print(A.head())

            elif Choice == 10 :
                print('The Total Number of cars realeased form each respective region are : ')
                A = pd.read_csv('cars.csv' , sep = ';' , skiprows = [1] )
                C = []
                Country = A['Origin'].unique()
                for x in Country :
                    B = len(A[A['Origin'] == x ])
                    C.append(B)
                print('US', C[0])
                print('Europe', C[1])
                print('Japan', C[2])

            elif Choice == 11 :
                print('The average displacement across all cars are as follows : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                print(A[['Displacement']].mean())

            elif Choice == 12 :
                print('The total No of cars released from 1970 - 76 are : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                F = A['Model'].value_counts()                
                F = F.drop( labels=[77,78,79,80,81,82] )
                F = F.reindex(index = [70,71,72,73,74,75] )                
                print(F)
                
            elif Choice == 13 :
                print('The highest & Lowest Horsepower acrss all cars are as follows : ')
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                A = A.sort_values(by = ['Horsepower'],ascending = False)
                pd.set_option("display.max_columns", None)
                print(A.head(1))
                print(A.tail(1))
                
            elif Choice == 14 :
                print('The total No of cars released from 1976 - 82 are : ')
                B=[]
                D=[]
                A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
                for x in A['Car']:
                    C = str(x.split()[0])
                    D.append(C)                      
                A['Company'] = D
                CName = A['Company'].value_counts()
                F = A['Model'].value_counts()
                F = F.drop( labels=[70,71,72,73,74,75] )
                F = F.reindex(index = [77,78,79,80,81,82])
                print(F)

            elif Choice == 15 :
                break

    elif Choice == 4 :
        print('The End !' )
        break






