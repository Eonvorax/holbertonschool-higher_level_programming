const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.querySelector('#hello');
  fetch(url)
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});
