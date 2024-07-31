import csv


def reportcsv(header,data,name):
    with open(name+".csv",'w') as file:
        content=csv.writer(file)
        content.writerow(header)
        for i in data:
            content.writerow(i)
    print("\n",name,".csv has been generated successfully!!")
    
