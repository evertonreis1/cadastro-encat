class Login{
    

    verificarLogin() {
        const login = document.getElementById("loginID").value;
        const senha = document.getElementById("senhaID").value;
        alert("Top");
        
    }
}

const submit = document.getElementById("submit");

submit.addEventListener("click", validate);

function validate(e) {
  e.preventDefault();

  const firstNameField = document.getElementById("firstname");
  let valid = true;

  if (!firstNameField.value) {
    const nameError = document.getElementById("nameError");
    nameError.classList.add("visible");
    firstNameField.classList.add("invalid");
    nameError.setAttribute("aria-hidden", false);
    nameError.setAttribute("aria-invalid", true);
  }
  return valid;
}
