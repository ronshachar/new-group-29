// Object to manage adding and removing toppings from the order
const toppingInOrder = [];
const UpdateToppingToOrder = {
    add: (item) => {
        // Add a topping to the order
        toppingInOrder.push(item.id)
    },

    remove: (item, double = false) => {
        // Remove a topping from the order
        toppingInOrder.splice(toppingInOrder.indexOf(item.id), 1)
        if (double) {
            toppingInOrder.splice(toppingInOrder.indexOf(item.id), 1)
        }
    }
}
// Function to add text to an image using canvas
const addTextToImg = (img, text) => {
    // Create a canvas element
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    // Get the 2D drawing context of the canvas
    const ctx = canvas.getContext('2d');
    // Draw the image onto the canvas
    ctx.drawImage(img, 0, 0);
    // Add text to the canvas
    ctx.font = `${img.naturalWidth / 5}px "Arial Rounded MT Bold"`;
    ctx.fillStyle = 'black';
    // Calculate text width
    const textWidth = ctx.measureText(text).width;
    // Draw text
    ctx.fillText(text, (canvas.width - textWidth) / 2, canvas.height / 2);
    // Return the modified image as a data URL
    return canvas.toDataURL();
}

// Selecting menu elements from the DOM
const toppingMenu = document.querySelector("#topping")
const hamburgerMenu = document.querySelector("#hamburgerMenu")


// upload the topping to the menu
for (let keys of Object.keys(toppings)) {
    let topping = toppings[keys]
    // price
    let price = document.createElement('h5')
    price.className = "Topping_price"
    price.textContent = topping.price + " ₪"
    // Topping
    let newTopping = document.createElement('img')
    newTopping.id = topping.id
    newTopping.src = topping.img
    newTopping.title = `Description : ${topping.description} \n Price : ${topping.price}  $ `
    newTopping.className = "topping"
    newTopping.toppingOrder = topping.order
    newTopping.double = false
    // Appending topping image and price to the topping menu
    toppingMenu.appendChild(newTopping)
    toppingMenu.appendChild(price)

}
// Selecting topping elements from toppingMenu
const toppingToChoose = document.querySelectorAll("#topping .topping")

// add Event Listener to the topping menu
for (let item of toppingToChoose) {
    item.addEventListener('click', (e) => {
        e.preventDefault()
        chooseTopping(item)
    })
}
// Function to handle click events on single toppings in the hamburger menu
toppingInHamburgerAddEventListener = (item) => {

    item.addEventListener('click', (e) => {
        e.preventDefault()
        item.remove()
        UpdateToppingToOrder.remove(document.getElementById(item.id.slice(0, -3)))
    })
}
// Function to handle click events on double toppings in the hamburger menu
toppingInHamburgerAddEventListenerX2 = (item) => {
    item.addEventListener('click', (e) => {
        e.preventDefault()
        item.remove()
        const oldItem = document.getElementById(item.id.slice(0, -3))
        UpdateToppingToOrder.remove(oldItem, true)
        toppings[oldItem.id].double = false
        chooseTopping(oldItem)
    })
}
// Function to handle topping selection
const chooseTopping = (item) => {
    if (toppings[item.id].double === false) {
        let newitem = document.createElement('img')
        newitem.toppingOrder = item.toppingOrder
        if (toppingInOrder.includes(item.id)) {
            // If topping is already in order, create a double topping
            newitem.src = addTextToImg(item, "X2")
            newitem.id = item.id + '_X2'
            newitem.title = item.title
            // Replace existing topping with double topping in the hamburger menu
            hamburgerMenu.replaceChild(newitem, document.getElementById(item.id + "_on"))
            newitem.double = true
            UpdateToppingToOrder.add(item)
            toppingInHamburgerAddEventListenerX2(newitem)
        } else {
            // If topping is not in order, create a single topping
            newitem.src = item.src
            newitem.id = item.id + "_on"
            newitem.title = item.title
            UpdateToppingToOrder.add(item)
            toppingInHamburgerAddEventListener(newitem)

            hamburgerMenu.appendChild(newitem)
            // Insert the topping into the hamburger menu based on its order
            for (let topping of document.querySelectorAll("#hamburgerMenu img")) {
                if (topping.toppingOrder < item.toppingOrder) {
                    hamburgerMenu.insertBefore(newitem, topping)
                    return;
                }
            }
            hamburgerMenu.appendChild(newitem)
        }

    }
}

///////////////////////////////////access functions/////////////////////
// Functions for accessing and manipulating the order
const pushItens = (items) => {
    for (id of items) {
        chooseTopping(document.querySelector(`#${id}`))
    }
}
pushItens(defaultTopping)


// Get the current order
getHamburgerOrder = () => {
    let price = products["hamburger"].price
    for (let topping of toppingInOrder) {
        price += toppings[topping].price
    }

    return new OrderProduct(
        products["hamburger"].id,
        `${products['hamburger'].description}
            \n topping : ${toppingInOrder}`,
        price,
        null)

}

// save the hamburger as product
document.getElementById('save').addEventListener('click', (e) => {
    e.preventDefault()
    appendProductToOrder(getHamburgerOrder())
    window.location.href = '/'
})