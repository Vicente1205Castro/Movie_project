import requests

def buscar_peliculas(nombre_pelicula):
    api_key = '1e464630617e4408ebd290e882b5ade7'
    base_url = 'https://api.themoviedb.org/3'
    endpoint = '/search/movie'
    url = f'{base_url}{endpoint}?api_key={api_key}&query={nombre_pelicula}'
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json()['results']
        if resultados:
            print("Películas encontradas:")
            for pelicula in resultados:
                print(f"Título: {pelicula['title']}, ID: {pelicula['id']}")
        else:
            print("No se encontraron películas con ese nombre.")
            # Si no se encuentra ninguna película, pedir al usuario nuevamente el nombre
            nombre_pelicula = input("Ingrese el nombre de la película (o 'q' para salir): ")
            if nombre_pelicula.lower() != 'q':
                buscar_peliculas(nombre_pelicula)
    else:
        print("Hubo un error al realizar la solicitud a la API.")

def main():
    nombre_pelicula = input("Ingrese el nombre de la película (o 'q' para salir): ")
    if nombre_pelicula.lower() != 'q':
        buscar_peliculas(nombre_pelicula)

if __name__ == "__main__":
    main()
