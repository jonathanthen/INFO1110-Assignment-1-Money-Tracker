def process_file(file_name):
    income = []
    expense = []
    i = 0
    
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        raise ValueError("Error: String does not represent a valid file!")
    
    for line in f:
        if i == 0 or i % 2 == 0:
            line_strip = line.rstrip("\n")
            line_strip = float(line_strip)
            income.append(line_strip)
            i += 1
        elif i == 1 or i % 2 == 1:
            line_strip = line.rstrip("\n")
            line_strip = float(line_strip)
            expense.append(line_strip)
            i += 1
            
    f.close()
    inc_exp = (income,expense)
    return (inc_exp)