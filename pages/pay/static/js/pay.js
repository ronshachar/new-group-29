//

const payAddEventListener = (item, text) => {
    item.addEventListener("click", (e) => {
        console.log(text)
        // Example data to send
        e.preventDefault()
        // Send data to server
        fetch('/sendPay', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'

            },
            body: JSON.stringify({
                'pay': text,
            })
        })
        window.location.href = 'end'
    });

}

payAddEventListener(document.getElementById('cash'), 'cash')

payAddEventListener(document.getElementById('credit'), 'credit')