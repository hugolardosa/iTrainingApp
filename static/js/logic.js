console.log("im here!");

// selectors
const ptcheckbox = document.getElementById("checkPT");


// event listeners
ptcheckbox.addEventListener('change', function() {
    if (this.checked){
        ptinputdiv.innerHTML = "<input class=\"form-control\" type=\"text\" name=\"pt_code\" placeholder=\"PT code\" required>";
    }else{
        ptinputdiv.innerHTML = "";
    }
});

