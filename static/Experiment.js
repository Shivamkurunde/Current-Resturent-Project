// Experiment.js
document.addEventListener("DOMContentLoaded", function() {
    var cart = [];
    var cartIsVisible = false;

    // Create cart box with a custom class
    var cartBox = document.createElement("div");
    cartBox.className = "cart-container";

    cartBox.innerHTML = `
        <div class="cart-header d-flex justify-content-between align-items-center mb-2">
            <h5>Your Cart</h5>
            <button id="close-cart" class="btn btn-sm btn-danger">X</button>
        </div>
        <div id="cart-items" class="cart-items-wrapper"></div>
        <hr />
        <p class="cart-total-text"><strong>Total:</strong> <span id="cart-total">Rs. 0</span></p>
        <button class="btn btn-success w-100 cart-buy-now" id="buy-now">Buy Now</button>
    `;

    document.body.appendChild(cartBox);

    var cartItemsArea = document.getElementById("cart-items");
    var cartTotalText = document.getElementById("cart-total");

    function updateCartDisplay() {
        cartItemsArea.innerHTML = "";
        var totalPrice = 0;

        for (var i = 0; i < cart.length; i++) {
            var item = cart[i];
            var itemBox = document.createElement("div");
            itemBox.className = "cart-item border p-2 mb-2";
            itemBox.innerHTML = `
                <div class="d-flex justify-content-between align-items-center">
                    <div class="cart-item-details">
                        <strong>${item.name}</strong><br>
                        <small>${item.priceText}</small>
                    </div>
                    <div class="cart-item-controls d-flex align-items-center">
                        <button class="btn btn-sm btn-secondary minus">-</button>
                        <span class="mx-2">${item.quantity}</span>
                        <button class="btn btn-sm btn-secondary plus">+</button>
                        <button class="btn btn-sm btn-danger ml-2 remove">x</button>
                    </div>
                </div>
            `;

            var plusButton = itemBox.querySelector(".plus");
            plusButton.addEventListener("click", (function(itemIndex) {
                return function() {
                    cart[itemIndex].quantity = cart[itemIndex].quantity + 1;
                    updateCartDisplay();
                };
            })(i));

            var minusButton = itemBox.querySelector(".minus");
            minusButton.addEventListener("click", (function(itemIndex) {
                return function() {
                    if (cart[itemIndex].quantity > 1) {
                        cart[itemIndex].quantity = cart[itemIndex].quantity - 1;
                        updateCartDisplay();
                    }
                };
            })(i));

            var removeButton = itemBox.querySelector(".remove");
            removeButton.addEventListener("click", (function(itemIndex) {
                return function() {
                    var newCart = [];
                    for (var j = 0; j < cart.length; j++) {
                        if (j !== itemIndex) {
                            newCart[newCart.length] = cart[j];
                        }
                    }
                    cart = newCart;
                    updateCartDisplay();
                    if (cart.length === 0) {
                        cartBox.style.display = "none";
                        cartIsVisible = false;
                    }
                };
            })(i));

            cartItemsArea.appendChild(itemBox);
            totalPrice = totalPrice + (item.price * item.quantity);
        }

        cartTotalText.textContent = "Rs. " + totalPrice;
    }

    var addToCartButtons = document.querySelectorAll(".add-to-cart-icon");
    for (var i = 0; i < addToCartButtons.length; i++) {
        addToCartButtons[i].addEventListener("click", function(event) {
            event.preventDefault();
            var card = this;
            while (!card.classList.contains("menu-item-card")) {
                card = card.parentElement;
            }

            if (card) {
                var itemName = card.querySelector(".menu-card-title").textContent;
                var itemPriceText = card.querySelector(".Dish-Price").textContent;
                var itemPrice = 0;
                var priceString = "";
                for (var j = 3; j < itemPriceText.length; j++) {
                    var char = itemPriceText[j];
                    if ((char >= "0" && char <= "9") || char === ".") {
                        priceString = priceString + char;
                    }
                }
                if (priceString !== "") {
                    itemPrice = parseFloat(priceString);
                } else {
                    itemPrice = 0;
                }

                var itemAlreadyInCart = false;
                for (var j = 0; j < cart.length; j++) {
                    if (cart[j].name === itemName) {
                        itemAlreadyInCart = true;
                        break;
                    }
                }
                if (itemAlreadyInCart) {
                    alert("Item already in cart!");
                    return;
                }

                var newItem = {
                    name: itemName,
                    priceText: itemPriceText,
                    price: itemPrice,
                    quantity: 1
                };
                cart[cart.length] = newItem;

                cartBox.style.display = "block";
                cartIsVisible = true;
                updateCartDisplay();
            }
        });
    }

    document.getElementById("close-cart").addEventListener("click", function() {
        cartBox.style.display = "none";
        cartIsVisible = false;
    });

    document.getElementById("buy-now").addEventListener("click", function() {
        if (cart.length === 0) {
            alert("Cart is empty.");
            return;
        }

        alert("Thank you for your purchase!");
        cart = [];
        updateCartDisplay();
        cartBox.style.display = "none";
        cartIsVisible = false;
    });
});