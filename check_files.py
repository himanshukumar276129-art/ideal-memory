import os
for root, dirs, files in os.walk('src'):
    for file in files:
        print(f"{root}/{file}")
