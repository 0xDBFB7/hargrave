
def save_file():
    # what if the program exits early? we want to save the output log... 
    # need some kind of finally check?

    files = {'upload_file': open('file.txt','rb')}
    values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

    r = requests.post(url, files=files, data=values)

