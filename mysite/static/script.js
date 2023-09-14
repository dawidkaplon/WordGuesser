// Get references to keyboard buttons
const buttonMap = {
    'Q': document.getElementById('buttonQ'),
    'W': document.getElementById('buttonW'),
    'E': document.getElementById('buttonE'),
    'R': document.getElementById('buttonR'),
    'T': document.getElementById('buttonT'),
    'Y': document.getElementById('buttonY'),
    'U': document.getElementById('buttonU'),
    'I': document.getElementById('buttonI'),
    'O': document.getElementById('buttonO'),
    'P': document.getElementById('buttonP'),
    'A': document.getElementById('buttonA'),
    'S': document.getElementById('buttonS'),
    'D': document.getElementById('buttonD'),
    'F': document.getElementById('buttonF'),
    'G': document.getElementById('buttonG'),
    'H': document.getElementById('buttonH'),
    'J': document.getElementById('buttonJ'),
    'K': document.getElementById('buttonK'),
    'L': document.getElementById('buttonL'),
    'Z': document.getElementById('buttonZ'),
    'X': document.getElementById('buttonX'),
    'C': document.getElementById('buttonC'),
    'V': document.getElementById('buttonV'),
    'B': document.getElementById('buttonB'),
    'N': document.getElementById('buttonN'),
    'M': document.getElementById('buttonM'),
    'BACKSPACE': document.getElementById('buttonBackspace'),
    'ENTER': document.getElementById('buttonEnter'),

}

// Function to simulate a button click
function simulateButtonClick(button) {
    const originalBackgroundColor = '';
    const originalStyleColor = '';
    button.style.backgroundColor = 'grey';
    button.style.color = 'white';

    setTimeout(() => {
        button.style.backgroundColor = originalBackgroundColor;
        button.style.color = originalStyleColor
    }, 200);
}



document.addEventListener('keydown', function (event) {
    const key = event.key.toUpperCase();

    if (buttonMap[key]) {
        simulateButtonClick(buttonMap[key]);
    }
});

document.querySelector(".digits").addEventListener("input", function(e){
    e.target.value = e.data.replace(/[^0-9]/g,'');
    if ( e.target.value !== "" && e.target.nextElementSibling && e.target.nextElementSibling.nodeName === "INPUT" ){
      e.target.nextElementSibling.focus();
    } 
  });

document.querySelector("input").focus();
document.querySelector(".digits").addEventListener("input", function({ target, data }){

  data && ( target.value = data.replace(/[^0-9]/g,'') );
  
  const hasValue = target.value !== "";
  const hasSibling = target.nextElementSibling;
  const hasSiblingInput = hasSibling && target.nextElementSibling.nodeName === "INPUT";

  if ( hasValue && hasSiblingInput ){

    target.nextElementSibling.focus();
  
  } 

});