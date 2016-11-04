import os

for entry in os.listdir('.'):
  if os.path.isdir(entry) and not entry.startswith('.'):
    os.system('cd {} && git pull && cd ..'.format(entry))

