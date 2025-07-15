document.addEventListener("DOMContentLoaded", function() {
    // Sidebar cart state
    let cart = [];
    let cartIsVisible = false;

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

    const cartItemsArea = cartBox.querySelector("#cart-items");
    const cartTotalElement = cartBox.querySelector("#cart-total");

    // Fetch cart from backend
    async function fetchCart() {
        try {
            const res = await fetch("/api/cart");
            if (!res.ok) throw new Error("Not logged in or error fetching cart");
            cart = await res.json();
            updateCartDisplay();
        } catch (err) {
            cart = [];
            updateCartDisplay();
        }
    }

    // Add to cart via backend
    async function addToCart(food_item_id, quantity = 1) {
        try {
            const res = await fetch("/api/cart/add", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ food_item_id, quantity })
            });
            if (!res.ok) {
                const data = await res.json();
                alert(data.error || "Error adding to cart");
                return;
            }
            await fetchCart();
            cartBox.style.display = "block";
            cartIsVisible = true;
        } catch (err) {
            alert("Error adding to cart");
        }
    }

    // Update cart item quantity via backend
    async function updateCartItem(cart_item_id, quantity) {
        try {
            const res = await fetch("/api/cart/update", {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ cart_item_id, quantity })
            });
            await fetchCart();
        } catch (err) {
            alert("Error updating cart");
        }
    }

    // Remove cart item via backend
    async function removeCartItem(cart_item_id) {
        try {
            await fetch(`/api/cart/remove/${cart_item_id}`, { method: "DELETE" });
            await fetchCart();
        } catch (err) {
            alert("Error removing item");
        }
    }

    // Update cart display
    function updateCartDisplay() {
        cartItemsArea.innerHTML = "";
        let total = 0;
        if (!cart || cart.length === 0) {
            cartBox.style.display = "none";
            cartIsVisible = false;
            cartTotalElement.textContent = 0;
            return;
        }
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
                updateCartItem(item.cart_id, item.quantity + 1);
            });
            itemElement.querySelector(".minus").addEventListener("click", () => {
                if (item.quantity > 1) {
                    updateCartItem(item.cart_id, item.quantity - 1);
                } else {
                    removeCartItem(item.cart_id);
                }
            });
            itemElement.querySelector(".remove").addEventListener("click", () => {
                removeCartItem(item.cart_id);
            });
            cartItemsArea.appendChild(itemElement);
            total += item.price * item.quantity;
        });
        cartTotalElement.textContent = total;
        cartBox.style.display = "block";
        cartIsVisible = true;
    }

    // Add to cart functionality (attach to add-to-cart buttons)
    document.querySelectorAll(".add-to-cart-icon").forEach(button => {
        button.addEventListener("click", function(e) {
            e.preventDefault();
            const card = this.closest(".menu-item-card");
            if (!card) return;
            // Get food_item_id from data attribute
            const food_item_id = card.getAttribute("data-food-item-id");
            if (!food_item_id) {
                alert("Food item ID not found!");
                return;
            }
            addToCart(food_item_id, 1);
        });
    });

    // Close cart button
    cartBox.querySelector("#close-cart").addEventListener("click", () => {
        cartBox.style.display = "none";
        cartIsVisible = false;
    });

    // Buy now button (redirect to /cart page)
    cartBox.querySelector("#buy-now").addEventListener("click", () => {
        if (!cart || cart.length === 0) {
            alert("Your cart is empty!");
            return;
        }
        window.location.href = "/cart";
    });

    // Initial fetch
    fetchCart();
});