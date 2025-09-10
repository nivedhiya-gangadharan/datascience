a={"inception","up","inside-out","intestellar","her"}
b={"madahascar","superman","spiderman","up","inside-out"}
common_movies=list(set(a)&set(b))
unique_a_movies=list(set(a)-set(b))
unique_b_movies=list(set(b)-set(a))
print("movies common to the set:",common_movies)
print("unique movies that a watched",unique_a_movies)
print("sujested movies for user a based on user b's watched list",unique_b_movies)