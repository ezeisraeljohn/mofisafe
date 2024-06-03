
$(document).ready(function(){

        // Get the total income available
        $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/income/',
                method: 'GET',
                headers: {
                        'Authorization': 'Basic ' + btoa('ezeisraeljohn:testuser123'),
                    },
                success: function(data) {
                        let totalAmount = 0;
                        data.forEach(function(income) {
                            totalAmount += parseFloat(income['amount']);
                        });
                        const formattedAmount = totalAmount.toFixed(2).toLocaleString();
                        $('.balance').text(`$${formattedAmount}`);
                    },
        });

        $.ajax({
                url: 'http://127.0.0.1:8000/api/v1/expenses/',
                method: 'GET',
                headers: {
                        'Authorization': 'Basic '+ btoa('ezeisraeljohn:testuser123'),
                },
                success: function(data) {
                        let totalAmount = 0;
                        data.forEach(function(expense){
                               const the_date = moment(expense['date'])
                               if (the_date.month() == moment().month()){

                                       totalAmount += parseFloat(expense['amount']);
                               }
                        });
                        const formattedAmount = totalAmount.toFixed(2).toLocaleString();
                        $('.total-expense').text(`$${formattedAmount}`);
                }
        })
        
});

      