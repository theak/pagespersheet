/*
 * Helper functions for render.html
 */

function replaceClass(classA, classB) {
  const elements = document.querySelectorAll(`.${classA}`);
  elements.forEach(element => {
    element.classList.replace(classA, classB);
  });
}

function setOrientation(orientation) {
  const previousOrientation = document.getElementById("pageOrientation");
  if (previousOrientation) previousOrientation.remove();

  const style = document.createElement('style');
  style.id = "pageOrientation";
  style.innerHTML = `@page {size: ${orientation}}`;
  document.head.appendChild(style);
}

function setPagesPerSheet(numPages) {
  if (numPages == 2) {
    setOrientation("landscape");
    replaceClass("portrait", "landscape");
    replaceClass("quarterpage", "halfpage");
    document.querySelectorAll('.hr_2').forEach(function(el) {
     el.style.display = '';
   });
  } else if (numPages == 4) {
    setOrientation("portrait");
    replaceClass("landscape", "portrait");
    replaceClass("halfpage", "quarterpage");
    document.querySelectorAll('.hr_2').forEach(function(el) {
     el.style.display = 'none';
   });
  }
}