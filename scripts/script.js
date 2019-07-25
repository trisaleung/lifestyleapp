var header = document.getElementById("stickybar");
var sticky = header.offsetTop;
var wrap = $("#stickybar");

// function stickyHeader() {

wrap.on("scroll", function(e){
  if (this.scrollTop > 400) {
    wrap.classList.addClass("stick");
  } else {
    wrap.classList.removeClass("stick");
  }
});
//
// window.onscroll = function(event) {
//   stickyHeader()
// };

<<<<<<< HEAD
// var wrap = $("#sticky");
//
// wrap.on("scroll", function(e)){
//   if(this.scrollTop > 200) {
//     wrap.addClass("sticky");
//   } else {
//     wrap.
//   }
=======
window.onscroll = function(event) {
  stickyHeader()
};

var input = document.getElementById("userInput").value;


}}

// function foodSearch(){   ---> grab user input
//
>>>>>>> 1e7980e386dd3a5405034c5c896885dfad4a2a77
// }
