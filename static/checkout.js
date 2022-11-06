    var form = document.getElementById("shipping-info-form")

    form.addEventListener('submit', function(e){
        e.preventDefault()
        document.getElementById("shipping-form-button").hidden = true
        document.getElementById("payment-info").hidden = false
    })

    document.getElementById('make-payment').addEventListener('click', function(e) {
        submitFormData()
    })

    function submitFormData() {
        var shipping_info = {
            'first_name': document.getElementById("first-name-field").value,
            'last_name': document.getElementById("last-name-field").value,
            'email': document.getElementById("email-field").value,
            'street_address': document.getElementById("street-field").value,
            'city': document.getElementById("city-field").value,
            'zip_code': document.getElementById("zip-field").value,
            'country': document.getElementById("country-field").value,
            'total': total
        }

        var url = '/process_order/'
        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'shipping':shipping_info})
        })
        .then((response) => 
            response.json())
        .then((data) => {
            if (data == 'Payment aborted') {
                alert('Please fill out all the necessary fields')
            } else {
                alert('Transaction completed')
                window.location.assign("http://localhost:8000/shop")
            }
            
    })
    }