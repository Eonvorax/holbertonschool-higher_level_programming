const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

document.addEventListener('DOMContentLoaded', function () {
  const characterElement = document.querySelector('#character');
  fetch(url)
    .then(response => response.json())
    .then(data => {
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching character name:', error);
    });
});
