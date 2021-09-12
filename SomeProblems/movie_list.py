fav_movie = []

while True:
    print('Movie No. ' + str(len(fav_movie)+1) + ' or press ENTER to stop adding to the list.')
    movie = input()

    if movie == '':
       break

    fav_movie = fav_movie + [movie]

if len(fav_movie) != 0:
    print('The lists are: ')
    for i in range(len(fav_movie)):
        print(str(i+1) + '. ' + fav_movie[i])
