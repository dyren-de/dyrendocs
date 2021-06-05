var checkbox = document.getElementById("theme-switch");

if (sessionStorage.getItem("theme") == "dark") {
  darktheme(); 
} else {
  nodark(); 
}

checkbox.addEventListener("change", function() {

  if (checkbox.checked) {
    darktheme(); 
    document.getElementById('dark').play();
  } else {
    nodark();
    document.getElementById('flashbang').play();
  }
});

function darktheme() {
  document.body.classList.add("darkmode"); 
  checkbox.checked = true; 
  sessionStorage.setItem("theme", "dark"); 
}

function nodark() {
  document.body.classList.remove("darkmode"); 
  checkbox.checked = false; 
  sessionStorage.setItem("theme", "light");
}

window.onload = function () {
  document.addEventListener("contextmenu", function (e) {
      e.preventDefault();
      document.getElementById('click').play();
  }, false);
  document.addEventListener("keydown", function (e) {
      //document.onkeydown = function(e) {
      // "I" key
      if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
          disabledEvent(e);
      }
      // "J" key
      if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
          disabledEvent(e);
      }
      // "S" key + macOS
      if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
          disabledEvent(e);
      }
      // "U" key
      if (e.ctrlKey && e.keyCode == 85) {
          disabledEvent(e);
      }
      // "F12" key
      if (event.keyCode == 123) {
          disabledEvent(e);
          document.getElementById('alert').play();
      }
  }, false);
  function disabledEvent(e) {
    document.getElementById('alert').play();
      if (e.stopPropagation) {
          e.stopPropagation();
      } else if (window.event) {
          window.event.cancelBubble = true;
      }
      e.preventDefault();
      return false;
  }
}
