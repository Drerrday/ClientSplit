"""
Created by Hunter Elam
Python 3.9
IDE: IntelliJ
Nov. 20, 2020
"""
# List does not contain contents
client_list = []


# Chunking Function
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


# Real Action
worker_names = ['basicuser']
workers = int(input("Enter how many people are monitoring clients(1-10): "))
for i in range(1, workers + 1):
    data = input("Enter the name of worker {}: ".format(i))
    worker_names.append(data)
split = int(len(client_list) / workers)
Client_Split = (list(chunk_list(client_list, split)))   # Chunking the list
final_item = 'WBK'

# Formatting
print('*' * 100)
print("Worker {}: ".format(worker_names[1]), Client_Split[0])
if workers == 2:
    if final_item not in Client_Split[1]:
        Client_Split[1].append(Client_Split[2])
    print("Worker {}: ".format(worker_names[2]), Client_Split[1])
if workers == 3:
    if final_item not in Client_Split[2]:
        Client_Split[2].append(Client_Split[3])
    for i in range(1, 3):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 4:
    if final_item not in Client_Split[3]:
        Client_Split[3].append(Client_Split[4])
    for i in range(1, 4):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 5:
    if final_item not in Client_Split[4]:
        Client_Split[4].append(Client_Split[5])
    for i in range(1, 5):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 6:
    if final_item not in Client_Split[5]:
        Client_Split[5].append(Client_Split[6])
    for i in range(1, 6):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 7:
    if final_item not in Client_Split[6]:
        Client_Split[6].append(Client_Split[7])
    for i in range(1, 7):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 8:
    if final_item not in Client_Split[7]:
        Client_Split[6].append(Client_Split[8])
        Client_Split[7].append(Client_Split[9])
    for i in range(1, 8):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 9:
    if final_item not in Client_Split[8]:
        Client_Split[8].append(Client_Split[9])
    if final_item not in Client_Split[9]:
        Client_Split[8].append(Client_Split[10])
    for i in range(1, 9):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
if workers == 10:
    if final_item not in Client_Split[9]:
        Client_Split[9].append(Client_Split[10])
    for i in range(1, 10):
        print("Worker {}: ".format(worker_names[i + 1]), Client_Split[i])
print('*' * 100)
input("Hit Enter to end")

#TIP: var final_item should always equal the last item in the list client_list.
