"""
Created by Hunter Elam
Python 3.9
IDE: IntelliJ
Nov. 20, 2020
"""

client_list = ['BGL',
               'BUTZ',
               'CANDD',
               'CANDT',
               'CANTEX',
               'CENSYN',
               'CRYE-LIEKE',
               'CUWI',
               'EAMC3',
               'EOC',
               'GLRM',
               'HPM',
               'JKV',
               'LAKEU',
               'LIGHTFOOT',
               'LP',
               'MANDK',
               'MBHB',
               'MTMARY',
               'NATION',
               'OLN',
               'PROGENITY',
               'RREOU',
               'SDF',
               'SNG',
               'SUSMAN',
               'THEO',
               'THOMCOB',
               'TM',
               'UB',
               'WBK',
               ]


# Chunking Function
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


# Real Action
worker_names = ['basicuser']
workers = int(input("Enter how many people are monitoring clients: "))
for i in range(1, workers + 1):
    data = input("Enter the name of worker {}: ".format(i))
    worker_names.append(data)
split = int(len(client_list) / workers)
Client_Split = (list(chunk_list(client_list, split)))   # Chunking the list

# Formatting
print('*' * 85)
print("Worker {}: ".format(worker_names[1]), Client_Split[0])
if workers == 2:
    Client_Split[1].append(Client_Split[2])
    print("Worker {}: ".format(worker_names[2]), Client_Split[1])
if workers == 3:
    print("Worker {}: ".format(worker_names[2]), Client_Split[1])
    Client_Split[2].append(Client_Split[3])
    print("Worker {}: ".format(worker_names[3]), Client_Split[2])
if workers == 4:
    print("Worker {}: ".format(worker_names[2]), Client_Split[1])
    print("Worker {}: ".format(worker_names[3]), Client_Split[2])
    Client_Split[3].append(Client_Split[4])
    print("Worker {}: ".format(worker_names[4]), Client_Split[3])
if workers == 5:
    print("Worker {}: ".format(worker_names[2]), Client_Split[1])
    print("Worker {}: ".format(worker_names[3]), Client_Split[2])
    print("Worker {}: ".format(worker_names[4]), Client_Split[3])
    Client_Split[4].append(Client_Split[5])
    print("Worker {}: ".format(worker_names[5]), Client_Split[4])
print('*' * 85)
input("Hit Enter to end")

# under the if statements is where you will need to make a change if program quits unexpectedly.
# This is due to the Chunking Function and can be fixed by commenting out or commenting out this.
# Client_Split[1].append(Client_Split[2])
