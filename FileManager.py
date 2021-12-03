class FileManager:
    
    def __init__(self, dbm):
        self.dbm = dbm
        self.cars = {}
    
    
    def load_csv(self, file):
        print("loading csv", file)
        
        with open(file, 'r') as infile:
            
            line_num = 0
            
            for line in infile: #load_csv cars.csv
                
                if line_num == 0:
                    keys = line.strip().split(',')
                    
                    for x in range(len(keys)):
                        keys[x] = keys[x].replace(' ', '-')
                    
                else:
                    vals = line.strip().split(',')
                    
                    car = {}
                    
                    for x in range(len(keys)):
                        car[keys[x]] = vals[x]
                    
                    ID = car['ID']
                    
                    if ID.isnumeric():
                        self.dbm.create(
                            car['ID'],
                            car['Make'],
                            car['Model'],
                            car['Year'],
                            car['Body-type'],
                            )
                
                line_num += 1
                
                if line_num == 100:
                    break
                
    
    
    def save_csv(self, file_name):
        print("saving csv", file_name)
        
        with open(file_name, 'w') as file:
        
            file.write("ID,Make,Model,Year,Body-type\n")
            for car in self.dbm.selection.values():
                vals = []
                for val in car.values():
                    vals.append(val)
                
                vals[2] = vals[2].replace(' ', '-')
                file.write(','.join(vals))
                file.write('\n')
        
        pass
                

if __name__ =="__main__":
    fm = FileManager()
    #fm.load_csv("cars.csv")