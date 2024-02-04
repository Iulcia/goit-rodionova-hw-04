""" This fnc calcutates total value and average for second row in input file (comma as separator) """

def total_salary(file_path):

    try:
        with open(file_path, "r", encoding = "utf-8") as fh:
        
            lines = [el.strip().split(',') for el in fh.readlines()] # remove blanks and separate values for list by comma

            if len(lines) == 0: # check if file is not not empty and prevent division by zero
                raise ValueError("Empty file")
            else:
                count = len(lines)

            total = 0
            for line in lines:
                total += float(line[1])

            average = round(total/count, 2)

            return total, average
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File with path {file_path} not found")
    
    except IndexError: # if not 2 columns in file
        raise IndexError(f"Check data structure of file {file_path}")
    
    except ValueError as e: # for non digital inputs
        raise ValueError(f"Check data types in file, {e} ")


