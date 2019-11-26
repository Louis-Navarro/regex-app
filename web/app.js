function send(){
  pattern = document.getElementById('pattern').value
  string = document.getElementById('string').value
  eel.process(pattern, string)
}

eel.expose(showResult)
function showResult(answer){
  document.getElementById('result').innerHTML = answer
}
