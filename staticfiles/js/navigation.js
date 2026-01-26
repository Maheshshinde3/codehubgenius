// DOM Loads js only when html is fully loaded.
document.addEventListener("DOMContentLoaded", function () {

//all elements of jsnavigationclasses are taken as input
const links = document.querySelectorAll(".jsnavignation");

//iterated through each element (home,about,playlists,quizzone,followus). and added click event listener
  links.forEach(link => {
    link.addEventListener("click", function(){
        // remove active class i.e. purple color from all elements and added color to anly clicked element.
        links.forEach(l => l.classList.remove("active"));
        link.classList.add("active");
    })
  });


  });
  const scrolling = document.querySelectorAll(".scrolling");
  const links = document.querySelectorAll(".jsnavignation");
  
  window.addEventListener("scroll", () => {
  let scrollPos = window.scrollY + 400
  

 
  scrolling.forEach(scrolling => {
    if (
      scrollPos >= scrolling.offsetTop &&
      scrollPos < scrolling.offsetTop + scrolling.offsetHeight
    ) {
    
      links.forEach(link => link.classList.remove("active"));

       document
        .querySelector(`a[href="#${scrolling.id}"]`)
        .classList.add("active");
    }
  });
});
 window.onload = function () {
    window.scrollTo(0, 0);
  };




   
 

 

