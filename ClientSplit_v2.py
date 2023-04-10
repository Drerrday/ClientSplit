# Initialize variables
client_list = []
worker_names = ['basicuser']

# Get user input
workers = int(input("Enter how many people are monitoring clients(1-10): "))
for i in range(workers):
    data = input("Enter the name of worker {}: ".format(i+1))
    worker_names.append(data)

# Split client_list into chunks
if client_list:
    chunk_size = len(client_list) // workers
    Client_Split = [client_list[i:i+chunk_size] for i in range(0, len(client_list), chunk_size)]
else:
    Client_Split = [[] for i in range(workers)]

# Append final item to last chunk
final_item = 'WBK'
if Client_Split:
    if final_item not in Client_Split[-1]:
        Client_Split[-1].append(final_item)

# Print results
print('*' * 100)
for i in range(workers):
    print("Worker {}: {}".format(worker_names[i+1], Client_Split[i]))
print('*' * 100)

# Wait for user input
input("Hit Enter to end")
