$.get('http://swapi.co/api/films?format=json', (data, code) => {
  $.each(data.results, (key, value) => {
    $('ul#list_movies').append($('<li></li>').text(value.title));
  });
});
