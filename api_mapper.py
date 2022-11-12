import argparse
import xml.etree.ElementTree as ET
import os.path


parser = argparse.ArgumentParser(description='Make markdown of the API from burp history')

def file_choices(choices,fname):
    ext = os.path.splitext(fname)[1][1:]
    if ext not in choices:
       parser.error("file doesn't end with {}".format(choices))
    return fname

parser.add_argument('-f',"--file",metavar="file",type=lambda s:file_choices(("xml"),s))  
parser.add_argument("-path",help="path to api",dest="path",default="/api")
args = parser.parse_args()


def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    path=args.path
    api_path=None
    for item in root.findall('item'):
        method=""
        for tags in item:
            if tags.tag =="method":
                method = tags.text
                #print(tags.text)
            if tags.tag == "path":
                if path in tags.text:
                    api_path=tags.text

                if api_path in data:
                    data[api_path].add(method)
                else:
                    data[api_path]={method}
    
    print(data.pop(None))
    return data

def print_line(i, req_methods, path):
    print("{} {} `{}`".format(i*'#', req_methods, path))
 
def create_markdown(data):
    levels = []
    for path in sorted(data):
        for i, lvl in enumerate(path.split('/')):
            if i == 0:
                continue
            split = path.split('/')
            req_methods = " "
            if len(split) == i+1:
                for method in data[path]:
                    req_methods += method + ' , '
                req_methods = req_methods[:-1]
            if len(levels) < i:
                levels.append(lvl)
                print_line(i, req_methods, lvl)
            elif levels[i-1] != lvl:
                levels[i-1] = lvl
                print_line(i, req_methods, lvl)

def main():
    #parser = argparse.ArgumentParser(description='Make markdown of the API from burp history')
    #parser.add_argument('-f', "--file", metavar="file", help='input as XML')
    data = {}
    #print(args.file)
    data = parse_xml(args.file)
    #print(data)
    create_markdown(data)




if __name__ == '__main__':
    main()