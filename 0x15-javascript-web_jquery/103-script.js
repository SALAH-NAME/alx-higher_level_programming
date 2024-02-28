$(document).ready(function () {
  function sayHello () {
    const lang = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(sayHello);
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      sayHello();
    }
  });
});
