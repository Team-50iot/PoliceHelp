function main() {
  var xhr = new XMLHttpRequest();
  var url = 'http://1pavel1.pythonanywhere.com/db';
  xhr.open('GET', url, false);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  var info = JSON.parse(xhr.response);
  for (var i = 0; i < info.length; i++) {
    id = info[i].id;
    time = info[i].time;
    number = info[i].number;
    console.log(id);
    console.log(number);
    console.log(time);
  }
}
