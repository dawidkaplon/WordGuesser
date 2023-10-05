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
  button.style.backgroundColor = '#C0C0C0';
  button.style.color = 'white';

  setTimeout(() => {
      button.style.backgroundColor = originalBackgroundColor;
      button.style.color = originalStyleColor
  }, 200);
}

document.addEventListener('keydown', function (event) {
  const key = event.key.toUpperCase();

  if (buttonMap[key]) {
      const button = buttonMap[key];
      const backgroundColor = button.style.backgroundColor;

      // Check if the background color is not already changed
      if (backgroundColor !== '' && backgroundColor !== '#C0C0C0') {
          // The background color is already changed, so do nothing
          return;
      }

      simulateButtonClick(button);
  }
});