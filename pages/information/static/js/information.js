const phonNumberIn = document.getElementById("phone")
//check valid phone number
phonNumberIn.addEventListener('input', function (event) {
    // Remove any non-digit characters
    let phoneNumber = event.target.value.replace(/\D/g, '');

    // Ensure the phone number has less than ten digits
    if (phoneNumber.length > 10) {
        // Trim the phone number to have only first 10 digits
        phoneNumber = phoneNumber.slice(0, 10);
    }

    // Update the input value with the cleaned phone number
    event.target.value = phoneNumber;
});