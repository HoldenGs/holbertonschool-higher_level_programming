$.get('http://swapi.co/api/people/5/?format=json', (data, code) => {
  $('div#character').text(data.name);
});
