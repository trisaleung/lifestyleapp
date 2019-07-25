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

vat input = document.getElementById("userInput").value;


}}

// function foodSearch(){   ---> grab user input
//
// }
