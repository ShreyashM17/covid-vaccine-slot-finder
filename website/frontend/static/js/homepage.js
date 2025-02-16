function myFunction() {
  var element = document.body;
  var x = document.getElementById("button");
  element.classList.toggle("dark-mode");
  if ( x.innerHTML == "Dark mode") {
    x.innerHTML = "Light mode";
    x.className = "light";
  } else {
    x.innerHTML = "Dark mode";
    x.className = "dark-mode";
  }
}