const Subject = require('./Subject');
const Observer = require('./Observer');

// Extend an object with an extension
function extend(obj, extension) {
  for (const key in extension) {
    obj[key] = extension[key];
  }
}

// References to our DOM elements

const controlCheckbox = document.getElementById('mainCheckbox'),
  addBtn = document.getElementById('addNewObserver'),
  container = document.getElementById('observersContainer');

// Concrete Subject

// Extend the controlling checkbox with the Subject class
extend(controlCheckbox, Subject);

// Clicking the checkbox will trigger notifications to its observers
controlCheckbox.onclick = function() {
  controlCheckbox.notify(controlCheckbox.checked);
};

addBtn.onclick = addNewObserver;

// Concrete Observer

function addNewObserver() {
  // Create a new checkbox to be added
  const check = document.createElement('input');
  check.type = 'checkbox';

  // Extend the checkbox with the Observer class
  extend(check, Observer);

  // Override with custom update behaviour
  check.update = function(value) {
    this.checked = value;
  };

  // Add the new observer to our list of observers
  // for our main subject
  controlCheckbox.addObserver(check);

  // Append the item to the container
  container.appendChild(check);
}
