const createUserForm = document.getElementById('createUserForm');
const createNameInput = document.getElementById('createName');
const createEmailInput = document.getElementById('createEmail');

createUserForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = createNameInput.value;
    const email = createEmailInput.value;
    createUser(name, email);
    createNameInput.value = '';
    createEmailInput.value = '';
});

function createUser(name, email) {
    fetch('/user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            email
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
}