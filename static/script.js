var log = function (x) { return console.log(arguments), x; },
  parse = JSON.parse,
  filter = function(obj, keys) {
    var result = {};
    for (var key in obj)
      if (keys.indexOf(key) != -1)
        result[key] = obj[key]
    return result;
  },
  tag = function (tagName) {
    return function (content) {
      return '<' + tagName + '>' + content + '</' + tagName + '>';
    };
  },
  id = document.getElementById.bind(document),
  table = tag('table'),
  row = tag('tr'),
  cell = tag('td'),
  element = function (cls) {
    return cell('<span class="' + cls + '"></span>');
  },
  game = function (info) {
    info['game'] = table(info.board.split(/\n/).map(function (e) {
      return row(e.split('').map(element).join(''))
    }).join(''));
    return info;
  },
  render = function (templateId, data) {
    return id(templateId).innerHTML.replace(/\{\{(.*?)\}\}/g, function(_, key){
      return data[key];
    });
  },
  load = function (templateId, data) {
    $('main').html(render(templateId, data));
  },
  LS = localStorage,
  enterGame = function (data) {
    data = parse(data);
    var game = parse(LS.GAME || '{}');

    if (data.id != game.id)
      LS.GAME = JSON.stringify(data);
    else
      game['white_token'] = data['white_token'], LS.GAME = JSON.stringify(game);

    location.hash = '/game/' + data.id;
  },
  getName = function(){
    return prompt("Please enter your name", "");
  }

$(document)
  .on('click', 'button#new', function(){
    $('#message').html(id('/new-game').innerHTML).slideDown();
  })
  .on('click', 'button#cancel', function(){
    $('#message').slideUp();
    return false;
  })
  .on('click', 'button.watch', function(e){
    location.hash = '/game/'+ $(e.target).parent().data('id');
  })
  .on('submit', '#new-game', function(e){
    e.preventDefault();
    $('#message').hide();
    $.post('/create', {name: id('name').value, ai: id('has-ai').checked}, enterGame);
  })
  .on('click', 'button.join', function(){
    var data = {
      id: $(this).parent().parent().data('id'),
      place: $(this).parent().attr('class'),
      name: getName()
    };
    $.post('/join', data, enterGame)
  })
  .on('click', '#game td', function(){
    var data = filter(parse(LS.GAME), ['id', 'white_token', 'black_token'])
    data['idx'] = $('#game td').index(this) // row, col
    $.post('/play', data)
  })
  .on('click', 'a[href$="#/game"]', function(){
    if (LS.GAME)
      return location.hash = '/game/' + parse(LS.GAME).id, false;
    return alert('You are not currently in a game'), false;
  })
var actions = {
  game: function(data){
    load('/game', game(data));
  },
  games: function(data){
    load('/games');
    $('#active-games').html(data.map(function (e) {
      return render('/game-state', e).replace('null', '<button class="join">Sit</button>')
    }).join(''));
  }
}
window.onhashchange = function (e) {
  var page = location.hash.slice(2);
  $.get(page, function (data){
    actions[page.split('/')[0]](parse((data)));
  });
  return false;
};
if (location.hash == '')
  location.hash = '/games';

setInterval(window.onhashchange, 1000)
