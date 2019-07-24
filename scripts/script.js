var header = document.getElementById("nav_bar");
var sticky = header.offsetTop;

function dropdownFunction() {
 document.getElementById("dropdown1").classList.toggle("show");
}

function dropdownFunction2() {
 document.getElementById("dropdown2").classList.toggle("show");
}

function dropdownFunction3() {
 document.getElementById("dropdown3").classList.toggle("show");
}

function dropdownFunction4() {
 document.getElementById("dropdown4").classList.toggle("show");
}

function dropdownFunction5() {
 document.getElementById("dropdown5").classList.toggle("show");
}

function stickyHeader() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

window.onclick = function(event) {
 if (!event.target.matches('.dropbutton')) {
   var dropdowns = document.getElementsByClassName("dropdown-content");
   var i;
   for (i = 0; i < dropdowns.length; i++) {
     var openDropdown = dropdowns[i];
     if (openDropdown.classList.contains('show')) {
       openDropdown.classList.remove('show');
     }
   }
 }
}

window.onscroll = function(event) {
  stickyHeader()
};
