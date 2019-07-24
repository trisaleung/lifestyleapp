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

// Close the dropdown menu if the user clicks outside of it
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
