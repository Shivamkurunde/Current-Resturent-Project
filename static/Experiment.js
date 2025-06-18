document.addEventListener("DOMContentLoaded", function() {
    // Initialize cart from localStorage or empty array
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    let cartIsVisible = localStorage.getItem("cartVisible") === "true";

    // Create cart element
    const cartBox = document.createElement("div");
    cartBox.className = "cart-container";
    cartBox.style.display = cartIsVisible ? "block" : "none";
    
    cartBox.innerHTML = `
        <div class="cart-header">
            <h5>Your Cart</h5>
            <button id="close-cart" class="close-btn">✕</button>
        </div>
        <div id="cart-items" class="cart-items-wrapper"></div>
        <div class="cart-footer">
            <p class="cart-total"><strong>Total:</strong> Rs. <span id="cart-total">0</span></p>
            <button class="btn btn-primary" id="buy-now">Buy Now</button>
        </div>
    `;
    document.body.appendChild(cartBox);

    // CSS for cart positioning
    const style = document.createElement("style");
    style.textContent = `
        .cart-container {
            position: fixed;
            top: 80px;
            right: 20px;
            width: 320px;
            max-height: 70vh;
            overflow-y: auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1050;
            padding: 15px;
        }
        .cart-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            position: sticky;
            top: 0;
            background: white;
            padding: 10px 0;
            z-index: 1;
        }
        .close-btn {
            background: none;
            border: none;
            font-size: 1.2rem;
            cursor: pointer;
            color: #dc3545;
            padding: 0 8px;
        }
        .cart-items-wrapper {
            margin-bottom: 15px;
        }
        .cart-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        .item-quantity {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .quantity-btn {
            width: 25px;
            height: 25px;
            border-radius: 50%;
            border: 1px solid #ddd;
            background: #fff;
            cursor: pointer;
        }
        .cart-footer {
            border-top: 1px solid #eee;
            padding-top: 15px;
        }
    `;
    document.head.appendChild(style);

    const cartItemsArea = document.getElementById("cart-items");
    const cartTotalElement = document.getElementById("cart-total");

    // Save cart state
    function saveCartState() {
        localStorage.setItem("cart", JSON.stringify(cart));
        localStorage.setItem("cartVisible", cartIsVisible);
    }

    // Update cart display
    function updateCartDisplay() {
        cartItemsArea.innerHTML = "";
        let total = 0;

        cart.forEach((item, index) => {
            const itemElement = document.createElement("div");
            itemElement.className = "cart-item";
            itemElement.innerHTML = `
                <div class="item-details">
                    <div class="item-name">${item.name}</div>
                    <div class="item-price">Rs. ${item.price}</div>
                </div>
                <div class="item-quantity">
                    <button class="quantity-btn minus">-</button>
                    <span>${item.quantity}</span>
                    <button class="quantity-btn plus">+</button>
                    <button class="btn btn-sm btn-danger remove">×</button>
                </div>
            `;
            
            itemElement.querySelector(".plus").addEventListener("click", () => {
                cart[index].quantity++;
                saveCartState();
                updateCartDisplay();
            });

            itemElement.querySelector(".minus").addEventListener("click", () => {
                if (cart[index].quantity > 1) {
                    cart[index].quantity--;
                    saveCartState();
                    updateCartDisplay();
                }
            });

            itemElement.querySelector(".remove").addEventListener("click", () => {
                cart.splice(index, 1);
                saveCartState();
                updateCartDisplay();
                if (cart.length === 0) {
                    cartBox.style.display = "none";
                    cartIsVisible = false;
                    saveCartState();
                }
            });

            cartItemsArea.appendChild(itemElement);
            total += item.price * item.quantity;
        });

        cartTotalElement.textContent = total;
    }

    // Add to cart functionality
    document.querySelectorAll(".add-to-cart-icon").forEach(button => {
        button.addEventListener("click", function(e) {
            e.preventDefault();
            const card = this.closest(".menu-item-card");
            if (!card) return;

            const itemName = card.querySelector(".menu-card-title").textContent.trim();
            const itemPriceText = card.querySelector(".Dish-Price").textContent.trim();
            const itemPrice = parseInt(itemPriceText.replace(/\D/g, ""));

            const existingItem = cart.find(item => item.name === itemName);
            
            if (existingItem) {
                alert(`${itemName} is already in your cart!`);
                return;
            }

            cart.push({
                name: itemName,
                price: itemPrice,
                quantity: 1
            });

            cartBox.style.display = "block";
            cartIsVisible = true;
            saveCartState();
            updateCartDisplay();
        });
    });

    // Close cart button
    document.getElementById("close-cart").addEventListener("click", () => {
        cartBox.style.display = "none";
        cartIsVisible = false;
        saveCartState();
    });

    // Buy now button
    document.getElementById("buy-now").addEventListener("click", () => {
        if (cart.length === 0) {
            alert("Your cart is empty!");
            return;
        }
        alert(`Order placed! Total: Rs. ${cartTotalElement.textContent}`);
        cart = [];
        saveCartState();
        updateCartDisplay();
        cartBox.style.display = "none";
        cartIsVisible = false;
    });

    // Initialize cart display
    if (cartIsVisible) updateCartDisplay();
});