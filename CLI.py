#comment this out before submitting to mimir
# file = open("CSV.txt", 'r')
# def input(prompt=''):
#     print(prompt, end='')
#     return file.readline().strip()

import DBManager
import FileManager

class CLI:
    
    def __init__(self, dbm, fm):
        
        self.dbm = dbm
        self.fm = fm
           

    def run_cli(self):
        #global cars
    
        while(1):
            inp = input()
            tokens = inp.split(" ")
            cmd = tokens[0]
    
            if cmd == "create":
                if len(tokens) == 6:
                    self.dbm.create(tokens[1], tokens[2], tokens[3], tokens[4], tokens[5])
                elif len(tokens) == 5:
                    self.dbm.create(tokens[1], tokens[2], tokens[3], tokens[4])
                else:
                    print("cannot create - missing or invalid parameter(s)")
        
            elif cmd == "update":
                self.dbm.update(tokens[1], tokens[2], tokens[3])
        
            elif cmd == "select_all":
                self.dbm.select_all()
            
            elif cmd == "select":
                try:
                    self.dbm.select(tokens[1], tokens[2])
                except IndexError:
                    print("cannot select - missing or invalid parameter(s)")
                
            elif cmd == "select_by_id":
                try:
                    self.dbm.select_by_id(tokens[1])
                except IndexError:
                    print("cannot select - missing or invalid parameter(s)")
            
            elif cmd == "print_selection":
                self.dbm.print_selection()
                
            elif cmd == "delete":
                self.dbm.delete_car(tokens[1])
        
            elif cmd == "exit":
                break
            
            elif cmd == "load_csv":
                self.fm.load_csv(tokens[1])
                
            elif cmd == "save_csv":
                self.fm.save_csv(tokens[1])
                
            elif cmd == "reset":
                self.dbm.data.clear()
                self.dbm.selection.clear()
            
            else:
                print("invalid command")
            pass
        
        #print(cars[1])
        
        
        
def main():
    dbm = DBManager.DBManager()
    fm = FileManager.FileManager(dbm)
    
    cli = CLI(dbm, fm)
    cli.run_cli()
    
    
main()



