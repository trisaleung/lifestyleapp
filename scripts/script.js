var header = document.getElementById("nav_bar");
var sticky = header.offsetTop;

function stickyHeader() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

window.onscroll = function(event) {
  stickyHeader()
};


document.getElementById("btnmyNumber").addEventListener("click", myFunctionVar);
function myFunctionVar() {
var numberr = parseInt(document.getElementById("myNumber").value, 10);
// alert(numberr);
if ( numberr > 1) {

  document.getElementById("minusE5").style.display = "none";

alert("number")


}}
