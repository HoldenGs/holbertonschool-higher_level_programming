$.ajax({
  url: 'http://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (json) {
    $('div#character').text(json.name);
  }
});
