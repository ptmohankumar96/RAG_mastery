from libs.preprocess import preprocessing_input

def search_command(data,search):
    results = []
    for movie in data["movies"]:
        movie_flag = False
        for q in preprocessing_input(search):
            for t in preprocessing_input(movie["title"]):
                if q in t:
                    movie_flag = True
        if movie_flag:
            results.append(movie)
    results.sort(key=lambda m: m["id"])
    results = results[:5]
    return results