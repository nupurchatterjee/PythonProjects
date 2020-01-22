# Request get and post
import requests
r=requests.get('https://xkcd.com/1906/')
print("Status code is {0}",r.status_code)
print("Header  is {0}",r.headers)


#Download an image using Request Response
import requests
receive=requests.get('https://imgs.xkcd.com/comics/making_progress.png')
with open(r'C:\Prosenjit\Nupur\image.png','wb') as f :
    f.write(receive.content)

