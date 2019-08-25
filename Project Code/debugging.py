import pafy
url = 'https://www.youtube.com/watch?v=3-0-81q-fGo'
video = pafy.new(url)
print(video.title)