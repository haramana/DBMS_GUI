import datetime
data_ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def crea_file(path, data): 
    with open(path, 'a') as file:
        file.write(data_ora+"\n")
        for row in data:
            file.write(','.join(str(item) for item in row) + '\n')