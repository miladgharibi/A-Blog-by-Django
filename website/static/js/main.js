document.getElementById("id_title").addEventListener("input", function () {
    let theSlug = slug(this.value);
    document.getElementById("id_slug").value = theSlug;
  });

function slug(titleStr){
  titleStr = titleStr.replace(/^\s+|\s+$/g, '');
  titleStr = titleStr.toLowerCase();
  //persian support
  titleStr = titleStr.replace(/[^a-z0-9_\s-ءاأإآؤئبتثجحخدذرزسشصضطظعغفقكلمنهويةى]#u/, '') 
  // Collapse whitespace and replace by -
      .replace(/\s+/g, '-')
      // Collapse dashes
      .replace(/-+/g, '-');
  return titleStr;       
}