document.querySelectorAll(".add-to-cart").forEach(button => {
    button.addEventListener("click", () => {
        const card = button.parentElement;
        const title = card.querySelector("h3").textContent;
        const priceText = card.querySelector(".price").textContent;
        const price = parseInt(priceText.replace(/[^0-9]/g, ""));

        cartCount += 1;
        cartTotal += price;

        document.getElementById("cart-count").textContent = cartCount;
        document.getElementById("cart-total").textContent = cartTotal.toLocaleString();

        // ذخیره‌سازی در localStorage
        let cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];
        cartItems.push({ title, price });
        localStorage.setItem("cartItems", JSON.stringify(cartItems));
    });
});
