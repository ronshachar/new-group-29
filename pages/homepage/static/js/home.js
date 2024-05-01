///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// list of  "OrderProduct" in order
const order = []
//the total price
var totalPrice = 0
var initialization = false
// A name definition for functions
var loudDrinks = () => {
}
var loudHamburger = () => {
}
var loudHome = () => {
}


// add event listener to the home button
document.getElementById('home').addEventListener('click', (e) => {
    e.preventDefault()
    window.location.href = '/'
})


// function that Add event listener to product for edding to order
const productAddEventListener = (product) => {
    // if product is 'hamburger' or 'drinks' move to relevant page else Add event listener to product for adding to order
    switch (product.id.slice(0, -3)) {
        case 'hamburger':
            product.addEventListener('click', (e) => {
                e.preventDefault()
                window.location.href = `/home_hamburger`;
            })
            break;
        case 'drinks':
            product.addEventListener('click', (e) => {
                e.preventDefault()

                window.location.href = `home_drinks`;
            })
            break;
        default:
            product.addEventListener('click', (e) => {
                appendProductToOrder(product.orderProduct)
            })
    }
}

// create form data button for the product
const productProductMenu = document.querySelector("#menu")
for (let keys of Object.keys(products)) {
    product = products[keys]
    // the price of product
    let price = document.createElement('h5')
    price.textContent = product.price + " ₪"
    price.className = "productPrice"
    // the button of product
    let newProduct = document.createElement('img')
    newProduct.id = product.id + "_si"
    newProduct.src = product.img
    newProduct.title = `Description : ${product.description} \n Price : ${product.price}  $ `
    newProduct.className = "product Button"
    newProduct.orderProduct = new OrderProduct(product.id, product.description, product.price, null)
    productAddEventListener(newProduct)
    productProductMenu.appendChild(newProduct)
    productProductMenu.appendChild(price)

}


const orderMenu = document.querySelector("footer")

// update the total price
const updateOPrice = (price) => {
    totalPrice += price
    const orderData = document.getElementById("orderData")
    const text = orderData.textContent.split(/[:]/)
    orderData.textContent = `${text[0]} : ${text[1]} : ${totalPrice}`
}

//append product to order and create the delete process
const appendProductToOrder = (orderProduct) => {
    // create the order 'node'
    const id = orderProduct.product
    const productMonitor = document.createElement('p')
    productMonitor.id = id + '_mo'
    productMonitor.className = "OrderMonitor"
    orderProduct.i = order.length + 1
    order.push(orderProduct)
    productMonitor.innerHTML = orderProduct.toText()
    productMonitor.title = `Description : ${orderProduct.toText()} \n ${orderProduct.description}`
    orderMenu.appendChild(productMonitor)
    updateOPrice(orderProduct.price)
    if (initialization) {
        update_order_in_server()
    }

    //create the delete "orderProduct"
    productMonitor.addEventListener('click', (e) => {
        e.preventDefault()
        updateOPrice(-orderProduct.price)
        order.splice(order.indexOf(orderProduct), 1)
        productMonitor.parentElement.removeChild(productMonitor)
        const ps = orderMenu.querySelectorAll("p");
        for (let i = 0; i < order.length; i++) {
            order[i].i = i + 1;
            ps[i + 1].innerHTML = order[i].toText();

        }

        update_order_in_server()
    })
}

// and to exist order

const loud_old_order = () => {
    for (product of old_order) {
        appendProductToOrder(
            new OrderProduct(
                product['product'],
                product['description'],
                product['price'],
                product['i']
            )
        )
    }
    initialization = true
}
loud_old_order()

// when the user click pay the order send to the server
document.getElementById("pay").addEventListener("click", function () {
    if (order.length > 0) {
        window.location.href = `information`;
    }
});
const update_order_in_server = () => {
// Example data to send

    // Send data to server
    fetch('/sendOrder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify([order, totalPrice])

    })
        .then(response => response.json())
        .then(data => {
            data.success
        });
}