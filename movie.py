import os
import boto3
import json
import requests

def buscar_peliculas_lambda(nombre_pelicula):
    api_key = os.environ.get('TMDB_API_KEY')
    base_url = 'https://api.themoviedb.org/3'
    endpoint = '/search/movie'
    url = f'{base_url}{endpoint}?api_key={api_key}&query={nombre_pelicula}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        return None

def buscar_peliculas(nombre_pelicula):
    resultados = buscar_peliculas_lambda(nombre_pelicula)
    
    if resultados:
        print("Películas encontradas:")
        for pelicula in resultados.get('results', []):
            print(f"Título: {pelicula.get('title')}, ID: {pelicula.get('id')}")
        codigo_pelicula = input("Ingrese el código de la película que desea obtener más información (o 'q' para salir): ")
        if codigo_pelicula.lower() != 'q':
            obtener_informacion_pelicula(codigo_pelicula)
            buscar_otra_pelicula()
    else:
        print("No se encontraron películas con ese nombre.")
        buscar_otra_pelicula()

def obtener_informacion_pelicula(codigo_pelicula):
    # Aquí puedes implementar la lógica para obtener información detallada de una película
    pass

def buscar_otra_pelicula():
    respuesta = input("¿Desea buscar otra película? (s/n): ")
    if respuesta.lower() == 's':
        nombre_pelicula = input("Ingrese el nombre de la película: ")
        buscar_peliculas(nombre_pelicula)
    else:
        print("Gracias por usar el programa.")

def main():
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    buscar_peliculas(nombre_pelicula)

if __name__ == "__main__":
    main()

