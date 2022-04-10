import sys

args = sys.argv # e.g. python init.py 'index.html'

command = args[1]

if command=='make': 
    file = args[2]

    if file.split('.')[1] =='html': 
        with open(file, 'w') as f: 

            html_dir = './resources/html/'

            start = [r'<!DOCTYPE html>',r'<html>'] 
            with open(html_dir+'header_temp.html', 'r') as file:
                for i in file: 
                    start.append(i)            

            body = []
            with open(html_dir+'body_temp.html', 'r') as file: 
                for i in file: 
                    body.append(i)

            end = [r'</html>']

            for command in start+body+end: 
                f.write(command.replace('\n','')+'\n')

elif command=='update': 
    file = args[2]
