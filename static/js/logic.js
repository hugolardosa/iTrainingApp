console.log("im here!");

// selectors
const ptcheckbox = document.getElementById("checkPT");
//---
const emailinput = document.getElementById('email');
const submitbtn = document.getElementById('btn');


// event listeners
ptcheckbox.addEventListener('change', function() {
    if (this.checked){
        ptinputdiv.innerHTML = "<input class=\"form-control\" type=\"text\" name=\"pt_code\" placeholder=\"PT code\" required>";
    }else{
        ptinputdiv.innerHTML = "";
    }
});

submitbtn.addEventListener("click", storeUser());


function storeUser(event){
    // prevent form from submiting
    event.preventDefault();

    if(emailinput.value != ""){
        localStorage.setItem('user', JSON.stringify(emailinput))
    }
}

