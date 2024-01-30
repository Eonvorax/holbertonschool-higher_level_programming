const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

document.addEventListener('DOMContentLoaded', function () {
  const listMovies = document.querySelector('#list_movies');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error fetching movie titles:', error);
    });
});
