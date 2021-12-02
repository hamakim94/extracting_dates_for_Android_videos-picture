# Extracting Dates for Android Videos & Pictures by using Python

- To be honest, it's super short code for easy editing videos & pictures

- When we take photos & videos, we use different application for better picture & video.

- When we edit these, we want to see these files in timeline(time order, **ESPECIALLY ME!**)



- I found that all the name of the photo/video has numbers of Date & Time

  ​	ex) DJI_20210924_170031_13_video.mp4,20210927_104158.jpg  etc..

- By using regular expression, this code only extracts numbers from name of file and make it to file, which makes easier for editing 

### Several things you must do

1. You must copy and paste orignal folder, this is **super important**!

2. You must put your videos/pictures folder's route

~~~python
file_path = 'F:/사진/동유럽/빈'       # must put your file route
~~~

3. If your length of file's extension is more than 3, you must adjust the numbers in the code. 

~~~ python
ext = src[-4:] # this code is example for extracting extension from .jpg, .mp4
~~~

#### This only works for Android phone in Window

- IPhone photo's names looks like 1632727390822-3.jpg in Window..

### you can see more in https://www.youtube.com/watch?v=ylwBo1XZiNk&ab_channel=%EA%B9%80%EC%A3%BC%EA%B4%80

