// send the time of the clicked button to the server
const timeAddEventListener = (item,text) => {
    item.addEventListener("click", (e) => {
        // Example data to send
        e.preventDefault()
        // Send data to server
        fetch('/sendTime', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'

            },
            body: JSON.stringify(text)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success === 'to home'){
                 window.location.href = ``;
            }

            if (data.success) {
                window.location.href = `pay`;
            } else {
                window.location.href = `Time`
            }


        });
    });
}

const timeMenu = document.querySelector('main')
// create all the button time from the database
for (let i in times) {
    let time = times[i]
    let time_button = document.createElement('button')
    time_button.innerHTML = time
    timeAddEventListener( time_button,time)
    timeMenu.appendChild(time_button)
}


