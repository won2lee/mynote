var Links = {
  setColor:function(color){
    var alist = document.querySelectorAll('a');
    var i = 0;
    while(i < alist.length){
      alist[i].style.color = color;
      i = i + 1;
    }
  }
}
var Body = {
  setColor:function (color){
    document.querySelector('body').style.color = color;
  },
  setBackgroundColor:function (color){
    document.querySelector('body').style.backgroundColor = color;
  }
}
var Form = {
  setColor:function (color){
    document.querySelector('textarea').style.color = color;
  },
  setBackgroundColor:function (color){
    document.querySelector('textarea').style.backgroundColor = color;
  }
}


var nightIs='night';
function nightDay(){
  // if(self.value === 'night'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    Form.setBackgroundColor('black');
    Form.setColor('white');
    // #self.value = 'day';
    // nightIs='night'

    Links.setColor('white');
  // } else {
  //   Body.setBackgroundColor('white');
  //   Body.setColor('black');
  //   self.value = 'night';
  //   nightIs='day'
  //
  //   Links.setColor('blue');
  // }
}
function nightDayHandler(self){
  // var target = document.querySelector('body');
  if(self.value === 'night'){
    Body.setBackgroundColor('black');
    Body.setColor('white');
    Form.setBackgroundColor('black');
    Form.setColor('white');
    self.value = 'day';

    Links.setColor('white');
  } else {
    Body.setBackgroundColor('white');
    Body.setColor('black');
    Form.setBackgroundColor('white');
    Form.setColor('black');
    self.value = 'night';

    Links.setColor('blue');
  }
}
