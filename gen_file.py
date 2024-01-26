import random
import string
from time import perf_counter


FILES_TO_GEN = 30
def generate_text_file(size_in_mb, file_name):
    filename = f"/tmp/data/{file_name+1}.txt"
    # filename = f"files/{file_name+1}.txt"
    with open(f"{filename}", 'w') as file:
        random_text = ''.join(random.choices(string.ascii_letters + string.digits + '\n', k=size_in_mb * 1024 * 1024))
        file.write(random_text)

desired_size_mb = 100
for i in range(FILES_TO_GEN):
    generate_text_file(desired_size_mb, i)