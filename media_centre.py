import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","The story of a boy whose toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=SgoiKLFBA3Q")

annable_two = media.Movie("Annabelle 2","Former toy maker Sam Mullins and his wife, Esther, are happy to welcome a nun and six orphaned girls into their California farmhouse.",
                        "https://upload.wikimedia.org/wikipedia/en/0/08/Annabelle_Creation.jpg",
                        "https://www.youtube.com/watch?v=EjZkJa6Z-SY")

avatar_movie = media.Movie("Avatar","On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved.",
                        "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")
                        
movies = [toy_story, annable_two, avatar_movie]

fresh_tomatoes.open_movies_page(movies)
