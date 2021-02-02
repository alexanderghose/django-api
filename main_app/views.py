from django.shortcuts import render
import requests

def astro_index(request):
  r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
  the_response = r.json()
  sprites = the_response['sprites']
  other = sprites['other']
  offic = other['official-artwork']
  img = offic['front_default']

  return render(request, 'astros.html', {
    'img': img
  })



class Cat:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]

# View functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
  return render(request, 'cats/index.html', { 'cats': cats })