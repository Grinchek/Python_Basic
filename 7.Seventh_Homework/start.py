import subprocess
import os

my_url = input('Paste the url:')
subprocess.run(f'yt-dlp {my_url} -F ', shell=False)
my_format = (input('Enter a number of format:'))

os.chdir("Downloads")

subprocess.run(f'yt-dlp -c {my_format} {my_url}', shell=False)
