""" This fnc transforms lines from file into list of dictionaries with keys: id, name, age """

def get_cats_info(file_path):

    try:
        with open(file_path, "r", encoding = "utf-8") as fh:
            cats = []      
            lines = [el.strip().split(',') for el in fh.readlines()] # remove blanks and separate values for list by comma

            if len(lines) == 0:
                    raise ValueError("Empty file") # check if file is not not empty
            
            for line in lines:
                cats.append({"id": line[0], "name": line[1], "age": line[2]}) # add each value of list into dictionary with keys: id, name, age
                
        return cats
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File with path {file_path} not found")
    
    except IndexError:
        raise IndexError(f"Check data structure of file {file_path}")
    
    except ValueError as e:
        raise ValueError(f"Check data types in file, {e} ")