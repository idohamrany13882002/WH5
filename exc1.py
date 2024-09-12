# START
movie_length: int = int(input('enter movies length in minutes: '))
hours: int = movie_length // 60
min: int = movie_length % 60
if hours == 1:
    print(f'the movie is an hour and {min} minutes')
else:
    print(f'the movie is {hours} hours and {min} minutes long')
# END
