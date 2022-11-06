var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        if (document.getElementById(`product${productId}-quantity`)){
            var quantity = document.getElementById(`product${productId}-quantity`).value
        } else {
            var quantity = 1
        }
        updateUserOrder(productId, action, quantity)
        
    })
}

function updateUserOrder(productId, action, quantity) {
    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'productId': productId, 'action': action, 'quantity': quantity})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        
        location.reload()
    })
}