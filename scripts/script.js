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

// var wrap = $("#sticky");
//
// wrap.on("scroll", function(e)){
//   if(this.scrollTop > 200) {
//     wrap.addClass("sticky");
//   } else {
//     wrap.
//   }
// }
