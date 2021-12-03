class DBManager:
    
    def __init__(self): #constructor
        self.data={}
        self.selection={}
        
    
    def create(self, ID, make, model, year, body=""):
        car = {
            "ID" : ID,
            "Make" : make,
            "Model" : model,
            "Year" : year,
            "Body-type" : body,
            }
    
        self.data[ID] = car
        
        #testing
        #print("created car with id", ID)
        
    
    def select(self, attr, val):
        #global selection
        #print("selected", attr, val)
        
        new_selection = {}
    
        for ID, car in self.data.items():
            if attr in car:
                if car[attr] == val:
                    new_selection[ID] = car
            else:
                print("select - no cars match that selection")
                return
        
        print("selecting", attr, val)
            
        self.selection = new_selection
        
        
    def update(self, ID, attr_name, val):
        car = self.data[ID]
    
        car[attr_name] = val
        
        
    def delete_car(self, ID):
        
        if ID in self.data:
            print("deleted", ID)
            self.data.pop(ID)
            self.selection.pop(ID)
        else:
            print("cannot delete - car", ID, "not found")
            
            
    def print_selection(self):
        
        if len(self.selection) == 0:
            print("print selection - no items selected")
            return
            
        print("printing selection:")
        
        for ID, car in self.selection.items():
            #print("printing selection:")
            print(ID)
        
            for key, val in car.items():
                print("\t", key, ":", val)
        
            print()

            
            
    def select_all(self):
        #global selection
        self.selection = self.data
        
        
    def select_by_id(self, ID):
        #global selection
        
        try:
            car = self.data[ID]
            self.selection = {ID: car}
            print("selected car with id", ID)
        except:
            print("cannot select - car", ID, "not found")
        
        
        
        